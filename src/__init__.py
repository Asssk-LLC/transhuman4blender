addon_name = 'Transhuman4Blender'

bl_info = {
    "name": 'Transhuman4Blender',
    "description": "Character generator for Blender",
    "author": "SM5 by Heledahn",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "3D View > Tools",
    "wiki_url": "https://sm5.heledahn.com/pages/transhuman-wiki",
    "tracker_url": "",
    "category": "Object",
}

if "bpy" in locals():
    import importlib
    importlib.reload(sm5_addon_utils)
    importlib.reload(preset_saver)
else:
    import bpy
    import bpy_types
    from . import sm5_addon_utils
    from . import preset_saver


from bpy.props import (
    PointerProperty,
)
from bpy.types import (
    Operator,
    UILayout,
)
from bpy_extras.io_utils import ImportHelper

from pathlib import Path

# fmt: off
presetSaver = preset_saver.PresetSaver(
    [
        # list of names of the props to save.
        "body_hair_image",
        "body_hair_mesh_UV_selector",
        "stubble_image",
        "eye_base_image",
        "pupil_switch",
        "iris",
        "pupil_cat",
        "pupil_goat",
        "pupil_star",
        "eyelashes_clump_switch",
        "body_hair_switch",
        "stubble_switch",
        "stubble_trim_switch",
        "underwear_top_switch",
        "underwear_bottom_switch",
        "scars_switch",
        "scars_selector",
        "tattoo_switch",
        "base_switch",
        "blush_switch",
        "lips_switch",
        "lip_liner_switch",
        "eyeshadow_switch",
        "lashline_switch",
        "inner_shadow_switch",
        "outer_shadow_switch",
        "highlight_switch",
        "eyeliner_switch",
        "facial_paint_switch",
        "eyebrows_switch",
        "nails_switch",
        "nail_length",
        "eyebrow_base_image",
        "old_age_switch",
        "female_base",
        "female_weight_plus",
        "female_weight_minus",
        "female_muscles",
        "male_base",
        "male_weight_plus",
        "male_weight_minus",
        "male_muscles",
        "feet_male",
        "feet_female",
        "hand_male",
        "hand_female",
        "hand_neutral",
        "hand_elder",
        "gender_definition",
        "eye_grow",
        "eye_shrink",
        "eye_inward",
        "eye_outward",
        "eye_forward",
        "eye_backward",
        "eyeball_height",
        "eyeball_depth",
        "eyeball_closeness",
        "eyeball_size",
        "eye_up",
        "eye_down",
        "eye_length",
        "eye_roundness",
        "eye_corner",
        "eye_rotate",
        "eye_fold",
        "eye_puff",
        "tearduct",
        "tearduct_sharp",
        "eyebrows_up",
        "eyebrows_down",
        "eyebrows_tail",
        "eyebrows_head",
        "eyebrows_arch",
        "eyebrows_rotate",
        "eyebrows_dist",
        "fem_face_1",
        "fem_face_2",
        "fem_face_3",
        "fem_face_4",
        "fem_face_5",
        "m_face_1",
        "m_face_2",
        "m_face_3",
        "m_face_4",
        "m_face_5",
        "head_size",
        "head_width",
        "face_length",
        "face_width",
        "face_convex",
        "face_concave",
        "baby_face",
        "face_rectangle",
        "face_triangle",
        "face_diamond",
        "face_inversend_triangle",
        "face_oval",
        "face_round",
        "forehead_protrusion",
        "root_scalp",
        "cheeks_plus_minus",
        "cheeks_hollow",
        "chin_position",
        "chin_vertical",
        "cleft_chin",
        "chin_height",
        "chin_width",
        "jaw_width",
        "jaw_length",
        "neck_girth",
        "glabella",
        "bridge",
        "bridge_width",
        "supratip",
        "supratip_width",
        "nose_tip_angle",
        "nose_tip_shape",
        "infratip",
        "infratip_thickness",
        "wings",
        "wings_arch",
        "nose_cleft",
        "nose_length",
        "nose_width",
        "nose_tip_position",
        "nose_tip_chisel",
        "nose_position",
        "nose_height",
        "mouth_position_1",
        "mouth_position_2",
        "mouth_size",
        "mouth_width",
        "lips_thickness",
        "lip_top_border",
        "lip_cupids_bow",
        "lip_bottom_border",
        "lip_bottom_cupids",
        "lip_tubercles_top",
        "lip_tubercles_bottom",
        "lip_cleft",
        "philtrum",
        "lip_crease_top",
        "lip_crease_bottom",
        "top_lip",
        "bottom_lip",
        "ear_in",
        "ear_out",
        "ear_pointy",
        "ear_back",
        "ear_height",
        "ear_depth",
        "ear_size",
        "breasts",
        "breasts_down",
        "breasts_push",
        "shoulders",
        "buttocks",
        "nipples",
        "waist",
        "hips",
        "circumcised",
        "vulva",
        "vulva_open",
        "labia_size",
        "labia_sym",
        "anus",
        "anus_open",
        "penis",
        "bulge",
        "bulge_protrusion",
        "teeth_age",
        "denture_height",
        "denture_position",
        "teeth_saturation",
        "teeth_gap_top",
        "teeth_gap_bottom",
        "crooked_teeth_top",
        "crooked_teeth_bottom",
        "missing_11",
        "missing_10",
        "missing_9",
        "missing_8",
        "missing_7",
        "missing_6",
        "missing_27",
        "missing_26",
        "missing_25",
        "missing_24",
        "missing_23",
        "missing_22",
        "teeth_length",
        "teeth_size",
        "fangs_top",
        "fangs_bottom",
        "eyelashes_curves",
        "peach_fuzz_curves",
        "chest_curves",
        "chest_extra_curves",
        "arms_curves",
        "forearms_curves",
        "armpit_curves",
        "back_curves",
        "stubble_curves",
        "nose_hair_curves",
        "hand_curves",
        "feet_curves",
        "shins_curves",
        "thighs_curves",
        "stomach_curves",
        "pubic_f_curves",
        "pubic_m_curves",
        "armpit_switch",
        "arms_switch",
        "forearms_switch",
        "chest_switch",
        "stomach_switch",
        "back_switch",
        "chest_extra_switch",
        "thighs_switch",
        "shins_switch",
        "hands_feet_switch",
        "eyebrows_1_curves",
        "eyebrows_2_curves",
        "eyebrows_3_curves",
        "eyebrows_4_curves",
        "eyebrows_5_curves",
        "eyebrows_1_mesh",
        "eyebrows_2_mesh",
        "eyebrows_3_mesh",
        "eyebrows_4_mesh",
        "eyebrows_5_mesh",
        "eyebrows_to_mesh",
        "eyebrows_type",
        "top_eyelashes_to_mesh",
        "top_eyelashes_type",
        "bottom_eyelashes_to_mesh",
        "bottom_eyelashes_type",
        "nosehair_to_mesh",
        "nosehair_type",
        "beard_to_mesh",
        "beard_type",
        "secondary_body_hair_switch",
        "secondary_beard_switch",
        "highlights_switch",
        "root_switch",
        "root_invert",
        "mesh_thickness",
        "imported_persona_displ",
        "persona_displ_value",
        "original_face_displ",
        "flip_displ_switch",
        "imported_persona_mesh",
        "imported_persona_skin",
        "persona_switch",
        "clothes_adjust_switch",
        "hide_hair_wig",
        "hide_render_hair_wig",
        "dynamic_breasts",
        "dynamic_wrinkles",
    ],
    {
        "smooth_custom":  [ lambda: bpy.data.objects["SM5 Rest Pose Transhuman"].modifiers[ "Smooth Custom"], "iterations", ],
        "scalp_color":  [ lambda: bpy.data.materials["SM5 Scalp Material Transhuman" ].node_tree.nodes["scalp_color" ].outputs[0], "default_value", ],
        "scalp_fade":  [ lambda: bpy.data.materials["SM5 Scalp Material Transhuman" ].node_tree.nodes["scalp_fade" ].inputs[1], "default_value", ],
        "hair_mesh_curve": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_mesh_curve"].inputs[1],"default_value",],
        "hair_spread": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_spread"].outputs[0],"default_value",],
        "root_puff": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["root_puff"].inputs[3],"default_value",],
        "hair_clump_switch": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_clump_switch"].inputs[0],"default_value",],
        "hair_clump_shape": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_clump_shape"].outputs[0],"default_value",],
        "hair_random_length": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_random_length"].outputs[0],"default_value",],
        "hair_resolution": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_resolution"], "integer",],
        "hair_curls_switch": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_curls_switch"].inputs[1],"default_value",],
        "curl_clump_mode": [lambda: bpy.data.node_groups["SM5 Hair Curls"].nodes["curl_clump_mode"].inputs[0],"default_value",],
        "gravity_clump": [lambda: bpy.data.node_groups["SM5 Hair Curls"].nodes["gravity_clump"].outputs[0],"default_value",],
        "curl_amplitude": [lambda: bpy.data.node_groups["SM5 Hair Curls"].nodes["curl_amplitude"].outputs[0],"default_value",],
        "curl_frequency": [lambda: bpy.data.node_groups["SM5 Hair Curls"].nodes["curl_frequency"].inputs[1],"default_value",],
        "curls_randomize": [lambda: bpy.data.node_groups["SM5 Hair Curls"].nodes["curls_randomize"].inputs[0],"default_value",],
        "waves_curls_switch": [lambda: bpy.data.node_groups["SM5 Hair Curls"].nodes["waves_curls_switch"].inputs[0],"default_value",],
        "curl_scale": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["curl_scale"].outputs[0],"default_value",],
        "curl_resolution": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["curl_resolution"].outputs[0],"default_value",],
        "loose_hair_decimate": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["loose_hair_decimate"].inputs[0],"default_value",],
        "loose_hair_spread": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["loose_hair_spread"].inputs[0],"default_value",],
        "loose_hair_amount": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["loose_hair_amount"].inputs[2],"default_value",],
        "loose_hairs_frizz": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["loose_hairs_frizz"].inputs[1],"default_value",],
        "hair_amount": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["interpolate_curves"],"integer",],
        "curves_hair_thickness": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["thickness"].outputs[0],"default_value",],
        "fluff_strands": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["fluff_strands"].inputs[3],"default_value",],
        "noise_strength": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["noise_strength"].inputs[0],"default_value",],
        "noise_scale": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["noise_scale"].inputs[1],"default_value",],
        "noise_shape": [lambda: bpy.data.node_groups["SM5 Hair Curves"].nodes["noise_shape"].inputs[1],"default_value",],
        "mesh_tubes_cards": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_tubes_cards"].inputs[0],"default_value",],
        "mesh_hair_subdivision": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_hair_subdivision"],"integer",],
        "feigned_uv_curls": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["feigned_uv_curls"].inputs[0],"default_value",],
        "tubes_amplitude": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["tubes_amplitude"].outputs[0],"default_value",],
        "inherit_curve_curls": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["inherit_curve_curls"].inputs[1],"default_value",],
        "random_direction_mesh": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["random_direction_mesh"].inputs[0],"default_value",],
        "mesh_loose_hairs": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_loose_hairs"].inputs[0],"default_value",],
        "mesh_loose_resample": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_loose_resample"],"integer",],
        "loose_hair_size": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["loose_hair_size"].outputs[0],"default_value",],
        "hair_type_mesh": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_type_mesh"],"integer",],
        "short_hair": [lambda:bpy.data.node_groups["SM5 Hair"].nodes["short_hair"], "boolean",],
        "interpolate_root_mesh": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["interpolate_root_mesh"].inputs[1],"default_value",],
        "interpolate_mesh_amount": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["interpolate_mesh_amount"],"integer",],
        "mesh_hair_metallic": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_hair"].inputs[6],"default_value",],
        "mesh_hair_specular": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_hair"].inputs[7],"default_value",],
        "mesh_hair_roughness": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_hair"].inputs[9],"default_value",],
        "mesh_hair_ior": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_hair"].inputs[16],"default_value",],
        "mesh_hair_clearcoat": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_hair"].inputs[14],"default_value",],
        "mesh_hair_clearcoat_roughness": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_hair"].inputs[15],"default_value",],
        "mesh_translucent": [lambda: bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes["mesh_translucent"].inputs[0],"default_value",],
        "eyebrows_color_group":  [ lambda: bpy.data.node_groups["SM5 Eyebrows Hair Color Transhuman" ].nodes["eyebrows_color_group" ].outputs[0], "default_value", ],
        "body_hair_color":  [ lambda: bpy.data.node_groups["SM5 Body Hair Color Transhuman" ].nodes["body_hair_color" ].outputs[0], "default_value", ],
        "secondary_hair_color_picker":  [ lambda: bpy.data.node_groups["SM5 Body Hair Color Transhuman" ].nodes["secondary_hair_color_picker" ].outputs[0], "default_value", ],
        "body_hair_amount":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["body_hair_amount" ].inputs[2], "default_value", ],
        "original_face_displ":  [ lambda: bpy.data.node_groups["SM5 Transhuman Normal"].nodes["original_face_displ"].inputs[0], "default_value", ],
        "persona_displ_value": [lambda:bpy.data.node_groups["SM5 Body Displacement"].nodes["persona_displ_value"].outputs[0],"default_value",],
        "body_hair_spread":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["body_hair_spread" ].outputs[0], "default_value", ],
        "body_hair_length":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["body_hair_length" ].inputs[3], "default_value", ],
        "body_hair_clump":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["hair_clump" ].inputs[0], "default_value", ],
        "body_hair_noise_scale":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["noise_scale" ].inputs[1], "default_value", ],
        "body_hair_noise_strength":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["noise_strength" ].outputs[0], "default_value", ],
        "body_hair_noise_shape":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["noise_shape" ].outputs[0], "default_value", ],
        "body_hair_random_length_min":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["hair_random_length" ].inputs[2], "default_value", ],
        "body_hair_random_length_max":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["hair_random_length" ].inputs[3], "default_value", ],
        "nose_hair_length":  [ lambda: bpy.data.node_groups["SM5 Nose Hairs Transhuman" ].nodes["nose_hair_length" ].inputs[3], "default_value", ],
        "body_hair_decimate":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["hair_decimate" ].inputs[6], "default_value", ],
        "body_hair_thickness":  [ lambda: bpy.data.node_groups["SM5 Body Hair Transhuman" ].nodes["thickness" ].outputs[0], "default_value", ],
        "body_hair_secondary_intensity":  [ lambda: bpy.data.node_groups["SM5 Body Hair Color Transhuman" ].nodes["secondary_intensity" ].color_ramp.elements[1], "position", ],
        "body_hair_bump":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["body_hair_bump" ].inputs[0], "default_value", ],
        "body_hair_thickness_texture":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["body_hair_thickness_texture" ].inputs[1], "default_value", ],
        "beard_color":  [ lambda: bpy.data.node_groups["SM5 Beard Color Transhuman" ].nodes["beard_color" ].outputs[0], "default_value", ],
        "secondary_beard_color_picker":  [ lambda: bpy.data.node_groups["SM5 Beard Color Transhuman" ].nodes["secondary_beard_color_picker" ].outputs[0], "default_value", ],
        "beard_secondary_intensity":  [ lambda: bpy.data.node_groups["SM5 Beard Color Transhuman" ].nodes["secondary_intensity" ].color_ramp.elements[1], "position", ],
        "stubble_texture_color":  [ lambda: bpy.data.node_groups["SM5 Stubble Texture Color Transhuman" ].nodes["stubble_color" ].outputs[0], "default_value", ],
        "stubble_bump":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["stubble_bump" ].inputs[0], "default_value", ],
        "stubble_mesh_thickness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["stubble_mesh_thickness" ].inputs[1], "default_value", ],
        "cornea_reflective":  [ lambda: bpy.data.materials["SM5 Cornea Material Transhuman" ].node_tree.nodes["cornea_reflective" ].outputs[0], "default_value", ],
        "eye_color_picker":  [ lambda: bpy.data.materials["SM5 Eyes Material Transhuman" ].node_tree.nodes["eye_color_picker" ].outputs[0], "default_value", ],
        "eye_color_chroma":  [ lambda: bpy.data.materials["SM5 Eyes Material Transhuman" ].node_tree.nodes["eye_color_chroma" ].inputs[1], "default_value", ],
        "halo":  [ lambda: bpy.data.materials["SM5 Eyes Material Transhuman" ].node_tree.nodes["halo" ].inputs[0], "default_value", ],
        "halo_color":  [ lambda: bpy.data.materials["SM5 Eyes Material Transhuman" ].node_tree.nodes["halo_color" ].outputs[0], "default_value", ],
        "sclera_cornea_mixer":  [ lambda: bpy.data.materials["SM5 Cornea Material Transhuman" ].node_tree.nodes["sclera_cornea_mixer" ].inputs[0], "default_value", ],
        "sclera_cornea_settings_color":  [ lambda: bpy.data.materials["SM5 Cornea Material Transhuman" ].node_tree.nodes["sclera_cornea_settings" ].inputs[0], "default_value", ],
        "sclera_cornea_settings_transmission":  [ lambda: bpy.data.materials["SM5 Cornea Material Transhuman" ].node_tree.nodes["sclera_cornea_settings" ].inputs[17], "default_value", ],
        "sclera_cornea_settings_roughness":  [ lambda: bpy.data.materials["SM5 Cornea Material Transhuman" ].node_tree.nodes["sclera_cornea_settings" ].inputs[18], "default_value", ],
        "sclera_cornea":  [ lambda: bpy.data.materials[ "SM5 Cornea Material Transhuman" ].node_tree.nodes["sclera_cornea"], "layer_name", ],
        "eye_redness":  [ lambda: bpy.data.materials["SM5 Eyes Material Transhuman" ].node_tree.nodes["eye_redness" ].inputs[0], "default_value", ],
        "eye_settings":  [ lambda: bpy.data.materials["SM5 Cornea Material Transhuman" ].node_tree.nodes["eye_settings" ].inputs[18], "default_value", ],
        "tear_settings":  [ lambda: bpy.data.materials["SM5 Tear Material Transhuman" ].node_tree.nodes["tear_settings" ].inputs[0], "default_value", ],
        "eyebrows_noise":  [ lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman" ].nodes["noise_strength" ].outputs[0], "default_value", ],
        "eyebrows_curves_thickness":  [ lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman" ].nodes["thickness" ].outputs[0], "default_value", ],
        "eyebrows_curves_spread":  [ lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman" ].nodes["eyebrows_spread" ].outputs[0], "default_value", ],
        "eyebrows_curves_amount":  [ lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman" ].nodes["eyebrows_amount" ].inputs[2], "default_value", ],
        "eyebrows_to_mesh":  [ lambda:bpy.data.node_groups["SM5 Eyebrows Transhuman"].nodes["eyebrows_to_mesh"].inputs[1], "default_value", ],
        "eyebrows_type":  [ lambda:bpy.data.node_groups["SM5 Eyebrows Transhuman"].nodes["eyebrows_type"], "integer",],
        "top_eyelashes_to_mesh":  [ lambda:bpy.data.node_groups["SM5 Top Eyelashes Transhuman"].nodes["top_eyelashes_to_mesh"].inputs[1], "default_value", ],
        "top_eyelashes_type":  [ lambda:bpy.data.node_groups["SM5 Top Eyelashes Transhuman"].nodes["top_eyelashes_type"], "integer",],
        "bottom_eyelashes_to_mesh":  [ lambda:bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman"].nodes["bottom_eyelashes_to_mesh"].inputs[1], "default_value", ],
        "bottom_eyelashes_type":  [ lambda:bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman"].nodes["bottom_eyelashes_type"], "integer",],
        "beard_to_mesh":  [ lambda:bpy.data.node_groups["SM5 Beard Transhuman"].nodes["beard_to_mesh"].inputs[1], "default_value", ],
        "beard_type":  [ lambda:bpy.data.node_groups["SM5 Beard Transhuman"].nodes["beard_type"], "integer",],
        "nosehair_to_mesh":  [ lambda:bpy.data.node_groups["SM5 Nose Hairs Transhuman"].nodes["nosehair_to_mesh"].inputs[1], "default_value", ],
        "nosehair_type":  [ lambda:bpy.data.node_groups["SM5 Nose Hairs Transhuman"].nodes["nosehair_type"], "integer",],
        "bodyhair_to_mesh":  [ lambda:bpy.data.node_groups["SM5 Body Hair Transhuman"].nodes["bodyhair_to_mesh"].inputs[1], "default_value", ],
        "eyelashes_color":  [ lambda: bpy.data.node_groups["SM5 Eyelashes Color Transhuman" ].nodes["eyelashes_color" ].outputs[0], "default_value", ],
        "eyelashes_thickness_top":  [ lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman" ].nodes["eyelashes_thickness" ].outputs[0], "default_value", ],
        "eyelashes_thickness_bottom":  [ lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman" ].nodes["eyelashes_thickness" ].outputs[0], "default_value", ],
        "eyelashes_length_top":  [ lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman" ].nodes["eyelashes_length" ].inputs[3], "default_value", ],
        "eyelashes_length_bottom":  [ lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman" ].nodes["eyelashes_length" ].inputs[3], "default_value", ],
        "eyelashes_amount_top":  [ lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman" ].nodes["Duplicate Elements" ].inputs[2], "default_value", ],
        "eyelashes_amount_bottom":  [ lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman" ].nodes["Duplicate Elements" ].inputs[2], "default_value", ],
        "eyelashes_spread_top":  [ lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman" ].nodes["eyelashes_spread" ].outputs[0], "default_value", ],
        "eyelashes_spread_bottom":  [ lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman" ].nodes["eyelashes_spread" ].outputs[0], "default_value", ],
        "eyelashes_clump":  [ lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman" ].nodes["eyelashes_clump" ].inputs[0], "default_value", ],
        "stubble_spread":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["stubble_spread" ].outputs[0], "default_value", ],
        "stubble_amount":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["stubble_amount" ].inputs[2], "default_value", ],
        "stubble_length":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["stubble_length" ].inputs[3], "default_value", ],
        "stubble_decimate":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["stubble_decimate" ].inputs[6], "default_value", ],
        "stubble_thickness":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["stubble_thickness" ].outputs[0], "default_value", ],
        "stubble_clump":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["stubble_clump" ].inputs[0], "default_value", ],
        "skin_hue":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["skin_hue" ].inputs[7], "default_value", ],
        "skin_saturation":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["skin_saturation" ].inputs[0], "default_value", ],
        "skin_chroma":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["skin_chroma" ].inputs[1], "default_value", ],
        "skin_health":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["health" ].inputs[0], "default_value", ],
        "skin_detail_strength":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["skin_detail_strength" ].inputs[0], "default_value", ],
        "face_definition":  [ lambda: bpy.data.node_groups["SM5 Transhuman Normal" ].nodes["face_definition" ].inputs[0], "default_value", ],
        "body_definition":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["transhuman_normal" ].inputs[0], "default_value", ],
        "skin_sweat":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["sweat" ].inputs[1], "default_value", ],
        "skin_reflection":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["skin_reflection" ].inputs[0], "default_value", ],
        "skin_subsurface":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["skin_subsurface" ].outputs[0], "default_value", ],
        "scars_color_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["scars_color_intensity" ].color_ramp.elements[1], "position", ],
        "scars_bump":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["scars_bump" ].inputs[0], "default_value", ],
        "scars_color_saturation":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["scars_color_saturation" ].inputs[1], "default_value", ],
        "underwear_color":  [ lambda: bpy.data.materials["SM5 Underwear Material" ].node_tree.nodes["underwear_color" ].inputs[6], "default_value", ],
        "scars_color_brightness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["scars_color_brightness" ].inputs[1], "default_value", ],
        "base_makeup_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["base_makeup_color" ].outputs[0], "default_value", ],
        "base_maiko":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["base_maiko" ].inputs[0], "default_value", ],
        "base_makeup":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["base_makeup" ].inputs[0], "default_value", ],
        "makeup_contouring":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["contouring" ].inputs[0], "default_value", ],
        "blush_1":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_1" ].inputs[0], "default_value", ],
        "blush_1_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_1_color" ].inputs[7], "default_value", ],
        "blush_2":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_2" ].inputs[0], "default_value", ],
        "blush_2_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_2_color" ].inputs[7], "default_value", ],
        "blush_3":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_3" ].inputs[0], "default_value", ],
        "blush_3_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_3_color" ].inputs[7], "default_value", ],
        "blush_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_intensity" ].color_ramp.elements[1], "position", ],
        "blush_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_settings" ].inputs[6], "default_value", ],
        "blush_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["blush_settings" ].inputs[9], "default_value", ],
        "lipstick_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lipstick" ].inputs[7], "default_value", ],
        "lip_gloss":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lip_gloss" ].inputs[0], "default_value", ],
        "lipstick_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lipstick" ].inputs[0], "default_value", ],
        "lipstick_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lipstick_settings" ].inputs[6], "default_value", ],
        "lipstick_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lipstick_settings" ].inputs[9], "default_value", ],
        "lip_liner":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lip_liner" ].inputs[0], "default_value", ],
        "lip_liner_gradient":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lip_liner_gradient" ].inputs[0], "default_value", ],
        "lip_liner_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lip_liner_color" ].outputs[0], "default_value", ],
        "lip_liner_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lip_liner_settings" ].inputs[6], "default_value", ],
        "lip_liner_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lip_liner_settings" ].inputs[9], "default_value", ],
        "eyeshadow_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow" ].inputs[0], "default_value", ],
        "eyeshadow_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_intensity" ].color_ramp.elements[1], "position", ],
        "eyeshadow_lid_colors_main":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_lid_colors" ].inputs[6], "default_value", ],
        "eyeshadow_lid_colors_inner":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_lid_colors" ].inputs[7], "default_value", ],
        "eyeshadow_tip":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_tip" ].inputs[0], "default_value", ],
        "eyeshadow_lid_tail":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_lid_tail" ].inputs[7], "default_value", ],
        "eyeshadow_tail":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_tail" ].inputs[0], "default_value", ],
        "eyeshadow_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_settings" ].inputs[6], "default_value", ],
        "eyeshadow_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeshadow_settings" ].inputs[9], "default_value", ],
        "lashline_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline" ].inputs[0], "default_value", ],
        "lashline_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_intensity" ].color_ramp.elements[1], "position", ],
        "lashline_main_under_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_main_under_color" ].inputs[7], "default_value", ],
        "lashline_tip_colors":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_tip_colors" ].inputs[7], "default_value", ],
        "lashline_tip":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_tip" ].inputs[0], "default_value", ],
        "lashline_tail_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_tail_color" ].inputs[7], "default_value", ],
        "lashline_tail":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_tail" ].inputs[0], "default_value", ],
        "lashline_main_under_color_smudge":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_main_under_color" ].inputs[6], "default_value", ],
        "lashline_under":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_under" ].inputs[0], "default_value", ],
        "lashline_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_settings" ].inputs[6], "default_value", ],
        "lashline_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["lashline_settings" ].inputs[9], "default_value", ],
        "inner_shadow_1":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_1" ].inputs[0], "default_value", ],
        "inner_shadow_1_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_1_color" ].inputs[7], "default_value", ],
        "inner_shadow_2":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_2" ].inputs[0], "default_value", ],
        "inner_shadow_2_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_2_color" ].inputs[7], "default_value", ],
        "inner_shadow_3":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_3" ].inputs[0], "default_value", ],
        "inner_shadow_3_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_3_color" ].inputs[7], "default_value", ],
        "inner_shadow_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_intensity" ].color_ramp.elements[1], "position", ],
        "inner_shadow_granularity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_granularity" ].inputs[0], "default_value", ],
        "inner_shadow_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_settings" ].inputs[6], "default_value", ],
        "inner_shadow_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["inner_shadow_settings" ].inputs[9], "default_value", ],
        "outer_shadow_1":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_1" ].inputs[0], "default_value", ],
        "outer_shadow_1_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_1_color" ].inputs[7], "default_value", ],
        "outer_shadow_2":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_2" ].inputs[0], "default_value", ],
        "outer_shadow_2_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_2_color" ].inputs[7], "default_value", ],
        "outer_shadow_3":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_3" ].inputs[0], "default_value", ],
        "outer_shadow_3_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_3_color" ].inputs[7], "default_value", ],
        "outer_shadow_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_intensity" ].color_ramp.elements[1], "position", ],
        "outer_shadow_granularity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_granularity" ].inputs[0], "default_value", ],
        "outer_shadow_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_settings" ].inputs[6], "default_value", ],
        "outer_shadow_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["outer_shadow_settings" ].inputs[9], "default_value", ],
        "highlight_shadow":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight" ].inputs[0], "default_value", ],
        "highlight_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight_intensity" ].color_ramp.elements[1], "position", ],
        "highlight_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight_colors" ].inputs[6], "default_value", ],
        "highlight_crease":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight_color" ].inputs[7], "default_value", ],
        "crease_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["crease_amount" ].inputs[0], "default_value", ],
        "highlight_contour":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight_colors" ].inputs[7], "default_value", ],
        "contour_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["contour_amount" ].inputs[0], "default_value", ],
        "highlight_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight_settings" ].inputs[6], "default_value", ],
        "highlight_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["highlight_settings" ].inputs[9], "default_value", ],
        "eyeliner_top_1":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_top_1" ].inputs[0], "default_value", ],
        "eyeliner_bottom_1":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_bottom_1" ].inputs[0], "default_value", ],
        "eyeliner_top_2":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_top_2" ].inputs[0], "default_value", ],
        "eyeliner_bottom_2":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_bottom_2" ].inputs[0], "default_value", ],
        "eyeliner_top_3":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_top_3" ].inputs[0], "default_value", ],
        "eyeliner_bottom_3":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_bottom_3" ].inputs[0], "default_value", ],
        "eyeliner_top_4":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_top_4" ].inputs[0], "default_value", ],
        "eyeliner_bottom_4":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_bottom_4" ].inputs[0], "default_value", ],
        "eyeliner_top_5":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_top_5" ].inputs[0], "default_value", ],
        "eyeliner_bottom_5":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_bottom_5" ].inputs[0], "default_value", ],
        "eyeliner_top_6":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_top_6" ].inputs[0], "default_value", ],
        "eyeliner_bottom_6":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_bottom_6" ].inputs[0], "default_value", ],
        "eyeliner_settings_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_settings" ].inputs[0], "default_value", ],
        "eyeliner_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_settings" ].inputs[6], "default_value", ],
        "eyeliner_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyeliner_settings" ].inputs[9], "default_value", ],
        "facial_paint_1":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_1" ].inputs[0], "default_value", ],
        "facial_paint_1_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_1_color" ].inputs[7], "default_value", ],
        "facial_paint_2":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_2" ].inputs[0], "default_value", ],
        "facial_paint_2_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_2_color" ].inputs[7], "default_value", ],
        "facial_paint_3":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_3" ].inputs[0], "default_value", ],
        "facial_paint_3_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_3_color" ].inputs[7], "default_value", ],
        "facial_paint_intensity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_intensity" ].color_ramp.elements[1], "position", ],
        "facial_paint_granularity":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_granularity" ].inputs[0], "default_value", ],
        "facial_paint_settings_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_settings" ].inputs[6], "default_value", ],
        "facial_paint_settings_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["facial_paint_settings" ].inputs[9], "default_value", ],
        "eyebrows_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyebrows" ].inputs[0], "default_value", ],
        "eyebrows_fade":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["eyebrows_fade" ].inputs[0], "default_value", ],
        "nail_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nail_amount" ].inputs[0], "default_value", ],
        "nail_polish_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nail_polish_color" ].inputs[7], "default_value", ],
        "nail_polish_metallic":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nail_polish" ].inputs[6], "default_value", ],
        "nail_polish_roughness":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nail_polish" ].inputs[9], "default_value", ],
        "nail_polish_coat":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nail_polish" ].inputs[14], "default_value", ],
        "nail_glitter":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nail_glitter" ].inputs[0], "default_value", ],
        "teeth_age":  [ lambda: bpy.data.materials["SM5 Teeth Material Transhuman" ].node_tree.nodes["teeth_age" ].outputs[0], "default_value", ],
        "teeth_saturation":  [ lambda: bpy.data.materials["SM5 Teeth Material Transhuman" ].node_tree.nodes["teeth_saturation" ].inputs[1], "default_value", ],
        "root_spread_1":  [ lambda: bpy.data.node_groups["SM5 Hair Color Transhuman" ].nodes["root_spread" ].color_ramp.elements[1], "position", ],
        "root_spread_0":  [ lambda: bpy.data.node_groups["SM5 Hair Color Transhuman" ].nodes["root_spread" ].color_ramp.elements[0], "position", ],
        "root_color_picker":  [ lambda: bpy.data.node_groups["SM5 Hair Color Transhuman" ].nodes["root_color_picker" ].outputs[0], "default_value", ],
        "hair_color_picker":  [ lambda: bpy.data.node_groups["SM5 Hair Color Transhuman" ].nodes["hair_color_picker" ].outputs[0], "default_value", ],
        "secondary_color_highlights":  [ lambda: bpy.data.node_groups["SM5 Hair Color Transhuman" ].nodes["secondary_hair_color_picker" ].outputs[0], "default_value", ],
        "secondary_intensity_1":  [ lambda: bpy.data.node_groups["SM5 Hair Color Transhuman" ].nodes["secondary_intensity" ].color_ramp.elements[1], "position", ],
        "tattoo_height":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["tattoo_height" ].inputs[0], "default_value", ],
        "tattoo_amount":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["tattoo_switch" ].inputs[0], "default_value", ],
        "beard_curls_switch":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["beard_curls_switch" ].inputs[1], "default_value", ],
        "beard_curls_scale":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["beard_curl_scale"].outputs[0],  "default_value", ],   
        "beard_noise":  [ lambda: bpy.data.node_groups["SM5 Beard Transhuman" ].nodes["beard_noise" ].outputs[0], "default_value", ],   
        "nipples_def":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nipple_def" ].color_ramp.elements[0], "position", ],
        "nipples_color":  [ lambda: bpy.data.materials["SM5 Skin Material Transhuman" ].node_tree.nodes["nipple_color" ].outputs[0], "default_value", ],
    },
    {
        "fem_face_1": [0, 0.2],
        "fem_face_2": [0, 0.2],
        "fem_face_3": [0, 0.2],
        "fem_face_4": [0, 0.2],
        "fem_face_5": [0, 0.2],
        "m_face_1": [0, 0.2],
        "m_face_2": [0, 0.2],
        "m_face_3": [0, 0.2],
        "m_face_4": [0, 0.2],
        "m_face_5": [0, 0.2],
        "face_length": [-1, 1],
        "face_width": [-1, 1],
        "face_concave": [0, 1],
        "face_convex": [0, 1],
        "forehead_protrusion": [-1, 1],
        "baby_face": [0, 1],
        "face_triangle": [0, 1],
        "face_inversend_triangle": [0, 1],
        "face_diamond": [0, 1],
        "face_rectangle": [0, 1],
        "face_oval": [0, 1],
        "face_round": [0, 1],
        "head_size": [-1, 1],
        "head_width": [-1, 1],
        "cheeks_plus_minus": [-1, 1],
        "cheeks_hollow": [0, 1],
        "chin_position": [0, 1],
        "cleft_chin": [0, 1],
        "chin_height": [-1, 1],
        "chin_width": [-1, 1],
        "chin_vertical": [-1, 1],
        "jaw_width": [-1, 1],
        "jaw_length": [-1, 1],
        "neck_girth": [-1, 1],
        "jowl": [-1, 1],
        "eye_grow": [0, 1],
        "eye_shrink": [0, 1],
        "eye_inward": [0, 1],
        "eye_outward": [0, 1],
        "eye_forward": [0, 1],
        "eye_backward": [0, 1],
        "eye_up": [0, 1],
        "eye_down": [0, 1],
        "eye_length": [0, 1],
        "eye_roundness": [0, 1],
        "eye_corner": [-1, 1],
        "eye_rotate": [-1, 1],
        "tearduct": [-1, 1],
        "tearduct_sharp": [0, 1],
        "eye_fold": [-1, 1],
        "eye_puff": [-1, 1],
        "eyebrows_up": [0, 1],
        "eyebrows_down": [0, 1],
        "eyebrows_head": [0, 1],
        "eyebrows_tail": [0, 1],
        "eyebrows_arch": [-1, 1],
        "eyebrows_rotate": [-1, 1],
        "eyebrows_dist": [-1, 1],
        "glabella": [-1, 1],
        "bridge": [-1, 1],
        "bridge_width": [-1, 1],
        "supratip": [-1, 1],
        "supratip_width": [-1, 1],
        "nose_tip_angle": [-1, 1],
        "nose_tip_shape": [-1, 1],
        "nose_tip_position": [-1, 1],
        "nose_tip_chisel": [-1, 1],
        "infratip": [-1, 1],
        "infratip_thickness": [-1, 1],
        "wings": [-1, 1],
        "wings_arch": [-1, 1],
        "nose_cleft": [0, 1],
        "nose_length": [-1, 1],
        "nose_width": [-1, 1],
        "nose_position": [-1, 1],
        "nose_height": [-1, 1],
        "mouth_position_1": [-1, 1],
        "mouth_position_2": [-1, 1],
        "mouth_size": [-1, 1],
        "mouth_width": [-1, 1],
        "lips_thickness": [-1, 1],
        "top_lip": [-1, 1],
        "bottom_lip": [-1, 1],
        "lip_top_border": [-1, 1],
        "lip_cupids_bow": [-1, 1],
        "lip_bottom_border": [-1, 1],
        "lip_bottom_cupids": [-1, 1],
        "lip_tubercles_top": [0, 1],
        "lip_tubercles_bottom": [0, 1],
        "lip_cleft": [-1, 1],
        "philtrum": [-1, 1],
        "lip_crease_top": [0, 1],
        "lip_crease_bottom": [0, 1],
        "ear_in": [0, 1],
        "ear_out": [0, 1],
        "ear_height": [-0.3, 0.3],
        "ear_depth": [-1, 1],
        "ear_size": [-1, 1],
        "ear_back": [0, 0.5],
        "ear_pointy": [0, 1],
    },
    [
        # {
        #     "keys": [
        #         "fem_face_1" , "fem_face_2" , "fem_face_3" , "fem_face_4" , "fem_face_5" , "m_face_1" , "m_face_2" , "m_face_3" , "m_face_4" , "m_face_5"
        #     ],
        #     "total": 0.9,
        # }
    ],
    sm5_addon_utils.get_addon_root(addon_name),
)
#fmt: on

