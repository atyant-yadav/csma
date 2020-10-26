# Author: Atyant Yadav

import os
import subprocess
from matplotlib import pyplot as plt

# ns csma.tcl -n 20 -r 0.1Mb -nc 0.1Mb -cd 1
val = 21
nc = "1Mb"
flag = 1 #1 for CSMA/CD and 0 for unslotted-aloha

f = open("file.txt", "w")
f.write("no of nodes,  throughput\n")

tputAll = []
nodes = []
ratee = ["0.01Mb", "0.1Mb", "0.25Mb", "0.5Mb", "1Mb"]

cmd2 = "awk -f tputAll.awk out1.tr"


for i in range(1, 21):
	nodes.append(i)
	cmd1 = "ns csma.tcl -n "+str(i)+" -r "+ratee[2]+" -nc "+nc+" -cd "+str(flag)
	os.system(cmd1)
	temp = subprocess.check_output(cmd2, shell=True)
	temp1 = str(i)+" "+temp
	f.write(temp1)
	temp = temp.strip('\n')
	tputAll.append(temp)

f.close()

y = list(map(float, tputAll))
q = []
for number in y:
	q.append( round((number / 1000), 2) )

plt.plot(nodes, q, color='red', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='blue', markersize=2) 

# naming the x axis 
plt.xlabel('No. of nodes') 
# naming the y axis 
plt.ylabel('Efficiency in percentage(%)') 
  
plt.show()