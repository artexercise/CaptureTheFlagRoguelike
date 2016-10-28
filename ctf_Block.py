__author__ = "jjeskiewicz"

class ctfBlock():
	def __init__(self):
		self.uid = ""			# track the Building Block
		self.NorthWest = ""		# NW Building ID
		self.NorthEast = ""		# NE Building ID
		self.SouthWest = ""		# SW Building ID
		self.SouthEast = ""		# SE Building ID
		
	def __str__(self):
		return "This is building Block has four buildings."

if __name__ == "__main__":
	BuildingBlock = ctfBlock()
	print(BuildingBlock);