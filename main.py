import pandas as pd
data = pd.read_csv('new_data.csv')
from mayavi import mlab
import numpy as  np




temp_list = list(data['Theta [deg]'])

x = []
z = []
for elem in data.keys():
    if elem != 'Theta [deg]':
        entry = elem.find("Phi")+5
        phi = int(elem[entry:elem.find('deg')])
        x.extend([phi for i in range(len(temp_list))])
        z.extend(data[elem])
y = []
for _ in range(len(data.keys())-1):
    y.extend([i for i in range(len(temp_list))])

X = []
Y = []
Z = []

for i in range(len(x)):
	X.append(z[i]*np.cos(x[i]/57)*np.cos(((y[i]-90))/57))
	Y.append(z[i]*np.sin(x[i]/57)*np.cos(((y[i]-90))/57))
	Z.append(z[i]*np.sin(((y[i]-90)/57)))
	
mlab.points3d(X,Y,Z,z)
#zin(mu), tube_radius=0.025, colormap='Spectral'mlab.mesh(x,y,z)
#mlab.mesh(x,y,z,representation='wireframe',color=(0,0,0))
a = int(input())
