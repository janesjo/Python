class bleed():
    def __init__ (self):
        self.name = "bleed"
        self.effect_value = 0
        self.effect_turns = 5
        self.effect_damage = 0
        self.stat_str = 0
        self.stat_agi = 0
        self.stat_dex = 0
        self.stat_vit = 0

bleed = bleed()

class dagger():
    def __init__ (self):
        self.name = "Dagger"
        self.description = ""
        self.type = "agi"
        self.dmg_low = 2
        self.dmg_high = 4
        self.effect = "bleed"
        self.extra = 0
        self.extra_1 = 0
        self.stat_str = 0
        self.stat_agi = 0
        self.stat_vit = 0
        self.stat_dex = 3
        self.stat_crit = 7
        self.stat_hit = 0
        self.stat_dodge = 0
        self.stat_speed = 0
        self.gold_value = 0
        self.stat_req_str = 0
        self.stat_req_agi = 0
        self.stat_req_dex = 0
        self.stat_req_vit = 0
        self.gold_value = 0

dagger = dagger()

class bastard_sword():
    def __init__ (self):
        self.name = "Bastard Sword"
        self.description = ""
        self.type = "str"
        self.dmg_low = 5
        self.dmg_high = 8
        self.effect = ""
        self.stat_str = 4
        self.stat_agi = 0
        self.stat_vit = 0
        self.stat_dex = 0
        self.stat_crit = 0
        self.stat_hit = 0
        self.stat_dodge = 0
        self.stat_speed = 0
        self.stat_req_str = 10
        self.stat_req_agi = 0
        self.stat_req_dex = 0
        self.stat_req_vit = 0
        self.gold_value = 0

bastard_sword = bastard_sword()

##############
### ARMOUR ###
##############



class leather_armour():
    def __init__ (self):
        self.name = "Leather Armour"
        self.type = "armour"
        self.armour_value = 3
        self.effect = ""
        self.stat_str = 2
        self.stat_agi = 0
        self.stat_vit = 0
        self.stat_dex = 0
        self.stat_crit = 0
        self.stat_hit = 0
        self.stat_dodge = 0
        self.stat_speed = 0
        self.gold_value = 0

leather_armour = leather_armour()
        
class naked():
    def __init__ (self):
        self.name = "Naked"
        self.type = "armour"
        self.armour_value = 0
        self.effect = ""
        self.stat_str = 0
        self.stat_agi = 0
        self.stat_vit = 0
        self.stat_dex = 0
        self.stat_crit = 0
        self.stat_hit = 0
        self.stat_dodge = 0
        self.stat_speed = 0
        self.gold_value = 0

naked = naked()