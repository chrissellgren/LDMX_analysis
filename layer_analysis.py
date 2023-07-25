import EventTree
import sys
import ROOT
import numpy as np

ROOT.gROOT.SetBatch(1)

tree = EventTree.EventTree(sys.argv[1])

f_output = ROOT.TFile(f'{sys.argv[2]}.root','recreate')

# histogram needs to be created **after** the file is opened, so it ends up inside of it
h_ecal_hit_Position = ROOT.TH1F('Ecal Hit Position','Hit Layer for 10k 10keV K+ Generated in 16th Layer of Ecal;Ecal Rec Hit Layer',34,0,33)

# convert z-pos to layer #
zd = np.loadtxt('layer.txt')
layerZs = {round(zd[i]):i for i in range(len(zd))}

def getlayer(zarr):
    def roundreturn(val):
        return layerZs[round(val)]
    return list(map(roundreturn, zarr))

z_hits = []
for event in tree :
    # do some analysis nonsense
    for ecal_hit in event.EcalRecHits :
        z_hits.append(ecal_hit.getZPos())
# end loop

layer_hits = getlayer(z_hits)

# new loop to add each element of the list to the histogram
for i in range(len(layer_hits)):
    h_ecal_hit_Position.Fill(layer_hits[i])
# end loop

c = ROOT.TCanvas()
h_ecal_hit_Position.Draw()
c.SaveAs(f'{sys.argv[2]}.pdf')

# this junk needs to be last because it deletes all of the ROOT objects inside the file from memory
f_output.Write()
f_output.Close()
