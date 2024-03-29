import bpy
import json
import random
import time
import logging
from mathutils import *

D = bpy.data
C = bpy.context
scene = C.scene

print("Blender Python Script")
bpy.context.area.type = "TEXT_EDITOR"

try:
    for index in range(2):
        randomOffset = (random.randint(0, 100) / 100.0) /2.5
        # Deselect all objs
        bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
        bpy.ops.object.select_all(action="DESELECT")

        # Set POSE Mode
        bpy.ops.object.mode_set(mode="POSE", toggle=False)
        # Clear all pose transforms
        bpy.ops.pose.select_all(action="SELECT")
        bpy.ops.pose.user_transforms_clear()
        bpy.ops.pose.transforms_clear()
        bpy.ops.pose.select_all(action="DESELECT")

        # Move hand.R to initial position
        (D.objects["rig"].data.bones["hand_ik.R"]).select = True
        bpy.ops.transform.translate(
            value=(-0, -0.187819 - randomOffset, -0),
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(False, True, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.pose.select_all(action="DESELECT")
        # Move hand.L to initial position
        (D.objects["rig"].data.bones["hand_ik.L"]).select = True
        bpy.ops.transform.translate(
            value=(-0, -0.187819 - randomOffset, -0),
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(False, True, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.pose.select_all(action="DESELECT")

        # Select Both Hands
        (D.objects["rig"].data.bones["hand_ik.R"]).select = True
        (D.objects["rig"].data.bones["hand_ik.L"]).select = True
        # Insert Keyframe
        bpy.context.scene.frame_current = 0
        bpy.ops.anim.keyframe_insert_menu(type="BUILTIN_KSI_LocRot")
        bpy.ops.pose.select_all(action="DESELECT")

        # Move hand.R to meet hand.L
        (D.objects["rig"].data.bones["hand_ik.R"]).select = True
        bpy.ops.transform.translate(
            value=(0.45, 0, 0),
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(True, False, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        # Rotate hand.R
        bpy.ops.transform.rotate(
            value=1.05929,
            orient_axis="Z",
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(False, False, True),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.pose.select_all(action="DESELECT")
        # Rotate Elbow
        (D.objects["rig"].data.bones["upper_arm_ik.R"]).select = True
        bpy.ops.transform.rotate(
            value=1.26934,
            orient_axis="X",
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(True, False, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.pose.select_all(action="DESELECT")
        # Move hand.L to meet hand.R
        (D.objects["rig"].data.bones["hand_ik.L"]).select = True
        bpy.ops.transform.translate(
            value=(-0.45, 0, 0),
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(True, False, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        # Rotate hand.L
        bpy.ops.transform.rotate(
            value=-1.05929,
            orient_axis="Z",
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(False, False, True),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.pose.select_all(action="DESELECT")
        # Rotate Elbow
        (D.objects["rig"].data.bones["upper_arm_ik.L"]).select = True
        bpy.ops.transform.rotate(
            value=1.26934,
            orient_axis="X",
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(True, False, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.pose.select_all(action="DESELECT")

        # Select Both Hands & Elbows
        (D.objects["rig"].data.bones["hand_ik.R"]).select = True
        (D.objects["rig"].data.bones["hand_ik.L"]).select = True
        (D.objects["rig"].data.bones["upper_arm_ik.R"]).select = True
        (D.objects["rig"].data.bones["upper_arm_ik.L"]).select = True
        # Insert Keyframe
        bpy.context.scene.frame_current = 23
        bpy.ops.anim.keyframe_insert_menu(type="BUILTIN_KSI_LocRot")
        bpy.ops.pose.select_all(action="DESELECT")

        # Move hand.L to drop item in bagging area
        (D.objects["rig"].data.bones["hand_ik.L"]).select = True
        bpy.ops.transform.translate(
            value=(0.370594, 0, 0),
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(True, False, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.transform.rotate(
            value=0.816452,
            orient_axis="Z",
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(False, False, True),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )

        # Insert Keyframe
        bpy.context.scene.frame_current = 47
        bpy.ops.anim.keyframe_insert_menu(type="BUILTIN_KSI_LocRot")

        # Push Action to NLA Stack
        currentContext = bpy.context.area.type
        bpy.context.area.type = "NLA_EDITOR"
        bpy.ops.nla.action_pushdown(channel_index=-1)
        bpy.context.area.type = currentContext
        bpy.ops.pose.select_all(action="DESELECT")

    # Render all animations - assuming cameras and render options for animations are set
    output_dir = "/tmp/renders/"

    # Make a list of all animations in the NLA
    nla_strips = []
    for obj in scene.objects:
        if obj.animation_data and obj.animation_data.nla_tracks:
            for track in obj.animation_data.nla_tracks:
                for strip in track.strips:
                    nla_strips.append((strip, strip.mute))
                    strip.mute = True

    # Save scene details in order to restore later
    orig_frame_start = scene.frame_start
    orig_frame_end = scene.frame_end
    orig_filepath = scene.render.filepath

    # render each strip
    for strip in nla_strips:
        scene.render.filepath = output_dir + strip[0].name + "/"
        scene.frame_start = strip[0].frame_start
        scene.frame_end = strip[0].frame_end
        # Unmute this strip
        strip[0].mute = False
        bpy.ops.render.render(animation=True)
        # Record metadata for each frame in the strip
        for frame_index in range(int(strip[0].frame_end - strip[0].frame_start)):
            try:
                scene.frame_set(frame_index)
                print("Recording Frame #{} Metadata: {}".format(frame_index, scene.render.filepath))
                data = {}
                data["frame_current"] = scene.frame_current
                data["hand.r.x"] = D.objects["rig"].pose.bones["hand_ik.R"].location.xyz.x
                data["hand.r.y"] = D.objects["rig"].pose.bones["hand_ik.R"].location.xyz.y
                data["hand.r.z"] = D.objects["rig"].pose.bones["hand_ik.R"].location.xyz.z
                data["hand.l.x"] = D.objects["rig"].pose.bones["hand_ik.L"].location.xyz.x
                data["hand.l.y"] = D.objects["rig"].pose.bones["hand_ik.L"].location.xyz.y
                data["hand.l.z"] = D.objects["rig"].pose.bones["hand_ik.L"].location.xyz.z
                with open(scene.render.filepath + 'annotations.txt', 'a') as f:
                       json.dump(data, f, sort_keys = False, indent = 4, ensure_ascii = False)
                       f.write('\n')
            except Exception as e:
                logging.exception("Custom Frame Handler Exception")
            finally:
                scene.frame_set(0)
        # Mute this strip
        strip[0].mute = True

    # Restore changes that were made
    scene.frame_start = orig_frame_start
    scene.frame_end = orig_frame_end
    scene.render.filepath = orig_filepath

    for strip in nla_strips:
        strip[0].mute = strip[1]

except Exception as e:
    logging.exception("Exception")
finally:
    print("Complete")
