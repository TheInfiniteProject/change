import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
import time

class globeWindow():
	
	def __init__(self,X,Y,Z,mainCats):

		self.X = X
		self.Y = Y
		self.Z = Z
		self.mainCats = mainCats

	def on_pick(self,event):
	
		ind = event.ind[0]
		x, y, z = event.artist._offsets3d
		print(x[ind]," | ", y[ind]," | ", z[ind])

	
	def createWindow(self):
		

		fig = plt.figure()
		sub1 = fig.add_subplot(111, projection='3d')
		
		sub1.plot(self.X,self.Y,self.Z, c="g")
		sub1.scatter(self.X,self.Y,self.Z, c="b", marker="o", picker=1)

		sub1.set_title("C H A N G E")
		# X cords
		sub1.set_xlabel("C A T E G O R I E S")
		# Y cords		
		sub1.set_ylabel("P O P U L A R I T Y")
		# Z cords	
		sub1.set_zlabel("P E R C I E V E D   I M P O R T A N C E")
				

		for index, value in enumerate(self.X):
			#print(value," | ",index)
			sub1.text(self.X[index],self.Y[index],self.Z[index],self.mainCats[index])

		fig.canvas.callbacks.connect('pick_event', self.on_pick)
					
		
		plt.show()

		

questionMainScreen = globeWindow([1,2,3,4,5,6,7,8,9,10],[1,5,7,3,8,9,3,4,6,8],[3,4,2,5,7,1,8,9,6,10],
["Economics","Agriculture | Water","Politics","Education","Safety | Security","Government Accountability","Poverty","Ideologies","War | Conflict","Climate Change | Society VS Nature"])

questionMainScreen.createWindow()
