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
├── rigAction.035
│   ├── 0000-0047.mp4
│   └── annotations.txt
├── rigAction.036
│   ├── 0000-0047.mp4
│   └── annotations.txt
├── rigAction.037
│   ├── 0000-0047.mp4
│   └── annotations.txt
├── rigAction.038
│   ├── 0000-0047.mp4
│   └── annotations.txt
├── rigAction.039
│   ├── 0000-0047.mp4
│   └── annotations.txt
└── rigAction.040
    ├── 0000-0047.mp4
    └── annotations.txt

6 directories, 12 files

```
#### Rendering - Video Output
The rendered output is currently an `mp4` containing `h264`  

 - Screenshot of the rendered output without any materials applied below;  

![alt text](/media/11.rendered_output_screenshot.jpg)

#### Rendering - Record accurate metadata/annotations for every frame

 - Example `annotations.txt` contents that is recorded alongside every rendered mp4  
 
```
{
    "frame_current": 0,
    "hand.r.x": -0.0824587419629097,
    "hand.r.y": 0.12269103527069092,
    "hand.r.z": 0.32035717368125916,
    "hand.l.x": 0.08245903998613358,
    "hand.l.y": 0.12269102036952972,
    "hand.l.z": 0.3203571140766144
}
{
    "frame_current": 1,
    "hand.r.x": -0.08431647717952728,
    "hand.r.y": 0.12105774134397507,
    "hand.r.z": 0.3205045163631439,
    "hand.l.x": 0.08431677520275116,
    "hand.l.y": 0.12105772644281387,
    "hand.l.z": 0.32050445675849915
}
{
    "frame_current": 2,
    "hand.r.x": -0.08966787159442902,
    "hand.r.y": 0.1163528710603714,
    "hand.r.z": 0.3209289610385895,
    "hand.l.x": 0.0896681696176529,
    "hand.l.y": 0.1163528561592102,
    "hand.l.z": 0.3209289014339447
}
```