# Cloth Simulation Database, and Generation Toolset

This repository contains two scripts, for Blender and Houdini, that can generate an infinite number of Physics-Based Cloth Simulations intended to train Machine Learning Algorithms.

<p align="center">
<img src="Images/Process.jpg" alt="Crossover Points" width = "50%" height="50%"></img>
</p>



## Blender Script
The Blender script file loops over the process of: <br>(a) creating a random SMPL body shape; <br>(b) retargeting; and <br>(c) exporting the body and skeletal animation.  <br><br>From each skeletal animation the script can create an infinite number of animated SMPL body shapes for each, male, female and neutral body types. So once the skeletal animation is set up in Blender, an infinite number of mesh animations can be generated.

## Houdini Script
The script in Houdini <br>(a) iterates over each folder (containing the animated SMPL mesh); <br>(b) loads the geometry, <br>(c) runs the simulation, and <br>(d) exports the cloth simulation to each respective folder.


<p align="center">
<img src="Images/Houdini Node Network.jpg" alt="Crossover Points" width = "50%" height="50%"></img>
</p>

<p align="center">
<img src="Images/Drapsing.jpg" alt="Crossover Points" width = "36%" height="50%"></img>
<img src="Images/deformation.jpg" alt="Crossover Points" width = "45%" height="50%"></img>
</p>


## Dataset Overview

### Link to Database :
https://drive.google.com/drive/folders/15Pm41YiPCGp4vHTGhWTkBAL64DMXvs4E?usp=sharing
<br><br>The final dataset consists of 600 simulations, made up of 100 SMPL body shapes, in 6 animations. <br>The dataset was split into training, validation and test sets with 500, 20 and 80 simulations respectively.

## Naming Scheme
Each animation is saved to its own individual folder that uses the following naming scheme:

Skeletal Animation (3 digit) + index (4 digits) + Gender (1 digit)

Eg: 00110001.filetype

The number for the neutral, male and female gender are referred to as 0,1,2 respectively.
