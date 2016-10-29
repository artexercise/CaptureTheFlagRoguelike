__author__ = "jjeskiewicz"

class ctfGender:
   class objGender:
      def __init__(self, name, desc):
         self.name = name
         self.desc = desc
      def __str__(self):
         return self.name

   Male = objGender("Male", "It's a guy.")
   Female = objGender("Female", "It's a gal.")
   Unknown = objGender("Unknown", "I don't know for... reasons.")
   Hermaphrodite = objGender("Hermaphrodite", "Little bit man, little bit woman.")
   Androgynous = objGender("Androgynous", "Ummm. Neither guy nor gal?")

   AttributeList = [Male, Female, Unknown, Hermaphrodite, Androgynous]


if __name__ == "__main__":
   import random
   for i in range(5):
      g = random.choice(ctfGender.AttributeList)
      print("{0} - {1}".format(g, g.desc))
   print("Calling Directly from class like an ENUM: {0}".format(ctfGender.Male))
   print("Because Gender is also an Object with another attribute: {0}".format(ctfGender.Male.desc))
