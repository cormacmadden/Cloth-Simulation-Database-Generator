# Cloth-Sim-Database-Toolset
Blender and Houdini Scripts for generating Physics-Based Cloth Simulations intended to train Machine Learning Algorithms

This repository contains two script files and a Houdini Digital Asset.

The Blender script file loops over the process of: (a) creating a random SMPL body shape; (b) retargeting; and (c) exporting the body and skeletal animation.  From each skeletal animation the script can create an infinite number of animated SMPL body shapes for each, male, female and neutral body types. So once the skeletal animation is set up in Blender, a near infinite amount of mesh animations can be generated with a single click.


The final dataset consists of 600 simulations, made up of 100 SMPL body shapes, in 6 animations. The dataset was split into training, validation and test sets with 500, 20 and 80 simulations, respectively similar to the dataset of GarNet.


Each animation is saved to its own individual folder that uses the following naming scheme:

Skeletal Animation (3 digit) + index (4 digits) + Gender (1 digit)
Eg: 00110001.filetype

The number for the neutral, male and female gender are referred to as 0,1,2 respectively. 
Another number would need to be added if the dataset used more than one garment.
