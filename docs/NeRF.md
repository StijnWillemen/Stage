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
