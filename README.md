# Zeaurk

Project 4 for CIS 343. Simple (but very difficult) text-based game with fake weapons and real monsters.

## Usage

Run Zork.py, either by python or as a shell script. Enter a house, kill everything, and move to the next house. Emptying all of the houses wins!

## Notes
Just a couple of things
### Shortcomings (Possible improvements)
* The layout is sort of not a grid. The neighborhood is laid out linearly. In order to make it seem more acceptable, I've decided that the neighborhood is a square, but the houses are numbered and traversed by a [Hilbert Curve](https://en.wikipedia.org/wiki/Hilbert_curve).
* There is no way for the user to check:
  * Number of monsters remaining
  * Number of houses not cleared yet
  * Types of monsters in a house
* The weapon randomizer may give you multiple HersheyKisses, even though one has infinite uses
* The attack option enumerator gives options to use any one of your weapons, even if there are multiple of the same weapon
* Commands *are* case sensitive
* Because of the way the observer pattern works (or possibly my interpretation of its use here), we can't print out any information between attacking and either winning or losing (e.g. damage dealt or taken)
* Basically all of the monster types differ only by their properties (not by their functionality). I think this is a good sign that this is a bad place to use an OOP-design this deep, but it *does* provide a way to add special functionality to any new monster types added
* It's really hard. I didn't think it was fair to be able to attack every monster while only being attacked by one, so I made sqrt(num_npcs_in_house) monsters attack during the NPC attack phase. I was able to beat one house after a few tries (when I was testing the win conditions), but it's not easy. Plus, you use up weapons and there is no way to get more. I think it might be impossible to win
