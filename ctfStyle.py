__author__ = "jjeskiewicz"

class ctfStyle:
   class ctfDecor:
      MidCenturyModern = "Mid-Century Modern"
      Industrial = "Industrial"
      Nautical = "Nautical"
      Scandinavian = "Scandinavian"
      Bohemian = "Bohemian"
      Farmhouse = "Farmhouse"
      UrbanModern = "Urban Modern"
      ShabbyChic = "Shabby Chic"

      AttributeList = [MidCenturyModern, Industrial, Nautical, Scandinavian, Bohemian, Farmhouse, UrbanModern, ShabbyChic]

if __name__ == "__main__":
   import random
   for i in range(5):
      print(random.choice(ctfStyle.ctfDecor.AttributeList))
   print("Calling Directly from class like an ENUM: {0}".format(ctfStyle.ctfDecor.MidCenturyModern))
