import uproot
import numpy as np
import awkward
import sys

filename = sys.argv[1]

id_branches = ['SimParticles_v3_v12.second.pdgID_']
energy_branches = ['SimParticles_v3_v12.second.energy_']
pz_branches = ['SimParticles_v3_v12.second.pz_']
py_branches = ['SimParticles_v3_v12.second.py_']
px_branches = ['SimParticles_v3_v12.second.px_']
z_branches = ['SimParticles_v3_v12.second.z_']
y_branches = ['SimParticles_v3_v12.second.y_']
x_branches = ['SimParticles_v3_v12.second.x_']

endz_branches = ['SimParticles_v3_v12.second.endZ_']
endy_branches = ['SimParticles_v3_v12.second.endY_']
endx_branches = ['SimParticles_v3_v12.second.endX_']
daughter_branches = ['SimParticles_v3_v12.second.daughters_']


# opens the file with uproot
t = uproot.open(filename)['LDMX_Events']

# uproot dictionary
id_table = t.arrays(expressions=id_branches)
energy_table = t.arrays(expressions=energy_branches)
pz_table = t.arrays(expressions=pz_branches)
py_table = t.arrays(expressions=py_branches)
px_table = t.arrays(expressions=px_branches)
z_table = t.arrays(expressions=z_branches)
y_table = t.arrays(expressions=y_branches)
x_table = t.arrays(expressions=x_branches)

endz_table = t.arrays(expressions=endz_branches)
endy_table = t.arrays(expressions=endy_branches)
endx_table = t.arrays(expressions=endx_branches)
daughter_table = t.arrays(expressions=daughter_branches)


# make our own dictionary, load each key in the uproot dictionary into our own
# do for each of the 5 trees we're examining
id_tree = {}
for branch in id_branches:
        id_tree[branch] = id_table[branch]

energy_tree = {}
for branch in energy_branches:
        energy_tree[branch] = energy_table[branch]

pz_tree = {}
for branch in pz_branches:
        pz_tree[branch] = pz_table[branch]

py_tree = {}
for branch in py_branches:
        py_tree[branch] = py_table[branch]

px_tree = {}
for branch in px_branches:
        px_tree[branch] = px_table[branch]

z_tree = {}
for branch in z_branches:
        z_tree[branch] = z_table[branch]

y_tree = {}
for branch in y_branches:
        y_tree[branch] = y_table[branch]

x_tree = {}
for branch in x_branches:
        x_tree[branch] = x_table[branch]

endz_tree = {}
for branch in endz_branches:
        endz_tree[branch] = endz_table[branch]

endy_tree = {}
for branch in endy_branches:
        endy_tree[branch] = endy_table[branch]

endx_tree = {}
for branch in endx_branches:
        endx_tree[branch] = endx_table[branch]

daughter_tree = {}
for branch in daughter_branches:
        daughter_tree[branch] = daughter_table[branch]
    
# list of each sim hit Pdg ID
pdgIDs = []
energies = []
pz = []
py = []
px = []
z = []
y = []
x = []

endz = []
endy = []
endx = []


numdaughters = []

# the second.pdgID array is organized like this: [ [event0], [event1], ... ]
# each event: [ particle 1, particle 2 ]

import sys
with np.printoptions(threshold=sys.maxsize):
    print(id_tree)

for event in range(len(id_tree['SimParticles_v3_v12.second.pdgID_'])):
    for particle in range(len(id_tree['SimParticles_v3_v12.second.pdgID_'][event])):
        ID = id_tree['SimParticles_v3_v12.second.pdgID_'][event][particle]
        # only look for kaons. K- has ID -321, K+ has ID 321
        if ID == 321 or ID == -321:
            #pdgIDs.append(id_tree['SimParticles_v3_v12.second.pdgID_'][event][particle])
            #energies.append(energy_tree['SimParticles_v3_v12.second.energy_'][event][particle])
            #pz.append(pz_tree['SimParticles_v3_v12.second.pz_'][event][particle])
            #py.append(py_tree['SimParticles_v3_v12.second.py_'][event][particle])
            #px.append(px_tree['SimParticles_v3_v12.second.px_'][event][particle])
            #z.append(z_tree['SimParticles_v3_v12.second.z_'][event][particle])
            #y.append(y_tree['SimParticles_v3_v12.second.y_'][event][particle])
            #x.append(x_tree['SimParticles_v3_v12.second.x_'][event][particle])
            endz.append(endz_tree['SimParticles_v3_v12.second.endZ_'][event][particle])
            endy.append(endy_tree['SimParticles_v3_v12.second.endY_'][event][particle])
            endx.append(endx_tree['SimParticles_v3_v12.second.endX_'][event][particle])
            #numdaughtersthisparticle = len(daughter_tree['SimParticles_v3_v12.second.daughters_'][event][particle])
            #numdaughters.append(numdaughtersthisparticle)


f = open(f'simparticleinfo_endpts.txt','w')
for i in range(len(endz)):
    f.write(str(endz[i])+',')
    f.write(str(endy[i])+',')
    f.write(str(endx[i])+',')
    f.write("\n")
f.close()

