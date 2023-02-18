---
layout: default
title: NeRF
nav_order: 1
---


# Neural Radiance Fields (NeRF)



[2020 2003.08934.pdf](https://github.com/StijnWillemen/Stage/files/10673519/2020.2003.08934.pdf)

# Proces

![image](https://user-images.githubusercontent.com/60694521/217211536-bcdf5d65-4d66-4498-a5c4-f2aa7da613aa.png)

Met een set van een afbeeldingen, kijken we per afbeelding vanwaar deze is genomen om hieruit nieuwe 'views' genereren.

**Algemene definitie:** 

Genereren van novel views van complexe scenes door het optimaliseren van een onderliggende continue volumetrische scene functie gebruikmakende van een sparse aantal input images. Een scene wordt voorgesteld aan de hand van een fully connected (nonconv) deep nn dat als input een 5D coord (space coord (x,y,z), kijkdirectie (θ, φ)) neemt en als output een density en kleur teruggeeft van dit specifieke punt in ruimte. Deze coord worden verkregen door deze te queryen langs camera rays en gebruikmakende van klassieke volume rendering technieken om de output te projecteren naar een image. Volume rendering is van nature differentieerbaar, de enige nodige input om de representatie te kunnen optimaliseren is een set van images met daaraan de correcte camera posities gelinkt. 

Het genereren van een fotorealistische output brengt met zich mee dat er correct moet omgegaan worden met de geometrie en materiaal properties zoals bijvoorbeeld reflectie van het materiaal. 

Een statische scene wordt voorgesteld als een continue 5D functie dat de straling uitgestraald in elke richting (θ, φ), op elk punt (x, ,y ,z) in de ruimte en de densiteit op elk punt. Dit controlleert hoeveel straling er door een ray geaccumuleerd wordt dat door een punt gaat.

Het netwerk gaat van een single 5D coord naar een single densiteit en view-dependant kleur.

Om deze NeRF te renderen van een specifiek viewpoint:

- March camera rays door de scene om een sampled set van 3D points te genereren
- Gebruik deze punten met bijhorende 2D view directies als input voor MLP om een output te krijgen (densiteit en kleur)
    - Gebruik klassieke volume rendering technieken om deze output om te vormen naar een 2D image, hierna wordt gradient descent toegepast om het netwerk te optimaliseren door de loss te berekenen tussen van de observed image en de bijhorende views gegeneerd door het netwerk. Door deze error te minimaliseren over verschillende views, zal het netwerk een coherent model kunnen voorspellen van de scene.

Een scene wordt dus zogezegd opgeslagen in de parameters van een NN, dit zorgt voor een relatief lage opslagkost.

# Scene representation

![image](https://user-images.githubusercontent.com/60694521/217211985-c9038f55-95fd-4bc0-b913-a241d5e4a28f.png)

Een scene bestaat uit een 5D vector met als input: een 3D input van X Y Z coordinaten en een kijk richting (θ, φ) hieruit krijgen we als output
een kleur (R,G,B) en een volume dichtheid (σ).

in het neuraal netwerk nemen we voor elke pixel op een afbeeldingen een ray die we kunnen gebruiken als datapunt. De dataset bestaat dan uit 
n(afbeeldingen) * n(pixels op afbeelding).

# Bevindingen

- Belangrijk om genoeg images te gebruiken → anders krijgt het netwerk niet genoeg data om dingen uit te kunnen leren omdat er bijgevolg te weinig parallax is
    - instant-ngp: 50 - 150 images
    - Nerfacto: 150 - 300
- Belangrijk om genoeg overlap in de images te voorzien = parallax → zelfde punt komt in meerdere images voor vanuit verschillende perspectieven→ netwerk kan duidelijk zien waar het punt zich in de ruimte bevindt en welke kleur en densiteit het moet krijgen
- Contrast is ook belangrijk → netwerk kan duidelijk zien wat wat is
- Textuur is belangrijk om makkelijk overeenkomstige punten te vinden tijdens het berekenen van de camerastandpunten
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

![Fire-ext2](../images/fire-ext_nerfstudio_vid-gif.gif)

