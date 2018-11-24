from decimal import *
import random, os, time
from characters import *

base_hit = 80

def pre_fighting():
    
    global enemy
    enemy = test_enemy()
        
    if player.speed > enemy.speed:
        player.turn = 1
    else:
        player.turn = 0
        
    if player.str > player.agi:
        player.main_stat = "str"
    if player.str < player.agi:
        player.main_stat = "agi"
    else:
        player.main_stat = "agi"
    

# Use only at spawn or stats will reset
def stat_calculation():
    
    global player_dodge_balance
    player_dodge_balance = 3
    
    global player_hit_balance
    player_hit_balance = 3
    
    global player_speed_balance
    player_speed_balance = 2
    
    global player_vit_balance
    player_vit_balance = 10
    
    global player_crit_balance
    player_crit_balance = 2


    global enemy_dodge_balance
    enemy_dodge_balance = 3
    
    global enemy_hit_balance
    enemy_hit_balance = 3
    
    global enemy_speed_balance
    enemy_speed_balance = 2
    
    global enemy_vit_balance
    enemy_vit_balance = 10
    
    global enemy_crit_balance
    enemy_crit_balance = 2

    player.dodge = player.agi // player_dodge_balance
    player.hit = player.dex + player.agi // player_hit_balance 
    player.speed = player.agi * 2 + player.dex // player_speed_balance
    player.max_hp = player.vit * player_vit_balance
    player.hp = player.max_hp
    player.crit = player.dex // player_crit_balance
    player.armour_value = player.armour_head.armour_value + player.armour_chest.armour_value + player.armour_legs.armour_value + player.armour_arms.armour_value
    player.armour_value = player.armour_value // 100
    player.armour_block = 1 - player.armour_value


    enemy.max_hp = enemy.vit * enemy_vit_balance
    enemy.hp = enemy.max_hp
    enemy.dodge = enemy.agi // enemy_dodge_balance
    enemy.speed = enemy.agi * 2 + player.agi // enemy_speed_balance
    enemy.crit = enemy.dex // enemy_crit_balance
    enemy.hit = player.dex + player.agi // enemy_hit_balance
    enemy.armour_value = enemy.armour_head.armour_value + enemy.armour_chest.armour_value + enemy.armour_legs.armour_value + enemy.armour_arms.armour_value
    enemy.armour_value = enemy.armour_value // 100
    enemy.armour_block = 1 - enemy.armour_value
    
