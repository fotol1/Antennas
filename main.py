import pandas as pd
data = pd.read_csv('new_data.csv')
from mayavi import mlab
import numpy as  np

STEP_THETA = 1
STEP_PHI = 1
[theta,phi] = np.mgrid[0:181:STEP_THETA, 0:360:STEP_PHI]


def find_value(data,phi, theta):
    for el in data.keys():
        if "Phi='"+str(phi) in el:
            return data[el][theta]
        
def form_value(data,phi,theta):
    z = np.array([[0. for i in range(len(phi[0]))] for j in range(len(theta))])
    for i in range(len(theta)):
        for j in range(len(phi[0])):
            z[i][j] = find_value(data, phi[i][j], theta[i][j])
    return z

z = form_value(data, phi,theta)

x = z*np.cos(phi/57)*np.cos((theta-90)/57)
y = z*np.sin(phi/57)*np.cos((theta-90)/57)
z_to = z
z = z * np.sin( (theta-90)/57)

#for i in range(len(x)):
#	X.append(z[i]*np.cos(x[i]/57)*np.cos(((y[i]-90))/57))
#	Y.append(z[i]*np.sin(x[i]/57)*np.cos(((y[i]-90))/57))
#	Z.append(z[i]*np.sin(((y[i]-90)/57)))
	
mlab.mesh(y,z,x,scalars = z_to)
a = int(input())
