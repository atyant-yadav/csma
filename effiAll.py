# Author: Atyant Yadav

import os
import subprocess
from matplotlib import pyplot as plt

# ns csma.tcl -n 20 -r 0.1Mb -nc 0.1Mb -cd 1
val = 21
nc = "1Mb"
nci = 1
flag = 1 #1 for CSMA/CD and 0 for unslotted-aloha

# f = open("file.txt", "w")
# f.write("no of nodes,  throughput")

tputAll = []
nodes = []
ratee = ["0.01Mb", "0.1Mb", "0.25Mb", "0.5Mb", "1Mb"]

cmd2 = "awk -f tputAll.awk out1.tr"

for x in ratee:
	arr = []
	for i in range(1, val):
		cmd1 = "ns csma.tcl -n "+str(i)+" -r "+x+" -nc "+nc+" -cd "+str(flag)
		os.system(cmd1)
		temp = subprocess.check_output(cmd2, shell=True)
		# temp1 = str(i)+" "+temp
		# f.write(temp1)
		temp = temp.strip('\n')
		temp = float(temp)
		temp = round((temp / (1000*nci)), 2)
		arr.append(temp)
	tputAll.append(arr)

for x in range(1, val):
	nodes.append(x)

for i in range(1,len(ratee)+1):
	plt.plot(nodes, tputAll[i-1], label = ratee[i-1]) 

# naming the x axis 
plt.xlabel('No. of nodes') 
# naming the y axis 
plt.ylabel('Efficiency') 
plt.legend(title="Packet Rate CBR")
plt.show()
