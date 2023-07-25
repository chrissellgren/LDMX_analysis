import numpy as np
import sys

from LDMX.Framework import ldmxcfg

p = ldmxcfg.Process('v3_v13')
p.run = 1

# importing necessary generator and simulator packages
from LDMX.SimCore import simulator
from LDMX.SimCore import generators

# get initial conditions from argument vector
print("Parameters are:")
print(sys.argv)
energy = float(sys.argv[1])
z = float(sys.argv[2])
angle = float(sys.argv[3])


# setting up the kaon gun initial conditions
xGun = 0.0 # in mm
yGun = 0.0 # in mm
zGun = z # mm
theta = angle

myGun = generators.gun('myGun')
myGun.particle = 'kaon+'
myGun.position = [ xGun, yGun, zGun]  # in mm
myGun.direction = [np.sin(theta), 0., np.cos(theta)] # unit vector
myGun.energy = energy # in GeV

sim = simulator.simulator('sim')
sim.generators = [myGun]
sim.setDetector('ldmx-det-v13')
sim.description = 'Kaon Gun Test Simulation'

# importing chip/geometry conditions
from LDMX.Ecal import EcalGeometry
from LDMX.Hcal import HcalGeometry
import LDMX.Ecal.ecal_hardcoded_conditions as ecal_conditions
import LDMX.Hcal.hcal_hardcoded_conditions as hcal_conditions

# import processor module
import LDMX.Ecal.digi as ecal_digi
import LDMX.Hcal.digi as hcal_digi

# setting the actions in order for simulation
p.sequence = [
    sim, 
    ecal_digi.EcalDigiProducer(),
    ecal_digi.EcalRecProducer(),
    hcal_digi.HcalDigiProducer(),
    hcal_digi.HcalRecProducer()
    ]

# output parameters
p.outputFiles = [f'kaons_energyis{sys.argv[1]}gev_zis{sys.argv[2]}_thetais{sys.argv[3]}.root']
p.maxEvents = 1000
p.logFrequency = 1000
p.maxTriesPerEvent = 1
p.termLogLevel = 1
print("Created 1000 K+ with %.3f GeV generated at z = %.2f with angle %.3f towards x direction" % (myGun.energy,zGun,theta))
