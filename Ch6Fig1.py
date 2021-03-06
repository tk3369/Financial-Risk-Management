import random
import frmbook_funcs

#Generate virtual reality
#Hardcoded: 91.5 years, annual standard deviation 18.49%
Sqrt12=12**0.5
targetsd=18.49/Sqrt12
NMonths=91*12+6           #Number of months of virtual reality
VirtualReality=[]
random.seed(3.14159265)
for x in range(NMonths):
    VirtualReality.append(random.gauss(0,targetsd))

#VirtualReality now contains Nmonths sample
#of normal variates mean 0 stddev targetsd

#Generate date array
Date=[]
Year,Month=1926,7
for x in range(NMonths):
    Date.append(float(Year+Month/100.0))
    Month+=1
    if (Month==13):
        Year+=1
        Month=1

lookbacks=[12,36,60]
SampleSd=frmbook_funcs.GenSampleSd(VirtualReality,lookbacks)
StubOffset=6
colors=['y-','b-','r-']
frmbook_funcs.PlotSampleSd('Figure 1',Date,SampleSd,StubOffset,\
lookbacks,colors)