def armour_stat():
        
    player.str = player.str + player.armour_head.stat_str + player.armour_chest.stat_str + player.armour_legs.stat_str + player.armour_arms.stat_str + player.main_hand.stat_str + player.off_hand.stat_str   
    player.agi = player.agi + player.armour_head.stat_agi + player.armour_chest.stat_agi + player.armour_legs.stat_agi + player.armour_arms.stat_agi + player.main_hand.stat_agi + player.off_hand.stat_agi
    player.dex = player.dex + player.armour_head.stat_dex + player.armour_chest.stat_dex + player.armour_legs.stat_dex + player.armour_arms.stat_dex + player.main_hand.stat_dex + player.off_hand.stat_dex
    player.vit = player.vit + player.armour_head.stat_vit + player.armour_chest.stat_vit + player.armour_legs.stat_vit + player.armour_arms.stat_vit + player.main_hand.stat_vit + player.off_hand.stat_vit
    
    player.hit = player.hit + player.armour_head.stat_hit + player.armour_chest.stat_hit + player.armour_legs.stat_hit + player.armour_arms.stat_hit + player.main_hand.stat_hit + player.off_hand.stat_hit
    player.crit = player.crit + player.armour_head.stat_crit + player.armour_chest.stat_crit + player.armour_legs.stat_crit + player.armour_arms.stat_crit + player.main_hand.stat_crit + player.off_hand.stat_crit
    player.dodge = player.dodge + player.armour_head.stat_dodge + player.armour_chest.stat_dodge + player.armour_legs.stat_dodge + player.armour_arms.stat_dodge + player.main_hand.stat_dodge + player.off_hand.stat_dodge
    player.speed = player.speed + player.armour_head.stat_speed + player.armour_chest.stat_speed + player.armour_legs.stat_speed + player.armour_arms.stat_speed + player.main_hand.stat_speed + player.off_hand.stat_speed
    
        
    enemy.str = enemy.str + enemy.armour_head.stat_str + enemy.armour_chest.stat_str + enemy.armour_legs.stat_str + enemy.armour_arms.stat_str + enemy.main_hand.stat_str + enemy.off_hand.stat_str
    enemy.agi = enemy.agi + enemy.armour_head.stat_agi + enemy.armour_chest.stat_agi + enemy.armour_legs.stat_agi + enemy.armour_arms.stat_agi + enemy.main_hand.stat_agi + enemy.off_hand.stat_agi
    enemy.dex = enemy.dex + enemy.armour_head.stat_dex + enemy.armour_chest.stat_dex + enemy.armour_legs.stat_dex + enemy.armour_arms.stat_dex + enemy.main_hand.stat_dex + enemy.off_hand.stat_dex
    enemy.vit = enemy.vit + enemy.armour_head.stat_vit + enemy.armour_chest.stat_vit + enemy.armour_legs.stat_vit + enemy.armour_arms.stat_vit + enemy.main_hand.stat_vit + enemy.off_hand.stat_vit

    enemy.hit = enemy.hit + enemy.armour_head.stat_hit + enemy.armour_chest.stat_hit + enemy.armour_legs.stat_hit + enemy.armour_arms.stat_hit + enemy.main_hand.stat_hit + enemy.off_hand.stat_hit
    enemy.crit = enemy.crit + enemy.armour_head.stat_crit + enemy.armour_chest.stat_crit + enemy.armour_legs.stat_crit + enemy.armour_arms.stat_crit + enemy.main_hand.stat_crit + enemy.off_hand.stat_crit
    enemy.dodge = enemy.dodge + enemy.armour_head.stat_dodge + enemy.armour_chest.stat_dodge + enemy.armour_legs.stat_dodge + enemy.armour_arms.stat_dodge + enemy.main_hand.stat_dodge + enemy.off_hand.stat_dodge
    enemy.speed = enemy.speed + enemy.armour_head.stat_speed + enemy.armour_chest.stat_speed + enemy.armour_legs.stat_speed + enemy.armour_arms.stat_speed + enemy.main_hand.stat_speed + enemy.off_hand.stat_speed

def damage_calculation():

    # player
    if player.main_stat == "str":
        player.wep_atk = random.randint(player.main_hand.dmg_low, player.main_hand.dmg_high)
        player.atk = player.wep_atk * player.str // 5
        player.atk = player.atk * enemy.armour_block
        global dmg_block_player
        dmg_block_player = player.atk * enemy.armour_value // 100

    if player.main_stat == "agi":
        player.wep_atk = random.randint(player.main_hand.dmg_low, player.main_hand.dmg_high)
        player.atk = player.wep_atk * player.agi // 5
    else:
        wep_atk = random.randint(player.main_hand.dmg_low, player.main_hand.dmg_high)
        player.atk = wep_atk * player.agi //  5


    # enemy
    enemy.wep_atk = random.randint(enemy.main_hand.dmg_low, enemy.main_hand.dmg_high)
    enemy.atk = enemy.wep_atk * enemy.str // 5
    enemy.atk = enemy.atk * player.armour_block
    global dmg_block_enemy
    dmg_block_enemy = player.atk * enemy.armour_value 

    
    player.dodge = player.agi // player_dodge_balance
    player.hit = player.dex + player.agi // player_hit_balance 
    player.speed = player.agi * 2 + player.dex // player_speed_balance
    player.crit = player.dex // player_crit_balance
    player.armour_value = player.armour_head.armour_value + player.armour_chest.armour_value + player.armour_legs.armour_value + player.armour_arms.armour_value
    player.armour_value = player.armour_value / 100
    player.armour_block = 1 - player.armour_value
    
    
    enemy.dodge = enemy.agi // enemy_dodge_balance
    enemy.speed = enemy.agi * 2 + player.agi // enemy_speed_balance
    enemy.crit = enemy.dex // enemy_crit_balance
    enemy.hit = player.dex + player.agi // enemy_hit_balance
    enemy.armour_value = enemy.armour_head.armour_value + enemy.armour_chest.armour_value + enemy.armour_legs.armour_value + enemy.armour_arms.armour_value
    enemy.armour_value = enemy.armour_value / 100
    enemy.armour_block = 1 - enemy.armour_value


