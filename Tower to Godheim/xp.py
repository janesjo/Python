from characters import *

def combat_reward():
	print(player.name, "has defeated", enemy.name, "and is rewarded with", enemy.xp_drop, "xp and", enemy.gold, "gold")
	player.xp = player.xp + enemy.xp_drop
	player.gold = player.gold + enemy.gold
	if enemy.bag[0] == True:
		print(enemy.name, "dropped", enemy.bag[1].name)

	if player.xp >= player.max_xp:
		lvl_up = True
		player.lvl_points = 5
		player.lvl += 1
		player.xp -= player.max_xp
		player.max_xp = round(max_xp * 1.25)
		print("You gained a level")
		print("LVL:", player.lvl, "\nXP:", player.xp, "NEXT LVL:", player.max_xp)


def lvl_menu():
	print("Point remaining:", player.lvl_points)
	print("Type the number for which stat you want")
	print("1) Strength      current:", player.str)
	print("2) Agility       current:", player.agi)
	print("2) Dexterity     current:", player.dex)
	print("2) Vitality      current:", player.vit)
	lvl_input = input("> ")

player.lvl_points = 5

while player.lvl_points > 0:
	print("You have gained a level which gives you 5 stat points")
	lvl_menu()

	if lvl_input == "1":
		player.str = player.str + 1
		player.lvl_points -= 1
		lvl_menu()
	if lvl_input == "1":
		player.agi = player.agi + 1
		player.lvl_points -= 1
		lvl_menu()
	if lvl_input == "1":
		player.dex = player.dex + 1
		player.lvl_points -= 1
		lvl_menu()
	if lvl_input == "1":
		player.vit = player.vit + 1
		player.lvl_points -= 1
		lvl_menu()
