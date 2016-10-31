__author__ = "jjeskiewicz"

class ctfSurname:
   class objSurname:
      def __init__(self, name):
         self.name = name
      def __str__(self):
         return self.name

   Smith = objSurname("Smith")
   Jones = objSurname("Jones")
   Miller = objSurname("Miller")
   Taylor = objSurname("Taylor")
   Jackson = objSurname("Jackson")
   Martin = objSurname("Martin")
   Rodriguez = objSurname("Rodriguez")
   Walker = objSurname("Walker")
   Young = objSurname("Young")
   Baker = objSurname("Baker")
   Carter = objSurname("Carter")
   Bell = objSurname("Bell")
   West = objSurname("West")
   Porter = objSurname("Porter")
   Jeskiewicz = objSurname("Jeskiewicz")

   AttributeList = [Smith, Jones, Miller, Taylor, Jackson, Martin,
                    Rodriguez, Walker, Young, Baker, Carter, Bell,
                    West, Porter, Jeskiewicz]

if __name__ == "__main__":
   import random
   for i in range(5):
      g = random.choice(ctfSurname.AttributeList)
      print("{0}".format(g))
   print("Calling Directly from class like an ENUM: {0}".format(ctfSurname.Smith))