def player_hit():
    enemy.hp = enemy.hp - player.atk
    print(player.name, "deal", round(player.atk), "damage to", enemy.name, "(", round(dmg_block_enemy), "damage blocked)","\n")
    player.turn = 0
    
def player_crit():
    player.atk = player.atk * 2
    enemy.hp = enemy.hp - player.atk
    print(player.name, "crit and deal", round(player.atk) , "damage to", enemy.name, "\n")
    player.turn = 0

def player_status():
	player.atk = player.atk * 2
	enemy.hp = enemy.hp - player.atk
	player.turn = 0
	if player.main_hand.effect == "bleed":
		enemy.status = "bleed"
		enemy.status_turn = 5
		enemy.status_dot = player.atk // 2
		print(player.name, "crit and deal", round(player.atk) , "damage to", enemy.name, "and apply", player.main_hand.effect)

	if player.main_hand.effect == "crushing":
		enemy.status = "crushing"
		enemy.status_turn = 5
		enemy.status_dot = 0
		print(player.name, "crit and deal", round(player.atk) , "damage to", enemy.name, "and apply", player.main_hand.effect)

	if player.main_hand.effect == "": 
		print(player.name, "crit and deal", round(player.atk) , "damage to", enemy.name)
    
    
            
def enemy_hit():
    player.hp = player.hp - enemy.atk
    print(enemy.name, "deal", round(enemy.atk), "damage to", player.name, "\n")
    player.turn = 1

def enemy_crit():
    enemy.atk = enemy.atk * 2
    player.hp = player.hp - enemy.atk
    print(enemy.name, "crit and deal", round(enemy.atk) , "damage to", player.name, "\n")
    player.turn = 1

def enemy_status():
	enemy.atk = enemy.atk * 2
	player.hp = player.hp - enemy.atk
	player.turn = 1
	if enemy.main_hand.effect == "bleed":
		player.status = "bleed"
		player.status_turn = 5
		player.status_dot = player.atk // 2
		print(enemy.name, "crit and deal", round(enemy.atk) , "damage to", player.name, "and apply", enemy.main_hand.effect)

	if enemy.main_hand.effect == "crushing":
		player.status = "crushing"
		player.status_turn = 5
		print(enemy.name, "crit and deal", round(enemy.atk) , "damage to", player.name, "and apply", enemy.main_hand.effect)

	if player.main_hand.effect == "":
		print(enemy.name, "crit and deal", round(enemy.atk) , "damage to", player.name)


def combat_reward():
	print(player.name, "has defeated", enemy.name, "and is rewarded with", enemy.xp_drop, "xp and", enemy.gold, "gold")
	player.xp = player.xp + enemy.xp_drop
	player.gold = player.gold + enemy.gold
	if enemy.bag[0] == True:
		print(enemy.name, "dropped", enemy.bag[1].name)
		player.bag.append(dagger)

	if player.xp >= player.max_xp:
		lvl_up = True
		player.lvl += 1
		player.xp -= player.max_xp
		player.max_xp = round(player.max_xp * 1.25)
		print("You gained a level")
		print("LVL:", player.lvl, "\nXP:", player.xp, "NEXT LVL:", player.max_xp)


