import Observer
import random

# This class represents a generic monster
class Monster(Observer.Observable):
	def __init__(self, house):
		super().__init__()
		
		self.house = house

		# set the label to something memorable so we can 
		# catch weird bugs
		self.label = "__MON__"

		self.setObser(house)
	
	# Called to attack the player, in accordance with the monster's
	# attack range
	def attack(self, player):
		damage = random.uniform(self.attrange[0], self.attrange[1])
		player.getHit(damage)
		return damage

	# Called when the player attacks the monster
	def getHit(self, damage, weapon):
		# Apply any vulnerabilities
		if weapon in self.vuln:
			damage = damage * self.vuln[weapon]

		self.health = self.health - damage

		# If we die, let the house know
		if self.health <= 0:
			self.show()

		return damage