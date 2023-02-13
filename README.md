---
layout: default
title: Home
nav_order: 1
permalink: /
---

# To-do

## Nerfstudio met input insta360 X2

run de Nerfstudio opstelling met zelfgenomen foto's van insta360 X2

## MINE: single photo novel-view synthesis

https://github.com/vincentfung13/MINE

MINE maakt gebruikt van een enkele foto waarvan de features worden geextract en gebruikt om een RGB en Volume dichtheid als output te geven
MINE: Multi plane Images NEural radiance fields

Voordelen:
- gebruikt een enkele image als input
- NERF gebruikt de scene-geometry in de netwerk gewichten, MINE's netwerk focust op de input image
- door inpainting worden er ongeziene standpunten gegenereerd.

Nadelen:
- neemt maar 1 afbeelding dus kan geen volledige 360° view creeeren rondom een object 
- MINE neemt geen camera standpunten als input dus kan geen standpunt-afhankelijke effecten genereren

## MatryODShka: Real-time 6DoF Video View Synthesis using Multi-Sphere Images

![image](https://user-images.githubusercontent.com/60694521/218472314-eb3fffe6-ba34-4f74-bba8-365ded5a519a.png)

https://github.com/brownvc/matryodshka

Deze paper gebruikt een multi-camera opstelling om stereo 360° video/afbeeldingen via een multi-sphere image (MSI ipv MPI) in 6 Degrees of freedom view te renderen.
Het probleem dat wordt aangehaald is dat er geen motion-parallax is bij stereo 360° imagery.
