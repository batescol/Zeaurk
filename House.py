import math
import random
import Observer
import Person
import Weapon
import Player
import Monsters

# Represents a house full of monsters
class House(Observer.Observable,Observer.Observer):

	# Helper to get a random value in a range tuple
	def __rr(self, t):
		return random.uniform(t[0], t[1])

	def __init__(self, world):
		super().__init__()

		random.seed()

		self.world = world
		self.monsters = []
		self.moncount = 0;	# Current monster count
		self.omoncount = 0;	# Original monster count

		# Make sure the world gets updates
		self.setObser(world)

	# Adds a monster to the house and updates counts to match
	def addMonster(self, monster):
		self.monsters.append(monster)
		if not isinstance(monster, Person.Person):
			self.moncount = self.moncount + 1
		pass

	# randomly generate 10 monsters (weighted distribution) and add to house
	def genMonsters(self):
		total = 0
		monl = random.choices("PZVGW", weights=[3, 5, 5, 5, 2], k=10)
		for m in monl:
			if m == "P":
				self.addMonster(Person.Person(self))
				total = total - 1 # Because persons aren't monsters
			elif m == "Z":
				self.addMonster(Monsters.Zombie(self))
			elif m == "V":
				self.addMonster(Monsters.Vampire(self))
			elif m == "G":
				self.addMonster(Monsters.Ghoul(self))
			elif m =="W":
				self.addMonster(Monsters.Werewolf(self))
			total = total + 1

		# update original monster count
		self.omoncount = self.moncount

		return total

	# Called by the world when the monsters get to attack.
	# The number of monsters that get to attack is proportional
	# to the square root of the number of NPCs in the house,
	# and this includes the Persons' "attack" of -1
	def attackTick(self, player):
		tdmg = 0
		numAttack = round(math.sqrt(len(self.monsters)))
		for monster in random.sample(self.monsters, numAttack):
			tdmg = tdmg + monster.attack(player)
		return tdmg

	# Called by the world when the player attacks.
	# Damage is applied to all monsters in the house
	# at once, but may be scaled differently for each
	def playerAttack(self, attrange, weapon):
		tdmg = 0
		for monster in self.monsters[:]:
			dmg = attrange
			if weapon != "Fists":
				dmg = dmg * self.__rr(Weapon.weapons[weapon]["mod"])

			tdmg = tdmg + monster.getHit(dmg, weapon)
		return tdmg

	# Called by the monsters, only when they die
	def look(self, obj):
		if obj.health <= 0:
			print(obj.label, "died")

			# Replace monster with a Person
			self.monsters.remove(obj)
			self.addMonster(Person.Person(self))

			self.moncount = self.moncount - 1

			# let the world know
			if self.moncount <= 0:
				self.show()

	