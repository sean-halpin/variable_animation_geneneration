### Description

This repo shows the steps that were involved going from a human shaped mesh to generating random animations of a person scanning items at a checkout.

Using Blender 2.82a and it's python scripting API

### Scripted Animation Output
![alt test](/media/0.scanning_anim.gif)  

### Step by Step (in pictures)
#### Align Armature
![alt text](/media/1.armature_alignment.png.jpg)  
#### Align Armature - Right Orthogonal View
![alt text](/media/2.armature_alignment_right_ortho.png.jpg)  
#### Align Armature - Left Hand Fingers
![alt text](/media/3.armature_alignment_hand.left.png.jpg)  
#### Rigify - give armature inverse & forward kinematics
![alt text](/media/4.rigidy_rig_IK_FK.png.jpg)  
#### Rigify - IK/FK Kinematic Demonstration
![alt text](/media/5.rigify_rig_demonstrate_kinematics.png.jpg)  
#### Model - A Supermarket Checkout
![alt text](/media/6.mode_checkout_imported.png.jpg)  
#### Scripting - Find Bones required for Scanning Animation
![alt text](/media/7.scripting_finding_bones.png.jpg)  
#### Scripting - Applying Transforms to Bones
![alt text](/media/8.scripting_applying_transforms_to_rig.png.jpg)  
#### Animating - Insert Keyframes at interval after transforms
![alt text](/media/9.scripting_inserting_keyframes_into_animation_timeline.png.jpg)  
#### Animating - Add a random variation and push animations to NLA in a loop
![alt text](/media/10.scripting_random_variation_pushing_animations_to_NLA_timeline.png.jpg)  
#### Rendering - file output
The Script will currently render all the animations to `/tmp/renders` with each animation in it's own folder
 - Named `/tmp/renders/actionName/#frames-in-render.mp4`
```
.
├── rigAction.045
│   └── 0000-0047.mp4
├── rigAction.046
│   └── 0000-0047.mp4
├── rigAction.047
│   └── 0000-0047.mp4
├── rigAction.048
│   └── 0000-0047.mp4
└── rigAction.049
    └── 0000-0047.mp4

5 directories, 5 files
```
#### Rendering - Video Output
The rendered output is currently an `mp4` containing `h264`
A screenshot of the rendered output without any materials applied below;  

![alt text](/media/11.rendered_output_screenshot.jpg)


