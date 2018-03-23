import Observer
import Weapon
import random

# This class represents the player of the game
class Player(Observer.Observable):
	def __init__(self, house):
		super().__init__()

		self.setObser(house)

		# set attack damage range
		self.attval = random.uniform(10, 20)

		# set health
		self.health = random.uniform(100, 125)
		self.weapons = []
		wepNames = list(Weapon.weapons.keys())

		# Generate 10 random weapons
		for i in range(10):
			wName = wepNames[random.randrange(0, len(wepNames))]
			self.weapons.append((wName, Weapon.weapons[wName]["uses"]))

	# Called when a monster attacks us
	def getHit(self, damage):
		self.health = self.health - damage

		# If we die, let the world know
		if self.health <= 0:
			self.show()

	# Used for the 'I' command
	def listInventory(self):
		print("Attack:", self.attval, "\tHealth:", self.health)
		for (w, u) in self.weapons:
			print(w, "(with", "infinite" if u == -1 else u, "uses left)")
