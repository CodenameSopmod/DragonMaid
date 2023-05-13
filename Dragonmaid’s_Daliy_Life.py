from adventurelib import *
import time as t

print("-DragonMaid's DailyLife-")
print("ver 1.0.0")



in_story = Room("you are in this fantasy world. You can enjoy a more eventful adventure than anyone else in this world and finding the secrets of the world, but on the contrary, you can also build trust with the people around you and enjoy a small daily life with your 'master'. Because the choice is yours.")

mansion = Room("This old mansion is where you first wake up on this world. Although it is small and old, the well-organized traces of the years make you feel somewhat familiar.")

garden = Room("This is a small garden attached to the front yard of an old mansion. Colorful wild flowers embroidered like stars flowing through green leaves heal the viewer. However, it seems that it needs maintenance and repairs in some parts of it.")

stairs = Room("A staircase with art and a corridor with landscape paintings. There's a lot of dust. If you're a good maid, you have to get rid of it, right?")

second_floor = Room("there's a room with some odds and ends. looks nothing special.")

master_room =Room("It looks like the room where the owner of this mansion lived. The door is tightly locked, and even the barrier is set. It seems that no one is inside.")
	
	
Room.can_start_story = False
in_story.can_start_story = True
	
	
in_story.north = mansion
mansion.east = stairs
mansion.west = garden
stairs.east = second_floor
second_floor.south = master_room


current_room = in_story

apple = Item("apples")
apple.def_name = "apples"
fruit_kinfe = Item("fruit kinfe")
fruit_kinfe.def_name = "fruit kinfe"


def prologue():
	global name
	print("A long time ago...")
	t.sleep(1)
	print("There lived a dragon that had lost its self.")
	t.sleep(2)
	print("The dragon's only memory was of its own name.")
	name=input(">>What's your name?")
	print(">>You can always check your available actions by typing <help>.")



def dialog():
	print(F"when {name} opened her eyes, {name} saw completely unfamiliar ceiling.")
	t.sleep(1.5)
	print(f"and {name} got up & looked around, there was an ornate door painted gold on a white background in front, and an apple and a fruit knife were placed on the table next to the bed.")
	t.sleep(3)
	print(f"then {name} looks her body. it seems {name} was a maid...?")
	print(f">>what should {name} do?")


prologue()


@when('north', direction = 'north')
@when('south', direction = 'south')
@when('east', direction = 'east')
@when('west', direction = 'west')
def go(direction):
	global current_room
	room = current_room.exit(direction)
	if room:
		current_room = room
		print(f'You go {direction}.')
		print(current_room)
	else :
		print("you stopped in front of blocked direction. it seems you can't go here.")

@when("start story")
def start_game():
	if current_room.can_start_story:
		print("Lets begin story,",name)
		dialog()
	else:
		print(">>you cannot start story now. maybe you are already in it?")


import adventurelib as adv
import random
def no_matches(command):
    print(random.choice([
        f"It didn't take long before {name} realized something was wrong.",
        f"Realizing that {name} was about to do something strange, She stopped.",
        f"what the hell was {name} doing?"
    ]))

adv.no_command_matches = no_matches


adv.start()