def preset_prop(self, name, **kwargs):
    args = presetSaver.get_ext_prop(name)
    return self.prop(args[0](), args[1], **kwargs)


setattr(UILayout, "preset_prop", preset_prop)


def add_open_set_image(layout, material, node, group):
    op = layout.operator(
        "transhuman_operators.open_set_image",
        icon="FILE",
    )
    op.material = material
    op.node = node
    op.group = group


# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------
def get_image(image_name):
    if image_name in bpy.data.images:
        return bpy.data.images[image_name]
    return None

def set_selected_image(self, prop_name, material, node):
    bpy.data.materials[material].node_tree.nodes[node].image = get_image(
        getattr(self, prop_name)
    )

def set_selected_image_node_group(self, prop_name, node_group_name, node_name):
    bpy.data.node_groups[node_group_name].nodes[node_name].inputs[
        "Image"
    ].default_value = get_image(getattr(self, prop_name))

def set_selected_node_group(self, prop_name, material, node):
    bpy.data.materials[material].node_tree.nodes[node].node_tree = bpy.data.node_groups[
        getattr(self, prop_name)
    ]

def set_selected_node_group(self, prop_name, material, node):
    bpy.data.materials[material].node_tree.nodes[node].node_tree = bpy.data.node_groups[
        getattr(self, prop_name)
    ]

def create_image_select_multi(
    prop_name,
    targets,
    image_prefix=None,
    image_suffix=None,
    description="Select base color"
):
    def handle_target(self, target):
        if "material" in target and "node" in target:
            return set_selected_image(self, prop_name, target['material'], target['node'])
        elif "node_group_name" in target and "node_name" in target:
            return set_selected_image_node_group(
                self, prop_name, target['node_group_name'], target['node_name']
            )

    update = lambda self, context: None if [
        handle_target(self, target) for target in targets
    ] else None

    return bpy.props.EnumProperty(
        items=lambda self, context: [
            (image.name, image.name, image.name)
            for image in bpy.data.images
            if (image_prefix is None or image.name.startswith(image_prefix))
            and (image_suffix is None or image.name.endswith(image_suffix))
        ],
        description=description,
        update=update,
    )

def create_image_select(
    prop_name,
    material=None,
    node=None,
    image_prefix=None,
    image_suffix=None,
    description="Select base color",
    node_group_name=None,
    node_name=None,
):
    update = lambda self, context: set_selected_image(self, prop_name, material, node)
    if node_group_name is not None:
        update = lambda self, context: set_selected_image_node_group(
            self, prop_name, node_group_name, node_name
        )

    return bpy.props.EnumProperty(
        items=lambda self, context: [
            (image.name, image.name, image.name)
            for image in bpy.data.images
            if (image_prefix is None or image.name.startswith(image_prefix))
            and (image_suffix is None or image.name.endswith(image_suffix))
        ],
        description=description,
        update=update,
    )

def create_mixamo_select():
    return bpy.props.EnumProperty(
        items=[
            ('Mixamo', 'Mixamo', 'Mixamo'),
            ('IK/FK', 'IK/FK', 'IK/FK'),
        ],
        description="",
        default='Mixamo',
        update=lambda self, context: update_mixamo(self, context)
    )

def create_face_rig_select():
    return bpy.props.EnumProperty(
        items=[
            ('FACE_RIG', 'Face rig', 'Face rig'),
            ('MOCAP', 'Mocap (add mocap data in animation panel)', 'Mocap'),
        ],
        description="",
        default='FACE_RIG',
        update=lambda self, context: update_face_rig(self.face_rig)
    )

def create_persona_select(prop_name, description="Select Persona"):
    persona_prefix = "SM5 Persona"
    persona_suffix = None

    def update(self, context):
        bpy.data.node_groups["SM5 Persona Selector"].nodes[
            "imported_persona_mesh"
        ].inputs[0].default_value = bpy.data.objects[getattr(self, prop_name)]

    return bpy.props.EnumProperty(
        items=lambda self, context: [
            (objects.name, objects.name, objects.name)
            for objects in bpy.data.objects
            if (persona_prefix is None or objects.name.startswith(persona_prefix))
            and (persona_suffix is None or objects.name.endswith(persona_suffix))
        ],
        description=description,
        update=update,
    )

