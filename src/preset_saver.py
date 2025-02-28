import json
import random
from functools import reduce
import os
import shutil

randomize_modes = ['Standard', 'Progressive']
randomize_modes_enum = [(mode, mode, mode) for mode in randomize_modes]

class PresetSaver:
    def __init__(self, props, ext_props, random_props, random_prop_groups, addon_root):
        self.props = props
        self.ext_props = ext_props
        self.prefix = "Transhuman_PRESET_"
        self.prefix_ext = '.json'
        self.ext_prop_prefix = "_EXT_PROP_"
        self.random_props = random_props
        self.random_prop_groups = random_prop_groups
        self.addon_root = addon_root

    def get_preset_name(self, name):
        return self.prefix + name + self.prefix_ext

    def save(self, context, name):
        preset_name = self.get_preset_name(name)
        values = {}
        for prop in self.props:
            values[prop] = getattr(context.scene.Transhuman_tool, prop, None)

        for prop in self.ext_props:
            ext = self.ext_props[prop]
            serialize = lambda x: x
            value = getattr(ext[0](), ext[1])

            if type(value) is not str:
                try:
                    iterator = iter(value)
                except TypeError:
                    pass
                else:
                    serialize = lambda x: list(x)

            if len(ext) > 2:
                options = ext[2]
                if "type" in options and options["type"] == "list":
                    serialize = lambda x: list(x)
            values[self.ext_prop_prefix + prop] = serialize(value)

        with open(self.get_presets_path() / preset_name, "w") as f:
            json.dump(values, f, indent=4)

    def set_selected_preset(self, context, name):
        setattr(context.scene.Transhuman_tool, "preset_name", name)

    def load(self, context, name, weight_override=1):
        return self.load_selected(context, name, None, weight_override, change_selected_preset = True)
    
    def load_selected(self, context, name, selected_attrs, weight_override=1, change_selected_preset=False):
        preset_name = self.get_preset_name(name)
        try:
            with open(self.get_presets_path() / preset_name, "r") as f:
                loaded = json.load(f)
                self.setattrs(loaded, context, weight_override, exclusively=selected_attrs)
            if change_selected_preset:
                self.set_selected_preset(context, name)
        except FileNotFoundError:
            raise Exception("Preset not found by key: " + name)

    def getattr(self, key, context):
        obj = None
        real_key = None
        if key.startswith(self.ext_prop_prefix):
            ext_prop_name = key[len(self.ext_prop_prefix) :]
            if ext_prop_name not in self.ext_props:
                print('ext prop not found: ' + ext_prop_name)
                return 0

            ext = self.ext_props[ext_prop_name]
            obj = ext[0]()
            real_key = ext[1]
        else:
            obj = context.scene.Transhuman_tool
            real_key = key

        return getattr(obj, real_key)

    def setattrs(self, key_values, context, weight_override=1, exclusively=None):
        for key in key_values:
            try:
                target_properties = None
                prop_name = None
                prop_value = None
                if key.startswith(self.ext_prop_prefix):
                    ext_prop_name = key[len(self.ext_prop_prefix) :]
                    # if exclusively is set, we only set the properties in the list
                    if exclusively is not None and ext_prop_name not in exclusively:
                        continue
                    ext = self.ext_props[ext_prop_name]
                    target_properties = ext[0]()
                    prop_name = ext[1]
                    prop_value = key_values[key]
                else:
                    target_properties = context.scene.Transhuman_tool
                    prop_name = key
                    prop_value = key_values[key]
                    # if exclusively is set, we only set the properties in the list
                    if exclusively is not None and prop_name not in exclusively:
                        continue

                self.setattr(target_properties, prop_name, prop_value, weight_override)
            except TypeError as e:
                print(e)
            except KeyError as e:
                print(e)
    
    def setattr(self, obj, key, value, weight_override):
        # if the weight is 0, we don't change the value
        if weight_override == 0:
            return
        # if the weight is 1, we replace the value
        elif weight_override == 1:
            setattr(obj, key, value)
            return
        # if the weight is between 0 and 1, we interpolate the value
        else:
            current = getattr(obj, key, None)
            # if the value is number, we interpolate it
            if type(value) is int or type(value) is float:
                change = (value - current) * weight_override
                # some properties are expecting integer values
                if type(current) is int:
                    change = int(change)
                # if the current value is None, it is considered as 0
                if current is None:
                    current = 0
                setattr(obj, key, current + change)
                return
            # if the value is a list or tuple, we interpolate each value
            elif type(value) is list or type(value) is tuple:
                # if the current value is None, it is considered as 0
                if current is None:
                    current = [0] * len(value)
                setattr(obj, key, [current[i] + (value[i] - current[i]) * weight_override for i in range(len(current))])
                return
            # if the value is a dict, we interpolate each value
            elif type(value) is dict:
                # if the current value is None, it is considered as 0
                if current is None:
                    current = {k: 0 for k in value}
                setattr(obj, key, {k: current[k] + (value[k] - current[k]) * weight_override for k in current})
                return
            # for other types, we replace the value if the weight is more than 0.5, otherwise we don't change it
            else:
                if weight_override > 0.5:
                    setattr(obj, key, value)
                return

    def randomize(self, context, randomize_mode='Standard'):
        extremity = getattr(context.scene.Transhuman_tool, "random_extremity", None)
        power = self.convert_extremity_to_power(extremity)
        created = {}
        for key in self.random_props:
            min = self.random_props[key][0]
            max = self.random_props[key][1]
            if randomize_mode == 'Progressive':
                current = self.getattr(key, context)
                new_value = self.get_random_value(-max, max, power) + current # -max is the min here because we want to be able to go back to 0.
                # make sure that the new value is in the range
                if new_value < min:
                    new_value = min
                elif new_value > max:
                    new_value = max
                created[key] = new_value
            else:
                created[key] = self.get_random_value(min, max, power)

        # comply with the total of each groups
        for group in self.random_prop_groups:
            total = group["total"]
            keys = group["keys"]
            sum = reduce(lambda result, key: result + created[key], keys, 0)
            if sum == 0:
                [].count
                value = total / len(keys)
                for key in keys:
                    created[key] = value
            else:
                multiply = total / sum
                for key in keys:
                    created[key] = created[key] * multiply

        self.setattrs(created, context)

    def convert_extremity_to_power(self, extremity):
        return pow(10000, 0.5 - extremity)

    def get_random_value(self, min, max, power):
        base = random.uniform(0, 1)
        sign = 1 if random.uniform(min, max) >= 0 else -1
        value = pow(base, power) * sign * max
        return value

    def randomize_from_preset(self, context, name, randomize_mode='Standard'):
        self.load(context, name)
        self.randomize(context, randomize_mode)
    
    def conceive_from_presets(self, context, name_a, name_b, weight_b):
        self.load(context, name_a)
        self.load(context, name_b, weight_b)
        self.set_selected_preset(context, name_a + ' x ' + name_b)

    def get_saved_presets(self):
        preset_path = self.get_presets_path()
        return [
            file[len(self.prefix) : -len(self.prefix_ext)]
            for file in os.listdir(str(preset_path.absolute()))
            if file.startswith(self.prefix)
        ]
    
    def get_presets_path(self):
        preset_path = self.addon_root / "presets"
        return preset_path

    def get_ext_prop(self, name):
        return self.ext_props[name]

    def import_preset(self, file_path):
        # copy the file to the preset folder
        # if the file already exists, add a number to the end of the name
        parsed_path = os.path.split(file_path)
        filename = parsed_path[1]
        filename_without_ext = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]
        preset_path = self.get_presets_path()
        target_path = preset_path / filename
        if os.path.exists(str(target_path)):
            i = 1
            while True:
                new_filename = filename_without_ext + "(" + str(i) + ")" +  ext
                target_path = preset_path / new_filename
                if not os.path.exists(str(target_path)):
                    break
                i += 1

        shutil.copy(file_path, target_path)
