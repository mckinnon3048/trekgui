import sys
import random
#gitversion

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
        print("Building a Factory consumes 2 manufactuing, requires a red or grey location \n and produces 1 manufacturing on each upkeep.\n")
        factory_yes = int(-1)
        factory_yes = int(input("Are you sure you wish to build a Factory?\n 1: Yes, 0: No"))
        if factory_yes == 1:
            print("\nPlease place a prodcution node of {} on the planet.\n".format(self.name))
            self.manufacturing -=2
            self.build_phase()

        if factory_yes == 0:
            print("\nA Factory was not built at this time, no resources were consumed.\n")
            self.build_phase()

        if factory_yes != 1 or 0:
            print("\nThat was an invalid selection, please try again.\n")
            self.build_factory()

    def build_lab(self): #this is the correct working model as of 6/5/2017 for structures, needs transposed onto all other types of construction
        print("Building a Laboratory consumes 2 Research and 1 Manufacturing, requires a blue or grey location \n and produces 1 Research on each upkeep.\n")
        if self.manufacturing >= 1 and self.research >= 2:
            lab_yes = int(-1)
            lab_yes = int(input("Are you sure you wish to build a Laboratory?\n 1: Yes, 0: No\n"))
            if lab_yes == 1:
                print("\nPlease place a research node of {} on the planet.\n".format(self.name))
                self.manufacturing -=1
                self.research -=2
                input("")
                self.build_phase()

            if lab_yes == 0:
                print("\nA research node was not built at this time, no resources were consumed.\n")
                self.build_phase()

            if lab_yes != 1 or 0:
                print("\nThat was an invalid selection, please try again.\n")
                self.build_factory()

        if self.manufacturing << 1 or self.research << 2:
            print("\n{} does not have enough resources to build a research node at this time\n".format(self.name))
            input("")

<<<<<<< Updated upstream
    def build_lab(self):
        self.research -= 1
        self.manufacturing -= 1
=======
>>>>>>> Stashed changes

    def build_civics(self):
        self.culture -= 1
        self.manufacturing -= 1

    def build_starbase(self):
        pass

    def build_colony(self):
        print("Building a colony consumes a ship in an unnocupied, habitable system and 1 culture.\n")
        colony_yes = int(-1)
        colony_yes = int(input("Are you sure you wish to build a colony?\n 1: Yes, 0: No"))
        if colony_yes == 1:
            print("\nPlease remove 1 ship from the system, and place a control node of {} on the planet.\n".format(self.name))
            self.culture -=1
            self.build_phase()

        if colony_yes == 0:
            print("\nA colony was not built at this time, no resources were consumed.\n")
            self.build_phase()

        if colony_yes != 1 or 0:
            print("\nThat was an invalid selection, please try again.\n")
            self.build_colony()

    def build_ship(self):
        ships_made = int(0)
        ships_made = int(input("\nHow many ships would you like to build? \n"))
        if ships_made > self.manufacturing:
            print("\n{} may place {} ships.\n".format(self.name, self.manufacturing))
            self.manufacturing = 0
            self.command_phase()

        if ships_made <= self.manufacturing:
            print("\n{} may place {} ships.\n".format(self.name, ships_made))
            self.manufacturing = self.manufacturing - ships_made
            self.build_phase()

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
<<<<<<< Updated upstream
        selection = int(input("1: Ship, 0: End \n \n"))
        while selection != 0:
            print ("The {} has produced another vessel.".format(self.name))
            self.manufacturing -= 1
            self.build_phase()
=======
        selection = int(input("\n1:Ships \n2:Colony \n3:Factory \n4:Laboratory \n5:Civic Center 0: End Build \n"))
        if selection == 1:
           self.build_ship()

        if selection == 2:
            self.build_colony()

        if selection == 3:
            self.build_factory()

        if selection == 4:
            self.build_lab()

        if selection == 5:
            self.build_civics()
>>>>>>> Stashed changes

        else:
<<<<<<< Updated upstream
            print("End of build phase, moving to command phase.")
            return()
=======
            print("\nInvalid choice, please try again.\n")
            self.build_phase()
        return()
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
    player = int(input("Which Faction's turn is it? \n 1: Federation \n 2: Klingons \n 3: Romulans \n 0: All players have gone\n \n"))#adtl factions added w/ rules updates
=======
    player = int(input("Which Faction's turn is it? \n 1: Federation \n 2: Klingons \n 3: Romulans \n 4: All players have gone\n"))#adtl factions added w/ rules updates
>>>>>>> Stashed changes
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