def create_vertex_select(
    prop_name,
    material,
    node,
    image_prefix=None,
    image_suffix=None,
    description="Select base color",
):
    return bpy.props.EnumProperty(
        items=lambda self, context: [
            (image.name, image.name, image.name)
            for image in bpy.data.images
            if (image_prefix is None or image.name.startswith(image_prefix))
            and (image_suffix is None or image.name.endswith(image_suffix))
        ],
        description=description,
        update=lambda self, context: set_selected_image(
            self, prop_name, material, node
        ),
    )

def create_node_group_select(
    prop_name, material, node, prefix=None, suffix=None, description="Select base color"
):
    return bpy.props.EnumProperty(
        items=lambda self, context: [
            (ng.name, ng.name, ng.name)
            for ng in bpy.data.node_groups
            if (prefix is None or ng.name.startswith(prefix))
            and (suffix is None or ng.name.endswith(suffix))
        ],
        description=description,
        update=lambda self, context: set_selected_node_group(
            self, prop_name, material, node
        ),
    )

def create_node_group_select(
    prop_name, material, node, prefix=None, suffix=None, description="Select base color"
):
    return bpy.props.EnumProperty(
        items=lambda self, context: [
            (ng.name, ng.name, ng.name)
            for ng in bpy.data.node_groups
            if (prefix is None or ng.name.startswith(prefix))
            and (suffix is None or ng.name.endswith(suffix))
        ],
        description=description,
        update=lambda self, context: set_selected_node_group(
            self, prop_name, material, node
        ),
    )

def set_subdivision_level_value(level_value, for_render):
    level_prop = "render_levels" if for_render else "levels"
    setattr(bpy.data.objects["SM5 Transhuman"].modifiers["Subdivision"], level_prop, level_value)
    levels = ['LV0', 'LV1', 'LV2', 'LV3']
    objects = ['SM5 Transhuman Underwear Top', 'SM5 Transhuman Underwear Bottom', 'SM5 Scalp Transhuman']

    show_prop = "show_render" if for_render else "show_viewport"
    for object in objects:
        for level in levels:
            setattr(bpy.data.objects[object].modifiers[level], show_prop, False)
        setattr(bpy.data.objects[object].modifiers[levels[level_value]], show_prop, True)


def update_mixamo(self, context):
    v = self.mixamo_mode
    objects_to_hide = [
        'SM5 Armature Transhuman',
        'SM5 Armature IK/FK Transhuman'
    ]
    for obj in objects_to_hide:
        bpy.data.objects[obj].hide_render = True
        bpy.data.objects[obj].hide_viewport = True

    target = ''
    if v == 'Mixamo':
        target = objects_to_hide[0]
    elif v == 'IK/FK':
        target = objects_to_hide[1]
    else:
        print('unknwon mixamo mode')
        return
    
    obj = bpy.data.objects[target]
    obj.hide_render = False
    obj.hide_viewport = False

    objects_for_modifier_update = [
        'SM5 Transhuman',
        'SM5 Teeth Transhuman',
        'SM5 Nails Transhuman',
        'SM5 Female Genitals Transhuman',
        'SM5 Scalp Transhuman',
    ]
    for obj_for_modifier in objects_for_modifier_update:
        bpy.data.objects[obj_for_modifier].modifiers["Armature"].object = obj

    objects_for_constraint_update = [
        'SM5 Male Genitals Rig Transhuman',
        'SM5 Face Armature Transhuman',
    ]
    for obj_for_constraint in objects_for_constraint_update:
        bpy.data.objects[obj_for_constraint].constraints["Child Of"].target = obj

    bpy.data.objects["SM5 Toes Armature Transhuman"].pose.bones[
        "SM5-toes-R"
    ].constraints["Child Of"].target = obj

    bpy.data.objects["SM5 Toes Armature Transhuman"].pose.bones[
        "SM5-toes-L"
    ].constraints["Child Of"].target = obj

def update_face_rig(face_rig):
    eye_objects = [
        "SM5 Eyes Target Transhuman",
        "SM5 Eyes Left Target",
        "SM5 Eyes Right Target",
    ]
    is_mocap = face_rig == 'MOCAP'
    for eye_object in eye_objects:
        bpy.data.objects[eye_object].hide_viewport = not is_mocap
        bpy.data.objects[eye_object].hide_render = not is_mocap

    set_face_rig_switch_value(face_rig == 'FACE_RIG')

def set_face_rig_switch_value(value):
    bpy.data.objects[
        "SM5 Face Armature Transhuman"
    ].hide_viewport = not value
    bpy.data.objects[
        "SM5 Face Armature Transhuman"
    ].hide_render = not value
    bpy.data.objects["SM5 Face Armature Transhuman"].pose.bones[
        "SM5-eyes-cntrl-L"
    ].constraints["Copy Location"].enabled = not value
    bpy.data.objects["SM5 Face Armature Transhuman"].pose.bones[
        "SM5-eyes-cntrl"
    ].constraints["Copy Location"].enabled = not value
    bpy.data.objects["SM5 Face Armature Transhuman"].pose.bones[
        "SM5-eyes-cntrl-R"
    ].constraints["Copy Location"].enabled = not value

    for driver in bpy.data.objects[
        "SM5 Transhuman"
    ].data.shape_keys.animation_data.drivers:
        driver.mute = not value
    for driver in bpy.data.objects[
        "SM5 Teeth Transhuman"
    ].data.shape_keys.animation_data.drivers:
        driver.mute = not value

def set_persona_switch_value(self, context):
    bpy.data.node_groups["SM5 Persona Selector"].nodes[
        "mute_persona"
    ].mute = not self.persona_switch
    bpy.data.node_groups["SM5 Transhuman Normal"].nodes[
        "male_base_normal"
    ].mute = not self.persona_switch
    bpy.data.node_groups["SM5 Transhuman Normal"].nodes[
        "female_base_normal"
    ].mute = not self.persona_switch
    bpy.data.node_groups["SM5 Body Displacement"].nodes[
        "male_base_displ"
    ].mute = not self.persona_switch
    bpy.data.node_groups["SM5 Body Displacement"].nodes[
        "female_base_displ"
    ].mute = not self.persona_switch
    bpy.data.node_groups["SM5 Body Displacement"].nodes[
        "persona_displ_val"
    ].mute = not self.persona_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "persona_displ_skin_mute"
    ].mute = not self.persona_switch

def set_clothes_adjust_switch_value(self, context):
    bpy.data.node_groups["SM5 Face Customization Import"].nodes[
        "clothes_adjust"
    ].mute = not self.clothes_adjust_switch

def set_hide_armatures_value(self, context):
    bpy.data.collections["Transhuman - RIGS"].hide_viewport = self.hide_armatures

def set_hide_body_hairs_value(self, context):
    bpy.data.collections["BODY HAIR CURVES"].hide_viewport = self.hide_body_hairs

def set_hide_hair_wig_value(self, context):
    bpy.data.collections["WIGS"].hide_viewport = self.hide_hair_wig

def set_hide_render_hair_wig_value(self, context):
    bpy.data.collections[
        "WIGS"
    ].hide_render = self.hide_render_hair_wig

def set_face_prop_value(self, context):
    bpy.data.objects[
        "SM5 Face Proportions"
    ].hide_viewport = not self.face_prop

def set_dynamic_breasts_value(self, context):
    bpy.data.objects["SM5 Transhuman"].modifiers["Dynamic Breasts"].show_viewport = self.dynamic_breasts
    bpy.data.objects["SM5 Transhuman"].modifiers["Dynamic Breasts"].show_render = self.dynamic_breasts

def set_dynamic_wrinkles_value(self, context):
    bpy.data.objects["SM5 Transhuman"].modifiers["Dynamic Wrinkles"].show_viewport = self.dynamic_wrinkles
    bpy.data.objects["SM5 Transhuman"].modifiers["Dynamic Wrinkles"].show_render = self.dynamic_wrinkles

def set_eyelashes_clump_switch_value(self, context):
    bpy.data.node_groups["SM5 Top Eyelashes Transhuman"].nodes[
        "clump_mute"
    ].mute = not self.eyelashes_clump_switch

def set_body_hair_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "body_hair_height"
    ].inputs[0].default_value = (1 if self.body_hair_switch else 0)
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "body_hair_mute"
    ].mute = not self.body_hair_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "body_hair_bump"
    ].mute = not self.body_hair_switch

def set_subdermal_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "subdermal_dynamic"
    ].mute = not self.subdermal_switch

def set_flip_displ_switch_value(self, context):
    bpy.data.node_groups["SM5 Transhuman Normal"].nodes[
        "flip_persona_displ"
    ].mute = not self.flip_displ_switch

def set_stubble_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "stubble_mute"
    ].mute = not self.stubble_switch

def set_stubble_trim_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "stubble_trim"
    ].mute = not self.stubble_trim_switch

def set_age_switch_value(self, context):
    bpy.data.node_groups["SM5 Body Displacement"].nodes["age_displ"].inputs[
        0
    ].default_value = self.old_age_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "old_age_height"
    ].inputs[0].default_value = self.old_age_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "old_age_color"
    ].inputs[0].default_value = self.old_age_switch

def set_scars_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "scars_color_mute"
    ].mute = not self.scars_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "scars_height_mute"
    ].mute = not self.scars_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "scars_roughness_mute"
    ].mute = not self.scars_switch

def set_tattoo_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "tattoo_switch"
    ].mute = not self.tattoo_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "tattoo_color"
    ].mute = not self.tattoo_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "tattoo_height"
    ].mute = not self.tattoo_switch

def set_base_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "base_mute"
    ].mute = not self.base_switch

def set_blush_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "blush_mute"
    ].mute = not self.blush_switch

def set_lips_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "lips_mute"
    ].mute = not self.lips_switch

def set_lip_liner_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "lip_liner_mute"
    ].mute = not self.lip_liner_switch
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "lip_liner_gloss_mute"
    ].mute = not self.lip_liner_switch

def set_eyeshadow_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "eyeshadow_mute"
    ].mute = not self.eyeshadow_switch


def set_lashline_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "lashline_mute"
    ].mute = not self.lashline_switch

def set_inner_shadow_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "inner_shadow_mute"
    ].mute = not self.inner_shadow_switch

def set_outer_shadow_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "outer_shadow_mute"
    ].mute = not self.outer_shadow_switch

def set_highlight_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "highlight_mute"
    ].mute = not self.highlight_switch

def set_eyeliner_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "eyeliner_mute"
    ].mute = not self.eyeliner_switch

def set_facial_paint_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "facial_paint_mute"
    ].mute = not self.facial_paint_switch

def set_eyebrows_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "eyebrows_mute"
    ].mute = not self.eyebrows_switch

def set_nails_switch_value(self, context):
    bpy.data.materials["SM5 Skin Material Transhuman"].node_tree.nodes[
        "nail_polish_mute"
    ].mute = not self.nails_switch

def set_mix_value(material_name, node_name, value):
    bpy.data.materials[material_name].node_tree.nodes[node_name].inputs[
        0
    ].default_value = value

def set_node_group_value(node_group_name, node_name, value):
    bpy.data.node_groups[node_group_name].nodes[node_name].inputs[
        0
    ].default_value = value

def set_secondary_body_hair_switch_value(self, context):
    bpy.data.materials["SM5 Body Hair Particle Material"].node_tree.nodes[
        "secondary_body_color_mute"
    ].mute = not self.secondary_body_hair_switch
    bpy.data.materials["SM5 Body Hair Mesh Material"].node_tree.nodes[
        "secondary_body_color_mute"
    ].mute = not self.secondary_body_hair_switch

def set_secondary_beard_switch_value(self, context):
    bpy.data.materials["SM5 Beard Particle Material"].node_tree.nodes[
        "secondary_beard_color_mute"
    ].mute = not self.secondary_beard_switch
    bpy.data.materials["SM5 Hair Mesh Beard Material"].node_tree.nodes[
        "secondary_beard_color_mute"
    ].mute = not self.secondary_beard_switch

def set_highlights_switch_value(self, context):
    bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes[
        "secondary_color_mute"
    ].mute = not self.highlights_switch
    bpy.data.materials["SM5 Hair Mesh Short Material"].node_tree.nodes[
        "secondary_color_mute"
    ].mute = not self.highlights_switch
    bpy.data.materials["SM5 Hair Feigned Curls Material"].node_tree.nodes[
        "secondary_color_mute"
    ].mute = not self.highlights_switch
    bpy.data.materials["SM5 Hair Mesh Loose Material"].node_tree.nodes[
        "secondary_color_mute"
    ].mute = not self.highlights_switch
    bpy.data.materials["SM5 Hair Particle Material"].node_tree.nodes[
        "secondary_color_mute"
    ].mute = not self.highlights_switch

def set_root_switch_value(self, context):
    bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes[
        "root_mute"
    ].mute = not self.root_switch
    bpy.data.materials["SM5 Hair Mesh Short Material"].node_tree.nodes[
        "root_mute"
    ].mute = not self.root_switch
    bpy.data.materials["SM5 Hair Feigned Curls Material"].node_tree.nodes[
        "root_mute"
    ].mute = not self.root_switch
    bpy.data.materials["SM5 Hair Mesh Loose Material"].node_tree.nodes[
        "root_mute"
    ].mute = not self.root_switch
    bpy.data.materials["SM5 Hair Particle Material"].node_tree.nodes[
        "root_mute"
    ].mute = not self.root_switch

def set_root_invert_value(self, context):
    bpy.data.node_groups["SM5 Hair Color Transhuman"].nodes[
        "root_invert"
    ].mute = not self.root_invert
    
def set_mesh_thickness_value(self,context):
    bpy.data.materials["SM5 Hair Mesh Material"].node_tree.nodes[
        "mesh_thickness"
        ].inputs[1].default_value = self.mesh_thickness
    bpy.data.materials["SM5 Hair Mesh Loose Material"].node_tree.nodes[
        "mesh_thickness"
        ].inputs[1].default_value = self.mesh_thickness
    bpy.data.materials["SM5 Hair Feigned Curls Material"].node_tree.nodes[
        "mesh_thickness"
        ].inputs[1].default_value = self.mesh_thickness
    bpy.data.materials["SM5 Hair Mesh Short Material"].node_tree.nodes[
        "mesh_thickness"
    ].inputs[1].default_value = self.mesh_thickness

def refresh_gender_definition(context):
    f_base = context.scene.Transhuman_tool["female_base"]
    m_base = context.scene.Transhuman_tool["male_base"]
    divide_by = f_base + m_base

    if divide_by == 0:
        value = 0.5
    else:
        value = m_base / divide_by
    setattr(context.scene.Transhuman_tool, "gender_definition", value)

def create_linked_props(
    prop_name,
    mesh_and_keys=[],
    max=1,
    min=0,
    update=None,
    neg_mesh_and_keys=None,
    bool=False,
    integer=False,
    objects=[],
    obj_and_modifiers=[],
):
    negative = neg_mesh_and_keys is not None and len(neg_mesh_and_keys) > 0

    def set_value_of_key(self, context):
        value = self[prop_name]
        pos_value = value
        neg_value = -value
        if negative and value < 0:
            pos_value = 0
        if negative and value > 0:
            neg_value = 0

        def set(mk, new_value):
            for mesh_key in mk:
                mesh = mesh_key[0]
                key = mesh_key[1]
                if bool:
                    bpy.data.shape_keys[mesh].key_blocks[key].mute = new_value == 0
                else:
                    bpy.data.shape_keys[mesh].key_blocks[key].value = new_value

        set(mesh_and_keys, pos_value)
        bool_value = pos_value == 0
        for obj in objects:
            bpy.data.objects[obj].hide_render = bool_value
            bpy.data.objects[obj].hide_viewport = bool_value
        for obj, modifier in obj_and_modifiers:
            bpy.data.objects[obj].modifiers[modifier].show_render = not bool_value
            bpy.data.objects[obj].modifiers[modifier].show_viewport = not bool_value

        if negative:
            set(neg_mesh_and_keys, neg_value)

        if update is not None:
            updates = []

            if not hasattr(update, "__len__"):
                updates = [update]
            else:
                updates = update

            for update_item in updates:
                if callable(update_item):
                    num_of_params = update_item.__code__.co_argcount
                    if num_of_params == 2:
                        update_item(self, context)
                    else:
                        update_item(value)

    if bool:
        return bpy.props.BoolProperty(
            name="", update=lambda self, context: set_value_of_key(self, context)
        )
    if integer:
        return bpy.props.IntProperty(
            name="",
            min=min,
            max=max,
            update=lambda self, context: set_value_of_key(self, context),
        )
    return bpy.props.FloatProperty(
        name="",
        max=max,
        min=-max if negative else min,
        update=lambda self, context: set_value_of_key(self, context),
    )

def create_shape_key_prop(prop_name, mesh_name, key_name, max=1, min=0, update=None):
    return create_linked_props(
        prop_name, [[mesh_name, key_name]], max=max, min=min, update=update
    )

def create_pos_neg_shape_key_prop(prop_name, mesh_name, pos_key, neg_key, max=2):
    return create_pos_neg_shape_key_prop_multi(
        prop_name, [[mesh_name, pos_key, neg_key]], max
    )

def create_pos_neg_shape_key_prop_multi(prop_name, mesh_keys_arr, max=2):
    def set_value_of_key(self, context):
        value = self[prop_name]
        for mesh_keys in mesh_keys_arr:
            mesh = mesh_keys[0]
            pos_key = mesh_keys[1]
            neg_key = mesh_keys[2]
            skeys = bpy.data.shape_keys[mesh].key_blocks
            if value >= 0:
                skeys[pos_key].value = value
                skeys[neg_key].value = 0
            elif value < 0:
                skeys[neg_key].value = -value
                skeys[pos_key].value = 0

    return bpy.props.FloatProperty(
        name="",
        max=max,
        min=-max,
        update=lambda self, context: set_value_of_key(self, context),
    )

