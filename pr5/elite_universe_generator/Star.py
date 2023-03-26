def rshift(val, n): return (val % 0x100000000) >> n


class Star:
    DIGRAM_STRING = "@@LEXEGEZACEBISOUSESARMAINDIREA'ERATENBERALAVETIEDORQUANTEISRION"

    SIZES = ("Large", "Fierce", "Small", "")

    COLORS = ("Green", "Red", "Yellow", "Blue", "Black", "Harmless", "")

    ATTR = ("Slimy", "Bug-Eyed", "Horned", "Bony", "Fat", "Furry", "")

    INHABITANTS = ("Rodents", "Frogs", "Lizards", "Lobsters", "Birds", "Humanoids", "Felines", "Insects")

    government_types = ("Anarchy", "Feudal", "Multi-Government", "Dictatorship",
                        "Communist", "Confederacy", "Democracy", "Corporate State")

    economic_types = ("Rich Industrial", "Average Industrial", "Poor Industrial",
                      "Mainly Industrial", "Mainly Agricultural", "Rich Agricultural", "Average Agricultural",
                      "Poor Agricultural")

    def __init__(self):
        self.inhabitants = None
        self.prod = None
        self.pops = None
        self.tech_lvl = None
        self.tl_data = None
        self.eco_name = None
        self.eco_id = None
        self.gov_name = None
        self.gov_id = None
        self.radius = None
        self.y = None
        self.x = None
        self.planet_name = None
        self.seed = None

    def init_star(self, seed):
        self.seed = seed
        self.planet_name = self.create_name(seed)
        self.x = self.create_coords(seed[0])
        self.y = self.create_coords(seed[1])
        self.radius = self.create_radius(seed[2])
        self.gov_id = self.create_gov(seed[1])
        self.gov_name = self.get_gov_name(self.gov_id)
        self.eco_id = self.create_eco(seed[0])
        self.eco_name = self.get_eco_name(self.eco_id)
        self.tl_data = self.create_tl_data(seed)
        self.tech_lvl = self.create_tech_lvl(self.tl_data)
        self.pops = self.create_pops()
        self.prod = self.create_prod(self.tl_data)
        self.inhabitants = self.create_inhabitants(seed)

    def get_gov_name(self, gov_id):
        return self.government_types[gov_id]

    def get_eco_name(self, eco_id):
        return self.economic_types[eco_id]

    def twist(self, seed):
        twist_seed = []
        twist_seed[0] = seed[1]
        twist_seed[1] = seed[2]
        twist_seed[2] = seed[0] + seed[1] + seed[2]
        return twist_seed

    def create_name(self, seed):
        name = ""
        name_seed = seed
        for i in range(5):
            if i != 3 or rshift(seed[0], 6) & 1 != 0:
                name += self.get_name_char(name_seed[2])
            name_seed = self.twist(name_seed)
        name = name.replace("@", "")
        name = name.replace("'", "")
        return name

    def get_name_char(self, seed_part):
        pair = ""
        shift = ((seed_part >> 8) & 31) * 2
        pair += self.DIGRAM_STRING[shift]
        pair += self.DIGRAM_STRING[shift + 1]
        return pair

    def create_tech_lvl(self, tl):
        return (1 - tl[0]) * 4 + (1 - tl[1]) * 2 + 1 - tl[2] + tl[3] + tl[4] + tl[5] + 1

    def create_prod(self, tl):
        return ((1 - tl[0]) * 4 + (1 - tl[1]) * 2 + 1 - tl[2] + 3) * (self.gov_id + 4) * self.pops * 80

    def create_tl_data(self, seed):
        tl = []
        tl[0] = rshift(seed[0], 10) & 1
        tl[1] = rshift(seed[0], 9) & 1
        tl[2] = rshift(seed[0], 8) & 1
        tl[3] = rshift(seed[1], 8) & 3
        tl[4] = rshift(seed[1], 4) & 3
        tl[5] = rshift(seed[1], 3) & 1
        return tl

    def create_inhabitants(self, seed):
        inhabitants = "Human Colonists"
        inhab_list = []
        if rshift(seed[2], 7) & 1 != 0:
            inhab_list[0] = min(rshift(seed[2], 10) & 7, 3)
            inhab_list[1] = min(rshift(seed[2], 13) & 7, 6)
            third_attr = 0
            for i in range(4):
                bin_start = 8 - (i + 1)
                comb_values = rshift(seed[0], (15 - bin_start) & 1)
                comb_values = comb_values % 2

                if i > 0:
                    comb_values *= i * 2
                third_attr = third_attr + comb_values
        inhab_list[2] = min(third_attr, 6)
        inhab_list[3] = (rshift(seed[2], 8 % 3) + third_attr) % 8
        return self.create_inhab_string(inhab_list)

    def create_inhab_string(self, inhab_list):
        inhab_str = ""

        inhab_str = self.SIZES[inhab_list[0]]
        if not (inhab_str == ""):
            inhab_str += " "

        inhab_str += self.COLORS[inhab_list[1]]
        if not (inhab_str == ""):
            inhab_str += " "

        inhab_str += self.ATTR[inhab_list[2]]
        if not (inhab_str == ""):
            inhab_str += " "

        inhab_str += self.INHABITANTS[inhab_list[3]]
        if not (inhab_str == ""):
            inhab_str += " "

        return inhab_str

    def create_pops(self):
        return ((self.tech_lvl - 1) * 4 + self.gov_id + self.eco_id + 1) / 10

    def create_coords(self, seed_part):
        return rshift(seed_part, 8) & 255

    def create_radius(self, seed_part):
        return 256 * (11 + (rshift(seed_part, 8) & 0xf)) + self.x

    def create_gov(self, seed_part):
        return rshift(seed_part, 3) & 0x7

    def create_eco(self, seed_part):
        return rshift(seed_part, 8) & 0x7
