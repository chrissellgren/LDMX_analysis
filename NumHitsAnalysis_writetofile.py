import EventTree
import sys
import ROOT

# import root tree

tree = EventTree.EventTree(sys.argv[1])

# scan through every event in tree, record number of ecal hits that each event produces
hitcount=[]
for event in tree:
    numhits = 0
    for ecal_hit in event.EcalRecHits: # ENSURE REC HITS
       numhits = numhits + 1
    hitcount.append(numhits)

# scan through array of number of hits per event
# if the event produced 0 or 1 hits, record
numevents = len(hitcount)
numzeros = 0
numones = 0
for i in range(numevents):
    if hitcount[i] == 0:
        numzeros += 1
    elif hitcount[i] == 1:
        numones += 1

# record perc of total events had that many hits
perczero = numzeros/numevents
percnotracks = (numzeros + numones)/numevents

name = sys.argv[1]
print(name)
# write a function to determine how many characters in string name should be included
def findnumofvalues(string): 
    i = 0
    while True:
        if string[i] == '_':
            return i
        i += 1
end = findnumofvalues(name)
energy = name[0:int(end)]

# write into a text file with the energy of the sample, perc no hits, perc no tracks
f = open('20samples_3.5mm.txt','a')
f.write(energy+','+str(perczero)+','+str(percnotracks)+'\n')
f.close()