class Transhuman_Properties(bpy.types.PropertyGroup):
    mixamo_mode: create_mixamo_select()

    hide_armatures: create_linked_props(
        "hide_armatures",
        [],
        update=lambda self, context: set_hide_armatures_value(self, context),
        bool=True,
    )

    hide_body_hairs: create_linked_props(
        "hide_body_hairs",
        [],
        update=lambda self, context: set_hide_body_hairs_value(self, context),
        bool=True,
    )

    hide_hair_wig: create_linked_props(
        "hide_hair_wig",
        [],
        update=lambda self, context: set_hide_hair_wig_value(self, context),
        bool=True,
    )

    hide_render_hair_wig: create_linked_props(
        "hide_render_hair_wig",
        [],
        update=lambda self, context: set_hide_render_hair_wig_value(self, context),
        bool=True,
    )

    face_prop: create_linked_props(
        "face_prop",
        [],
        update=lambda self, context: set_face_prop_value(self, context),
        bool=True,
    )

    subdivision_level: create_linked_props(
        "subdivision_level",
        [],
        update=lambda self, context: set_subdivision_level_value(self.subdivision_level, False),
        integer=True,
        min=0,
        max=3
    )

    subdivision_level_for_render: create_linked_props(
        "subdivision_level_for_render",
        [],
        update=lambda self, context: set_subdivision_level_value(self.subdivision_level_for_render, True),
        integer=True,
        min=0,
        max=3
    )
    
    dynamic_breasts: create_linked_props(
        "dynamic_breasts",
        [],
        update=lambda self, context: set_dynamic_breasts_value(self, context),
        bool=True,
    )

    dynamic_wrinkles: create_linked_props(
        "dynamic_wrinkles",
        [],
        update=lambda self, context: set_dynamic_wrinkles_value(self, context),
        bool=True,
    )

    face_rig: create_face_rig_select()

    toes_rig: create_linked_props(
        "toes_rig", [], objects=["SM5 Toes Armature Transhuman"], bool=True
    )

    gen_rig: create_linked_props(
        "gen_rig", [], objects=["SM5 Male Genitals Rig Transhuman"], bool=True
    )

    underwear_top_switch: create_linked_props(
        "underwear_top_switch", [], objects=["SM5 Transhuman Underwear Top"], bool=True
    )

    underwear_bottom_switch: create_linked_props(
        "underwear_bottom_switch",
        [],
        objects=["SM5 Transhuman Underwear Bottom"],
        bool=True,
    )

    body_hair_image: create_image_select(
        "body_hair_image",
        image_suffix="Hair",
        material="SM5 Skin Material Transhuman",
        node="body_hair_image_input",
        description="Select body hair type",
    )

    stubble_image: create_image_select(
        "stubble_image",
        image_suffix="Stubble",
        material="SM5 Skin Material Transhuman",
        node="stubble_image_input",
        description="Select stubble type",
    )

    eye_base_image: create_image_select(
        "eye_base_image",
        image_suffix="Eyes",
        material="SM5 Eyes Material Transhuman",
        node="eye_color",
        description="Select base color texture",
    )

    pupil_switch: create_shape_key_prop(
        "pupil_switch", "Eye Shape Keys Transhuman", "Pupil", max=1
    )

    iris: create_pos_neg_shape_key_prop(
        "iris",
        "Eye Shape Keys Transhuman",
        "Iris +",
        "Iris -",
    )

    pupil_cat: create_linked_props(
        "pupil_cat",
        [
            ["Eye Shape Keys Transhuman", "Cat"],
        ],
    )

    pupil_goat: create_linked_props(
        "pupil_goat",
        [
            ["Eye Shape Keys Transhuman", "Goat"],
        ],
    )

    pupil_star: create_linked_props(
        "pupil_star",
        [
            ["Eye Shape Keys Transhuman", "Star"],
        ],
    )

    persona_switch: bpy.props.BoolProperty(
        name="Load Persona",
        update=lambda self, context: set_persona_switch_value(self, context),
    )
    
    clothes_adjust_switch: bpy.props.BoolProperty(
        name="Clothes Adjust (Animation)",
        update=lambda self, context: set_clothes_adjust_switch_value(self, context),
    )

    eyelashes_clump_switch: bpy.props.BoolProperty(
        name="Clump",
        update=lambda self, context: set_eyelashes_clump_switch_value(self, context),
    )

    body_hair_switch: bpy.props.BoolProperty(
        name="On / Off",
        update=lambda self, context: set_body_hair_switch_value(self, context),
    )

    subdermal_switch: bpy.props.BoolProperty(
        name="Subdermal (Off - Simple / On - Adaptive)",
        update=lambda self, context: set_subdermal_switch_value(self, context),
    )

    flip_displ_switch: bpy.props.BoolProperty(
        name="Only Face / Body",
        update=lambda self, context: set_flip_displ_switch_value(self, context),
    )

    stubble_switch: bpy.props.BoolProperty(
        name="On / Off",
        update=lambda self, context: set_stubble_switch_value(self, context),
    )

    stubble_trim_switch: bpy.props.BoolProperty(
        name="Groom stubble",
        update=lambda self, context: set_stubble_trim_switch_value(self, context),
    )

    scars_switch: bpy.props.BoolProperty(
        name="Scars", update=lambda self, context: set_scars_switch_value(self, context)
    )

    scars_selector: create_node_group_select(
        "scars_selector",
        suffix="Scars",
        material="SM5 Skin Material Transhuman",
        node="scars_selector",
        description="Select scars",
    )

    tattoo_switch: bpy.props.BoolProperty(
        name="Tattoo",
        update=lambda self, context: set_tattoo_switch_value(self, context),
    )

    base_switch: bpy.props.BoolProperty(
        name="Base", update=lambda self, context: set_base_switch_value(self, context)
    )

    blush_switch: bpy.props.BoolProperty(
        name="Blush", update=lambda self, context: set_blush_switch_value(self, context)
    )

    lips_switch: bpy.props.BoolProperty(
        name="Lips", update=lambda self, context: set_lips_switch_value(self, context)
    )

    lip_liner_switch: bpy.props.BoolProperty(
        name="Lip liner",
        update=lambda self, context: set_lip_liner_switch_value(self, context),
    )

    eyeshadow_switch: bpy.props.BoolProperty(
        name="Eyeshadow",
        update=lambda self, context: set_eyeshadow_switch_value(self, context),
    )

    lashline_switch: bpy.props.BoolProperty(
        name="Lashline",
        update=lambda self, context: set_lashline_switch_value(self, context),
    )

    inner_shadow_switch: bpy.props.BoolProperty(
        name="Inner corner shadow",
        update=lambda self, context: set_inner_shadow_switch_value(self, context),
    )

    outer_shadow_switch: bpy.props.BoolProperty(
        name="Outer corner shadow",
        update=lambda self, context: set_outer_shadow_switch_value(self, context),
    )

    highlight_switch: bpy.props.BoolProperty(
        name="Highlight",
        update=lambda self, context: set_highlight_switch_value(self, context),
    )

    eyeliner_switch: bpy.props.BoolProperty(
        name="Eyeliner",
        update=lambda self, context: set_eyeliner_switch_value(self, context),
    )

    facial_paint_switch: bpy.props.BoolProperty(
        name="Facial Paint",
        update=lambda self, context: set_facial_paint_switch_value(self, context),
    )

    eyebrows_switch: bpy.props.BoolProperty(
        name="Eyebrows",
        update=lambda self, context: set_eyebrows_switch_value(self, context),
    )

    nails_switch: bpy.props.BoolProperty(
        name="Nail polish",
        update=lambda self, context: set_nails_switch_value(self, context),
    )

    eyebrow_base_image: create_image_select(
        "eyebrow_base_image",
        image_prefix="Eyebrow",
        material="SM5 Skin Material Transhuman",
        node="eyebrow_type",
        description="Select eyebrow type",
    )

    old_age_switch: bpy.props.FloatProperty(
        name="",
        update=lambda self, context: set_age_switch_value(self, context),
        max=1,
        min=0,
    )

    mesh_thickness: bpy.props.FloatProperty(
        name="",
        update=lambda self, context: set_mesh_thickness_value(self, context),
    )

    imported_persona_mesh: create_persona_select("imported_persona_mesh")

    imported_persona_skin: create_node_group_select(
        "imported_persona_skin",
        suffix="Skin",
        material="SM5 Skin Material Transhuman",
        node="skin_selector",
        description="Select Skin",
    )

    imported_persona_displ: create_image_select_multi(
        "imported_persona_displ",
        image_suffix="Displacement",
        description="Select Displacement",
        targets=[
            {
                "material": "SM5 Skin Material Transhuman",
                "node": "persona_displ_skin",
            },
            {
                "node_group_name": "SM5 Body Displacement",
                "node_name": "persona_displ",
            }
        ]
    )

    male_base: create_linked_props(
        "male_base",
        [
            ["Transhuman Keys Rest", "Male Base"],
            ["Female Genitals Shape Keys", "Male Base"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "male_base_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "male_base_displ", value
            ),
            lambda _, context: refresh_gender_definition(context),
        ],
    )

    female_base: create_linked_props(
        "female_base",
        [
            ["Transhuman Keys Rest", "Female Base"],
            ["Female Genitals Shape Keys", "Female Base"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "female_base_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "female_base_displ", value
            ),
            lambda _, context: refresh_gender_definition(context),
        ],
    )

    male_weight_plus: create_linked_props(
        "male_weight_plus",
        [
            ["Transhuman Keys Rest", "Male Weight +"],
            ["Female Genitals Shape Keys", "Male Weight +"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "male_weight_plus_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "male_weight_plus_displ", value
            ),
        ],
    )

    male_weight_minus: create_linked_props(
        "male_weight_minus",
        [
            ["Transhuman Keys Rest", "Male Weight -"],
            ["Female Genitals Shape Keys", "Male Weight -"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "male_weight_minus_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "male_weight_minus_displ", value
            ),
        ],
    )

    male_muscles: create_linked_props(
        "male_muscles",
        [
            ["Transhuman Keys Rest", "Male Muscles"],
            ["Female Genitals Shape Keys", "Male Muscles"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "male_muscles_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "male_muscles_displ", value
            ),
        ],
    )

    female_weight_plus: create_linked_props(
        "female_weight_plus",
        [
            ["Transhuman Keys Rest", "Female Weight +"],
            ["Female Genitals Shape Keys", "Female Weight +"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "female_weight_plus_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "female_weight_plus_displ", value
            ),
        ],
    )

    female_weight_minus: create_linked_props(
        "female_weight_minus",
        [
            ["Transhuman Keys Rest", "Female Weight -"],
            ["Female Genitals Shape Keys", "Female Weight -"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "female_weight_minus_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "female_weight_minus_displ", value
            ),
        ],
    )

    female_muscles: create_linked_props(
        "female_muscles",
        [
            ["Transhuman Keys Rest", "Female Muscles"],
            ["Female Genitals Shape Keys", "Female Muscles"],
        ],
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "female_muscles_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "female_muscles_displ", value
            ),
        ],
    )

    gender_definition: create_linked_props(
        "gender_definition",
        max=1,
        update=[
            lambda value: set_node_group_value(
                "SM5 Transhuman Normal", "gender_switch_normal", value
            ),
            lambda value: set_node_group_value(
                "SM5 Body Displacement", "gender_switch_displ", value
            ),
            lambda value: set_node_group_value(
                "SM5 Transhuman Skin", "gender_switch_displ", value
            ),
        ],
    )

    teeth_gap_top: create_shape_key_prop(
        "teeth_gap_top",
        "Teeth Shape Keys",
        "Teeth Gap Top",
    )

    teeth_gap_bottom: create_shape_key_prop(
        "teeth_gap_bottom",
        "Teeth Shape Keys",
        "Teeth Gap Bottom",
    )

    crooked_teeth_top: create_shape_key_prop(
        "crooked_teeth_top",
        "Teeth Shape Keys",
        "Teeth Crooked Top",
    )

    crooked_teeth_bottom: create_shape_key_prop(
        "crooked_teeth_bottom",
        "Teeth Shape Keys",
        "Teeth Crooked Bottom",
    )

    missing_11: create_linked_props(
        "missing_11",
        [
            ["Teeth Shape Keys", "Teeth Missing 11"],
        ],
        bool=True,
    )

    missing_10: create_linked_props(
        "missing_10",
        [
            ["Teeth Shape Keys", "Teeth Missing 10"],
        ],
        bool=True,
    )

    missing_9: create_linked_props(
        "missing_9",
        [
            ["Teeth Shape Keys", "Teeth Missing 9"],
        ],
        bool=True,
    )

    missing_8: create_linked_props(
        "missing_8",
        [
            ["Teeth Shape Keys", "Teeth Missing 8"],
        ],
        bool=True,
    )

    missing_7: create_linked_props(
        "missing_7",
        [
            ["Teeth Shape Keys", "Teeth Missing 7"],
        ],
        bool=True,
    )

    missing_6: create_linked_props(
        "missing_6",
        [
            ["Teeth Shape Keys", "Teeth Missing 6"],
        ],
        bool=True,
    )

    missing_27: create_linked_props(
        "missing_27",
        [
            ["Teeth Shape Keys", "Teeth Missing 27"],
        ],
        bool=True,
    )

    missing_26: create_linked_props(
        "missing_26",
        [
            ["Teeth Shape Keys", "Teeth Missing 26"],
        ],
        bool=True,
    )

    missing_25: create_linked_props(
        "missing_25",
        [
            ["Teeth Shape Keys", "Teeth Missing 25"],
        ],
        bool=True,
    )

    missing_24: create_linked_props(
        "missing_24",
        [
            ["Teeth Shape Keys", "Teeth Missing 24"],
        ],
        bool=True,
    )

    missing_23: create_linked_props(
        "missing_23",
        [
            ["Teeth Shape Keys", "Teeth Missing 23"],
        ],
        bool=True,
    )

    missing_22: create_linked_props(
        "missing_22",
        [
            ["Teeth Shape Keys", "Teeth Missing 22"],
        ],
        bool=True,
    )

    teeth_length: create_pos_neg_shape_key_prop(
        "teeth_length",
        "Teeth Shape Keys",
        "Teeth Length +",
        "Teeth Length -",
    )

    teeth_size: create_pos_neg_shape_key_prop(
        "teeth_size",
        "Teeth Shape Keys",
        "Teeth Size +",
        "Teeth Size -",
    )
    
    denture_height: create_pos_neg_shape_key_prop_multi(
        "denture_height",
        [
            ["Teeth Shape Keys", "Denture Height +", "Denture Height -"],
            ["Transhuman Keys Rest", "Denture Height +", "Denture Height -"],
        ],
    )

    denture_position: create_pos_neg_shape_key_prop_multi(
        "denture_position",
        [
            ["Teeth Shape Keys", "Denture Forward", "Denture Backward"],
            ["Transhuman Keys Rest", "Denture Forward", "Denture Backward"],
        ],
    )

    fangs_top: create_shape_key_prop(
        "fangs_top",
        "Teeth Shape Keys",
        "Fangs Top",
    )

    fangs_bottom: create_shape_key_prop(
        "fangs_bottom",
        "Teeth Shape Keys",
        "Fangs Bottom",
    )

    feet_male: create_linked_props(
        "feet_male",
        [
            ["Transhuman Keys Rest", "Feet Male"],
        ],
    )

    feet_female: create_linked_props(
        "feet_female",
        [
            ["Transhuman Keys Rest", "Feet Female"],
        ],
    )

    hand_male: create_linked_props(
        "hand_male",
        [
            ["Transhuman Keys Rest", "Hand Male"],
            ["Transhuman Nails Keys", "Hand Male"],
        ],
    )

    hand_female: create_linked_props(
        "hand_female",
        [
            ["Transhuman Keys Rest", "Hand Female"],
            ["Transhuman Nails Keys", "Hand Female"],
        ],
    )

    hand_neutral: create_linked_props(
        "hand_neutral",
        [
            ["Transhuman Keys Rest", "Hand Neutral"],
            ["Transhuman Nails Keys", "Hand Neutral"],
        ],
    )

    hand_elder: create_linked_props(
        "hand_elder",
        [
            ["Transhuman Keys Rest", "Hand Elder"],
            ["Transhuman Nails Keys", "Hand Elder"],
        ],
    )

    eye_grow: create_linked_props(
        "eye_grow",
        [
            ["Eye Shape Keys Transhuman", "Eyes +"],
            ["Transhuman Keys Rest", "Eyes +"],
        ],
    )

    eye_shrink: create_linked_props(
        "eye_shrink",
        [
            ["Eye Shape Keys Transhuman", "Eyes -"],
            ["Transhuman Keys Rest", "Eyes -"],
        ],
    )

    eye_inward: create_linked_props(
        "eye_inward",
        [
            ["Eye Shape Keys Transhuman", "Eyes in"],
            ["Transhuman Keys Rest", "Eyes in"],
        ],
    )

    eye_outward: create_linked_props(
        "eye_outward",
        [
            ["Eye Shape Keys Transhuman", "Eyes out"],
            ["Transhuman Keys Rest", "Eyes out"],
        ],
    )

    eye_forward: create_linked_props(
        "eye_forward",
        [
            ["Eye Shape Keys Transhuman", "Eyes front"],
            ["Transhuman Keys Rest", "Eyes front"],
        ],
    )

    eye_backward: create_linked_props(
        "eye_backward",
        [
            ["Eye Shape Keys Transhuman", "Eyes back"],
            ["Transhuman Keys Rest", "Eyes back"],
        ],
    )

    eye_up: create_linked_props(
        "eye_up",
        [
            ["Eye Shape Keys Transhuman", "Eyes up"],
            ["Transhuman Keys Rest", "Eye up"],
        ],
    )

    eye_down: create_linked_props(
        "eye_down",
        [
            ["Eye Shape Keys Transhuman", "Eyes down"],
            ["Transhuman Keys Rest", "Eye down"],
        ],
    )
    
    eyeball_height: create_pos_neg_shape_key_prop_multi(
        "eyeball_height",
        [
            ["Eye Shape Keys Transhuman", "Eyeball Up", "Eyeball Down"],
        ],
    )
    
    eyeball_depth: create_pos_neg_shape_key_prop_multi(
        "eyeball_depth",
        [
            ["Eye Shape Keys Transhuman", "Eyeball Front", "Eyeball Back"],
        ],
    )

    eyeball_size: create_pos_neg_shape_key_prop_multi(
        "eyeball_size",
        [
            ["Eye Shape Keys Transhuman", "Eyeball Size +", "Eyeball Size -"],
        ],
    )

    eyeball_closeness: create_pos_neg_shape_key_prop_multi(
        "eyeball_closeness",
        [
            ["Eye Shape Keys Transhuman", "Eyeball Out", "Eyeball In"],
        ],
    )

    eye_length: create_linked_props(
        "eye_length",
        [
            ["Transhuman Keys Rest", "Eyes long"],
        ],
    )

    eye_roundness: create_linked_props(
        "eye_roundness",
        [
            ["Transhuman Keys Rest", "Eyes round"],
        ],
    )

    eye_rotate: create_pos_neg_shape_key_prop_multi(
        "eye_rotate",
        [
            ["Transhuman Keys Rest", "Eye Rotate R", "Eye Rotate L"],
        ],
    )

    eye_corner: create_pos_neg_shape_key_prop_multi(
        "eye_corner",
        [
            ["Transhuman Keys Rest", "Eye corner up", "Eye corner down"],
        ],
    )

    eye_fold: create_pos_neg_shape_key_prop_multi(
        "eye_fold",
        [
            ["Transhuman Keys Rest", "Eye fold +", "Eye fold -"],
        ],
    )
    
    eye_puff: create_pos_neg_shape_key_prop_multi(
        "eye_puff",
        [
            ["Transhuman Keys Rest", "Puffy Eyes -", "Puffy Eyes +"],
        ],
    )

    tearduct: create_pos_neg_shape_key_prop_multi(
        "tearduct",
        [
            ["Transhuman Keys Rest", "Tearduct Up", "Tearduct"],
        ],
    )

    tearduct_sharp: create_linked_props(
        "tearduct_sharp",
        [
            ["Transhuman Keys Rest", "Tearduct Sharpen"],
        ],
    )

    eyebrows_up: create_linked_props(
        "eyebrows_up",
        [
            ["Transhuman Keys Rest", "Eyebrows up"],
        ],
    )

    eyebrows_down: create_linked_props(
        "eyebrows_down",
        [
            ["Transhuman Keys Rest", "Eyebrows down"],
        ],
    )

    eyebrows_tail: create_linked_props(
        "eyebrows_tail",
        [
            ["Transhuman Keys Rest", "Eyebrows tail up"],
        ],
    )

    eyebrows_head: create_linked_props(
        "eyebrows_head",
        [
            ["Transhuman Keys Rest", "Eyebrows head up"],
        ],
    )

    eyebrows_arch: create_pos_neg_shape_key_prop_multi(
        "eyebrows_arch",
        [
            ["Transhuman Keys Rest", "Eyebrows arch +", "Eyebrows arch -"],
        ],
    )

    eyebrows_rotate: create_pos_neg_shape_key_prop_multi(
        "eyebrows_rotate",
        [
            ["Transhuman Keys Rest", "Eyebrows Rotate R", "Eyebrows Rotate L"],
        ],
    )

    eyebrows_dist: create_pos_neg_shape_key_prop_multi(
        "eyebrows_dist",
        [
            ["Transhuman Keys Rest", "Eyebrows close", "Eyebrows far"],
        ],
    )

    fem_face_1: create_linked_props(
        "fem_face_1",
        [
            ["Transhuman Keys Rest", "Female Face 1"],
        ],
    )

    fem_face_2: create_linked_props(
        "fem_face_2",
        [
            ["Transhuman Keys Rest", "Female Face 2"],
        ],
    )

    fem_face_3: create_linked_props(
        "fem_face_3",
        [
            ["Transhuman Keys Rest", "Female Face 3"],
        ],
    )

    random_extremity: bpy.props.FloatProperty(name="Extremity", max=1, min=0)

    fem_face_4: create_linked_props(
        "fem_face_4",
        [
            ["Transhuman Keys Rest", "Female Face 4"],
        ],
    )

    fem_face_5: create_linked_props(
        "fem_face_5",
        [
            ["Transhuman Keys Rest", "Female Face 5"],
        ],
    )

    m_face_1: create_linked_props(
        "m_face_1",
        [
            ["Transhuman Keys Rest", "Male Face 1"],
        ],
    )

    m_face_2: create_linked_props(
        "m_face_2",
        [
            ["Transhuman Keys Rest", "Male Face 2"],
        ],
    )

    m_face_3: create_linked_props(
        "m_face_3",
        [
            ["Transhuman Keys Rest", "Male Face 3"],
        ],
    )

    m_face_4: create_linked_props(
        "m_face_4",
        [
            ["Transhuman Keys Rest", "Male Face 4"],
        ],
    )

    m_face_5: create_linked_props(
        "m_face_5",
        [
            ["Transhuman Keys Rest", "Male Face 5"],
        ],
    )

    face_length: create_pos_neg_shape_key_prop_multi(
        "face_length",
        [
            ["Transhuman Keys Rest", "Face length +", "Face length -"],
        ],
    )

    face_width: create_pos_neg_shape_key_prop_multi(
        "face_width",
        [
            ["Transhuman Keys Rest", "Face width +", "Face width -"],
        ],
    )

    face_convex: create_linked_props(
        "face_convex",
        [
            ["Transhuman Keys Rest", "Face convex"],
        ],
    )

    face_concave: create_linked_props(
        "face_concave",
        [
            ["Transhuman Keys Rest", "Face concave"],
        ],
    )

    forehead_protrusion: create_pos_neg_shape_key_prop_multi(
        "forehead_protrusion",
        [
            ["Transhuman Keys Rest", "Forehead Front", "Forehead Back"],
        ],
    )

    cheeks_plus_minus: create_pos_neg_shape_key_prop_multi(
        "cheeks_plus_minus",
        [
            ["Transhuman Keys Rest", "Cheeks +", "Cheeks -"],
        ],
    )

    cheeks_hollow: create_linked_props(
        "cheeks_hollow",
        [
            ["Transhuman Keys Rest", "Hollow Cheeks"],
        ],
    )

    cleft_chin: create_linked_props(
        "cleft_chin",
        [
            ["Transhuman Keys Rest", "Chin cleft"],
        ],
    )

    chin_position: create_pos_neg_shape_key_prop_multi(
        "chin_position",
        [
            ["Transhuman Keys Rest", "Chin +", "Chin -"],
        ],
    )

    chin_vertical: create_pos_neg_shape_key_prop_multi(
        "chin_vertical",
        [
            ["Transhuman Keys Rest", "Chin Tall", "Chin Short"],
        ],
    )

    chin_height: create_pos_neg_shape_key_prop_multi(
        "chin_height",
        [
            ["Transhuman Keys Rest", "Chin up", "Chin down"],
        ],
    )

    chin_width: create_pos_neg_shape_key_prop_multi(
        "chin_width",
        [
            ["Transhuman Keys Rest", "Chin wide", "Chin narrow"],
        ],
    )

    jaw_width: create_pos_neg_shape_key_prop_multi(
        "jaw_width",
        [
            ["Transhuman Keys Rest", "Jaw +", "Jaw -"],
        ],
    )

    jaw_length: create_pos_neg_shape_key_prop_multi(
        "jaw_length",
        [
            ["Transhuman Keys Rest", "Jaw Length +", "Jaw Length -"],
        ],
    )

    jowl: create_pos_neg_shape_key_prop_multi(
        "jowl",
        [
            ["Transhuman Keys Rest", "Jowl +", "Jowl -"],
        ],
    )

    neck_girth: create_pos_neg_shape_key_prop_multi(
        "neck_girth",
        [
            ["Transhuman Keys Rest", "Neck +", "Neck -"],
        ],
    )

    glabella: create_pos_neg_shape_key_prop_multi(
        "glabella",
        [
            ["Transhuman Keys Rest", "Glabella out", "Glabella in"],
        ],
    )

    bridge: create_pos_neg_shape_key_prop_multi(
        "bridge",
        [
            ["Transhuman Keys Rest", "Bridge up", "Bridge down"],
        ],
    )

    bridge_width: create_pos_neg_shape_key_prop_multi(
        "bridge_width",
        [
            ["Transhuman Keys Rest", "Bridge width +", "Bridge width -"],
        ],
    )

    supratip: create_pos_neg_shape_key_prop_multi(
        "supratip",
        [
            ["Transhuman Keys Rest", "Supratip up", "Supratip down"],
        ],
    )

    supratip_width: create_pos_neg_shape_key_prop_multi(
        "supratip_width",
        [
            ["Transhuman Keys Rest", "Supratip Width +", "Supratip Width -"],
        ],
    )

    nose_tip_angle: create_pos_neg_shape_key_prop_multi(
        "nose_tip_angle",
        [
            ["Transhuman Keys Rest", "Nose tip up", "Nose tip down"],
        ],
    )

    nose_tip_shape: create_pos_neg_shape_key_prop_multi(
        "nose_tip_shape",
        [
            ["Transhuman Keys Rest", "Nose tip sharp", "Nose tip round"],
        ],
    )

    infratip: create_pos_neg_shape_key_prop_multi(
        "infratip",
        [
            ["Transhuman Keys Rest", "Infratip up", "Infratip down"],
        ],
    )

    infratip_thickness: create_pos_neg_shape_key_prop_multi(
        "infratip_thickness",
        [
            ["Transhuman Keys Rest", "Infratip Thickness +", "Infratip Thickness -"],
        ],
    )

    wings: create_pos_neg_shape_key_prop_multi(
        "wings",
        [
            ["Transhuman Keys Rest", "Wings up", "Wings down"],
        ],
    )

    nose_length: create_pos_neg_shape_key_prop_multi(
        "nose_length",
        [
            ["Transhuman Keys Rest", "Nose length +", "Nose length -"],
        ],
    )

    wings_arch: create_pos_neg_shape_key_prop_multi(
        "wings_arch",
        [
            ["Transhuman Keys Rest", "Wings arch +", "Wings arch -"],
        ],
    )

    nose_cleft: create_linked_props(
        "nose_cleft",
        [
            ["Transhuman Keys Rest", "Nose cleft"],
        ],
    )

    nose_width: create_pos_neg_shape_key_prop_multi(
        "nose_width",
        [
            ["Transhuman Keys Rest", "Nose width +", "Nose width -"],
        ],
    )

    nose_tip_position: create_pos_neg_shape_key_prop_multi(
        "nose_tip_position",
        [
            ["Transhuman Keys Rest", "Nose tip forward", "Nose tip backward"],
        ],
    )

    nose_tip_chisel: create_pos_neg_shape_key_prop_multi(
        "nose_tip_chisel",
        [
            ["Transhuman Keys Rest", "Nose tip chisel +", "Nose tip chisel -"],
        ],
    )

    nose_position: create_pos_neg_shape_key_prop_multi(
        "nose_position",
        [
            ["Transhuman Keys Rest", "Nose forward", "Nose backward"],
        ],
    )

    nose_height: create_pos_neg_shape_key_prop_multi(
        "nose_height",
        [
            ["Transhuman Keys Rest", "Nose height +", "Nose height -"],
        ],
    )

    mouth_position_1: create_pos_neg_shape_key_prop_multi(
        "mouth_position_1",
        [
            ["Transhuman Keys Rest", "Mouth forward", "Mouth backward"],
            ["Teeth Shape Keys", "Mouth forward", "Mouth backward"],
        ],
    )

    mouth_position_2: create_pos_neg_shape_key_prop_multi(
        "mouth_position_2",
        [
            ["Transhuman Keys Rest", "Mouth up", "Mouth down"],
            ["Teeth Shape Keys", "Mouth up", "Mouth down"],
        ],
    )

    mouth_size: create_pos_neg_shape_key_prop_multi(
        "mouth_size",
        [
            ["Transhuman Keys Rest", "Mouth size +", "Mouth size -"],
        ],
    )

    mouth_width: create_pos_neg_shape_key_prop_multi(
        "mouth_width",
        [
            ["Transhuman Keys Rest", "Mouth width +", "Mouth width -"],
            ["Teeth Shape Keys", "Mouth width +", "Mouth width -"],
        ],
    )

    lips_thickness: create_pos_neg_shape_key_prop_multi(
        "lips_thickness",
        [
            ["Transhuman Keys Rest", "Lips thick", "Lips thin"],
        ],
    )

    lip_top_border: create_pos_neg_shape_key_prop_multi(
        "lip_top_border",
        [
            ["Transhuman Keys Rest", "Lip top border out", "Lip top border in"],
        ],
    )

    lip_cupids_bow: create_pos_neg_shape_key_prop_multi(
        "lip_cupids_bow",
        [
            ["Transhuman Keys Rest", "Lip top in", "Lip top out"],
        ],
    )

    lip_bottom_border: create_pos_neg_shape_key_prop_multi(
        "lip_bottom_border",
        [
            ["Transhuman Keys Rest", "Lip bottom border in", "Lip bottom border out"],
        ],
    )

    lip_bottom_cupids: create_pos_neg_shape_key_prop_multi(
        "lip_bottom_cupids",
        [
            ["Transhuman Keys Rest", "Lip bottom in", "Lip bottom out"],
        ],
    )

    lip_cleft: create_pos_neg_shape_key_prop_multi(
        "lip_cleft",
        [
            ["Transhuman Keys Rest", "Lip cleft +", "Lip cleft -"],
        ],
    )

    philtrum: create_pos_neg_shape_key_prop_multi(
        "philtrum",
        [
            ["Transhuman Keys Rest", "Philtrum +", "Philtrum -"],
        ],
    )

    lip_crease_top: create_pos_neg_shape_key_prop_multi(
        "lip_crease_top",
        [
            ["Transhuman Keys Rest", "Top Lip Crease +", "Top Lip Crease"],
        ],
    )

    lip_crease_bottom: create_pos_neg_shape_key_prop_multi(
        "lip_crease_bottom",
        [
            ["Transhuman Keys Rest", "Bottom Lip Crease +", "Bottom Lip Crease"],
        ],
    )

    lip_tubercles_top: create_linked_props(
        "lip_tubercles_top",
        [
            ["Transhuman Keys Rest", "Lip top tubercles"],
        ],
    )

    lip_tubercles_bottom: create_linked_props(
        "lip_tubercles_bottom",
        [
            ["Transhuman Keys Rest", "Lip bottom tubercles"],
        ],
    )

    top_lip: create_pos_neg_shape_key_prop_multi(
        "top_lip",
        [
            ["Transhuman Keys Rest", "Top Lip +", "Top Lip -"],
        ],
    )

    bottom_lip: create_pos_neg_shape_key_prop_multi(
        "bottom_lip",
        [
            ["Transhuman Keys Rest", "Bottom Lip +", "Bottom Lip -"],
        ],
    )

    ear_in: create_linked_props(
        "ear_in",
        [
            ["Transhuman Keys Rest", "Ears in"],
        ],
    )

    ear_out: create_linked_props(
        "ear_out",
        [
            ["Transhuman Keys Rest", "Ears out"],
        ],
    )

    ear_pointy: create_linked_props(
        "ear_pointy",
        [
            ["Transhuman Keys Rest", "Ears pointy"],
        ],
    )

    ear_back: create_linked_props(
        "ear_back",
        [
            ["Transhuman Keys Rest", "Ears back"],
        ],
    )

    ear_height: create_pos_neg_shape_key_prop_multi(
        "ear_height",
        [
            ["Transhuman Keys Rest", "Ears up", "Ears down"],
        ],
    )

    ear_depth: create_pos_neg_shape_key_prop_multi(
        "ear_depth",
        [
            ["Transhuman Keys Rest", "Ears front", "Ears backwards"],
        ],
    )

    ear_size: create_pos_neg_shape_key_prop_multi(
        "ear_size",
        [
            ["Transhuman Keys Rest", "Ears size +", "Ears size -"],
        ],
    )

    shoulders: create_pos_neg_shape_key_prop_multi(
        "shoulders",
        [
            ["Transhuman Keys Rest", "Shoulders +", "Shoulders -"],
        ],
    )

    breasts: create_pos_neg_shape_key_prop_multi(
        "breasts",
        [
            ["Transhuman Keys Rest", "Breast +", "Breast -"],
        ],
    )

    breasts_down: create_pos_neg_shape_key_prop_multi(
        "breasts_down",
        [
            ["Transhuman Keys Rest", "Breasts Up", "Breasts Down"],
        ],
    )

    breasts_push: create_linked_props(
        "breasts_push",
        [
            ["Transhuman Keys Rest", "Pushup"],
        ],
    )

    buttocks: create_pos_neg_shape_key_prop_multi(
        "buttocks",
        [
            ["Transhuman Keys Rest", "Buttocks +", "Buttocks -"],
        ],
    )

    baby_face: create_linked_props(
        "baby_face",
        [
            ["Transhuman Keys Rest", "Baby face"],
        ],
    )

    face_rectangle: create_linked_props(
        "face_rectangle",
        [
            ["Transhuman Keys Rest", "Face Rectangle"],
        ],
    )

    face_triangle: create_linked_props(
        "face_triangle",
        [
            ["Transhuman Keys Rest", "Face Triangle"],
        ],
    )

    face_diamond: create_linked_props(
        "face_diamond",
        [
            ["Transhuman Keys Rest", "Face Diamond"],
        ],
    )

    face_round: create_linked_props(
        "face_round",
        [
            ["Transhuman Keys Rest", "Face Round"],
        ],
    )

    face_oval: create_linked_props(
        "face_oval",
        [
            ["Transhuman Keys Rest", "Face Oval"],
        ],
    )

    face_inversend_triangle: create_linked_props(
        "face_inversend_triangle",
        [
            ["Transhuman Keys Rest", "Face Inversed Triangle"],
        ],
    )

    head_size: create_pos_neg_shape_key_prop_multi(
        "head_size",
        [
            ["Transhuman Keys Rest", "Head Size +", "Head Size -"],
            ["Teeth Shape Keys", "Head Size +", "Head Size -"],
        ],
    )

    head_width: create_pos_neg_shape_key_prop_multi(
        "head_width",
        [
            ["Transhuman Keys Rest", "Head Width +", "Head Width -"],
        ],
    )

    nipples: create_pos_neg_shape_key_prop_multi(
        "nipples",
        [
            ["Transhuman Keys Rest", "Nipples protruding", "Nipples flat"],
        ],
    )

    hips: create_pos_neg_shape_key_prop_multi(
        "hips",
        [
            ["Transhuman Keys Rest", "Hip +", "Hip -"],
        ],
    )

    waist: create_pos_neg_shape_key_prop_multi(
        "waist",
        [
            ["Transhuman Keys Rest", "Waist +", "Waist -"],
        ],
    )

    vulva: create_linked_props(
        "vulva",
        [
            ["Female Genitals Shape Keys", "Vulva open"],
            ["Transhuman Keys Rest", "Vulva"],
            ["Transhuman Keys Rest", "Vulva open"],
        ],
        objects=["SM5 Female Genitals Transhuman"],
        bool=True,
    )

    vulva_open: create_linked_props(
        "vulva_open",
        [
            ["Female Genitals Shape Keys", "Vulva open"],
            ["Transhuman Keys Rest", "Vulva open"],
        ],
    )
    
    labia_size: create_linked_props(
        "labia_size",
        [
            ["Female Genitals Shape Keys", "Labia Size"],
        ],
    )
    
    labia_sym: create_linked_props(
        "labia_sym",
        [
            ["Female Genitals Shape Keys", "Labia Asymmetry"],
        ],
    )

    anus: create_linked_props(
        "anus",
        [
            ["Transhuman Keys Rest", "Anus"],
            ["Transhuman Keys Rest", "Anus open"],
        ],
        bool=True,
    )

    anus_open: create_linked_props(
        "anus_open",
        [
            ["Transhuman Keys Rest", "Anus open"],
        ],
    )

    circumcised: create_linked_props(
        "circumcised",
        [
            ["Male Genitals Key", "Circumcised"],
        ],
    )

    penis: create_linked_props(
        "penis",
        [],
        objects=["SM5 Male Genitals Transhuman", "SM5 Male Genitals Rig Transhuman"],
        bool=True,
    )

    bulge: create_linked_props(
        "bulge",
        [
            ["Transhuman Keys Rest", "Bulge"],
        ],
        bool=True,
    )

    bulge_protrusion: create_linked_props(
        "bulge_protrusion",
        [
            ["Transhuman Keys Rest", "Bulge"],
        ],
    )

    nail_length: create_linked_props(
        "nail_length",
        [
            ["Transhuman Nails Keys", "Nail Length +"],
        ],
    )
    
    peach_fuzz_curves: create_linked_props(
        "peach_fuzz_curves", [], objects=["SM5 Peach Fuzz Transhuman"], bool=True
    )

    chest_curves: create_linked_props(
        "chest_curves", [], objects=["SM5 Chest Transhuman"], bool=True
    )

    chest_extra_curves: create_linked_props(
        "chest_extra_curves", [], objects=["SM5 Chest Extra Transhuman"], bool=True
    )

    arms_curves: create_linked_props(
        "arms_curves", [], objects=["SM5 Arms Transhuman"], bool=True
    )

    forearms_curves: create_linked_props(
        "forearms_curves", [], objects=["SM5 Forearms Transhuman"], bool=True
    )

    shins_curves: create_linked_props(
        "shins_curves", [], objects=["SM5 Shins Transhuman"], bool=True
    )

    thighs_curves: create_linked_props(
        "thighs_curves", [], objects=["SM5 Thighs Transhuman"], bool=True
    )

    stubble_curves: create_linked_props(
        "stubble_curves", [], objects=["SM5 Stubble Transhuman"], bool=True
    )

    stomach_curves: create_linked_props(
        "stomach_curves", [], objects=["SM5 Stomach Transhuman"], bool=True
    )

    back_curves: create_linked_props(
        "back_curves", [], objects=["SM5 Back Transhuman"], bool=True
    )

    hands_curves: create_linked_props(
        "hands_curves", [], objects=["SM5 Hands Transhuman"], bool=True
    )

    feet_curves: create_linked_props(
        "feet_curves", [], objects=["SM5 Feet Transhuman"], bool=True
    )

    armpit_curves: create_linked_props(
        "armpit_curves", [], objects=["SM5 Armpit Transhuman"], bool=True
    )

    nose_hair_curves: create_linked_props(
        "nose_hair_curves", [], objects=["SM5 Nose Hair Transhuman"], bool=True
    )

    pubic_f_curves: create_linked_props(
        "pubic_f_curves", [], objects=["SM5 Pubic F Transhuman"], bool=True
    )

    pubic_m_curves: create_linked_props(
        "pubic_m_curves", [], objects=["SM5 Pubic M Transhuman"], bool=True
    )

    eyelashes_curves: create_linked_props(
        "eyelashes_curves",
        [],
        objects=["SM5 Eyelashes Top Transhuman", "SM5 Eyelashes Bottom Transhuman"],
        bool=True,
    )

    eyebrows_1_mesh: create_linked_props(
        "eyebrows_1_mesh", [], objects=["SM5 Eyebrows Mesh - 1 Transhuman"], bool=True
    )

    eyebrows_2_mesh: create_linked_props(
        "eyebrows_2_mesh", [], objects=["SM5 Eyebrows Mesh - 2 Transhuman"], bool=True
    )

    eyebrows_3_mesh: create_linked_props(
        "eyebrows_3_mesh", [], objects=["SM5 Eyebrows Mesh - 3 Transhuman"], bool=True
    )

    eyebrows_4_mesh: create_linked_props(
        "eyebrows_4_mesh", [], objects=["SM5 Eyebrows Mesh - 4 Transhuman"], bool=True
    )

    eyebrows_5_mesh: create_linked_props(
        "eyebrows_5_mesh", [], objects=["SM5 Eyebrows Mesh - 5 Transhuman"], bool=True
    )

    eyebrows_1_curves: create_linked_props(
        "eyebrows_1_curves", [], objects=["SM5 Eyebrows - 1 Transhuman"], bool=True
    )

    eyebrows_2_curves: create_linked_props(
        "eyebrows_2_curves", [], objects=["SM5 Eyebrows - 2 Transhuman"], bool=True
    )

    eyebrows_3_curves: create_linked_props(
        "eyebrows_3_curves", [], objects=["SM5 Eyebrows - 3 Transhuman"], bool=True
    )

    eyebrows_4_curves: create_linked_props(
        "eyebrows_4_curves", [], objects=["SM5 Eyebrows - 4 Transhuman"], bool=True
    )

    eyebrows_5_curves: create_linked_props(
        "eyebrows_5_curves", [], objects=["SM5 Eyebrows - 5 Transhuman"], bool=True
    )

    secondary_body_hair_switch: bpy.props.BoolProperty(
        name="Secondary Color",
        update=lambda self, context: set_secondary_body_hair_switch_value(
            self, context
        ),
    )

    secondary_beard_switch: bpy.props.BoolProperty(
        name="Secondary Color",
        update=lambda self, context: set_secondary_beard_switch_value(
            self, context
        ),
    )

    highlights_switch: bpy.props.BoolProperty(
        name="Add Highlights",
        update=lambda self, context: set_highlights_switch_value(self, context),
    )

    root_switch: bpy.props.BoolProperty(
        name="Color Root",
        update=lambda self, context: set_root_switch_value(self, context),
    )

    root_invert: bpy.props.BoolProperty(
        name="Invert", update=lambda self, context: set_root_invert_value(self, context)
    )

    preset_name: bpy.props.StringProperty(name="Preset Name")

    randomize_mode: bpy.props.EnumProperty(
        items=preset_saver.randomize_modes_enum,
        description="Randomize Mode",
    )

    saved_presets: bpy.props.EnumProperty(
        items=lambda self, context: [
            (v, v, v) for v in presetSaver.get_saved_presets()
        ],
        description="Saved Presets",
    )

    randomize_from_preset: bpy.props.EnumProperty(
        items=lambda self, context: [
            (v, v, v) for v in presetSaver.get_saved_presets()
        ],
        description="Base preset for selective (targets only value=0) randomizer",
    )

    conceive_preset_a: bpy.props.EnumProperty(
        items=lambda self, context: [
            (v, v, v) for v in presetSaver.get_saved_presets()
        ],
        description="Conceive preset A",
    )
    
    conceive_preset_b: bpy.props.EnumProperty(
        items=lambda self, context: [
            (v, v, v) for v in presetSaver.get_saved_presets()
        ],
        description="Conceive preset B",
    )

    conceive_b_weight: bpy.props.FloatProperty(
        description="0 => A (100%) / B (0%), 1 => A (0%) / B (100%)", min=0, max=1, default=0.5
    )

    is_bound: bpy.props.BoolProperty(name="Is Bound", default=False)

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------
th4b_collection_name = 'Transhuman 4 Blender'
def is_transhuman_loaded():
    return bpy.data.collections.get(th4b_collection_name) is not None

