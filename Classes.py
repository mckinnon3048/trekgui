import sys
import random


class Faction:
    def __init__(self, name, ascendancy, manufacturing, research, culture, speed, m_node, r_node, c_node, defense, attack):
        self.name = name
        self.ascendancy = ascendancy
        self.manufacturing = manufacturing
        self.research = research
        self.culture = culture
        self.speed = speed
        self.m_node = m_node
        self.r_node = r_node
        self.c_node = c_node
        self.defense = defense
        self.attack = attack

    def show_stats(self):
        print(" {} level {}\n Manufacture = {}\n Research = {}\n Culture = {}\n Warp speed = {}\n Deflectors = {}\n Phasers = {}\n"
.format(self.name, self.ascendancy, self.manufacturing, self.research, self.culture, self.speed, self.defense, self.attack))

    def ascend(self):
        self.culture -= 5
        self.ascendancy += 1
        return (self.culture, self.ascendancy)

    def build_factory(self):
        pass

    def build_lab(self):
        self.research -= 1
        self.manufacturing -= 1

    def build_civics(self):
        self.culture -= 1
        self.manufacturing -= 1

    def build_starbase(self):
        pass

    def build_colony(self):
        pass

    def build_ship(self):
        self.manufacturing -= 1

    def upkeep_man(self):
        self.manufacturing = manufacturing + m_node
        return(self.manufacturing)

    def upkeep_res(self):
        self.research = research + r_node
        return(self.research)

    def upkeep_cul(self):
        self.culture = culture + c_node
        return(self.culture)

    def upkeep_phase(self):
        self.upkeep_cul()
        self.upkeep_man()
        self.upkeep_res()
        return(self.manufacturing, self.research, self.culture)

    def build_phase(self):
        self.show_stats()
        print("Build Phase, please select a construction.")
        selection = int(input("1: Ship, 0: End \n \n"))
        while selection != 0:
            print ("The {} has produced another vessel.".format(self.name))
            self.manufacturing -= 1
            self.build_phase()

        else:
            print("End of build phase, moving to command phase.")
            return()

    def command_phase(self):
        print("Commandstuff goes here need rules bye")
        return()


class Vessel:
    def __init__(self, fleet, owner, warp, location):
        self.fleet = fleet
        self.owner = owner
        self.warp = warp
        self.location = location

class System:
    pass


#player listings
federation = Faction("The Federation", 1, 3, 3, 3, 1, 1, 1, 1, 1, 1)
klingon = Faction("The Klingon Empire", 1, 3, 3, 3, 1, 1, 1, 1, 1, 1)
romulan = Faction("The Romulan Empire", 1, 3, 3 ,3 ,1 ,1 ,1, 1, 1, 1)
ferengi = Faction("The Ferengi Aliance", 1, 3, 3, 3, 1, 1, 1, 1, 1, 1)
cardasian = Faction("The Cardassian Union", 1, 3, 3, 3, 1, 1, 1, 1, 1, 1)
#[player_value = Faction(Name, starting values

federation.show_stats()

def game(name, ascendancy, manufacturing, research, culture, speed, m_node, r_node, c_node, defense, attack):
    player = int(input("Which Faction's turn is it? \n 1: Federation \n 2: Klingons \n 3: Romulans \n 0: All players have gone\n \n"))#adtl factions added w/ rules updates
    if player == 1:
        federation.build_phase()
        federation.command_phase()
        game(name, ascendancy, manufacturing, research, culture, speed, m_node, r_node, c_node, defense, attack)
    if player == 2:
        klingon.build_phase()
        klingon.command_phase()
        game(name, ascendancy, manufacturing, research, culture, speed, m_node, r_node, c_node, defense, attack)

    if player == 3:
        romulan.build_phase()
        romulan.command_phase()
        game(name, ascendancy, manufacturing, research, culture, speed, m_node, r_node, c_node, defense, attack)

    if player == 4:
        federation.upkeep_phase()
        klingon.upkeep_phase()
        romulan.upkeep_phase()

    else:
        game(name, ascendancy, manufacturing, research, culture, speed, m_node, r_node, c_node, defense, attack)




game(None, None, None, None, None, None, None, None, None, None, None)