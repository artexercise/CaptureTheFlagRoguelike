__author__ = "jjeskiewicz"

class ctfStreet():
	def __init__(self):
		self.uid = ""			# track the Street
		self.name = ""			# Street Name
		self.orientation = ""	# EastWest, NorthSouth
		
	def __str__(self):
		return "This is {0}. It runs {1}.".format(self.name, self.orientation)

if __name__ == "__main__":
	ScooterStreet = ctfStreet()
	ScooterStreet.name = "Scooter St."
	ScooterStreet.orientation = "EastWest"
	print(ScooterStreet);