class TRANSHUMAN_OT_LOAD_ORIGINAL_COLLECTION(Operator):
    bl_idname = "transhuman_operators.load_original_collection"
    bl_label = "Load Transhuman"
    bl_description = "Load Transhuman into this blender file"

    def execute(self, context):
        path = sm5_addon_utils.get_addon_root(addon_name=addon_name) / 'assets' / 'SM5 Transhuman.blend'
        with bpy.data.libraries.load(str(path.absolute())) as (data_from, data_to):
            data_to.collections.append(th4b_collection_name)
            data_to.images = data_from.images
            data_to.node_groups = ['SM5 Freckles 1 Scars']
            data_to.actions = data_from.actions

        collection = bpy.data.collections.get(th4b_collection_name)
        bpy.ops.outliner.collection
        bpy.context.scene.collection.children.link(collection)

        presetSaver.load(context, 'SM5_ZERO')

        return {"FINISHED"}

class TRANSHUMAN_OT_OPEN_SET_IMAGE(Operator, ImportHelper):
    bl_idname = "transhuman_operators.open_set_image"
    bl_label = "Load Custom Image"
    bl_description = "Load Custom Image"
    material: bpy.props.StringProperty()
    node: bpy.props.StringProperty()
    group: bpy.props.StringProperty()

    def execute(self, context):
        path = self.filepath
        filename = bpy.path.basename(path)
        bpy.ops.image.open(filepath=path)
        image = bpy.data.images[filename]

        material = bpy.data.materials[self.material]
        if len(self.group) > 0:
            material = material.node_tree.nodes[self.group]

        material.node_tree.nodes[self.node].image = image

        return {"FINISHED"}

