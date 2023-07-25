#!/usr/bin/env python3


"""
This program will determine what the "threshold energy" is for a type of kaon event
This event will have a specified z-position of generation and angle wrt the x axis
The first version will just use one z, theta case, and then be generalized after it has been tested

Once the z and theta have been determined set, the program will generate a series of samples
these samples will have identical conditions except with energy incremented by 5 mev at a time
in a specified range

Once all the samples have been created, they will be analyzed to find what the cutoff is for 0, 1, 2, 3, 4, 5, hits
"""

import numpy as np
import subprocess

# first generate samples in a guess energy range - use 30mev to 300mev
z = 528.7 + 3 # 3mm into first D layer
# z1 = [428.3 + 0.5*i for i in range(0,8)] # front of 16th ecal layer steps through at 0.5mm - zero angle will make particle travel 3.5mm
thetas = np.arange(0,100,20) # example to start

# choose energy ranges from comparing to theory graph
# each range sound have 10mev range around value

# could be adjusted for arbitrary inputs
energyrange = np.arange(10,500,20)
energyrange = energyrange/1000 # convert to Mev.

# now loop over the samples we're going to make

for i in range(len(thetas)):
    # label this theta 
    theta = thetas[i]
    for i in range(len(energyrange)): # loop over energies for this angle
        energy = energyrange[i]
        # create a root file with this energy
        subprocess.call(['singularity','run','--no-home','/home/csellgren/work.sif','.','config_inputEztheta.py',str(energy),str(z),str(theta)])
    
    for i in range(len(energyrange)): # analyze
        energy = energyrange[i]
        rootname = 'kaons_energyis'+str(energy)+'gev_zis'+str(z)+'_thetais'+str(theta)+'.root'
        # analyze the result
        subprocess.call(['singularity','run','--no-home','/home/csellgren/work.sif','.','python3','analyze_energycutoffs.py',rootname,str(theta)])
        print(i)


