import EventTree
import sys
import ROOT
import numpy as np

tree = EventTree.EventTree(sys.argv[1])

# convert z-pos to layer #
zd = np.loadtxt('layer.txt')
layerZs = {round(zd[i]):i for i in range(len(zd))}

def getlayer(zarr):
    def roundreturn(val):
        return layerZs[round(val)]
    return list(map(roundreturn, zarr))

z_hits = []
x_hits = []
y_hits = []
energy_hits= []
isNoise = []
ID = []
amplitude = []

for event in tree :
    # do some analysis nonsense
    for ecal_hit in event.EcalRecHits :
        z_hits.append(ecal_hit.getZPos())
        x_hits.append(ecal_hit.getXPos())
        y_hits.append(ecal_hit.getYPos())
        energy_hits.append(ecal_hit.getEnergy())
        isNoise.append(ecal_hit.isNoise())
        ID.append(ecal_hit.getID())
        amplitude.append(ecal_hit.getAmplitude())
# end loop

layer_hits = getlayer(z_hits)

f = open('RECHITinfo_10kevkaons.txt','a')
f.write('hit layer, x position, y position, energy deposited, is noise, amplitude, ID\n')
# new loop to add each element of the list to the histogram
for i in range(len(layer_hits)):
    f.write(str(layer_hits[i])+',')
    f.write(str(x_hits[i])+',')
    f.write(str(y_hits[i])+',')
    f.write(str(energy_hits[i])+',')
    f.write(str(isNoise[i])+',')
    f.write(str(amplitude[i])+',')
    f.write(str(ID[i])+'\n')
# e nd loop
