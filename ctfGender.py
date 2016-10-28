__author__ = "jjeskiewicz"

class ctfGender:
   Male = "Male"
   Female = "Female"
   Unknown = "Unknown"
   Hermaphrodite = "Hermaphrodite"
   Androgynous = "Androgynous"

   AttributeList = [Male, Female, Unknown, Hermaphrodite, Androgynous]

if __name__ == "__main__":
   import random
   for i in range(5):
      print(random.choice(ctfGender.AttributeList))
