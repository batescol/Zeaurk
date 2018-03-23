import Monster
import random

# This file contains all of the specific monster types, setting up:
#	attack damage range
#	health
# 	vulnerabilities to weapons (including invulnerabilities etc.)
#	a label for the UI to print for this type of monster


class Vampire(Monster.Monster):
	def __init__(self, house):
		super().__init__(house)

		self.attrange = (0, 10)
		self.health = random.uniform(100, 200)
		self.vuln = {"ChocolateBar": 0.0}
		self.label = "Vampire"

class Zombie(Monster.Monster):
	def __init__(self, house):
		super().__init__(house)

		self.attrange = (0, 10)
		self.health = random.uniform(50, 100)
		self.vuln = {"SourStraw": 2.0}
		self.label = "Zombie"

class Ghoul(Monster.Monster):
	def __init__(self, house):
		super().__init__(house)

		self.attrange = (15, 30)
		self.health = random.uniform(40, 80)
		self.vuln = {"NerdBomb": 5.0}
		self.label = "Ghoul"

class Werewolf(Monster.Monster):
	def __init__(self, house):
		super().__init__(house)

		self.attrange = (0, 40)
		self.health = 200
		self.vuln = {"ChocolateBar": 0.0,
					 "SourStraw": 0.0}
		self.label = "Werewolf"