presetSaver = preset_saver.PresetSaver(
    [
        # list of names of the props to save.
        "body_hair_image",
        "body_hair_mesh_UV_selector",
        "stubble_image",
        "eyelashes_top_length",
        "eyelashes_bottom_length",
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
        "nose_tip_position",
        "nose_tip_shape",
        "infratip",
        "infratip_thickness",
        "wings",
        "wings_arch",
        "nose_cleft",
        "nose_length",
        "nose_width",
        "nose_tip_move",
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
        "denture_height",
        "fangs_top",
        "fangs_bottom",
        "eyelashes_mesh",
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
        "pubic_f_switch",
        "pubic_m_switch",
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
        "secondary_body_hair_switch",
        "highlights_switch",
        "root_switch",
        "root_invert",
        "imported_persona_displ",
        "persona_displ_value",
        "imported_persona_mesh",
        "imported_persona_skin",
        "persona_switch",
        "clothes_adjust_switch",
        "hide_hair_wig",
        "hide_render_hair_wig",
        "dynamic_breasts",
    ],
    {
        "smooth_custom": [
            lambda: bpy.data.objects["SM5 Rest Pose Transhuman"].modifiers[
                "Smooth Custom"
            ],
            "iterations",
        ],
        "color_amount": [
            lambda: bpy.data.node_groups["SM5 Dome"].nodes["color_amount"].inputs[0],
            "default_value",
        ],
        "environment_color": [
            lambda: bpy.data.node_groups["SM5 Dome"]
            .nodes["environment_color"]
            .outputs[0],
            "default_value",
            {"type": "list"},
        ],
        "light_intensity": [
            lambda: bpy.data.node_groups["SM5 Dome"].nodes["light_intensity"].inputs[0],
            "default_value",
        ],
        "dome_mapping": [
            lambda: bpy.data.node_groups["SM5 Dome"].nodes["dome_mapping"].inputs[2],
            "default_value",
            {"type": "list"},
        ],
        "dome_scale": [lambda: bpy.data.objects["SM5 Environment Dome"], "scale"],
        "dome_location": [lambda: bpy.data.objects["SM5 Environment Dome"], "location"],
        "dome_flat": [
            lambda: bpy.data.shape_keys["Dome Keys"].key_blocks["Flat"],
            "value",
        ],
        "dome_ceiling": [
            lambda: bpy.data.shape_keys["Dome Keys"].key_blocks["Ceiling Flat"],
            "value",
        ],
        "dome_sphere": [
            lambda: bpy.data.shape_keys["Dome Keys"].key_blocks["Sphere"],
            "value",
        ],
        "floor_reflection": [
            lambda: bpy.data.materials["Shadow Catcher Material"]
            .node_tree.nodes["Principled BSDF"]
            .inputs[6],
            "default_value",
        ],
        "floor_roughness": [
            lambda: bpy.data.materials["Shadow Catcher Material"]
            .node_tree.nodes["Principled BSDF"]
            .inputs[9],
            "default_value",
        ],
        "scalp_color": [
            lambda: bpy.data.materials["SM5 Scalp Material Transhuman"]
            .node_tree.nodes["scalp_color"]
            .outputs[0],
            "default_value",
        ],
        "scalp_fade": [
            lambda: bpy.data.materials["SM5 Scalp Material Transhuman"]
            .node_tree.nodes["scalp_fade"]
            .inputs[1],
            "default_value",
        ],
        "eyebrows_color_group": [
            lambda: bpy.data.node_groups["SM5 Eyebrows Hair Color Transhuman"]
            .nodes["eyebrows_color_group"]
            .outputs[0],
            "default_value",
        ],
        "body_hair_color": [
            lambda: bpy.data.node_groups["SM5 Body Hair Color Transhuman"]
            .nodes["body_hair_color"]
            .outputs[0],
            "default_value",
        ],
        "secondary_hair_color_picker": [
            lambda: bpy.data.node_groups["SM5 Body Hair Color Transhuman"]
            .nodes["secondary_hair_color_picker"]
            .outputs[0],
            "default_value",
        ],
        "body_hair_amount": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["body_hair_amount"]
            .inputs[2],
            "default_value",
        ],
        "hair_mesh_curve": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_mesh_curve"].inputs[1],"default_value",],
        "feigned_uv_curls": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["feigned_uv_curls"].inputs[0],"default_value",],
        "inherit_curve_curls": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["inherit_curve_curls"].inputs[1],"default_value",],
        "mesh_tubes_cards": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_tubes_cards"].inputs[0],"default_value",],
        "hair_type_mesh": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_type_mesh"],"integer",],
        "random_direction_mesh": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["random_direction_mesh"].inputs[0],"default_value",],
        "mesh_loose_hairs": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_loose_hairs"].inputs[0],"default_value",],
        "tubes_amplitude": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["tubes_amplitude"].outputs[0],"default_value",],
        "mesh_loose_resample": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["mesh_loose_resample"],"integer",],
        "hair_random_length": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["hair_random_length"].outputs[0],"default_value",],
        "interpolate_root_mesh": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["interpolate_root_mesh"].inputs[1],"default_value",],
        "interpolate_mesh_amount": [lambda: bpy.data.node_groups["SM5 Hair"].nodes["interpolate_mesh_amount"],"integer",],
        "persona_displ_value": [lambda:bpy.data.node_groups["SM5 Body Displacement"].nodes["persona_displ_value"].outputs[0],"default_value",],
        
        "body_hair_spread": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["body_hair_spread"]
            .outputs[0],
            "default_value",
        ],
        "body_hair_length": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["body_hair_length"]
            .inputs[3],
            "default_value",
        ],
        "body_hair_clump": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["hair_clump"]
            .inputs[0],
            "default_value",
        ],
        "body_hair_noise_scale": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["noise_scale"]
            .inputs[1],
            "default_value",
        ],
        "body_hair_noise_strength": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["noise_strength"]
            .outputs[0],
            "default_value",
        ],
        "body_hair_noise_shape": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["noise_shape"]
            .outputs[0],
            "default_value",
        ],
        "body_hair_random_length_min": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["hair_random_length"]
            .inputs[2],
            "default_value",
        ],
        "body_hair_random_length_max": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["hair_random_length"]
            .inputs[3],
            "default_value",
        ],
        "nose_hair_length": [
            lambda: bpy.data.node_groups["SM5 Nose Hairs Transhuman"]
            .nodes["nose_hair_length"]
            .inputs[3],
            "default_value",
        ],
        "body_hair_decimate": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["hair_decimate"]
            .inputs[6],
            "default_value",
        ],
        "body_hair_thickness": [
            lambda: bpy.data.node_groups["SM5 Body Hair Transhuman"]
            .nodes["thickness"]
            .outputs[0],
            "default_value",
        ],
        "body_hair_secondary_intensity": [
            lambda: bpy.data.node_groups["SM5 Body Hair Color Transhuman"]
            .nodes["secondary_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "body_hair_mesh_thickness": [
            lambda: bpy.data.materials["SM5 Body Hair Mesh Material"]
            .node_tree.nodes["body_hair_mesh_thickness"]
            .inputs[1],
            "default_value",
        ],
        "mesh_body_hair_amount": [
            lambda: bpy.data.node_groups["SM5 Mesh Body Hair Transhuman"]
            .nodes["mesh_body_hair_amount"]
            .inputs[2],
            "default_value",
        ],
        "mesh_body_hair_scale": [
            lambda: bpy.data.node_groups["SM5 Mesh Body Hair Transhuman"]
            .nodes["mesh_body_hair_scale"]
            .inputs[2],
            "default_value",
        ],
        "mesh_body_hair_groom": [
            lambda: bpy.data.node_groups["SM5 Mesh Body Hair Transhuman"]
            .nodes["mesh_body_hair_groom"]
            .inputs[0],
            "default_value",
        ],
        "mesh_body_hair_factor": [
            lambda: bpy.data.node_groups["SM5 Mesh Body Hair Transhuman"]
            .nodes["mesh_body_hair_factor"]
            .inputs[1],
            "default_value",
        ],
        "body_hair_bump": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["body_hair_bump"]
            .inputs[0],
            "default_value",
        ],
        "body_hair_thickness_texture": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["body_hair_thickness_texture"]
            .inputs[1],
            "default_value",
        ],
        "stubble_color": [
            lambda: bpy.data.node_groups["SM5 Stubble Color Transhuman"]
            .nodes["stubble_color"]
            .outputs[0],
            "default_value",
        ],
        "stubble_bump": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["stubble_bump"]
            .inputs[0],
            "default_value",
        ],
        "stubble_thickness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["stubble_thickness"]
            .inputs[1],
            "default_value",
        ],
        "cornea_reflective": [
            lambda: bpy.data.materials["SM5 Cornea Material Transhuman"]
            .node_tree.nodes["cornea_reflective"]
            .outputs[0],
            "default_value",
        ],
        "eye_color_picker": [
            lambda: bpy.data.materials["SM5 Eyes Material Transhuman"]
            .node_tree.nodes["eye_color_picker"]
            .outputs[0],
            "default_value",
        ],
        "eye_color_chroma": [
            lambda: bpy.data.materials["SM5 Eyes Material Transhuman"]
            .node_tree.nodes["eye_color_chroma"]
            .inputs[1],
            "default_value",
        ],
        "halo": [
            lambda: bpy.data.materials["SM5 Eyes Material Transhuman"]
            .node_tree.nodes["halo"]
            .inputs[0],
            "default_value",
        ],
        "halo_color": [
            lambda: bpy.data.materials["SM5 Eyes Material Transhuman"]
            .node_tree.nodes["halo_color"]
            .outputs[0],
            "default_value",
        ],
        "sclera_cornea_mixer": [
            lambda: bpy.data.materials["SM5 Cornea Material Transhuman"]
            .node_tree.nodes["sclera_cornea_mixer"]
            .inputs[0],
            "default_value",
        ],
        "sclera_cornea_settings_color": [
            lambda: bpy.data.materials["SM5 Cornea Material Transhuman"]
            .node_tree.nodes["sclera_cornea_settings"]
            .inputs[0],
            "default_value",
        ],
        "sclera_cornea_settings_transmission": [
            lambda: bpy.data.materials["SM5 Cornea Material Transhuman"]
            .node_tree.nodes["sclera_cornea_settings"]
            .inputs[17],
            "default_value",
        ],
        "sclera_cornea_settings_roughness": [
            lambda: bpy.data.materials["SM5 Cornea Material Transhuman"]
            .node_tree.nodes["sclera_cornea_settings"]
            .inputs[18],
            "default_value",
        ],
        "sclera_cornea": [
            lambda: bpy.data.materials[
                "SM5 Cornea Material Transhuman"
            ].node_tree.nodes["sclera_cornea"],
            "layer_name",
        ],
        "eye_redness": [
            lambda: bpy.data.materials["SM5 Eyes Material Transhuman"]
            .node_tree.nodes["eye_redness"]
            .inputs[0],
            "default_value",
        ],
        "eye_settings": [
            lambda: bpy.data.materials["SM5 Cornea Material Transhuman"]
            .node_tree.nodes["eye_settings"]
            .inputs[18],
            "default_value",
        ],
        "tear_settings": [
            lambda: bpy.data.materials["SM5 Tear Material Transhuman"]
            .node_tree.nodes["tear_settings"]
            .inputs[0],
            "default_value",
        ],
        "eyebrows_noise": [
            lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman"]
            .nodes["noise_strength"]
            .outputs[0],
            "default_value",
        ],
        "eyebrows_curves_thickness": [
            lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman"]
            .nodes["thickness"]
            .outputs[0],
            "default_value",
        ],
        "eyebrows_curves_spread": [
            lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman"]
            .nodes["eyebrows_spread"]
            .outputs[0],
            "default_value",
        ],
        "eyebrows_curves_amount": [
            lambda: bpy.data.node_groups["SM5 Eyebrows Transhuman"]
            .nodes["eyebrows_amount"]
            .inputs[2],
            "default_value",
        ],
        "eyelashes_color": [
            lambda: bpy.data.node_groups["SM5 Eyelashes Color Transhuman"]
            .nodes["eyelashes_color"]
            .outputs[0],
            "default_value",
        ],
        "eyelashes_thickness_top": [
            lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman"]
            .nodes["eyelashes_thickness"]
            .outputs[0],
            "default_value",
        ],
        "eyelashes_thickness_bottom": [
            lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman"]
            .nodes["eyelashes_thickness"]
            .outputs[0],
            "default_value",
        ],
        "eyelashes_length_top": [
            lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman"]
            .nodes["eyelashes_length"]
            .inputs[3],
            "default_value",
        ],
        "eyelashes_length_bottom": [
            lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman"]
            .nodes["eyelashes_length"]
            .inputs[3],
            "default_value",
        ],
        "eyelashes_amount_top": [
            lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman"]
            .nodes["Duplicate Elements"]
            .inputs[2],
            "default_value",
        ],
        "eyelashes_amount_bottom": [
            lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman"]
            .nodes["Duplicate Elements"]
            .inputs[2],
            "default_value",
        ],
        "eyelashes_spread_top": [
            lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman"]
            .nodes["eyelashes_spread"]
            .outputs[0],
            "default_value",
        ],
        "eyelashes_spread_bottom": [
            lambda: bpy.data.node_groups["SM5 Bottom Eyelashes Transhuman"]
            .nodes["eyelashes_spread"]
            .outputs[0],
            "default_value",
        ],
        "eyelashes_clump": [
            lambda: bpy.data.node_groups["SM5 Top Eyelashes Transhuman"]
            .nodes["eyelashes_clump"]
            .inputs[0],
            "default_value",
        ],
        "eyelashes_thickness_mesh": [
            lambda: bpy.data.materials["SM5 Eyelashes Mesh Material"]
            .node_tree.nodes["eyelashes_thickness"]
            .inputs[1],
            "default_value",
        ],
        "stubble_spread": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["stubble_spread"]
            .outputs[0],
            "default_value",
        ],
        "stubble_amount": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["stubble_amount"]
            .inputs[2],
            "default_value",
        ],
        "stubble_length": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["stubble_length"]
            .inputs[3],
            "default_value",
        ],
        "stubble_decimate": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["stubble_decimate"]
            .inputs[6],
            "default_value",
        ],
        "stubble_thickness": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["stubble_thickness"]
            .outputs[0],
            "default_value",
        ],
        "stubble_clump": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["stubble_clump"]
            .inputs[0],
            "default_value",
        ],
        "skin_hue": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["skin_hue"]
            .inputs[7],
            "default_value",
        ],
        "skin_saturation": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["skin_saturation"]
            .inputs[0],
            "default_value",
        ],
        "skin_chroma": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["skin_chroma"]
            .inputs[1],
            "default_value",
        ],
        "skin_health": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["health"]
            .inputs[0],
            "default_value",
        ],
        "skin_detail_strength": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["skin_detail_strength"]
            .inputs[0],
            "default_value",
        ],
        "face_definition": [
            lambda: bpy.data.node_groups["SM5 Transhuman Normal"]
            .nodes["face_definition"]
            .inputs[0],
            "default_value",
        ],
        "body_definition": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["transhuman_normal"]
            .inputs[0],
            "default_value",
        ],
        "skin_sweat": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["sweat"]
            .inputs[1],
            "default_value",
        ],
        "skin_reflection": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["skin_reflection"]
            .inputs[0],
            "default_value",
        ],
        "skin_subsurface": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["skin_subsurface"]
            .outputs[0],
            "default_value",
        ],
        "scars_color_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["scars_color_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "scars_bump": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["scars_bump"]
            .inputs[0],
            "default_value",
        ],
        "scars_color_saturation": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["scars_color_saturation"]
            .inputs[1],
            "default_value",
        ],
        "underwear_color": [
            lambda: bpy.data.materials["SM5 Underwear Material"]
            .node_tree.nodes["underwear_color"]
            .inputs[6],
            "default_value",
        ],
        "scars_color_brightness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["scars_color_brightness"]
            .inputs[1],
            "default_value",
        ],
        "base_makeup_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["base_makeup_color"]
            .outputs[0],
            "default_value",
        ],
        "base_maiko": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["base_maiko"]
            .inputs[0],
            "default_value",
        ],
        "base_makeup": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["base_makeup"]
            .inputs[0],
            "default_value",
        ],
        "makeup_contouring": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["contouring"]
            .inputs[0],
            "default_value",
        ],
        "blush_1": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_1"]
            .inputs[0],
            "default_value",
        ],
        "blush_1_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_1_color"]
            .inputs[7],
            "default_value",
        ],
        "blush_2": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_2"]
            .inputs[0],
            "default_value",
        ],
        "blush_2_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_2_color"]
            .inputs[7],
            "default_value",
        ],
        "blush_3": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_3"]
            .inputs[0],
            "default_value",
        ],
        "blush_3_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_3_color"]
            .inputs[7],
            "default_value",
        ],
        "blush_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "blush_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_settings"]
            .inputs[6],
            "default_value",
        ],
        "blush_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["blush_settings"]
            .inputs[9],
            "default_value",
        ],
        "lipstick_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lipstick"]
            .inputs[7],
            "default_value",
        ],
        "lip_gloss": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lip_gloss"]
            .inputs[0],
            "default_value",
        ],
        "lipstick_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lipstick"]
            .inputs[0],
            "default_value",
        ],
        "lipstick_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lipstick_settings"]
            .inputs[6],
            "default_value",
        ],
        "lipstick_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lipstick_settings"]
            .inputs[9],
            "default_value",
        ],
        "lip_liner": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lip_liner"]
            .inputs[0],
            "default_value",
        ],
        "lip_liner_gradient": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lip_liner_gradient"]
            .inputs[0],
            "default_value",
        ],
        "lip_liner_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lip_liner_color"]
            .outputs[0],
            "default_value",
        ],
        "lip_liner_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lip_liner_settings"]
            .inputs[6],
            "default_value",
        ],
        "lip_liner_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lip_liner_settings"]
            .inputs[9],
            "default_value",
        ],
        "eyeshadow_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow"]
            .inputs[0],
            "default_value",
        ],
        "eyeshadow_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "eyeshadow_lid_colors_main": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_lid_colors"]
            .inputs[6],
            "default_value",
        ],
        "eyeshadow_lid_colors_inner": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_lid_colors"]
            .inputs[7],
            "default_value",
        ],
        "eyeshadow_tip": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_tip"]
            .inputs[0],
            "default_value",
        ],
        "eyeshadow_lid_tail": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_lid_tail"]
            .inputs[7],
            "default_value",
        ],
        "eyeshadow_tail": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_tail"]
            .inputs[0],
            "default_value",
        ],
        "eyeshadow_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_settings"]
            .inputs[6],
            "default_value",
        ],
        "eyeshadow_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeshadow_settings"]
            .inputs[9],
            "default_value",
        ],
        "lashline_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline"]
            .inputs[0],
            "default_value",
        ],
        "lashline_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "lashline_main_under_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_main_under_color"]
            .inputs[7],
            "default_value",
        ],
        "lashline_tip_colors": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_tip_colors"]
            .inputs[7],
            "default_value",
        ],
        "lashline_tip": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_tip"]
            .inputs[0],
            "default_value",
        ],
        "lashline_tail_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_tail_color"]
            .inputs[7],
            "default_value",
        ],
        "lashline_tail": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_tail"]
            .inputs[0],
            "default_value",
        ],
        "lashline_main_under_color_smudge": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_main_under_color"]
            .inputs[6],
            "default_value",
        ],
        "lashline_under": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_under"]
            .inputs[0],
            "default_value",
        ],
        "lashline_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_settings"]
            .inputs[6],
            "default_value",
        ],
        "lashline_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["lashline_settings"]
            .inputs[9],
            "default_value",
        ],
        "inner_shadow_1": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_1"]
            .inputs[0],
            "default_value",
        ],
        "inner_shadow_1_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_1_color"]
            .inputs[7],
            "default_value",
        ],
        "inner_shadow_2": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_2"]
            .inputs[0],
            "default_value",
        ],
        "inner_shadow_2_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_2_color"]
            .inputs[7],
            "default_value",
        ],
        "inner_shadow_3": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_3"]
            .inputs[0],
            "default_value",
        ],
        "inner_shadow_3_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_3_color"]
            .inputs[7],
            "default_value",
        ],
        "inner_shadow_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "inner_shadow_granularity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_granularity"]
            .inputs[0],
            "default_value",
        ],
        "inner_shadow_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_settings"]
            .inputs[6],
            "default_value",
        ],
        "inner_shadow_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["inner_shadow_settings"]
            .inputs[9],
            "default_value",
        ],
        "outer_shadow_1": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_1"]
            .inputs[0],
            "default_value",
        ],
        "outer_shadow_1_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_1_color"]
            .inputs[7],
            "default_value",
        ],
        "outer_shadow_2": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_2"]
            .inputs[0],
            "default_value",
        ],
        "outer_shadow_2_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_2_color"]
            .inputs[7],
            "default_value",
        ],
        "outer_shadow_3": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_3"]
            .inputs[0],
            "default_value",
        ],
        "outer_shadow_3_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_3_color"]
            .inputs[7],
            "default_value",
        ],
        "outer_shadow_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "outer_shadow_granularity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_granularity"]
            .inputs[0],
            "default_value",
        ],
        "outer_shadow_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_settings"]
            .inputs[6],
            "default_value",
        ],
        "outer_shadow_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["outer_shadow_settings"]
            .inputs[9],
            "default_value",
        ],
        "highlight_shadow": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight"]
            .inputs[0],
            "default_value",
        ],
        "highlight_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "highlight_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight_colors"]
            .inputs[6],
            "default_value",
        ],
        "highlight_crease": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight_color"]
            .inputs[7],
            "default_value",
        ],
        "crease_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["crease_amount"]
            .inputs[0],
            "default_value",
        ],
        "highlight_contour": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight_colors"]
            .inputs[7],
            "default_value",
        ],
        "contour_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["contour_amount"]
            .inputs[0],
            "default_value",
        ],
        "highlight_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight_settings"]
            .inputs[6],
            "default_value",
        ],
        "highlight_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["highlight_settings"]
            .inputs[9],
            "default_value",
        ],
        "eyeliner_top_1": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_top_1"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_bottom_1": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_bottom_1"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_top_2": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_top_2"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_bottom_2": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_bottom_2"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_top_3": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_top_3"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_bottom_3": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_bottom_3"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_top_4": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_top_4"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_bottom_4": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_bottom_4"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_top_5": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_top_5"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_bottom_5": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_bottom_5"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_top_6": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_top_6"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_bottom_6": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_bottom_6"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_settings_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_settings"]
            .inputs[0],
            "default_value",
        ],
        "eyeliner_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_settings"]
            .inputs[6],
            "default_value",
        ],
        "eyeliner_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyeliner_settings"]
            .inputs[9],
            "default_value",
        ],
        "facial_paint_1": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_1"]
            .inputs[0],
            "default_value",
        ],
        "facial_paint_1_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_1_color"]
            .inputs[7],
            "default_value",
        ],
        "facial_paint_2": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_2"]
            .inputs[0],
            "default_value",
        ],
        "facial_paint_2_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_2_color"]
            .inputs[7],
            "default_value",
        ],
        "facial_paint_3": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_3"]
            .inputs[0],
            "default_value",
        ],
        "facial_paint_3_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_3_color"]
            .inputs[7],
            "default_value",
        ],
        "facial_paint_intensity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "facial_paint_granularity": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_granularity"]
            .inputs[0],
            "default_value",
        ],
        "facial_paint_settings_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_settings"]
            .inputs[6],
            "default_value",
        ],
        "facial_paint_settings_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["facial_paint_settings"]
            .inputs[9],
            "default_value",
        ],
        "eyebrows_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyebrows"]
            .inputs[0],
            "default_value",
        ],
        "eyebrows_fade": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["eyebrows_fade"]
            .inputs[0],
            "default_value",
        ],
        "nail_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nail_amount"]
            .inputs[0],
            "default_value",
        ],
        "nail_polish_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nail_polish_color"]
            .inputs[7],
            "default_value",
        ],
        "nail_polish_metallic": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nail_polish"]
            .inputs[6],
            "default_value",
        ],
        "nail_polish_roughness": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nail_polish"]
            .inputs[9],
            "default_value",
        ],
        "nail_polish_coat": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nail_polish"]
            .inputs[14],
            "default_value",
        ],
        "nail_glitter": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nail_glitter"]
            .inputs[0],
            "default_value",
        ],
        "teeth_age": [
            lambda: bpy.data.materials["SM5 Teeth Material Transhuman"]
            .node_tree.nodes["teeth_age"]
            .outputs[0],
            "default_value",
        ],
        "teeth_saturation": [
            lambda: bpy.data.materials["SM5 Teeth Material Transhuman"]
            .node_tree.nodes["teeth_saturation"]
            .inputs[1],
            "default_value",
        ],
        "mesh_thickness": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_thickness"]
            .inputs[1],
            "default_value",
        ],
        "root_spread_1": [
            lambda: bpy.data.node_groups["SM5 Hair Color Transhuman"]
            .nodes["root_spread"]
            .color_ramp.elements[1],
            "position",
        ],
        "root_spread_0": [
            lambda: bpy.data.node_groups["SM5 Hair Color Transhuman"]
            .nodes["root_spread"]
            .color_ramp.elements[0],
            "position",
        ],
        "root_color_picker": [
            lambda: bpy.data.node_groups["SM5 Hair Color Transhuman"]
            .nodes["root_color_picker"]
            .outputs[0],
            "default_value",
        ],
        "hair_color_picker": [
            lambda: bpy.data.node_groups["SM5 Hair Color Transhuman"]
            .nodes["hair_color_picker"]
            .outputs[0],
            "default_value",
        ],
        "secondary_color_highlights": [
            lambda: bpy.data.node_groups["SM5 Hair Color Transhuman"]
            .nodes["secondary_hair_color_picker"]
            .outputs[0],
            "default_value",
        ],
        "secondary_intensity_1": [
            lambda: bpy.data.node_groups["SM5 Hair Color Transhuman"]
            .nodes["secondary_intensity"]
            .color_ramp.elements[1],
            "position",
        ],
        "mesh_hair_metallic": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_hair"]
            .inputs[6],
            "default_value",
        ],
        "mesh_hair_specular": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_hair"]
            .inputs[7],
            "default_value",
        ],
        "mesh_hair_roughness": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_hair"]
            .inputs[9],
            "default_value",
        ],
        "mesh_hair_ior": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_hair"]
            .inputs[16],
            "default_value",
        ],
        "mesh_hair_clearcoat": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_hair"]
            .inputs[14],
            "default_value",
        ],
        "mesh_hair_clearcoat_roughness": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_hair"]
            .inputs[15],
            "default_value",
        ],
        "mesh_translucent": [
            lambda: bpy.data.materials["SM5 Hair Mesh Material"]
            .node_tree.nodes["mesh_translucent"]
            .inputs[0],
            "default_value",
        ],
        "tattoo_height": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["tattoo_height"]
            .inputs[0],
            "default_value",
        ],
        "tattoo_amount": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["tattoo_switch"]
            .inputs[0],
            "default_value",
        ],
        "beard_curls_switch": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["beard_curls_switch"]
            .inputs[1],
            "default_value",
        ],
        "beard_curls_scale": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["beard_curl_scale"].outputs[0], 
            "default_value",
            ],   
        "beard_noise": [
            lambda: bpy.data.node_groups["SM5 Beard Transhuman"]
            .nodes["beard_noise"]
            .outputs[0],
            "default_value",
        ],   
        "hair_curls_switch": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["hair_curls_switch"]
            .inputs[1],
            "default_value",
        ],
        "curl_scale": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["curl_scale"]
            .outputs[0],
            "default_value",
        ],
        "curl_resolution": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["curl_resolution"]
            .outputs[0],
            "default_value",
        ],
        "curl_amplitude": [
            lambda: bpy.data.node_groups["SM5 Hair Curls"]
            .nodes["curl_amplitude"]
            .inputs[0],
            "default_value",
        ],
        "curl_frequency": [
            lambda: bpy.data.node_groups["SM5 Hair Curls"]
            .nodes["curl_frequency"]
            .inputs[1],
            "default_value",
        ],
        "curls_randomize": [
            lambda: bpy.data.node_groups["SM5 Hair Curls"]
            .nodes["curls_randomize"]
            .inputs[0],
            "default_value",
        ],
        "waves_curls_switch": [
            lambda: bpy.data.node_groups["SM5 Hair Curls"]
            .nodes["waves_curls_switch"]
            .inputs[0],
            "default_value",
        ],
        "curl_clump_mode": [
            lambda: bpy.data.node_groups["SM5 Hair Curls"]
            .nodes["curl_clump_mode"]
            .inputs[0],
            "default_value",
        ],
        "gravity_clump": [
            lambda: bpy.data.node_groups["SM5 Hair Curls"]
            .nodes["gravity_clump"]
            .outputs[0],
            "default_value",
        ],
        "interpolate_curves": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["interpolate_switch"]
            .inputs[1],
            "default_value",
        ],
        "hair_amount": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["interpolate_curves"],
            "integer",
        ],
        "hair_resolution": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["hair_resolution"],
            "integer",
        ],
        "hair_spread": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["hair_spread"]
            .outputs[0],
            "default_value",
        ],
        "hair_clump_switch": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["hair_clump_switch"]
            .inputs[0],
            "default_value",
        ],
        "hair_clump_shape": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["hair_clump_shape"]
            .outputs[0],
            "default_value",
        ],
        "loose_hair_decimate": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["loose_hair_decimate"]
            .inputs[0],
            "default_value",
        ],
        "loose_hair_spread": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["loose_hair_spread"]
            .inputs[0],
            "default_value",
        ],
        "loose_hair_amount": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["loose_hair_amount"]
            .inputs[2],
            "default_value",
        ],
        "loose_hairs_frizz": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["loose_hairs_frizz"]
            .inputs[1],
            "default_value",
        ],
        "root_puff": [
            lambda: bpy.data.node_groups["SM5 Hair"]
            .nodes["root_puff"]
            .inputs[3],
            "default_value",
        ],
        "fluff_strands": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["fluff_strands"]
            .inputs[3],
            "default_value",
        ],
        "noise_strength": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["noise_strength"]
            .inputs[0],
            "default_value",
        ],
        "noise_scale": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["noise_scale"]
            .inputs[1],
            "default_value",
        ],
        "noise_shape": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["noise_shape"]
            .inputs[1],
            "default_value",
        ],
        "curves_hair_thickness": [
            lambda: bpy.data.node_groups["SM5 Hair Curves"]
            .nodes["thickness"]
            .outputs[0],
            "default_value",
        ],
        "nipples_def": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nipple_def"]
            .color_ramp.elements[0],
            "position",
        ],
        "nipples_color": [
            lambda: bpy.data.materials["SM5 Skin Material Transhuman"]
            .node_tree.nodes["nipple_color"]
            .outputs[0],
            "default_value",
        ],
    },
    {
        "fem_face_1": [0, 1],
        "fem_face_2": [0, 1],
        "fem_face_3": [0, 1],
        "fem_face_4": [0, 1],
        "fem_face_5": [0, 1],
        "m_face_1": [0, 1],
        "m_face_2": [0, 1],
        "m_face_3": [0, 1],
        "m_face_4": [0, 1],
        "m_face_5": [0, 1],
        "head_size": [-1, 1],
        "head_width": [-1, 1],
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
        "cheeks_plus_minus": [-1, 1],
        "cheeks_hollow": [0, 1],
        "chin_position": [-1, 1],
        "cleft_chin": [0, 1],
        "chin_height": [-1, 1],
        "chin_width": [-1, 1],
        "chin_vertical": [-1, 1],
        "jaw_width": [-1, 1],
        "jaw_length": [-1, 1],
        "neck_girth": [-1, 1],
        #    'feet_male': [0, 1],
        #    'feet_female': [0, 1],
        #    'hand_male': [0, 1],
        #    'hand_female': [0, 1],
        #    'hand_neutral': [0, 1],
        #    'hand_elder': [0, 1],
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
        "nose_tip_position": [-1, 1],
        "nose_tip_shape": [-1, 1],
        "nose_tip_move": [-1, 1],
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
        "ear_in": [-1, 1],
        "ear_out": [-1, 1],
        "ear_height": [-0.3, 0.3],
        "ear_depth": [-1, 1],
        "ear_size": [-1, 1],
        "ear_back": [-0.5, 0.5],
        "ear_pointy": [-1, 1],
    },
    [
        {
            "keys": [
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
            ],
            "total": 0.1,
        }
    ],
    sm5_addon_utils.get_addon_root(addon_name)
)