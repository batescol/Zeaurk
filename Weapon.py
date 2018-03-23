# Simple dict of weapon properties.
# 	mod is a range for the multiplier of damage
#	uses is the number of uses the weapon has 
# before it is removed. (-1 represents infinite uses)
weapons = {"HersheyKiss": {
			"mod": (1, 1),
			"uses": -1
		}, "SourStraw": {
			"mod": (1, 1.75),
			"uses": 2
		}, "ChocolateBar": {
			"mod": (2, 2.4),
			"uses": 4
		}, "NerdBomb": {
			"mod": (3.5, 5),
			"uses": 1
		}
}