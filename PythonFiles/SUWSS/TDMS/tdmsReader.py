"""
import numpy as np
from nptdms import TdmsFile
from nptdms import tdms
    
filenameS = "24July2018_Intact_1.tdms"
tdms_file = TdmsFile(filenameS)
root_object = tdms_file.object()
for name, value in root_object.properties.items():
      print("{0}: {1}".format(name, value))
      print(root_object.properties)
"""
import scipy.io
import plotly.plotly as plt
import plotly.graph_objs as go
import numpy as np

mat = scipy.io.loadmat('24July2018_Intact_1.mat')
data = []
x = mat.get('VoltageAI0')[0][0][1][0][0]
time = []
for i in range(0,x):
      time.append(i)

print(time)
data.append(mat.get('VoltageAI0')[0][0][0])
data.append(mat.get('VoltageAI1')[0][0][0])
data.append(mat.get('VoltageAI2')[0][0][0])
data.append(mat.get('VoltageAI3')[0][0][0])
print(data[0])
random_x = np.linspace(0,1,100)
random_y = np.random.randn(100)

trace = go.Scatter( x =random_x,y=random_y)
data1 = [trace]
plt.iplot(data1,filename="basic line")
