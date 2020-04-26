import bpy
import random
import time
from mathutils import *

D = bpy.data
C = bpy.context

print("Blender Python Script")

for index in range(5):
    randomOffset = (random.randint(0, 100)/100.0)/5.0
    # Grab the Rig
    rig = bpy.data.objects['rig']
    rig.select_set(state=True)
    # Deselect all objs
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    bpy.ops.object.select_all(action='DESELECT')

    # Set POSE Mode
    bpy.ops.object.mode_set(mode='POSE', toggle=False)
    # Clear all pose transforms
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.user_transforms_clear()
    bpy.ops.pose.transforms_clear()
    bpy.ops.pose.select_all(action='DESELECT')

    # Move hand.R to initial position
    (D.objects["rig"].data.bones["hand_ik.R"]).select = True
    bpy.ops.transform.translate(value=(-0, -0.187819 - randomOffset, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.pose.select_all(action='DESELECT')
    # Move hand.L to initial position
    (D.objects["rig"].data.bones["hand_ik.L"]).select = True
    bpy.ops.transform.translate(value=(-0, -0.187819 - randomOffset, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.pose.select_all(action='DESELECT')

    # Select Both Hands
    (D.objects["rig"].data.bones["hand_ik.R"]).select = (True)
    (D.objects["rig"].data.bones["hand_ik.L"]).select = (True)
    # Insert Keyframe
    bpy.context.scene.frame_current = 0
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
    bpy.ops.pose.select_all(action='DESELECT')

    # Move hand.R to meet hand.L
    (D.objects["rig"].data.bones["hand_ik.R"]).select = True
    bpy.ops.transform.translate(value=(0.45, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    # Rotate hand.R
    bpy.ops.transform.rotate(value=1.05929, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.pose.select_all(action='DESELECT')
    # Rotate Elbow
    (D.objects["rig"].data.bones["upper_arm_ik.R"]).select = True
    bpy.ops.transform.rotate(value=1.26934, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.pose.select_all(action='DESELECT')
    # Move hand.L to meet hand.R
    (D.objects["rig"].data.bones["hand_ik.L"]).select = True
    bpy.ops.transform.translate(value=(-0.45, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    # Rotate hand.L
    bpy.ops.transform.rotate(value=-1.05929, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.pose.select_all(action='DESELECT')
    # Rotate Elbow
    (D.objects["rig"].data.bones["upper_arm_ik.L"]).select = True
    bpy.ops.transform.rotate(value=1.26934, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.pose.select_all(action='DESELECT')

    # Select Both Hands & Elbows 
    (D.objects["rig"].data.bones["hand_ik.R"]).select = (True)
    (D.objects["rig"].data.bones["hand_ik.L"]).select = (True)
    (D.objects["rig"].data.bones["upper_arm_ik.R"]).select = (True)
    (D.objects["rig"].data.bones["upper_arm_ik.L"]).select = (True)
    # Insert Keyframe
    bpy.context.scene.frame_current = 23
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
    bpy.ops.pose.select_all(action='DESELECT')

    # Move hand.L to drop item in bagging area
    (D.objects["rig"].data.bones["hand_ik.L"]).select = (True)
    bpy.ops.transform.translate(value=(0.370594, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.rotate(value=0.816452, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    # Insert Keyframe
    bpy.context.scene.frame_current = 47
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
    bpy.ops.pose.select_all(action='DESELECT')

    # Push Action to NLA Stack
    currentContext = bpy.context.area.type
    bpy.context.area.type = "NLA_EDITOR"
    bpy.ops.nla.action_pushdown(channel_index=1)
    bpy.context.area.type = currentContext
