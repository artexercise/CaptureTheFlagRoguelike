__author__ = "jjeskiewicz"

class ctfRoom():
	def __init__(self):
		self.uid = ""			# track the Room
		self.floor = ""			# Address 1
		self.roomletter = ""	# Address 2
		self.occupied = ""		# Toggle: Might be empty
		self.occupantcount = ""	# If not Empty, number of Occupants
		self.occupant1 = ""		# uid of first occupant - might be empty
		self.occupant2 = ""		# uid of second occupant - might be empty
		self.decor = ""			# Grab from first occupant
		self.bFlag = ""			# Toggle: Is this a flag room?
		self.xFlag = ""			# Whose Flag is it?
		
	def getOccupancy(self):
		return "Nobody lives" if not self.occupied else "One person lives" if self.occupantcount==1 else "Two people live"
		
	def __str__(self):
		return "This is room {0}.  {1} here.".format((self.floor + self.roomletter), self.getOccupancy())

if __name__ == "__main__":
	Room1A = ctfRoom()
	Room1A.floor = "1"
	Room1A.roomletter = "A"
	Room1A.occupied = False
	print(Room1A);
	Room2B = ctfRoom()
	Room2B.floor = "2"
	Room2B.roomletter = "B"
	Room2B.occupied = True
	Room2B.occupantcount = 1
	print(Room2B);
	Room3C = ctfRoom()
	Room3C.floor = "3"
	Room3C.roomletter = "C"
	Room3C.occupied = True
	Room3C.occupantcount = 2
	print(Room3C);