class TRANSHUMAN_OT_CONFIRM(Operator):
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class TRANSHUMAN_OT_SAVE_PRESET(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.save_preset"
    bl_label = "This will overwrite the preset if exists."

    def execute(self, context):
        presetSaver.save(context, context.scene.Transhuman_tool.preset_name)

        return {"FINISHED"}

class TRANSHUMAN_OT_LOAD_PRESET(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.load_preset"
    bl_label = "This will overwrite the current settings."

    def execute(self, context):
        presetSaver.load(context, context.scene.Transhuman_tool.saved_presets)

        return {"FINISHED"}

class TRANSHUMAN_OT_RANDOMIZE_PRESET(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.randomize_preset"
    bl_label = "This will randomize the current settings. Continue?"
    bl_description = "Randomize everything"

    def execute(self, context):
        presetSaver.randomize(context, context.scene.Transhuman_tool.randomize_mode)

        return {"FINISHED"}

class TRANSHUMAN_OT_RANDOMIZE_FROM_PRESET(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.randomize_from_preset"
    bl_label = "This will overwrite the current settings. Continue?"
    bl_description = "Randomize while keeping the selected preset as base"

    def execute(self, context):
        presetSaver.randomize_from_preset(
            context, context.scene.Transhuman_tool.randomize_from_preset,
            context.scene.Transhuman_tool.randomize_mode
        )

        return {"FINISHED"}
    
class TRANSHUMAN_OT_CONCEIVE_FROM_PRESETS(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.conceive_from_presets"
    bl_label = "This will overwrite the current settings. Continue?"
    bl_description = "Mix the selected 2 presets with the selected weight"

    def execute(self, context):
        presetSaver.conceive_from_presets(
            context,
            context.scene.Transhuman_tool.conceive_preset_a,
            context.scene.Transhuman_tool.conceive_preset_b,
            context.scene.Transhuman_tool.conceive_b_weight,
        )

        return {"FINISHED"}

class TRANSHUMAN_OT_UNBIND_MESH(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.unbind_mesh"
    bl_label = "This will disable/unbind the mesh from its current state"
    bl_description = "This will disable/unbind the mesh from its current state"

    def execute(self, context):
        bpy.ops.object.correctivesmooth_bind(modifier="--Nipples fix")
        bpy.data.objects["SM5 Transhuman"].modifiers["--Nipples fix"].show_viewport = False
        bpy.data.objects["SM5 Transhuman"].modifiers["--Nipples fix"].show_render = False
        bpy.ops.object.correctivesmooth_bind(modifier="POSE SMOOTH")
        bpy.data.objects["SM5 Transhuman"].modifiers["POSE SMOOTH"].show_viewport = False
        bpy.data.objects["SM5 Transhuman"].modifiers["POSE SMOOTH"].show_render = False
        setattr(context.scene.Transhuman_tool, "is_bound", False)

        return {"FINISHED"}
    
def finalize_hair(obj_name):
    object = bpy.data.objects[obj_name]
    if object.hide_viewport:
        return

    object.select_set(True)
    bpy.ops.object.convert(target='MESH')
    mesh = bpy.data.meshes[obj_name]
    attrs = ['SM5-UVs', 'SM5-UVs-Short', 'SM5-UVs-Curls', 'SM5-UVs-Loose']
    for attr_name in attrs:
        ind = mesh.attributes.find(attr_name)
        if ind == -1:
            continue
        mesh.attributes.active_index = ind
        bpy.ops.geometry.attribute_convert(domain='CORNER', data_type='FLOAT2')

class TRANSHUMAN_OT_FINALIZE_HAIR(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.finalize_hair"
    bl_label = "Converting will lose hair edit capabilities. Continue?"
    bl_description = "This will convert the mesh hair to geometry"

    def execute(self, context):
        finalize_hair('SM5 Transhuman Hair')

        return {"FINISHED"}
    
class TRANSHUMAN_OT_FINALIZE_BODY_HAIR(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.finalize_body_hair"
    bl_label = "Converting will lose hair edit capabilities. Continue?"
    bl_description = "This will convert the mesh hair to geometry"

    def execute(self, context):
        objs = [
            'SM5 Eyebrows - 1 Transhuman',
            'SM5 Eyebrows - 2 Transhuman',
            'SM5 Eyebrows - 3 Transhuman',
            'SM5 Eyebrows - 4 Transhuman',
            'SM5 Eyebrows - 5 Transhuman',
            'SM5 Eyelashes Top Transhuman',
            'SM5 Eyelashes Bottom Transhuman',
            'SM5 Thighs Transhuman',
            'SM5 Stubble Transhuman',
            'SM5 Stomach Transhuman',
            'SM5 Shins Transhuman',
            'SM5 Pubic M Transhuman',
            'SM5 Pubic F Transhuman',
            'SM5 Nose Hair Transhuman',
            'SM5 Hands Transhuman',
            'SM5 Forearms Transhuman',
            'SM5 Feet Transhuman',
            'SM5 Chest Transhuman',
            'SM5 Chest Extra Transhuman',
            'SM5 Back Transhuman',
            'SM5 Arms Transhuman',
            'SM5 Armpit Transhuman',
        ]
        for obj in objs:
            finalize_hair(obj)

        return {"FINISHED"}


class TRANSHUMAN_OT_BIND_MESH(TRANSHUMAN_OT_CONFIRM):
    bl_idname = "transhuman_operators.bind_mesh"
    bl_label = "This will enable/bind the mesh to its current state"
    bl_description = "This will enable/bind the mesh to its current state"

    def execute(self, context):
        bpy.data.objects["SM5 Transhuman"].modifiers["--Nipples fix"].show_viewport = True
        bpy.data.objects["SM5 Transhuman"].modifiers["--Nipples fix"].show_render = True
        bpy.ops.object.correctivesmooth_bind(modifier="--Nipples fix")
        bpy.data.objects["SM5 Transhuman"].modifiers["POSE SMOOTH"].show_viewport = True
        bpy.data.objects["SM5 Transhuman"].modifiers["POSE SMOOTH"].show_render = True
        bpy.ops.object.correctivesmooth_bind(modifier="POSE SMOOTH")
        setattr(context.scene.Transhuman_tool, "is_bound", True)
        
        return {"FINISHED"}

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------
class TranshumanRootPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Transhuman"

class TranshumanPanel(TranshumanRootPanel):
    bl_options = {"DEFAULT_CLOSED"}

class TRANSHUMAN_PT_INIT(TranshumanRootPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_INIT"
    bl_label = "Transhuman4Blender"

    @classmethod
    def poll(cls, context):
        return not is_transhuman_loaded()

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().operator(
            "transhuman_operators.load_original_collection", text="Load Transhuman", icon="IMPORT"
        )

class TRANSHUMAN_PT_MAIN(TranshumanRootPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_MAIN"
    bl_label = "Transhuman4Blender"

    @classmethod
    def poll(cls, context):
        return is_transhuman_loaded()

    def draw(self, context):
        layout = self.layout

        box = layout.box()

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "preset_name", text="")
        row.column().operator(
            "transhuman_operators.save_preset", text="SAVE", icon="FILE"
        )

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "saved_presets", text="")
        row.column().operator(
            "transhuman_operators.load_preset", text="LOAD", icon="FILE"
        )

class TRANSHUMAN_PT_RIG(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_RIG"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "ARMATURES"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool,
            "hide_armatures",
            text="Hide Armatures from View",
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "face_prop", text="Check Proportions")

        box = layout.box()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "mixamo_mode", text="Armature")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "face_rig", text="Face")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Extras:")
        row.column().prop(context.scene.Transhuman_tool, "toes_rig", text="Toes")


class TRANSHUMAN_PT_EYES(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_EYES"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "EYE COLOR"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tool = scene.Transhuman_tool

        box = layout.box()
        row = box.row()
        row.column().label(text="Iris:", icon="EYEDROPPER")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Color base:")
        row.column().prop(context.scene.Transhuman_tool, "eye_base_image", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Custom color")
        row.column().preset_prop("eye_color_picker", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Lighten / Darken:")
        row.column().preset_prop("eye_color_chroma", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Halo:")
        row.column().preset_prop("halo", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Halo Color:")
        row.column().preset_prop("halo_color", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Redness:")
        row.column().preset_prop("eye_redness", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Cornea Roughness:")
        row.column().preset_prop("eye_settings", text="")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Cornea Reflectivity:")
        row.column().preset_prop("cornea_reflective", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Iris size:")
        row.column().prop(context.scene.Transhuman_tool, "iris", text="±")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Pupil:")
        row.column().prop(context.scene.Transhuman_tool, "pupil_switch", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Pupil shape:")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "pupil_cat", text="Cat")
        row.column().prop(context.scene.Transhuman_tool, "pupil_goat", text="Goat")
        row.column().prop(context.scene.Transhuman_tool, "pupil_star", text="Star")

        box = layout.box()
        row = box.row()
        row.column().label(text="Cornea / Sclera:", icon="EYEDROPPER")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("sclera_cornea_mixer", text="Tint Amount")
        row.column().preset_prop("sclera_cornea_settings_color", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop(
            "sclera_cornea_settings_transmission", text="Transmission"
        )
        row.column().preset_prop("sclera_cornea_settings_roughness", text="Roughness")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("sclera_cornea", text="Select Area")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Options: 'Right / Left / Both' followed by 'Cornea / Sclera'",
            icon="INFO",
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="Tears Color:", icon="EYEDROPPER")
        row.column().preset_prop("tear_settings", text="")

        # layout.row().separator()

class TRANSHUMAN_PT_SKIN(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_SKIN"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "SKIN SETTINGS"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="Skin color hue:")
        row.column().preset_prop("skin_hue", text="")

        row = box.row()
        row.column().label(text="Color desaturate:")
        row.column().preset_prop("skin_saturation", text="")

        row = box.row()
        row.column().label(text="Lighten / Darken:")
        row.column().preset_prop("skin_chroma", text="")

        row = box.row()
        row.column().label(text="Sickness level (Subdermal):")
        row.column().preset_prop("skin_health", text="")

        row = box.row()
        row.column().label(text="Skin details:")
        row.column().preset_prop("skin_detail_strength", text="")

        row = box.row()
        row.column().label(text="Face harden:")
        row.column().preset_prop("face_definition", text="")

        row = box.row()
        row.column().label(text="Body definition:")
        row.column().preset_prop("body_definition", text="")

        row = box.row()
        row.column().label(text="Skin oil:")
        row.column().preset_prop("skin_sweat", text="")

        row = box.row()
        row.column().label(text="Skin reflectivity:")
        row.column().preset_prop("skin_reflection", text="")

        row = box.row()
        row.column().label(text="Subsurface:")
        row.column().preset_prop("skin_subsurface", text="")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "subdermal_switch")

        row = box.row()
        row.column().label(text="Add lip gloss:")
        row.column().preset_prop("lip_gloss", text="")

        box = layout.box()
        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "scars_switch")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "scars_selector", text="Type")

        row = box.row()
        row.column().preset_prop("scars_color_intensity", text="Blend")
        row.column().preset_prop("scars_bump", text="Bump")

        row = box.row()
        row.column().preset_prop("scars_color_saturation", text="Color intensity")
        row.column().preset_prop("scars_color_brightness", text="Brightness")

        box = layout.box()
        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "tattoo_switch")

        row = box.row()
        row.column().preset_prop("tattoo_height", text="Bump")
        row.column().preset_prop("tattoo_amount", text="Transparency")

        row = box.row()
        add_open_set_image(
            row.column(),
            material="SM5 Skin Material Transhuman",
            node="tattoo_image",
            group="",
        )
        row = box.row()

        box = layout.box()
        row = box.row()
        row = box.row()
        row.column().label(icon="BLANK1")
        op = row.column().operator(
            "wm.url_open", text="Get more Scars & Tattoos", icon="URL"
        )
        op.url = (
            "https://sm5.heledahn.com/collections/3d-models/transhuman/scars-tattoos"
        )
        row.column().label(icon="BLANK1")
        row = box.row()

class TRANSHUMAN_PT_FACE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "APPEARANCE - FACE"

    def draw(self, context):
        layout = self.layout

class TRANSHUMAN_PT_HEAD_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Base"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="FEMALE:", icon="EVENT_F")
        row.column().label(text="MALE:", icon="EVENT_M")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "fem_face_1", text="Face 1")
        row.column().prop(context.scene.Transhuman_tool, "m_face_1", text="Face 1")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "fem_face_2", text="Face 2")
        row.column().prop(context.scene.Transhuman_tool, "m_face_2", text="Face 2")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "fem_face_3", text="Face 3")
        row.column().prop(context.scene.Transhuman_tool, "m_face_3", text="Face 3")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "fem_face_4", text="Face 4")
        row.column().prop(context.scene.Transhuman_tool, "m_face_4", text="Face 4")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "fem_face_5", text="Face 5")
        row.column().prop(context.scene.Transhuman_tool, "m_face_5", text="Face 5")

class TRANSHUMAN_PT_FACE_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Face"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "face_length", text="Face Length ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "face_width", text="Face Width ±"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "face_concave", text="Concave")
        row.column().prop(context.scene.Transhuman_tool, "face_convex", text="Convex")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "forehead_protrusion", text="Forehead Protrusion ±"
        )
        row.column().prop(context.scene.Transhuman_tool, "baby_face", text="Baby Face")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "face_triangle", text="Triangle"
        )
        row.column().prop(
            context.scene.Transhuman_tool,
            "face_inversend_triangle",
            text="Inversed Triangle",
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "face_diamond", text="Diamond")
        row.column().prop(
            context.scene.Transhuman_tool, "face_rectangle", text="Rectangle"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "face_oval", text="Oval")
        row.column().prop(context.scene.Transhuman_tool, "face_round", text="Round")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "head_size", text="Head Size ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "head_width", text="Head Width ±"
        )

class TRANSHUMAN_PT_CHEEKS_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Cheeks"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool,
            "cheeks_plus_minus",
            text="Outward / Inward ±",
        )
        row.column().prop(context.scene.Transhuman_tool, "cheeks_hollow", text="Hollow")

class TRANSHUMAN_PT_CHIN_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Chin"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "chin_position", text="Protrusion ±"
        )
        row.column().prop(context.scene.Transhuman_tool, "cleft_chin", text="Cleft")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "chin_height", text="Up / Down ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "chin_width", text="Wide / Narrow ±"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "chin_vertical", text="Tall / Short ±"
        )
        row.column().label(text="")

class TRANSHUMAN_PT_JAW_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Jaw"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "jaw_width", text="Width ±")
        row.column().prop(context.scene.Transhuman_tool, "jaw_length", text="Length ±")

class TRANSHUMAN_PT_NECK_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Neck"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "neck_girth", text="Girth ±")
        row.column().prop(context.scene.Transhuman_tool, "jowl", text="Jowl ±")

class TRANSHUMAN_PT_EYE_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Eyes"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eye_grow", text="Magnify")
        row.column().prop(context.scene.Transhuman_tool, "eye_shrink", text="Shrink")

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eye_inward", text="Inward")
        row.column().prop(context.scene.Transhuman_tool, "eye_outward", text="Outward")

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eye_forward", text="Forward")
        row.column().prop(
            context.scene.Transhuman_tool, "eye_backward", text="Backward"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eye_up", text="Up")
        row.column().prop(context.scene.Transhuman_tool, "eye_down", text="Down")

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eye_length", text="Length")
        row.column().prop(
            context.scene.Transhuman_tool, "eye_roundness", text="Roundness"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "eye_corner", text="Eye corner ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eye_rotate", text="Eye rotate ±"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "tearduct", text="Tearduct Rotation ±")
        row.column().prop(
            context.scene.Transhuman_tool, "tearduct_sharp", text="Tearduct Sharpen +"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "eye_fold", text="Eyelid fold ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eye_puff", text="Puffy Eyes ±"
        )
       
        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "eyeball_height", text="Eyeball Height ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyeball_depth", text="Eyeball Depth ±"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "eyeball_closeness", text="Eyeball Closeness ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyeball_size", text="Eyeball Size ±"
        )


class TRANSHUMAN_PT_BROW_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Brow"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eyebrows_up", text="Raise")
        row.column().prop(context.scene.Transhuman_tool, "eyebrows_down", text="Lower")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_head", text="Head up"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_tail", text="Tail up"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "eyebrows_arch", text="Arch ±")
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_rotate", text="Rotate ±"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_dist", text="Closenes ±"
        )
        row.column().label(text="")

class TRANSHUMAN_PT_NOSE_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Nose"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Glabella:")
        row.column().prop(context.scene.Transhuman_tool, "glabella", text="±")

        row = layout.row()
        row.column().label(text="Bridge:")
        row.column().prop(context.scene.Transhuman_tool, "bridge", text="±")

        row = layout.row()
        row.column().label(text="Bridge width:")
        row.column().prop(context.scene.Transhuman_tool, "bridge_width", text="±")

        row = layout.row()
        row.column().label(text="Supratip:")
        row.column().prop(context.scene.Transhuman_tool, "supratip", text="±")

        row = layout.row()
        row.column().label(text="Supratip Width:")
        row.column().prop(context.scene.Transhuman_tool, "supratip_width", text="±")

        row = layout.row()
        row.column().label(text="Tip angle:")
        row.column().prop(context.scene.Transhuman_tool, "nose_tip_angle", text="±")

        row = layout.row()
        row.column().label(text="Tip shape:")
        row.column().prop(context.scene.Transhuman_tool, "nose_tip_shape", text="±")

        row = layout.row()
        row.column().label(text="Tip position:")
        row.column().prop(context.scene.Transhuman_tool, "nose_tip_position", text="±")

        row = layout.row()
        row.column().label(text="Tip chisel:")
        row.column().prop(context.scene.Transhuman_tool, "nose_tip_chisel", text="±")

        row = layout.row()
        row.column().label(text="Infratip height:")
        row.column().prop(context.scene.Transhuman_tool, "infratip", text="±")

        row = layout.row()
        row.column().label(text="Infratip thickness:")
        row.column().prop(context.scene.Transhuman_tool, "infratip_thickness", text="±")

        row = layout.row()
        row.column().label(text="Wings angle:")
        row.column().prop(context.scene.Transhuman_tool, "wings", text="±")

        row = layout.row()
        row.column().label(text="Wings arch:")
        row.column().prop(context.scene.Transhuman_tool, "wings_arch", text="±")

        row = layout.row()
        row.column().label(text="Cleft:")
        row.column().prop(context.scene.Transhuman_tool, "nose_cleft", text="+")

        row = layout.row()
        row.column().label(text="Nose length:")
        row.column().prop(context.scene.Transhuman_tool, "nose_length", text="±")

        row = layout.row()
        row.column().label(text="Nose width:")
        row.column().prop(context.scene.Transhuman_tool, "nose_width", text="±")

        row = layout.row()
        row.column().label(text="Nose position:")
        row.column().prop(context.scene.Transhuman_tool, "nose_position", text="±")

        row = layout.row()
        row.column().label(text="Nose height:")
        row.column().prop(context.scene.Transhuman_tool, "nose_height", text="±")

class TRANSHUMAN_PT_MOUTH_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Lips"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Forward / Backward:")
        row.column().prop(context.scene.Transhuman_tool, "mouth_position_1", text="±")

        row = layout.row()
        row.column().label(text="Up / down:")
        row.column().prop(context.scene.Transhuman_tool, "mouth_position_2", text="±")

        row = layout.row()
        row.column().label(text="Size:")
        row.column().prop(context.scene.Transhuman_tool, "mouth_size", text="±")

        row = layout.row()
        row.column().label(text="Width:")
        row.column().prop(context.scene.Transhuman_tool, "mouth_width", text="±")

        row = layout.row()
        row.column().label(text="Global thickness:")
        row.column().prop(context.scene.Transhuman_tool, "lips_thickness", text="±")

        row = layout.row()
        row.column().label(text="Top lip thickness:")
        row.column().prop(context.scene.Transhuman_tool, "top_lip", text="±")

        row = layout.row()
        row.column().label(text="Bottom lip thickness:")
        row.column().prop(context.scene.Transhuman_tool, "bottom_lip", text="±")

        row = layout.row()
        row.column().label(text="Top border shape:")
        row.column().prop(context.scene.Transhuman_tool, "lip_top_border", text="±")

        row = layout.row()
        row.column().label(text="Cupids bow:")
        row.column().prop(context.scene.Transhuman_tool, "lip_cupids_bow", text="±")

        row = layout.row()
        row.column().label(text="Bottom border shape:")
        row.column().prop(context.scene.Transhuman_tool, "lip_bottom_border", text="±")

        row = layout.row()
        row.column().label(text="Bottom cupids bow:")
        row.column().prop(context.scene.Transhuman_tool, "lip_bottom_cupids", text="±")

        row = layout.row()
        row.column().label(text="Tubercles top:")
        row.column().prop(context.scene.Transhuman_tool, "lip_tubercles_top", text="+")

        row = layout.row()
        row.column().label(text="Tubercles bottom:")
        row.column().prop(
            context.scene.Transhuman_tool, "lip_tubercles_bottom", text="+"
        )

        row = layout.row()
        row.column().label(text="Bottom cleft:")
        row.column().prop(context.scene.Transhuman_tool, "lip_cleft", text="±")

        row = layout.row()
        row.column().label(text="Top Lip Crease:")
        row.column().prop(context.scene.Transhuman_tool, "lip_crease_top", text="±")

        row = layout.row()
        row.column().label(text="Bottom Lip Crease:")
        row.column().prop(context.scene.Transhuman_tool, "lip_crease_bottom", text="±")

        row = layout.row()
        row.column().label(text="Philtrum Width:")
        row.column().prop(context.scene.Transhuman_tool, "philtrum", text="±")

