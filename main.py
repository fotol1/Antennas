import pandas as pd
from mayavi import mlab
import numpy as  np
import re

class Data_table():
	
	def __init__(self, data):
		self.data = pd.read_csv(data)

		initial_theta = int(self.data[self.data.keys()[0]][0])
		end_theta = int(list(self.data[self.data.keys()[0]])[-1])
		
		step_theta = int( self.data[self.data.keys()[0]][1]-initial_theta)
		temp = str(re.findall(r"Phi='[-0123456789]+", self.data.keys()[1])[0])[5:]
		
		self.step_theta = step_theta
		initial_phi = int(temp)
#		print(initial_phi)
		temp = str(re.findall(r"Phi='[-0123456789]+", self.data.keys()[-1])[0])[5:]
		end_phi = int(temp)
		temp = str(re.findall(r"Phi='[-0123456789]+", self.data.keys()[2])[0])[5:]
		second = int(temp)
		step_phi = second - initial_phi
		
#		print('{} - initial theta, {} - end_theta, {}-step_theta'.format(initial_theta,end_theta,step_theta))
#		print('{} - initial phi, {} - end_phi, {} - step_phi'.format(initial_phi, end_phi, step_phi))

		[self.theta, self.phi] = np.mgrid[initial_theta:end_theta+1:step_theta,initial_phi:end_phi:step_phi]
#		print(self.phi)
		self.z = self.form_value(self.phi, self.theta)

	def find_value(self,phi, theta):
		for el in self.data.keys():
			if "Phi='"+str(phi) in el:
				return self.data[el][int(theta/self.step_theta)]
		return 0
	def form_value(self,phi,theta):
		z = np.array([[0. for i in range(len(phi[0]))] for j in range(len(theta))])
		for i in range(len(theta)):
			for j in range(len(phi[0])):
				z[i][j] = self.find_value(phi[i][j], theta[i][j])
		return z

	def draw(self):
		grad_to_rad = 180/np.pi
		self.x = self.z*np.cos(self.phi/grad_to_rad)*np.cos((self.theta-90)/grad_to_rad)
		self.y = self.z*np.sin(self.phi/grad_to_rad)*np.cos((self.theta-90)/grad_to_rad)
		self.z_to = self.z
		self.z = self.z * np.sin( (self.theta-90)/grad_to_rad)
		mlab.mesh(self.y,self.z,self.x,scalars = self.z_to)
		a = int(input())



	def __str__(self):
		return str(self.z)
if __name__ == '__main__':
	temp = Data_table('data_bow.csv')
#	print(temp)
	temp.draw()


