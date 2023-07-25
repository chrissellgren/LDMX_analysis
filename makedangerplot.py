import matplotlib.pyplot as plt
import numpy as np

# find danger zone events
data = np.genfromtxt('/home/csellgren/Kaonsamples_fromdanyisample/particledata.txt',delimiter=',')
# grab kinematic info from txt file 
E = data[:,1]
pz = data[:,2]
pz_pos = np.abs(pz)
py = data[:,3]
px = data[:,4]

kmass = 493.7
KE = E - kmass

r = np.sqrt(px**2 + py**2)
tan_theta = r/np.abs(pz)
theta = np.arctan(tan_theta) * 180/np.pi

# find indices of items in danger zone
indices = []
for i in range(len(E)):
    if KE[i] < 150 or theta[i] > 60:
        indices.append(i)



Adata = np.genfromtxt("layerAnumhits.txt",delimiter=',')
B4data = np.genfromtxt("layerB4numhits.txt",delimiter=',')
C7data = np.genfromtxt("layerC7numhits.txt",delimiter=',')

Adanger = [Adata[i] for i in indices]
B4danger = [B4data[i] for i in indices]
C7danger = [C7data[i] for i in indices]

print(np.average(Adanger),np.average(B4danger),np.average(C7danger))
print(np.std(Adanger),np.std(B4danger),np.std(C7danger))

print(len(indices))
print(C7danger)

print([KE[i] for i in indices])
print([theta[i] for i in indices])


plt.figure(figsize=(9,6),dpi=600)
plt.xlabel("Number of hits per event")
plt.ylabel("Frequency")
plt.title("Number of hits for danger zone events")

bins=np.arange(0,100,2)
plt.hist(Adanger,bins=bins,histtype='step',linewidth=2,label="0.75mm Layer A1")
plt.hist(B4danger,bins=bins,histtype='step',linewidth=2,label="1.5mm Layer B4")
plt.hist(C7danger,bins=bins,histtype='step',linewidth=2,label="3.5mm Layer C7")
plt.legend()
plt.xlim(0,80)
#plt.hist(Adata,bins=bins,histtype='step',linewidth=2,label="0.75mm Layer A1")
plt.savefig("Numhitplots_danger.png")