def status_check_player():
	if player.status == "bleed":
		player.hp -= player.status_dot
		player.status_turn -= 1
		print(player.name, "bleeds for", player.status_dot, "damage.")
		if player.status_turn <= 0:
			print(player.name, player.status, "wears off.")
			player.status = 0

	if player.status == "crushing":
		player.armour_value = round(player.armour_value * 0.80)
		player.status_turn -= 1
		print(player.name, "is affected by", player.status)
		if player.status_turn <= 0:
			print(player.name, player.status, "wears off.")
			player.status = 0



def status_check_enemy():
	if enemy.status == "bleed":
		enemy.hp -= enemy.status_dot
		enemy.status_turn -= 1
		print(enemy.name, "bleeds for", enemy.status_dot, "damage.")
		if enemy.status_turn <= 0:
			print(enemy.name, enemy.status, "wears off.")
			enemy.status = 0

	if enemy.status == "crushing":
		enemy.armour_value = round(enemy.armour_value * 0.80)
		enemy.status_turn -= 1
		print(enemy.name, "is affected by", enemy.status)
		if enemy.status_turn <= 0:
			print(enemy.name, enemy.status, "wears off.")
			enemy.status = 0

def combat():
    in_combat = True
    while in_combat:
            
        while player.turn == 1 and in_combat == True:
            damage_calculation()
            status_check_player()
            print (player.name, "s turn. HP:", round(player.hp), "\n")
            roll = random.randint (0, 99)
            total_hit = player.hit + base_hit - enemy.dodge
            hit = list(range(total_hit))
            crit = list(range(player.crit))
            status = list(range(player.status_chance))
            dodge = list(range(enemy.dodge))
            

            if roll in hit:
                if roll in crit:
                    if roll in status:

                    	player_status()
                    	if enemy.hp <= 0:                    			
	                        combat_reward()
	                        in_combat = False
	                        break
                
                    else:
                        player_crit()
                        if enemy.hp <= 0:
                            combat_reward()
                            in_combat = False
                            break
                else:
                    player_hit()    
                    if enemy.hp <= 0:
                        combat_reward()
                        in_combat = False
                        break
            else:
                if roll in dodge:
                	print(enemy.name, "dodged the attack.")
                	player.turn = 0
                	break
                else:
                	print(player.name, "missed the attack on", enemy.name)
                	player.turn = 0
                	break

                if enemy.hp <= 0:
                    combat_reward()
                    in_combat = False
                    break
                
        while player.turn == 0 and in_combat == True:
            damage_calculation()
            status_check_enemy()
            print (enemy.name, "s turn HP:", round(enemy.hp), "\n")
            roll = random.randint (0, 99)
            total_hit = enemy.hit + base_hit - player.dodge
            hit = list(range(total_hit))
            crit = list(range(enemy.hit))
            status = list(range(enemy.status_chance))
            dodge = list(range(player.dodge))

            if roll in hit:
                if roll in crit:
                    if roll in status:
                        
                        enemy_status()
                        if player.hp <= 0:
                            print(player.name, "died")
                            in_combat = False
                            break
        
                    else:
                        enemy_crit()
                        if player.hp <= 0:
                            print(player.name, "died")
                            in_combat = False
                            break
                else:
                    enemy_hit()
                    if player.hp <= 0:
                        print(player.name, "died")
                        in_combat = False
                        break
            else:
                if roll in dodge:
                	print(player.name, "dodged the attack")
                	player.turn = 1
                	break
                else:
                	print(enemy.name, "missed the attack on", player.name)
                	player.turn = 1
                	break

                if player.hp <= 0:
                    print(player.name, "died")
                    in_combat = False
                    break

pre_fighting()
stat_calculation()
damage_calculation()
combat()
print(enemy.armour_value)
print(enemy.armour_block)