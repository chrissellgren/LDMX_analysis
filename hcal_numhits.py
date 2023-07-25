import EventTree
import sys
import ROOT

ROOT.gROOT.SetBatch(1)

tree = EventTree.EventTree(sys.argv[1])

f_output = ROOT.TFile(f'{sys.argv[2]}.root','recreate')

# histogram needs to be created after the file is opened, so it ends up inside of it
h_hcal_num_hits = ROOT.TH1F('Number Hits in HCal','Number of HCal Rec Hits for Each Event;Num Hits',25,0,25)

for event in tree :
     # do some analysis nonsense
    numhits = 0
    for hcal_hit in event.HcalRecHits:
        numhits = numhits + 1
    h_hcal_num_hits.Fill(numhits)

c = ROOT.TCanvas()
h_hcal_num_hits.Draw()
c.SaveAs(f'{sys.argv[2]}.pdf')

# this needs to be last because it deletes all of the ROOT objects inside the file from memory
f_output.Write()
f_output.Close()
