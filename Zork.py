import Observer
import House
import Player
import Person
import Monster
import Monsters

# 
class World(Observer.Observer):
	def __init__(self):
		self.houses = []
		self.moncount = 0

		# Generate 16 houses and generate their monsters
		for i in range(16):
			nhouse = House.House(self)
			self.moncount = self.moncount + nhouse.genMonsters()
			self.houses.append(nhouse)

		self.player = Player.Player(self)

		# Position of the player. When this is negative, 
		# the player is outside of the house; positive, 
		# inside the house. Because -0 == +0, this is 1-indexed
		self.pos = -1

	# Handles input from the user depending on the state
	def doInput(self):
		if self.pos < 0: # Outside of the house
			print("You are now outside house number", -self.pos)
			cmd = input("\t>")
			if cmd[0] == "?":
				print("Valid inputs:")
				print("Q\tQuit Zork")
				print("I\tList inventory")
				print("E\tEnter house", -self.pos)
				if -self.pos < len(self.houses):
					print("N\tGo to the next house")
				if -self.pos > 1:
					print("P\tGo to the previous house")
				self.doInput()
			elif cmd[0] == "E":
				self.pos = -self.pos
			elif cmd[0] == "N" and -self.pos < len(self.houses):
				self.pos = self.pos - 1
			elif cmd[0] == "P" and -self.pos > 1:
				self.pos = self.pos + 1
			else:
				self.commonInput(cmd[0])
		else: # Inside the house
			print("You are now inside house number", self.pos)
			print("There are", self.houses[self.pos-1].moncount, "Monsters inside")
			cmd = input("\t>")
			if cmd[0] == "?":
				print("Valid inputs:")
				print("Q\tQuit Zork")
				print("I\tList inventory")
				print("E\tExit house", self.pos)
				print("A\tAttack with your fists")

				# Enumerate commands for all of the weapons the player has
				for i in range(len(self.player.weapons)):
					print(i, "\tAttack with", self.player.weapons[i][0])
				self.doInput()
			elif cmd[0] == "E":
				self.pos = -self.pos
			else:
				self.attackInput(cmd[0])

	# Handles inputs that are attack commands
	def attackInput(self, istr):
		if istr == "A":
			self.attack("Fists")
		elif istr.isdigit():
			widx = ord(istr)-48 # The value of the digit

			# wep is the tuple of weapon name and weapon uses left
			wep = self.player.weapons[widx]

			# Attack with named weapon
			self.attack(wep[0])
			if wep[1] == 1: # No uses left
				self.player.weapons.remove(wep)
			else: # Decrement uses left (unless -1 = infinite) 
				self.player.weapons[widx] = (wep[0], max(wep[1]-1, -1))
		else:
			self.commonInput(istr)

	# Handles inputs that are common across phases
	def commonInput(self, istr):
		if istr == "I":
			self.player.listInventory()
		elif istr == "Q":
			exit()
		else:
			print("Invalid input. Try '?' for help")

		self.doInput()

	# Attacks the monsters in the current house with the named weapon
	def attack(self, wep):
		tdmg = self.houses[self.pos-1].playerAttack(self.player.attval, wep)
		print("You dealt a total of", tdmg, "damage!")

	# Ticks the game. Monsters get the first tick, then the player gets to move.
	# This is so you cannot kill a few monsters and immediately get healed by their
	# new Person counterparts
	def tick(self):
		if self.pos > 0:
			dmg = self.houses[self.pos-1].attackTick(self.player)
			print("You take", dmg, "damage")
		self.doInput()

	# Called by observables when either the player dies, or a house is emptied
	# of monsters
	def look(self, obj):
		if isinstance(obj, Player.Player):
			print("You have died.")
			exit()
		print("You have successfully cleared the house!")

		# Subtract all the monsters that *used* to be in this house
		self.moncount = self.moncount - obj.omoncount

		if self.moncount == 0:
			print("You have killed all of the monsters! Congratulations!!!")
			exit()


# Actual game loop. Very simple.
z = World()
while(True):
	z.tick()