class TRANSHUMAN_PT_EAR_SHAPE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_FACE"
    bl_label = "Ears"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "ear_in", text="Ears in")
        row.column().prop(context.scene.Transhuman_tool, "ear_out", text="Ears out")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "ear_height", text="Ears height ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "ear_depth", text="Ears depth ±"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "ear_size", text="Ears size ±")
        row.column().prop(context.scene.Transhuman_tool, "ear_back", text="Pull back")

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "ear_pointy", text="Pointy")
        row.column().label(text="")

class TRANSHUMAN_PT_BODY(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_BODY"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "APPEARANCE - BODY"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="FEMALE:", icon="EVENT_F")
        row.column().label(text="MALE:", icon="EVENT_M")

        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "female_base", text="Base Shape"
        )
        row.column().prop(context.scene.Transhuman_tool, "male_base", text="Base Shape")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "female_weight_minus", text="Weight -"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "male_weight_minus", text="Weight -"
        )
        row.column().label(icon="BLANK1")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "female_weight_plus", text="Weight +"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "male_weight_plus", text="Weight +"
        )
        row.column().label(icon="BLANK1")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "female_muscles", text="Musculature"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "male_muscles", text="Musculature"
        )
        row.column().label(icon="BLANK1")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "old_age_switch", text="Age")
        row.column().label(icon="BLANK1")

        box = layout.box()
        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "breasts", text="Breast Size ±"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "breasts_down", text="Breast Up/Down ±"
        )

        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "breasts_push", text="Breast Push-up"
        )
        row.column().prop(context.scene.Transhuman_tool, "waist", text="Waist ±")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "hips", text="Hips ±")
        row.column().prop(
            context.scene.Transhuman_tool, "buttocks", text="Buttocks Size ±"
        )

        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "shoulders", text="Shoulder Width ±"
        )
        row.column().label(text="")

        box = layout.box()

        row = box.row()
        row.column().label(text="HANDS:")

        row = layout.row()
        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "hand_male", text="Masculine")
        row.column().prop(context.scene.Transhuman_tool, "hand_female", text="Feminine")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "hand_neutral", text="Neutral")
        row.column().prop(context.scene.Transhuman_tool, "hand_elder", text="Elder")

        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "nail_length", text="Nails Length"
        )
        row.column().label(text="")

        row = box.row()
        row.column().label(text="FEET:")

        row = layout.row()
        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "feet_male", text="Masculine")
        row.column().prop(context.scene.Transhuman_tool, "feet_female", text="Feminine")

class TRANSHUMAN_PT_BODY_OPT(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_BODY_OPT"
    bl_parent_id = "TRANSHUMAN_PT_BODY"
    bl_label = "Gender Definition Ratio (Optional)"

    def draw(self, context):
        layout = self.layout

        box = layout.box()

        row = box.row()
        row.column().label(
            text=" This slider blends the displacement maps of the Female-Male anatomy",
            icon="INFO",
        )
        row = box.row()
        row.column().label(
            text=" It automatically updates based on your choices, but you can adjust the averaged value below",
            icon="BLANK1",
        )
        row = box.row()
        row.column().label(
            text=" If anatomical discrepancies occur, pick 0 (100% F) or 1 (100% M)",
            icon="BLANK1",
        )

        row = box.row()
        row.column().label(text="", icon="EVENT_F")
        row.column().prop(
            context.scene.Transhuman_tool, "gender_definition", text="Definition Ratio"
        )
        row.column().label(text="", icon="EVENT_M")

class TRANSHUMAN_PT_PERSONA(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_PERSONA"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "PERSONA (Addon)"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="", icon="EYEDROPPER")
        row.column().prop(
            context.scene.Transhuman_tool, "persona_switch", text="Load Persona"
        )

        op = row.column().operator("wm.url_open", text="Browse Catalogue", icon="URL")
        op.url = "https://sm5.heledahn.com/collections/transhuman"

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "imported_persona_mesh", text="Mesh"
        )

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "imported_persona_skin", text="Skin"
        )

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "imported_persona_displ", text="Displacement"
        )
        
        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="Displ. Amount")
        row.column().preset_prop("persona_displ_value", text=""
        )

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="Blend Original Displacement")
        row.column().preset_prop("original_face_displ", text=""
        )

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="")
        row.column().prop(context.scene.Transhuman_tool, "flip_displ_switch")

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="", icon="INFO")
        row.column().label(
            text="Import and select new Personas to replace the Base Transhuman"
        )

        row.column().label(text="", icon="BLANK1")
        row = box.row()

