from adventurelib import *


def setrooms():
	in_story = Room("you are in this fantasy world. You can enjoy a more eventful adventure than anyone else in this world and finding the secrets of the world, but on the contrary, you can also build trust with the people around you and enjoy a small daily life with your 'master'. Because the choice is yours.")

	mansion = Room("This old mansion is where you first wake up on this world. Although it is small and old, the well-organized traces of the years make you feel somewhat familiar.")

	garden = Room("This is a small garden attached to the front yard of an old mansion. Colorful wild flowers embroidered like stars flowing through green leaves heal the viewer. However, it seems that it needs maintenance and repairs in some parts of it.")

	stairs = Room("A staircase with art and a corridor with landscape paintings. There's a lot of dust. If you're a good maid, you have to get rid of it, right?")

	second_floor = Room("there's a room and some odds and ends. looks nothing special.")

	master_room =Room("It looks like the room where the owner of this mansion lived. The door is tightly locked, and even the barrier is set. It seems that no one is inside.")
	
	
	Room.can_start_story = False
	in_story.can_start_story = True
	current_room = in_story
	
	
	in_story.north = mansion
	mansion.east = stairs
	mansion.west = garden
	stairs.east = second_floor
	second_floor.south = master_room
	
	