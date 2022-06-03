from cProfile import label
import matplotlib.pyplot as plt


nbThreads = [4,8,12,16,18,32,48,64]
nbNodes = [4,6,8,10,12,14,16]


#OpenMP temps
OMPTF16 = [14,10,10,9,9,12,18,24] # en s
OMPEasy = [11.9,6.5,4.55,3.6,3.4,2.6,3.1,3.15] #en mn 
OMPMedium = [4.71,2.33,1.63,1.26,1.15,0.76,1,1.08] #en h
OMPHard = [4.4,2.25,1.58,1.16,1.125,0.91,1.04,1.06] #en jours
OMPHPC = [204,99,52,46,37,34,34.1,36.3] #en jours 

#MPI temps
MPITF16 = [25,22,24,21,23,24,28,42] # en s
MPIEasy = [14.5,9.4,8.1,7,6.9,6.1,6.7,6.9] #en mn 
MPIMedium = [5,2.83,2.15,1.71,1.65,1.26,1.28,1.3] #en h
MPIHard = [4.6,2.5,1.83,1.41,1.33,0.95,0.92,1.04] #en jours
MPIHPC = [126,69,51,41,38,32,29,30.5] #en jours 

#Hybrid temps
HybridHard = [18.9,15.4,18.4,17.3,16.9,16.4,10.9] #en h 
HybridHPC = [24,19,17,16,15.9,15.4,14.5]  #en j


#MPI vs Hybrid
MPIDahuHard = [1.79,1.75,1.58,1.57,1.57,1.54,1.5] #en j puis converti en heures
MPIDahuHPC = [56,55,53.5,53.6,53.1,56,54.6]  #en j

for i in range(len(MPIDahuHard)):
        MPIDahuHard[i] = MPIDahuHard[i] * 24


#plt.plot(nbThreads,OMPHPC,label = "OpenMP")
#plt.plot(nbThreads,MPIHPC,label = "MPI")
plt.plot(nbNodes,MPIDahuHPC,label = "MPI")
plt.plot(nbNodes,HybridHPC,label = "Hybrid")
#plt.axvline(x=32, color='r', linestyle='-',label="Nombre de thread optimal")
plt.xlabel("Nombre de noeuds")
plt.ylabel("Temps (en jours)")
plt.legend()
plt.title("Matrice HPC")
plt.savefig("OpenMP/plots/HybridvsMPIHPC.png",bbox_inches='tight')
plt.show()