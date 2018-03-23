import Monster

# Represents a person. Technically this could go in Monsters.py
class Person(Monster.Monster):
	def __init__(self, house):
		super().__init__(house)

		self.attrange = (-1, -1)
		self.health = 100
		self.vuln = {}
		self.label = "Person"

	# Completely invulnerable
	def getHit(self, damage, weapon):
		return 0