class TRANSHUMAN_PT_MODIFIERS(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_DYNAMIC"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "MODIFIERS"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(
            text="Subdivision Level:", icon="MOD_SUBSURF"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool,
            "subdivision_level", text="Viewport"
        )
        row.column().prop(
            context.scene.Transhuman_tool,
            'subdivision_level_for_render', text="Render"
        )
        
        box = layout.box()
        row = box.row()
        row.column().label(
            text="Face Randomizer:", icon="SHADERFX"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool,
            "randomize_mode",
            text="Mode",
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool,
            "random_extremity",
            slider=True,
            text="< Harmony / Chaos >",
        )
        row.column().operator(
            "transhuman_operators.randomize_preset",
            text="Randomize",
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "randomize_from_preset", text=""
        )
        row.column().operator(
            "transhuman_operators.randomize_from_preset",
            text="Randomize Preset",
        )
        row = box.row()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Select amount of Harmony / Chaos. Use 0.2 for natural results", icon="INFO"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="You can choose a preset to randomize upon", icon="INFO"
        )         

        ## concepion
        box = layout.box()
        row = box.row()
        row.column().label(
            text="Conception:", icon="COMMUNITY"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.label(text="Choose A and B specimens (presets):")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, 'conceive_preset_a', text="A"
        )
        row.column().prop(
            context.scene.Transhuman_tool, 'conceive_preset_b', text="B"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.prop(
            context.scene.Transhuman_tool, 'conceive_b_weight', text="B Weight"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.operator(
            'transhuman_operators.conceive_from_presets',
            text="Conceive",
        )

        box = layout.box()
        row = box.row()
        row.column().label(
            text="Smooth Anatomy & Facial Features:", icon="MOD_SMOOTH"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop(
            "smooth_custom", text="Level"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Increase as needed to smooth chaotic anatomy", icon="INFO"
        )

        box = layout.box()
        row = box.row()
        row.column().label(
            text="Bind Finished Transhuman:", icon="OUTLINER_OB_ARMATURE"
        )
        row = box.row()
        row.column().label(icon="BLANK1")

        if getattr(context.scene.Transhuman_tool, "is_bound", False):
            row.column().operator(
                "transhuman_operators.unbind_mesh", text="UNBIND",            
            )
        else:
            row.column().operator(
                "transhuman_operators.bind_mesh", text="BIND",
            )

        row = box.row() 
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Bind in T-Pose before render", icon="INFO"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Remember to unbind before modifying appearance", icon="INFO"
        )

        box = layout.box()
        row = box.row()
        row = box.row()
        row.column().label(
            text="Dynamic Breasts:", icon="MOD_SOFT"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "dynamic_breasts", text="On / Off")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Cloth modifier for breast motion. Play animation and/or  bake",
            icon="INFO",
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="To avoid scares, turn on at 'Frame 1' only!",
            icon="ERROR",
        )

        box = layout.box()
        row = box.row()
        row.column().label(
            text="Dynamic Wrinkles:", icon="FORCE_TURBULENCE"
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "dynamic_wrinkles", text="On / Off")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(
            text="Automatically adds wrinkles in compressed areas for extra realism",
            icon="INFO",
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="FINALIZE HAIR:", icon="MOD_REMESH")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().operator(
            "transhuman_operators.finalize_hair", text="Finalize Wig", 
        )
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().operator(
            "transhuman_operators.finalize_body_hair", text="Finalize Body Hair", 
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Converting will lose grooming / editing capabilities.", icon="INFO")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="This feature sometimes fails. If so, please try again.", icon="ERROR")
   
class TRANSHUMAN_PT_MAKEUP(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_MAKEUP"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "MAKEUP"

    def draw(self, context):
        layout = self.layout

class TRANSHUMAN_PT_MAKEUP_BASE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Base"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "base_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Base color:")
        row.column().preset_prop("base_makeup_color", text="")

        row = layout.row()
        row.column().label(text="Expand Base:")
        row.column().preset_prop("base_maiko", text="")

        row = layout.row()
        row.column().label(text="Base thickness:")
        row.column().preset_prop("base_makeup", text="")

        row = layout.row()
        row.column().label(text="Contouring:")
        row.column().preset_prop("makeup_contouring", text="")

class TRANSHUMAN_PT_MAKEUP_BLUSH(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Blush"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "blush_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().preset_prop("blush_1", text="Blush 1")
        row.column().preset_prop("blush_1_color", text="")

        row = layout.row()
        row.column().preset_prop("blush_2", text="Blush 2")
        row.column().preset_prop("blush_2_color", text="")

        row = layout.row()
        row.column().preset_prop("blush_3", text="Blush 3")
        row.column().preset_prop("blush_3_color", text="")

        row = layout.row()
        row.column().label(text="Thickness:")
        row.column().preset_prop("blush_intensity", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("blush_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("blush_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_LIPS(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Lips"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "lips_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Lip color amount:")
        row.column().preset_prop("lipstick_amount", text="")

        row = layout.row()
        row.column().label(text="Color:")
        row.column().preset_prop("lipstick_color", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("lipstick_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("lipstick_settings_roughness", text="")

        row = layout.row()
        row.column().label(text="Add lip gloss:")
        row.column().preset_prop("lip_gloss", text="")

class TRANSHUMAN_PT_MAKEUP_LIP_LINER(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Lip liner"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "lip_liner_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Lip liner amount:")
        row.column().preset_prop("lip_liner", text="")

        row = layout.row()
        row.column().label(text="Color:")
        row.column().preset_prop("lip_liner_color", text="")

        row = layout.row()
        row.column().label(text="Smudge:")
        row.column().preset_prop("lip_liner_gradient", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("lip_liner_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("lip_liner_settings_roughness", text="")

        row = layout.row()
        row.column().label(text="Add lip gloss:")
        row.column().preset_prop("lip_gloss", text="")

class TRANSHUMAN_PT_MAKEUP_EYESHADOW(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Eyeshadow - Lid"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "eyeshadow_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Shadow amount:")
        row.column().preset_prop("eyeshadow_amount", text="")

        row = layout.row()
        row.column().label(text="Shadow fade:")
        row.column().preset_prop("eyeshadow_intensity", text="")

        row = layout.row()
        row.column().label(text="Main color:")
        row.column().preset_prop("eyeshadow_lid_colors_main", text="")

        row = layout.row()
        row.column().label(text="Inner color:")
        row.column().preset_prop("eyeshadow_lid_colors_inner", text="")

        row.column().preset_prop("eyeshadow_tip", text="")

        row = layout.row()
        row.column().label(text="Outer color:")
        row.column().preset_prop("eyeshadow_lid_tail", text="")
        row.column().preset_prop("eyeshadow_tail", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("eyeshadow_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("eyeshadow_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_LASHLINE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Eyeshadow - Lower lashline"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "lashline_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Shadow amount:")
        row.column().preset_prop("lashline_amount", text="")

        row = layout.row()
        row.column().label(text="Shadow fade:")
        row.column().preset_prop("lashline_intensity", text="")

        row = layout.row()
        row.column().label(text="Main color:")
        row.column().preset_prop("lashline_main_under_color", text="")

        row = layout.row()
        row.column().label(text="Inner color:")
        row.column().preset_prop("lashline_tip_colors", text="")
        row.column().preset_prop("lashline_tip", text="Amount")

        row = layout.row()
        row.column().label(text="Outer color:")
        row.column().preset_prop("lashline_tail_color", text="")
        row.column().preset_prop("lashline_tail", text="Amount")

        row = layout.row()
        row.column().label(text="Smudge Down:")
        row.column().preset_prop("lashline_main_under_color_smudge", text="")
        row.column().preset_prop("lashline_under", text="Amount")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("lashline_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("lashline_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_SHADOW_INNER(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Eyeshadow - Inner corner"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "inner_shadow_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().preset_prop("inner_shadow_1", text="Type 1")
        row.column().preset_prop("inner_shadow_1_color", text="")

        row = layout.row()
        row.column().preset_prop("inner_shadow_2", text="Type 2")
        row.column().preset_prop("inner_shadow_2_color", text="")

        row = layout.row()
        row.column().preset_prop("inner_shadow_3", text="Type 3")
        row.column().preset_prop("inner_shadow_3_color", text="")

        row = layout.row()
        row.column().label(text="Thickness:")
        row.column().preset_prop("inner_shadow_intensity", text="")

        row = layout.row()
        row.column().label(text="Granularity:")
        row.column().preset_prop("inner_shadow_granularity", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("inner_shadow_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("inner_shadow_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_SHADOW_OUTER(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Eyeshadow - Outer corner"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "outer_shadow_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().preset_prop("outer_shadow_1", text="Type 1")
        row.column().preset_prop("outer_shadow_1_color", text="")

        row = layout.row()
        row.column().preset_prop("outer_shadow_2", text="Type 2")
        row.column().preset_prop("outer_shadow_2_color", text="")

        row = layout.row()
        row.column().preset_prop("outer_shadow_3", text="Type 3")
        row.column().preset_prop("outer_shadow_3_color", text="")

        row = layout.row()
        row.column().label(text="Thickness:")
        row.column().preset_prop("outer_shadow_intensity", text="")

        row = layout.row()
        row.column().label(text="Granularity:")
        row.column().preset_prop("outer_shadow_granularity", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("outer_shadow_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("outer_shadow_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_HIGHLIGHT(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Highlight"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "highlight_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Shadow amount:")
        row.column().preset_prop("highlight_shadow", text="")

        row = layout.row()
        row.column().label(text="Shadow fade:")
        row.column().preset_prop("highlight_intensity", text="")

        row = layout.row()
        row.column().label(text="Highlight color:")
        row.column().preset_prop("highlight_color", text="")

        row = layout.row()
        row.column().label(text="Crease color:")
        row.column().preset_prop("highlight_crease", text="")
        row.column().preset_prop("crease_amount", text="Amount")

        row = layout.row()
        row.column().label(text="Contour color:")
        row.column().preset_prop("highlight_contour", text="")
        row.column().preset_prop("contour_amount", text="Amount")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("highlight_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("highlight_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_EYELINER(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Eyeliner"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "eyeliner_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().preset_prop("eyeliner_top_1", text="T1")
        row.column().preset_prop("eyeliner_bottom_1", text="B1")

        row = layout.row()
        row.column().preset_prop("eyeliner_top_2", text="T2")
        row.column().preset_prop("eyeliner_bottom_2", text="B2")

        row = layout.row()
        row.column().preset_prop("eyeliner_top_3", text="T3")
        row.column().preset_prop("eyeliner_bottom_3", text="B3")

        row = layout.row()
        row.column().preset_prop("eyeliner_top_4", text="T4")
        row.column().preset_prop("eyeliner_bottom_4", text="B4")

        row = layout.row()
        row.column().preset_prop("eyeliner_top_5", text="T5")
        row.column().preset_prop("eyeliner_bottom_5", text="B5")

        row = layout.row()
        row.column().preset_prop("eyeliner_top_6", text="T6")
        row.column().preset_prop("eyeliner_bottom_6", text="B6")

        row = layout.row()
        row.column().label(text="Color:")
        row.column().preset_prop("eyeliner_settings_color", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("eyeliner_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("eyeliner_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_FACIAL_PAINT(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Facial Paint"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "facial_paint_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().preset_prop("facial_paint_1", text="Eyes")
        row.column().preset_prop("facial_paint_1_color", text="")

        row = layout.row()
        row.column().preset_prop("facial_paint_2", text="Forehead")
        row.column().preset_prop("facial_paint_2_color", text="")

        row = layout.row()
        row.column().preset_prop("facial_paint_3", text="Jaw")
        row.column().preset_prop("facial_paint_3_color", text="")

        row = layout.row()
        row.column().label(text="Thickness:")
        row.column().preset_prop("facial_paint_intensity", text="")

        row = layout.row()
        row.column().label(text="Granularity:")
        row.column().preset_prop("facial_paint_granularity", text="")

        row = layout.row()
        row.column().label(text="Metallic effect:")
        row.column().preset_prop("facial_paint_settings_metallic", text="")

        row = layout.row()
        row.column().label(text="Gloss / Matte:")
        row.column().preset_prop("facial_paint_settings_roughness", text="")

class TRANSHUMAN_PT_MAKEUP_EYEBROWS(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Eyebrows"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "eyebrows_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().label(text="Eyebrow type:")
        row.column().prop(context.scene.Transhuman_tool, "eyebrow_base_image", text="")

        row = layout.row()
        row.column().label(text="Eyebrows amount:")
        row.column().preset_prop("eyebrows_amount", text="")

        row = layout.row()
        row.column().label(text="Smudge:")
        row.column().preset_prop("eyebrows_fade", text="")

        row = layout.row()
        row.column().label(text="Color:")
        row.column().preset_prop("eyebrows_color_group", text="")

class TRANSHUMAN_PT_MAKEUP_NAILS(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAKEUP"
    bl_label = "Nail polish"

    def draw_header(self, context):
        if not context.scene.render.use_lock_interface:
            self.layout.enabled = False
        self.layout.prop(context.scene.Transhuman_tool, "nails_switch", text="")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().preset_prop("nail_amount", text="Amount")
        row.column().preset_prop("nail_polish_color", text="")

        row = layout.row()
        row.column().preset_prop("nail_polish_metallic", text="Metallic")
        row.column().preset_prop("nail_polish_roughness", text="Roughness")

        row = layout.row()
        row.column().preset_prop("nail_polish_coat", text="Coat")
        row.column().preset_prop("nail_glitter", text="Glitter")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "nail_length", text="Nail Length"
        )

class TRANSHUMAN_PT_WIG(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_WIG"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "WIG"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool,"hide_hair_wig", text="Hide Wig from View")
        row.column().prop(context.scene.Transhuman_tool,"hide_render_hair_wig",text="Hide Wig from Render",)
        row = box.row()

        box = layout.box()
        row = box.row()
        row.column().label(text="COLOR OPTIONS", icon="EYEDROPPER")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Scalp Color:")
        row.column().preset_prop("scalp_color", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Scalp Strength:")
        row.column().preset_prop("scalp_fade", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Main Color:")
        row.column().preset_prop("hair_color_picker", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "root_switch")
        row.column().preset_prop("root_color_picker", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Root Spread:")
        row.column().preset_prop("root_spread_0", text="")
        row.column().preset_prop("root_spread_1", text="")
        row.column().prop(context.scene.Transhuman_tool, "root_invert")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "highlights_switch")
        row.column().preset_prop("secondary_color_highlights", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Highlights Spread:")
        row.column().preset_prop("secondary_intensity_1", text="")
        row = box.row()
        
        box = layout.box()
        row = box.row()
        row.column().label(text="HAIR APEARANCE (BASIC):", icon="OPTIONS")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_mesh_curve", text="Curves to Mesh")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_spread", text="Spread Radius")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("root_puff", text="Puff Root")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_clump_switch", text="Clump")
        row.column().preset_prop("hair_clump_shape", text="Shape")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_random_length", text="Random length")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_resolution", text="Global Resolution")
        row = box.row()
        
        
        box = layout.box()

        row = box.row()
        row.column().label(text="CURLS & WAVES:", icon="OPTIONS")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_curls_switch", text="Curls On / Off")
        row.column().preset_prop("curl_clump_mode", text="Gravity")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("gravity_clump", text="Gravity Shape")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("curl_amplitude", text="Amplitude")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("curl_frequency", text="Frequency")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("curls_randomize", text="Randomize Direction")
        row.column().preset_prop("waves_curls_switch", text="Waves")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("curl_scale", text="Curl Scale Adjust")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("curl_resolution", text="Curl Resolution")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Global Resolution takes priority", icon="INFO")

        box = layout.box()

        row = box.row()
        row.column().label(text="LOOSE HAIRS:", icon="OPTIONS")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("loose_hair_decimate", text="Loose Hairs Probability")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("loose_hair_amount", text="Amount")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("loose_hair_spread", text="Spread")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("loose_hairs_frizz", text="Frizz")
        row = box.row()


class TRANSHUMAN_PT_WIG_CURVES(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_WIG_CURVES"
    bl_parent_id = "TRANSHUMAN_PT_WIG"
    bl_label = "  Advanced Options (Curves)  ▼"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="Hair Appearance (CURVES):", icon="OUTLINER_OB_CURVES")
        
        row = box.row()
        row.column().label(text="HAIR LOOK:", icon="OPTIONS")
    
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_amount", text="Hairs Amount")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("curves_hair_thickness", text="Hairs Thickness")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("fluff_strands", text="Fluff Strands")

        row = box.row()
        
        box = layout.box()
        row = box.row()
        row = box.row()
        row.column().label(text="HAIR FRIZZ:", icon="OPTIONS")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("noise_strength", text="Noise Strength")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("noise_scale", text="Noise Density")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("noise_shape", text="Noise Shape")
        row = box.row()


class TRANSHUMAN_PT_WIG_MESH(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_WIG_MESH"
    bl_parent_id = "TRANSHUMAN_PT_WIG"
    bl_label = "  Advanced Options (Mesh)  ▼"

    def draw(self, context):
        layout = self.layout

        box = layout.box()

        row = box.row()
        row.column().label(text="Hair Appearance (MESH):", icon="MESH_DATA")

        row = box.row()
        row.column().label(text="CURLS & WAVES:", icon="OPTIONS")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("mesh_tubes_cards", text="Tubes to Cards")
        row.column().preset_prop("mesh_hair_subdivision", text="Mesh Resolution")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("inherit_curve_curls", text="Inherit Curls From Curves")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("feigned_uv_curls", text="Feign Curls from UV (Tubes only. Incompatible with TYPES)")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("tubes_amplitude", text="Tubes Curl Amplitude")
        
        box = layout.box()
        row = box.row()
        row.column().label(text="HAIR TYPES:", icon="OPTIONS")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="0 - Straight")
        row.column().label(text="1 - Messy")
        row.column().label(text="2 - Soft Waves")
        row.column().label(text="3 - Wavy")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="4 - Zig-Zag")
        row.column().label(text="5 - Curls")
        row.column().label(text="6 - Frizzy")
        row.column().label(text="7 - Coils")
        row = box.row()

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("hair_type_mesh", text="Hair Type Number")
        row.column().preset_prop("short_hair", text="Short Hair")
        row = box.row()
        
        box = layout.box()
        row = box.row()
        row.column().label(text="EXTRAS:", icon="OPTIONS")
        row = box.row()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("random_direction_mesh", text="Random Direction")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Randomly changes the direction of the hair texture.", icon="INFO")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("mesh_loose_hairs", text="Loose Hairs")
        row.column().preset_prop("mesh_loose_resample", text="Resolution")
        row.column().preset_prop("loose_hair_size", text="Width")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Add Loose Hairs and increase/decrease their resolution.", icon="INFO")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("interpolate_root_mesh", text="Fix bald spots")
        row.column().preset_prop("interpolate_mesh_amount", text="Amount")
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="You can edit area of effect in vertex group 'FILL'", icon="INFO")
        
        box = layout.box()
        row = box.row()
        row.column().label(text="MATERIAL:", icon="OPTIONS")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("mesh_hair_metallic", text="Metallic")
        row.column().preset_prop("mesh_hair_specular", text="Specular")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("mesh_hair_roughness", text="Roughness")
        row.column().preset_prop("mesh_hair_ior", text="IOR")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("mesh_hair_clearcoat", text="Clearcoat")
        row.column().preset_prop(
            "mesh_hair_clearcoat_roughness", text="Clearcoat Roughness"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("mesh_translucent", text="Translucency")
        row.column().prop(
            context.scene.Transhuman_tool, "mesh_thickness", text="Hair thickness"
        )
        row = box.row()

class TRANSHUMAN_PT_BODY_HAIR(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_BODY_HAIR"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "HAIR & FUR"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool,
            "hide_body_hairs",
            text="Hide Body Hairs from View",
        )

class TRANSHUMAN_PT_EYEBROWS_HAIR(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_BODY_HAIR"
    bl_label = "   Eyebrows"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="Eyebrows Color:", icon="EYEDROPPER")
        row.column().preset_prop("eyebrows_color_group", text="")

        box = layout.box()
        row = box.row()
        row.column().label(text="EYEBROWS (CURVES)", icon="OUTLINER_OB_CURVES")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_1_curves", text="Eyebrows 1"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_2_curves", text="Eyebrows 2"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_3_curves", text="Eyebrows 3"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_4_curves", text="Eyebrows 4"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_5_curves", text="Eyebrows 5"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("eyebrows_curves_amount", text="Hair Amount")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("eyebrows_curves_spread", text="Hair Spread")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("eyebrows_curves_thickness", text="Thickness")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("eyebrows_noise", text="Noise")

        box = layout.box()
        row = box.row()
        row.column().label(text="EYEBROWS (MESH)", icon="MESH_DATA")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_1_mesh", text="Eyebrows 1"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_2_mesh", text="Eyebrows 2"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_3_mesh", text="Eyebrows 3"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_4_mesh", text="Eyebrows 4"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "eyebrows_5_mesh", text="Eyebrows 5"
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="TURN CURVES TO MESH", icon="ARROW_LEFTRIGHT")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("eyebrows_to_mesh", text="Curves to Mesh")
        row.column().preset_prop("eyebrows_type", text="Hair Type")

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="You can edit options in the obejct's modifier panel →", icon="INFO")

class TRANSHUMAN_PT_EYELASHES_HAIR(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_BODY_HAIR"
    bl_label = "   Eyelashes"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="Eyelashes Color:", icon="EYEDROPPER")
        row.column().preset_prop("eyelashes_color", text="")

        box = layout.box()
        row = box.row()
        row.column().label(text="EYELASHES (CURVES)", icon="OUTLINER_OB_CURVES")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "eyelashes_curves", text="On / Off"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair thickness:")
        row.column().preset_prop("eyelashes_thickness_top", text="Top")
        row.column().preset_prop("eyelashes_thickness_bottom", text="Bottom")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Length:")
        row.column().preset_prop("eyelashes_length_top", text="Top")
        row.column().preset_prop("eyelashes_length_bottom", text="Bottom")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Amount:")
        row.column().preset_prop("eyelashes_amount_top", text="Top")
        row.column().preset_prop("eyelashes_amount_bottom", text="Bottom")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Spread:")
        row.column().preset_prop("eyelashes_spread_top", text="Top")
        row.column().preset_prop("eyelashes_spread_bottom", text="Bottom")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "eyelashes_clump_switch")
        row.column().preset_prop("eyelashes_clump", text="Amount")

        box = layout.box()
        row = box.row()
        row.column().label(text="TURN CURVES TO MESH", icon="ARROW_LEFTRIGHT")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("top_eyelashes_to_mesh", text="Top")
        row.column().preset_prop("top_eyelashes_type", text="Hair Type")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("bottom_eyelashes_to_mesh", text="Bottom")
        row.column().preset_prop("bottom_eyelashes_type", text="Hair Type")

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="You can edit options in the obejct's modifier panel →", icon="INFO")

class TRANSHUMAN_PT_BEARD(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_BODY_HAIR"
    bl_label = "   Beard & Stubble"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().label(text="Beard Color:", icon="EYEDROPPER")
        row.column().preset_prop("beard_color", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "secondary_beard_switch")
        row.column().preset_prop("secondary_beard_color_picker", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop(
            "beard_secondary_intensity", text="Secondary Amount"
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="BEARD (CURVES)", icon="OUTLINER_OB_CURVES")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "stubble_curves", text="On / Off"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Amount:")
        row.column().preset_prop("stubble_amount", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Spread:")
        row.column().preset_prop("stubble_spread", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Length:")
        row.column().preset_prop("stubble_length", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Clump:")
        row.column().preset_prop("stubble_clump", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Decimate:")
        row.column().preset_prop("stubble_decimate", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Thickness:")
        row.column().preset_prop("stubble_thickness", text="")
          
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("beard_curls_switch", text="Curl (Inherits settings from WIG Curls)")
        
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("beard_curls_scale", text="Scale")
        row.column().preset_prop("beard_noise", text="Noise")

        box = layout.box()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "nose_hair_curves", text="Nose Hair"
        )
        row.column().preset_prop("nose_hair_length", text="Nose Hair Length")

        box = layout.box()
        row = box.row()
        row.column().label(text="STUBBLE (TEXTURE)", icon="TEXTURE_DATA")

        row = box.row()
        row.column().label(text="Stubble Color:", icon="BLANK1")
        row.column().preset_prop("stubble_texture_color", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "stubble_switch")
        row.column().prop(context.scene.Transhuman_tool, "stubble_trim_switch")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Stubble hair bump:")
        row.column().preset_prop("stubble_bump", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Stubble hair thickness:")
        row.column().preset_prop("stubble_mesh_thickness", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "stubble_image", text="")

        box = layout.box()
        row = box.row()
        row.column().label(text="TURN CURVES TO MESH", icon="ARROW_LEFTRIGHT")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("beard_to_mesh", text="Beard")
        row.column().preset_prop("beard_type", text="Hair Type")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("nosehair_to_mesh", text="Nose Hair")
        row.column().preset_prop("nosehair_type", text="Hair Type")

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="You can edit options in the obejct's modifier panel →", icon="INFO")

class TRANSHUMAN_PT_BODY_HAIR_SUB(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_BODY_HAIR"
    bl_label = "   Body Hair"

    def draw(self, context):
        layout = self.layout

        box = layout.box()

        row = box.row()
        row.column().label(text="Body Hair Color:", icon="EYEDROPPER")
        row.column().preset_prop("body_hair_color", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "secondary_body_hair_switch")
        row.column().preset_prop("secondary_hair_color_picker", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop(
            "body_hair_secondary_intensity", text="Secondary Amount"
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="BODY HAIR", icon="OUTLINER_OB_CURVES")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "peach_fuzz_curves", text="Peach Fuzz"
        )
        row.column().prop(context.scene.Transhuman_tool, "chest_curves", text="Chest")
        row.column().prop(
            context.scene.Transhuman_tool, "chest_extra_curves", text="Chest Extra"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "armpit_curves", text="Armpit")
        row.column().prop(
            context.scene.Transhuman_tool, "stomach_curves", text="Stomach"
        )
        row.column().prop(context.scene.Transhuman_tool, "back_curves", text="Back")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "arms_curves", text="Arms")
        row.column().prop(
            context.scene.Transhuman_tool, "forearms_curves", text="Forearms"
        )
        row.column().prop(context.scene.Transhuman_tool, "hands_curves", text="Hands")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "thighs_curves", text="Thighs")
        row.column().prop(context.scene.Transhuman_tool, "shins_curves", text="Shins")
        row.column().prop(context.scene.Transhuman_tool, "feet_curves", text="Feet")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "pubic_f_curves", text="Pubic (F)"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "pubic_m_curves", text="Pubic (M)"
        )

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Amount:")
        row.column().preset_prop("body_hair_amount", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Spread:")
        row.column().preset_prop("body_hair_spread", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Trim:")
        row.column().preset_prop("body_hair_length", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Clump:")
        row.column().preset_prop("body_hair_clump", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Decimate:")
        row.column().preset_prop("body_hair_decimate", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Hair Thickness:")
        row.column().preset_prop("body_hair_thickness", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Noise Scale:")
        row.column().preset_prop("body_hair_noise_scale", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Noise Strength:")
        row.column().preset_prop("body_hair_noise_strength", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Noise Shape:")
        row.column().preset_prop("body_hair_noise_shape", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Random Length:")
        row.column().preset_prop("body_hair_random_length_min", text="Min.")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="")
        row.column().preset_prop("body_hair_random_length_max", text="Max.")

        box = layout.box()
        row = box.row()
        row.column().label(text="TURN CURVES TO MESH", icon="ARROW_LEFTRIGHT")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().preset_prop("bodyhair_to_mesh", text="Curves to Mesh")

        row = box.row()
        row.column().label(text="", icon="BLANK1")
        row.column().label(text="You can edit options in the obejct's modifier panel →", icon="INFO")

        box = layout.box()
        row = box.row()
        row.column().label(text="BODY HAIR (TEXTURE)", icon="TEXTURE_DATA")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "body_hair_switch")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Bump:")
        row.column().preset_prop("body_hair_bump", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().label(text="Thickness:")
        row.column().preset_prop("body_hair_thickness_texture", text="")

        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(
            context.scene.Transhuman_tool, "body_hair_image", text="Amount"
        )

class TRANSHUMAN_PT_TEETH(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_TEETH"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "TEETH"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tool = scene.Transhuman_tool

        box = layout.box()
        row = box.row()
        row.column().label(text="Denture Height:")
        row.column().prop(context.scene.Transhuman_tool, "denture_height", text="±")

        row = box.row()
        row.column().label(text="Denture Position:")
        row.column().prop(context.scene.Transhuman_tool, "denture_position", text="±")
        
        box = layout.box()
        row = box.row()
        row.column().label(text="Teeth age:")
        row.column().preset_prop("teeth_age", text="")
        
        row = box.row()
        row.column().label(text="Color Saturation:")
        row.column().preset_prop("teeth_saturation", text="")

        box = layout.box()
        row = box.row()
        row.column().label(text="Gap:")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "teeth_gap_top", text="Top")
        row.column().prop(
            context.scene.Transhuman_tool, "teeth_gap_bottom", text="Bottom"
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="Crookedness:")

        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "crooked_teeth_top", text="Top"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "crooked_teeth_bottom", text="Bottom"
        )

        box = layout.box()
        row = box.row()
        row.column().label(text="Shape:")

        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "teeth_length", text="Length ±"
        )
        row.column().prop(context.scene.Transhuman_tool, "teeth_size", text="Size ±")

        box = layout.box()
        row = box.row()
        row.column().label(text="Fangs:")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "fangs_top", text="Top")
        row.column().prop(context.scene.Transhuman_tool, "fangs_bottom", text="Bottom")

        box = layout.box()
        row = box.row()
        row.column().label(text="Missing teeth (by Dental Chart Nº):")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "missing_6", text="6")
        row.column().prop(context.scene.Transhuman_tool, "missing_7", text="7")
        row.column().prop(context.scene.Transhuman_tool, "missing_8", text="8")
        row.column().prop(context.scene.Transhuman_tool, "missing_9", text="9")
        row.column().prop(context.scene.Transhuman_tool, "missing_10", text="10")
        row.column().prop(context.scene.Transhuman_tool, "missing_11", text="11")

        row = box.row()
        row.column().prop(context.scene.Transhuman_tool, "missing_27", text="27")
        row.column().prop(context.scene.Transhuman_tool, "missing_26", text="26")
        row.column().prop(context.scene.Transhuman_tool, "missing_25", text="25")
        row.column().prop(context.scene.Transhuman_tool, "missing_24", text="24")
        row.column().prop(context.scene.Transhuman_tool, "missing_23", text="23")
        row.column().prop(context.scene.Transhuman_tool, "missing_22", text="22")

class TRANSHUMAN_PT_UNDERWEAR(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "CLOTHES"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.column().prop(
            context.scene.Transhuman_tool, "underwear_top_switch", text="Top"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "underwear_bottom_switch", text="Bottom"
        )
        row.column().label(icon="EYEDROPPER")
        row.column().preset_prop("underwear_color", text="")

        row = box.row()
        row = box.row()
        op = row.column().operator(
            "wm.url_open", text="Get Clothes & Accessories", icon="URL"
        )
        op.url = "https://sm5.heledahn.com/collections/clothes"
        
        box = layout.box()
        row = box.row()
        row.column().label(icon="BLANK1")
        row.column().prop(context.scene.Transhuman_tool, "clothes_adjust_switch", text="Clothes Adjust")
        
        row = box.row()
        row.column().label(
            text="• Adds animation to adjust ZERO clothes to custom body (frames 1-40)",
            icon="INFO",)
        row = box.row()
        row.column().label(
            text="• Use 'Mixamo' armature & play animation to see adjust",
            icon="BLANK1",
        )
        row = box.row()
        row.column().label(
            text="• Imported garment needs 'Cloth Modifier'",
            icon="BLANK1",
        )

class TRANSHUMAN_PT_NSFW(TranshumanPanel, bpy.types.Panel):
    bl_idname = "TRANSHUMAN_PT_NSFW"
    bl_parent_id = "TRANSHUMAN_PT_MAIN"
    bl_label = "NSFW (Adult)"

    def draw(self, context):
        layout = self.layout

class TRANSHUMAN_PT_NIPPLES(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_NSFW"
    bl_label = "Nipples"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "nipples", text="Flat / Protruding ±"
        )

        row = layout.row()
        row.column().preset_prop("nipples_color", text="")
        row.column().preset_prop("nipples_def", text="Border Definition")

class TRANSHUMAN_PT_FEMALE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_NSFW"
    bl_label = "Female Genitals"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "vulva", text="Female genitals"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "pubic_f_curves", text="Pubic hair (Curves)"
        )

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "labia_size", text="Size"
        )
        row.column().prop(
            context.scene.Transhuman_tool, "labia_sym", text="Asymmetry"
        )
        
        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "vulva_open", text="Open / Close"
        )

class TRANSHUMAN_PT_MALE(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_NSFW"
    bl_label = "Male Genitals"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "penis", text="Male genitals")
        row.column().prop(
            context.scene.Transhuman_tool, "circumcised", text="Circumcision"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "gen_rig", text="Rig")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "pubic_m_curves", text="Pubic hair (Curves)"
        )

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "bulge", text="Bulge")
        row.column().prop(
            context.scene.Transhuman_tool, "bulge_protrusion", text="Bulge amount"
        )

        row = layout.row()
        row.column().label(
            text="Add 'Bulge' when using Underwear to simulate volume", icon="INFO"
        )

class TRANSHUMAN_PT_ANUS(TranshumanPanel, bpy.types.Panel):
    bl_parent_id = "TRANSHUMAN_PT_NSFW"
    bl_label = "Anus"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.column().prop(context.scene.Transhuman_tool, "anus", text="Anus")

        row = layout.row()
        row.column().prop(
            context.scene.Transhuman_tool, "anus_open", text="Open / Close"
        )


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    # Main Transhuman Properties
    Transhuman_Properties,
    # Operators
    TRANSHUMAN_OT_LOAD_ORIGINAL_COLLECTION,
    TRANSHUMAN_OT_OPEN_SET_IMAGE,
    TRANSHUMAN_OT_SAVE_PRESET,
    TRANSHUMAN_OT_LOAD_PRESET,
    TRANSHUMAN_OT_RANDOMIZE_PRESET,
    TRANSHUMAN_OT_RANDOMIZE_FROM_PRESET,
    TRANSHUMAN_OT_CONCEIVE_FROM_PRESETS,
    TRANSHUMAN_OT_BIND_MESH,
    TRANSHUMAN_OT_UNBIND_MESH,
    TRANSHUMAN_OT_FINALIZE_HAIR,
    TRANSHUMAN_OT_FINALIZE_BODY_HAIR,
    # Panels
    TRANSHUMAN_PT_INIT,
    TRANSHUMAN_PT_MAIN,
    TRANSHUMAN_PT_RIG,
    TRANSHUMAN_PT_EYES,
    TRANSHUMAN_PT_SKIN,
    TRANSHUMAN_PT_FACE,
    TRANSHUMAN_PT_HEAD_SHAPE,
    TRANSHUMAN_PT_FACE_SHAPE,
    TRANSHUMAN_PT_CHEEKS_SHAPE,
    TRANSHUMAN_PT_CHIN_SHAPE,
    TRANSHUMAN_PT_JAW_SHAPE,
    TRANSHUMAN_PT_NECK_SHAPE,
    TRANSHUMAN_PT_EYE_SHAPE,
    TRANSHUMAN_PT_BROW_SHAPE,
    TRANSHUMAN_PT_NOSE_SHAPE,
    TRANSHUMAN_PT_MOUTH_SHAPE,
    TRANSHUMAN_PT_EAR_SHAPE,
    TRANSHUMAN_PT_BODY,
    TRANSHUMAN_PT_BODY_OPT,
    TRANSHUMAN_PT_PERSONA,
    TRANSHUMAN_PT_MODIFIERS,
    TRANSHUMAN_PT_TEETH,
    TRANSHUMAN_PT_MAKEUP,
    TRANSHUMAN_PT_MAKEUP_BASE,
    TRANSHUMAN_PT_MAKEUP_BLUSH,
    TRANSHUMAN_PT_MAKEUP_LIPS,
    TRANSHUMAN_PT_MAKEUP_LIP_LINER,
    TRANSHUMAN_PT_MAKEUP_EYESHADOW,
    TRANSHUMAN_PT_MAKEUP_LASHLINE,
    TRANSHUMAN_PT_MAKEUP_SHADOW_INNER,
    TRANSHUMAN_PT_MAKEUP_SHADOW_OUTER,
    TRANSHUMAN_PT_MAKEUP_HIGHLIGHT,
    TRANSHUMAN_PT_MAKEUP_EYELINER,
    TRANSHUMAN_PT_MAKEUP_FACIAL_PAINT,
    TRANSHUMAN_PT_MAKEUP_EYEBROWS,
    TRANSHUMAN_PT_MAKEUP_NAILS,
    TRANSHUMAN_PT_WIG,
    TRANSHUMAN_PT_WIG_CURVES,
    TRANSHUMAN_PT_WIG_MESH,
    TRANSHUMAN_PT_BODY_HAIR,
    TRANSHUMAN_PT_EYEBROWS_HAIR,
    TRANSHUMAN_PT_EYELASHES_HAIR,
    TRANSHUMAN_PT_BEARD,
    TRANSHUMAN_PT_BODY_HAIR_SUB,
    TRANSHUMAN_PT_UNDERWEAR,
    TRANSHUMAN_PT_NSFW,
    TRANSHUMAN_PT_NIPPLES,
    TRANSHUMAN_PT_FEMALE,
    TRANSHUMAN_PT_MALE,
    TRANSHUMAN_PT_ANUS,
)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    bpy.types.Scene.Transhuman_tool = PointerProperty(type=Transhuman_Properties)


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.Transhuman_tool


if __name__ == "__main__":
    register()
