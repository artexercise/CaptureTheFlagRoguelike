__author__ = "jjeskiewicz"

class ctfFlag():
	def __init__(self):
		self.uid = ""			# track the Flag
		self.alias = ""			# Flag Looks Like...
		self.location = ""		# Room ID
		
	def __str__(self):
		return "This flag looks like {0}. It is in room {1}.".format(self.alias, self.location)

if __name__ == "__main__":
	PlayerAFlag = ctfFlag()
	PlayerAFlag.alias = "1959 State Fair Calendar"
	PlayerAFlag.location = "17"
	print(PlayerAFlag);