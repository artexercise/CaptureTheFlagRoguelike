__author__ = "jjeskiewicz"

class ctfBuilding():
	def __init__(self):
		self.uid = ""			# track the Building
		self.address = ""		# Address number
		self.EWStreet = ""		# Closest street running East and West => StreetID
		self.NSStreet = ""		# Closest street running North and South => StreetID
		self.floorcount = ""	# Number of Floors
		self.bbasement = ""		# Toggle: Is there a basement in this building
		self.basement = ""		# uid of Basement
		self.floor1 = ""		# uid of floor
		self.floor2 = ""		# uid of floor - MIGHT BE EMPTY
		self.floor3 = ""		# uid of floor - MIGHT BE EMPTY
		self.floor4 = ""		# uid of floor - MIGHT BE EMPTY
		self.roof = ""			# uid of floor
		
	def getFloorCount(self):
		return "is 1 floor" if self.floorcount == 1 else "are " + str(self.floorcount) + " floors" if self.floorcount > 1 else "are infinite floors" 
	
	def __str__(self):
		return "This is building {0}. It is on the corner of {1} and {2}.  There {3}.".format(self.address, self.EWStreet, self.NSStreet, self.getFloorCount())

if __name__ == "__main__":
	Building107 = ctfBuilding()
	Building107.address = 107
	Building107.floorcount = 2
	Building107.EWStreet = "Scrabble Blvd"
	Building107.NSStreet = "Clue Ave"
	print(Building107);