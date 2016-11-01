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

   class ctfLifeStyle:
      class objLifeStyle:
         def __init__(self, name, desc):
            self.name = name
            self.desc = desc
         def __str__(self):
            return self.name

      _1ATopTier = objLifeStyle("Top Tier", "Suburban Periphery: affluence in the suburbs")
      _1BProfessionalPride = objLifeStyle("Professional Pride", "Suburban Periphery: affluence in the suburbs")
      _1CBoomburbs = objLifeStyle("Boomburbs", "Suburban Periphery: affluence in the suburbs")
      _1DSavvySuburbanites = objLifeStyle("Savvy Suburbanites", "Suburban Periphery: affluence in the suburbs")
      _1EExurbanites = objLifeStyle("Exurbanites", "Suburban Periphery: affluence in the suburbs")
      _2AUrbanChic = objLifeStyle("Urban Chic", "Suburban Periphery: affluence in the suburbs")
      _2BPleasantville = objLifeStyle("Pleasantville", "Suburban Periphery: affluence in the suburbs")
      _2CPacificHeights = objLifeStyle("Pacific Heights", "Urban Periphery: City life for starting families")
      _2DEnterprisingProfessionals = objLifeStyle("Enterprising Professionals", "Suburban Periphery: affluence in the suburbs")
      _3ALaptopsandLattes = objLifeStyle("Laptops and Lattes", "Principal Urban Centers: Densely populated neighborhoods")
      _3BMetroRenters = objLifeStyle("Metro Renters", "Principal Urban Centers: Densely populated neighborhoods")
      _3CTrendsetters = objLifeStyle("Trendsetters", "Principal Urban Centers: Densely populated neighborhoods")
      _4ASoccerMoms = objLifeStyle("Soccer Moms", "Suburban Periphery: affluence in the suburbs")
      _4BHomeImprovement = objLifeStyle("Home Improvement", "Suburban Periphery: affluence in the suburbs")
      _4CMiddleburg = objLifeStyle("Middleburg", "Semirural: Quiet, country lifestyle")
      _5AComfortableEmptyNesters = objLifeStyle("Comfortable Empty Nesters", "Suburban Periphery: affluence in the suburbs")
      _5BInStyle = objLifeStyle("In Style", "Metro Cities: Affordable city life")
      _5CParksandRec = objLifeStyle("Parks and Rec", "Suburban Periphery: affluence in the suburbs")
      _5DRustbeltTraditions = objLifeStyle("Rustbelt Traditions", "Urban Periphery: City life for starting families")
      _5EMidlifeConstants = objLifeStyle("Midlife Constants", "Suburban Periphery: affluence in the suburbs")
      _6AGreenAcres = objLifeStyle("Green Acres", "Rural: Country Living")
      _6BSaltoftheEarth = objLifeStyle("Salt of the Earth", "Rural: Country Living")
      _6CTheGreatOutdoors = objLifeStyle("The Great Outdoors", "Rural: Country Living")
      _6DPrairieLiving = objLifeStyle("Prairie Living", "Rural: Country Living")
      _6ERuralResortDwellers = objLifeStyle("Rural Resort Communities", "Rural: Country Living")
      _6FHeartlandCommunities = objLifeStyle("Heartland Communities", "Semirural: Quiet, country lifestyle")
      _7AUpandComingFamilies = objLifeStyle("Up and Coming Families", "Suburban Periphery: affluence in the suburbs")
      _7BUrbanVillages = objLifeStyle("Urban Villages", "Urban Periphery: City life for starting families")
      _7CAmericanDreamers = objLifeStyle("American Dreamers", "Urban Periphery: City life for starting families")
      _7DBarriosUrbanos = objLifeStyle("Barrios Urbanos", "Urban Periphery: City life for starting families")
      _7EValleyGrowers = objLifeStyle("Valley Growers", "Semirural: Quiet, country lifestyle")
      _7FSouthwesternFamilies = objLifeStyle("Southwestern Families", "Urban Periphery: City life for starting families")
      _8ACityLights = objLifeStyle("City Lights", "Urban Periphery: City life for starting families")
      _8BEmeraldCity = objLifeStyle("Emerald City", "Metro Cities: Affordable city life")
      _8CBrightYoungProfessionals = objLifeStyle("Bright Young Professionals", "Urban Periphery: City life for starting families")
      _8DDowntownMeltingPot = objLifeStyle("Downtown Melting Pot", "Principal Urban Centers: Densely populated neighborhoods")
      _8EFrontPorches = objLifeStyle("Front Porches", "Metro Cities: Affordable city life")
      _8FOldandNewcomers = objLifeStyle("Old and Newcomers", "Metro Cities: Affordable city life")
      _8GHardscrabbleRoad = objLifeStyle("Hardscrabble Road", "Metro Cities: Affordable city life")
      _9ASilverandGold = objLifeStyle("Silver & Gold", "Suburban Periphery: affluence in the suburbs")
      _9BGoldenYears = objLifeStyle("Golden Years", "Suburban Periphery: affluence in the suburbs")
      _9CTheElders = objLifeStyle("The Elders", "Suburban Periphery: affluence in the suburbs")
      _9DSeniorEscapes = objLifeStyle("Senior Escapees", "Semirural: Quiet, country lifestyle")
      _9ERetirementCommunities = objLifeStyle("Retirement Communities", "Metro Cities: Affordable city life")
      _9FSocialSecuritySet = objLifeStyle("Social Security Set", "Metro Cities: Affordable city life")
      _10ASouthernSatellites = objLifeStyle("Southern Satellites", "Rural: Country Living")
      _10BRootedRural = objLifeStyle("Rooted Rural", "Rural: Country Living")
      _10CDinersandMiners = objLifeStyle("Diner & Miners", "Rural: Country Living")
      _10DDowntheRoad = objLifeStyle("Down the Road", "Semirural: Quiet, country lifestyle")
      _10ERuralBypasses = objLifeStyle("Rural Bypasses", "Rural: Country Living")
      _11ACityStrivers = objLifeStyle("City Strivers", "Principal Urban Centers: Densely populated neighborhoods")
      _11BYoungandRestless = objLifeStyle("Young and Restless", "Metro Cities: Affordable city life")
      _11CMetroFusion = objLifeStyle("Metro Fusion", "Urban Periphery: City life for starting families")
      _11DSettoImpress = objLifeStyle("Set to Impress", "Metro Cities: Affordable city life")
      _11ECityCommons = objLifeStyle("City Commons", "Metro Cities: Affordable city life")
      _12AFamilyFoundations = objLifeStyle("Family Traditions", "Urban Periphery: City life for starting families")
      _12BTraditionalLiving = objLifeStyle("Traditional Living", "Metro Cities: Affordable city life")
      _12CSmallTownSimplicity = objLifeStyle("Small Town Simplicity", "Semirural: Quiet, country lifestyle")
      _12DModestIncomeHomes = objLifeStyle("Modest Income Homes", "Urban Periphery: City life for starting families")
      _13AInternationalMarketplace = objLifeStyle("International Marketplace", "Urban Periphery: City life for starting families")
      _13BLasCasas = objLifeStyle("Las Casas", "Urban Periphery: City life for starting families")
      _13CNeWestResidents = objLifeStyle("NeWest Residents", "Principal Urban Centers: Densely populated neighborhoods")
      _13DFreshAmbitions = objLifeStyle("Fresh Ambitions", "Principal Urban Centers: Densely populated neighborhoods")
      _13EHighRiseRenters = objLifeStyle("High Rise Renters", "Principal Urban Centers: Densely populated neighborhoods")
      _14AMilitaryProximity = objLifeStyle("Military Proximity", "Suburban Periphery: affluence in the suburbs")
      _14BCollegeTowns = objLifeStyle("College Towns", "Metro Cities: Affordable city life")
      _14CDormstoDiplomas = objLifeStyle("Dorms to Diplomas", "Metro Cities: Affordable city life")

      AttributeList = [_1ATopTier, _1BProfessionalPride, _1CBoomburbs, _1DSavvySuburbanites, _1EExurbanites,
                       _2AUrbanChic, _2BPleasantville, _2CPacificHeights, _2DEnterprisingProfessionals,
                       _3ALaptopsandLattes, _3BMetroRenters, _3CTrendsetters,
                       _4ASoccerMoms, _4BHomeImprovement, _4CMiddleburg,
                       _5AComfortableEmptyNesters, _5BInStyle, _5CParksandRec, _5DRustbeltTraditions, _5EMidlifeConstants,
                       _6AGreenAcres, _6BSaltoftheEarth, _6CTheGreatOutdoors, _6DPrairieLiving, _6ERuralResortDwellers, _6FHeartlandCommunities,
                       _7AUpandComingFamilies, _7BUrbanVillages, _7CAmericanDreamers, _7DBarriosUrbanos, _7EValleyGrowers, _7FSouthwesternFamilies,
                       _8ACityLights, _8BEmeraldCity, _8CBrightYoungProfessionals, _8DDowntownMeltingPot, _8EFrontPorches, _8FOldandNewcomers, _8GHardscrabbleRoad,
                       _9ASilverandGold, _9BGoldenYears, _9CTheElders, _9DSeniorEscapes, _9ERetirementCommunities, _9FSocialSecuritySet,
                       _10ASouthernSatellites, _10BRootedRural, _10CDinersandMiners, _10DDowntheRoad, _10ERuralBypasses,
                       _11ACityStrivers, _11BYoungandRestless, _11CMetroFusion, _11DSettoImpress, _11ECityCommons,
                       _12AFamilyFoundations, _12BTraditionalLiving, _12CSmallTownSimplicity, _12DModestIncomeHomes,
                       _13AInternationalMarketplace, _13BLasCasas, _13CNeWestResidents, _13DFreshAmbitions, _13EHighRiseRenters,
                       _14AMilitaryProximity, _14BCollegeTowns, _14CDormstoDiplomas]

if __name__ == "__main__":
   import random
   for i in range(5):
      print(random.choice(ctfStyle.ctfDecor.AttributeList))
   print("Calling Directly from class like an ENUM: {0}".format(ctfStyle.ctfDecor.MidCenturyModern))
   for i in range(5):
      s = random.choice(ctfStyle.ctfLifeStyle.AttributeList)
      print("{0} - {1}".format(s, s.desc))
   print("Calling Directly from class like an ENUM: {0}".format(ctfStyle.ctfLifeStyle._13BLasCasas))
