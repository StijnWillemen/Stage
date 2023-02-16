---
layout: default
title: NeRF
nav_order: 1
---


# Neural Radiance Fields (NeRF)



[2020 2003.08934.pdf](https://github.com/StijnWillemen/Stage/files/10673519/2020.2003.08934.pdf)

# Proces

![image](https://user-images.githubusercontent.com/60694521/217211536-bcdf5d65-4d66-4498-a5c4-f2aa7da613aa.png)

Met een set van een afbeeldingen, kijken we per afbeelding vanwaar deze is genomen en hieruit nieuwe 'views' genereren.

# Scene representation

![image](https://user-images.githubusercontent.com/60694521/217211985-c9038f55-95fd-4bc0-b913-a241d5e4a28f.png)

Een scene bestaat uit een 5D vector met als input: een 3D input van X Y Z coordinaten en een kijk richting (θ, φ) hieruit krijgen we als output
een kleur (R,G,B) en een volume dichtheid (σ).

in het neuraal netwerk nemen we voor elke pixel op een afbeeldingen een ray die we kunnen gebruiken als datapunt. De dataset bestaat dan uit 
n(afbeeldingen) * n(pixels op afbeelding).

# Resultaten
### Camera gsm instant-ngp : aabb = 1 rest default
![ezgif com-video-to-gif](https://user-images.githubusercontent.com/60694521/217826097-368a003f-4d26-4ecb-af9c-02ec42aee414.gif) 

### Camera gsm instant-ngp : aabb = 16 rest default
![Fire ext](../images/gif_fire_ext.gif)

### Camera gsm Luma AI webApp
![Chair_](../images/chair_luma.gif)

### insta360 x2 images nerfacto colmap
![Electricity](../images/electricity-gif.gif)

### insta360 x2 video nerfacto colmap
!Fire ext2](../images/fire-ext_nerfstudio_vid-gif.gif)

