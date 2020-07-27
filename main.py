
'''
Jonathan Benson
CS404
26 July 2020
Project
'''


import math
import copy
import random
import matplotlib.pyplot as plt



STEP = 20

class Request :
	# composed of a vertex with a zipcode and a vehicle type

	def __init__(self, vt, v) :

		self.vehicleType = vt
		self.vertex = v

class Response :
	# a response is a response to a request containing a vertex and vehicle

	def __init__(self, a, b) :

		self.vertex = a
		self.vehicle = b

	def __str__(self) :

		return "{:10}{:10}{:10}{:10}".format(self.vehicle.type, self.vertex.zipcode(), self.vehicle.id, self.vehicle.distance(self.vertex))

class Vertex :
	# a vertex is a reference point on a graph representing a zipcode
	# zipcodes: 111111 to 999999 (the first 3 digits represent the x-coordinate and the last 3 represent the y-coordinate)
	def __init__(self, x, y) :
		# x and y can range from 1 to 999

		self.x = x
		self.y = y



	def zipcode(self) :
		#zip code is a 6 digit number ranging from 111111 to 999999

		return int(str(self.x) + str(self.y))

	




class Graph :
	# a graph is composed of zipcodes 111111 to 999999 (the first 3 digits represent the x-coordinate and the last 3 represent the y-coordinate)

	def __init__(self, vertices, vehicles) :

		self.vertices = vertices
		self.vehicles = vehicles


class Vehicle :
	# a vehicle is composed of a type, and a zipcode telling where it is located on the graph

	def __init__(self, t, x, y, i) :

		self.type = t
		self.x = x
		self.y = y

		self.id = i

	def distance(self, vertex) :

		return round(math.sqrt(math.pow(self.x - vertex.x, 2) + math.pow(self.y - vertex.y, 2)))


#random generation of zipcodes

vertices = list()

xy = list()

for i in range(1,999, STEP) :

	for j in range(1, 999, STEP) :

		xy.append([i, j])


for i in range(750) :

	randDigit = random.choice(xy)

	randomVertex = Vertex(randDigit[0], randDigit[1])

	vertices.append(randomVertex)

	xy.remove(randDigit)
		
# end of random generation of zipcodes



# random generation of vehicles
vehicles = list()

verticesCopy = copy.deepcopy(vertices)

for i in range(200) :

	randomVertex = random.choice(verticesCopy)

	vehicles.append(Vehicle(random.randint(1,3), randomVertex.x, randomVertex.y, i))

	verticesCopy.remove(randomVertex)

graph = Graph(vertices, vehicles)

# end of random generation of vehicles



# randomly generating requests

requests = list()


for i in range(75) :

	randomVertex = random.choice(vertices)

	requests.append(Request(random.randint(1,3), randomVertex))

# end of random generation of requests





# creation of responses

responses = list()


ambulances = list(filter(lambda v: v.type == 1, vehicles))
firetrucks = list(filter(lambda v: v.type == 2, vehicles))
police = list(filter(lambda v: v.type == 3, vehicles))

print("{:10}{:10}{:10}{:10}".format("V-Type", "Zipcode", "V-Id", "Distance"))

for r in requests :

	if r.vehicleType == 1 :
		# if the vehicle is an ambulance

		# sort ambulances by their distance to the location of the request ascending
		ambulances.sort(key = lambda v: v.distance(r.vertex))

		# select the closest ambulance to the request location
		responses.append(Response(r.vertex, ambulances[0]))

		# output the result to the console
		print(responses[-1])

		ambulances.pop(0)

	elif r.vehicleType == 2 :
		#if the vehicle is a firetruck


		# sort firetrucks by their distance to the location of the request ascending
		firetrucks.sort(key = lambda v: v.distance(r.vertex))

		# select the closest firetruck to the request location
		responses.append(Response(r.vertex, firetrucks[0]))

		# output the result to the console
		print(responses[-1])

		firetrucks.pop(0)

	elif r.vehicleType == 3 :
		#if the vehicle is a police car

		# sort police by their distance to the location of the request ascending
		police.sort(key = lambda v: v.distance(r.vertex))

		# select the closest police car to the request location
		responses.append(Response(r.vertex, police[0]))

		# output the result to the console
		print(responses[-1])

		police.pop(0)

# plotting the path taken by each vehicle to their request location
for response in responses :
	
	if response.vehicle.type == 1 :

		c = "red"

	elif response.vehicle.type == 2 :

		c = "orange"

	elif response.vehicle.type == 3 :

		c = "blue"


	plt.plot([response.vehicle.x, response.vertex.x], [response.vehicle.y, response.vertex.y], color = c)



# end of creation of responses




# plotting vehicles on the graph

verticesX = [v.x for v in graph.vertices]
verticesY = [v.y for v in graph.vertices]



ambulanceX = list()
ambulanceY = list()
firetruckX = list()
firetruckY = list()
policeX = list()
policeY = list()

for v in vehicles :

	if v.type == 1 :

		ambulanceX.append(v.x)
		ambulanceY.append(v.y)

	elif v.type == 2 :

		firetruckX.append(v.x)
		firetruckY.append(v.y)

	elif v.type == 3 :

		policeX.append(v.x)
		policeY.append(v.y)





plt.scatter(verticesX, verticesY, color = "black")

plt.scatter(ambulanceX, ambulanceY, color = "red")
plt.scatter(firetruckX, firetruckY, color = "orange")
plt.scatter(policeX, policeY, color = "blue")




plt.show()

# end of plotting vehicles on the graph
