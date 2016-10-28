__author__ = "jjeskiewicz"

class ctfCityGrid():
	def __init__(self):
		self.uid = ""							# track the Map?
		self.HorizontalStreetCollection = ""	# East West Streets From Top to Bottom
		self.VerticalStreetCollection = ""		# North South Streets from Left to Right
		self.BlockArray = ""					# 2D Array of Blocks where Upper Left Block is (0,0)

	def makeStreets(self):
		pass
		
	def makeBlocks(self):
		pass
		
	def outputAscii(self):
		pass

	def outputText(self):
		pass
		
	def __str__(self):
		return "The Map is Made."

if __name__ == "__main__":
	CityMap = ctfCityGrid()
	print(CityMap);