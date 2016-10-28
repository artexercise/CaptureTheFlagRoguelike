__author__ = "jjeskiewicz"

class ctfFloor():
	def __init__(self):
		self.uid = ""			# track the Floor
		self.floor = ""			# Address
		self.roomA = ""			# Room Floor-A
		self.roomB = ""			# Room Floor-B
		self.roomC = ""			# Room Floor-C
		self.roomD = ""			# Room Floor-D
		self.roomE = ""			# Room Floor-E
		self.roomF = ""			# Room Floor-F
		
	def getFloorOrdinal(self):
		return "basement" if self.floor == 0 else "ground floor" if self.floor == 1 else "second floor" if self.floor == 2 else "third floor" if self.floor == 3 else "fourth floor" if self.floor == 4 else "roof" if self.floor == 5 else "wrong floor"
	
	def __str__(self):
		return "This is the {0}.".format(self.getFloorOrdinal())

if __name__ == "__main__":
	Basement = ctfFloor()
	Basement.floor = 0
	print(Basement);
	Floor1 = ctfFloor()
	Floor1.floor = 1
	print(Floor1);
	Floor2 = ctfFloor()
	Floor2.floor = 2
	print(Floor2);
	Floor3 = ctfFloor()
	Floor3.floor = 3
	print(Floor3);
	Floor4 = ctfFloor()
	Floor4.floor = 4
	print(Floor4);
	Roof = ctfFloor()
	Roof.floor = 5
	print(Roof);
