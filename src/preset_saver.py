import json
import random
from functools import reduce
import os

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

    def load(self, context, name):
        preset_name = self.get_preset_name(name)
        try:
            with open(self.get_presets_path() / preset_name, "r") as f:
                loaded = json.load(f)
                self.setattrs(loaded, context)
            
            setattr(context.scene.Transhuman_tool, "preset_name", name)
        except FileNotFoundError:
            raise Exception("Preset not found by key: " + name)

    def getattr(self, key, context):
        obj = None
        real_key = None
        if key.startswith(self.ext_prop_prefix):
            ext_prop_name = key[len(self.ext_prop_prefix) :]
            ext = self.ext_props[ext_prop_name]
            obj = ext[0]()
            real_key = ext[1]
        else:
            obj = context.scene.Transhuman_tool
            real_key = key

        return obj[real_key]

    def setattrs(self, key_values, context):
        for key in key_values:
            try:
                if key.startswith(self.ext_prop_prefix):
                    ext_prop_name = key[len(self.ext_prop_prefix) :]
                    ext = self.ext_props[ext_prop_name]
                    setattr(ext[0](), ext[1], key_values[key])
                else:
                    setattr(context.scene.Transhuman_tool, key, key_values[key])
            except TypeError as e:
                print(e)

    def randomize(self, context, selective=False):
        extremity = getattr(context.scene.Transhuman_tool, "random_extremity", None)
        power = self.convert_extremity_to_power(extremity)
        created = {}
        for key in self.random_props:
            min = self.random_props[key][0]
            max = self.random_props[key][1]
            if selective:
                current = self.getattr(key, context)
                if current == 0:
                    created[key] = self.get_random_value(min, max, power)
                else:
                    created[
                        key
                    ] = current  # leave the current value so later created[key] won't throw
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

    def randomize_from_preset(self, context, name):
        self.load(context, name)
        self.randomize(context, selective=True)

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
