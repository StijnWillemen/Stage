# Algemene definities

- View synthesis: Het renderen van nieuwe views van een scene gegeven een set van input images en de respectievelijke camera posities gelinkt aan deze images
- NeRF: Neural radiance field
- MLP: Multi layer perceptron
- SFM: Structure for motion -> berekenen van intrisieke en extrensieke camera parameters
- IBR: Image based rendering

# Extra begrippen
### Google Multi-Plane Image (MPI)

- Afbeelding formaat met verschillende vlakken achter elkaar om zo vanuit een ander perspectief een correcte view te krijgen
- Vlakken hebben elk andere info/kleur/transparantie vanuit de input (werkt op basis van layers in de input afbeelding, near to far) om te bepalen welke kleur pixel moet hebben
- Model genereert MPI vanuit input
- Trainen is zwaar maar renderen is real time → Geen aparte MPI per gegenereerd view synthesis → 1 MPI om alle views uit te halen
- Dataset = YT, moeilijk te vinden welke video’s
- Niet open source
- Goed resultaat
- Nerfs populairder op de moment