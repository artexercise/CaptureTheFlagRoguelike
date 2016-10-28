__author__ = "jjeskiewicz"

class ctfPerson():
	def __init__(self):
		self.uid = ""			# Track the NPCs
		self.gender = ""		# Can be Male or Female
		self.age = ""			# Start with ages 19 to 115
		self.givenname = ""		# Gender and Age Based
		self.surname = ""		# To Trace families
		self.profession = ""	# From the environment and strangeness
		self.married = ""		# Toggle: A decision for different kinds of families may have to be made
		self.children = ""		# Toggle: Consider adoption based on above as well?
		self.father = ""		# name or number
		self.mother = ""		# name or number
		self.siblings = ""		# Toggle
		self.decostyle = ""		# From plain to weird
		
	def __str__(self):
		return "Hi.  My Name is {0}.  How are you?".format(self.givenname)

if __name__ == "__main__":
	AuthorJoe = ctfPerson()
	AuthorJoe.givenname = "Joe"
	AuthorJoe.gender = "Male"
	AuthorJoe.age = "40"
	AuthorJoe.decostyle = "Dark"
	print(AuthorJoe);
