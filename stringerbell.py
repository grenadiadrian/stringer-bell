from sys import exit
from random import randint
import webbrowser
new = 2
url = "http://i.imgur.com/C70LMTN.gif"
url2 = "https://youtu.be/TJI5EBxdP6k?t=1m4s"
url3 = "https://www.youtube.com/watch?v=-mPKV6-Zwlc"
url4 = "https://youtu.be/3-Rzb6fpwBc?t=14s"
url5 = "https://www.youtube.com/watch?v=hFeEALBfXUY"
url6 = "https://youtu.be/m5Pb8MHIy2s?t=54s"
url7 = "https://youtu.be/sR7uE4nSbas"
url8 = "https://youtu.be/7dY6noZ2BCk"
url9 = "https://youtu.be/nyPHJZ77VRA"

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True and current_scene is not None:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class GameOver(Scene):

	quips = [
		"Wow, you're horrible at this. You HAVE watched the show, right?",
		"Yeah, you suck. Adjourn your ass and watch more 'Wire'.",
		"I hope Omar caresses you in your sleep. You SUCK! Watch more 'Wire'!",
		"Your wackness is on proud display. WATCH THE SHOW and start over!"
		"I should have Prez pistol whip you...watch the show again and come back\nwhen you actually know what the fuck you're doing."
	]

	def enter(self):
		print GameOver.quips[randint(0, len(self.quips)-1)]
		exit(1)

class FuneralHome(Scene):

	def enter(self):
		print "You are Stringer Bell, now in charge of the Barksdale Empire while Avon does"
		print "his bid in Jessup. While in charge, your main connect for the"
		print "product believes Avon's sentence was 'too light' and now you're"
		print "having to find a new connect. Also, D\'Angelo, who is carrying"
		print "the weight of a 20-year bid, seems to be distancing himself from"
		print "Avon, Donette, and his mom. You know this could be trouble..."
		print "Time for you to make some moves!"
		print "Type 'Product' to continue..."

		choice = raw_input("> ")

		if choice == "Product":
			print "Welp, your previous connect now believes Avon is a snitch."
			print "Saw that he only got 7 years for a massive drug conspiracy case"
			print "and is now shutting you out. What you gon' do?\n"
			print "1. Put your business acumen to use and find a connect yourself."
			print "2. Finish up your BCCC degree and get out the game."
			print "3. Suggest to Avon that they should buy from Proposition Joe."

		decision = raw_input("> ")

		if decision == "1":
			return 'game_over'
		elif decision == "2":
			return 'game_over'
		elif decision == "3":
			print "Bold idea, but there's something (read: someone) you need to take care of"
			print "first. Type 'D\'Angelo' to proceed...you heartless bastard."
		else:
			print "That's not a choice, DUMBASS!"
			return 'funeral_home'

		dangelo = raw_input("> ")

		print "D\'Angelo has been out of pocket. He won\'t listen to Avon, nor Donette."
		print "You already had a brief altercation with him in Jersey when he got stopped"
		print "bringing back a key of dope. You know he can't be trusted. What would Stringer"
		print "do in this situation?\n"
		print "1. Reach out to someone in D.C."
		print "2. Convince Avon that he needs to take out his nephew to protect the Empire."
		print "3. Convince Wee Bey to take out D\'Angelo without Avon\'s knowledge."

		decision = raw_input("> ")

		if decision == "1":
			print "Wow, you've got SOME reach there, String! Ya man has a cousin in there."
			print "Seriously, he's damn good. See for yourself..."
			webbrowser.open(url2, new=new)
			return 'jessup'
		elif decision == "2":
			return 'game_over'
		elif decision == "3":
			return 'game_over'
		else:
			print "Really? You have 3 options...stop being a DUMBASS and start over!"
			return 'funeral_home'


class Jessup(Scene):

	def enter(self):
		print "You sinister genius! You\'ve eliminated D\'Angelo without Avon knowing it was you."
		print "The prison is taking it as a suicide AND you\'re piping his baby mama. Hooray!!!!"
		print "Now, at D\'s funeral, Prop Joe approaches you about your current plight with having" 
		print "shitty dope and prime real estate.\nHe's got that raw, but needs more territory to slang it."
		print "Now that D is out of the mix, time to revisit your earlier decision with Avon about\n Prop Joe\'s..."
		print "Proposition.\n"
		print "Press RETURN to continue."

		raw_input("> ")
		print "So you told Avon about Prop Joe\'s offer. Safe to say he was none too pleased..."
		print "Press RETURN to see Avon\'s reaction."

		raw_input("> ")
		webbrowser.open(url, new=new)

		print "Knowing his contempt for Joe, and knowing the fact that y\'all have been"
		print "selling dogshit up in them towers, you now have to face respecting loyalty"
		print "or respecting the almighty dollar. What\'s your play, String?\n"
		print "1. Loyalty"
		print "2. Money"

		decision = raw_input("> ")

		if decision == "1":
			print "You\'re a loyal friend, String. You told Prop Joe the offer is declined and"
			print "you and Avon are brothers for life!!!!"
			print "However, your product fucking sucks, the fiends went East and the Empire is dead. Way to go, loser."
			return 'finished'
		elif decision == "2":
			print "Wow, willing to backdoor your boy to make this happen."
			print "Time to see the fat man and strike a partnership...behind Avon's back."
			return 'prop_joe'

class PropJoe(Scene):

	def enter(self):
		print "FANTASTIC! The towers are flooded with high quality dope! Way to go!"
		print "But, you KNOW there's a catch. You gave up 3 of the towers AND"
		print "you lied to Avon stating that you didn't have enough muscle to"
		print "hold down the towers. So Avon reached out to NY and brought to"
		print "Baltimore, Brother Mouzone. Oops. Press RETURN to see what you did."

		raw_input("> ")
		webbrowser.open(url3, new=new)

		print "Oh, Stringer...you THOUGHT you had time before Mouzone arrived. Alas..."
		print "Press RETURN to proceed"

		raw_input("> ")
		webbrowser.open(url4, new=new)

		print "This is a MAJOR problem. With Brother Mouzone firmly entrenched in the towers"
		print "running those East Baltimore gentlemen off, you're now faced with a dilemma."
		print "What's your play, String?\n"
		print "1. Go speak to Mouzone yourself and explain the situation."
		print "2. Devise a genius plan to put Omar on Mouzone."
		print "3. Stay loyal to Avon and let Mouzone do his thing."

		decision = raw_input("> ")

		if decision == "1":
			print "*smh*"
			return 'game_over'
		elif decision == "2":
			print "YOU sir are going to great lengths to make sure your vision of"
			print "reforming the drug game comes true. Already feeling yourself after"
			print "the successful hit on D\'Angelo, you\'re now setting your sights on"
			print "tricking your local town enemy into believing Brother Mouzone was"
			print "responsible for what happened to Omar\'s lover Brandon. Wow,"
			print "you are ONE DEVIOUS MU'FUCKA!"
			return 'butchies'
		elif decision == "3":
			print "Gave up that easily? Wow..."
			return 'game_over'
		else:
			print "Um, WHAT!?"
			return 'prop_joe'

class Butchies(Scene):

	def enter(self):
		print "Proposition Joe has spoken to Butchie about you wanting to 'clarify' what"
		print "happened to Brandon to Omar and, reluctantly, he\'s agreed to set it up."
		print "Time to have a sitdown with Mr. Omar Little. Press RETURN to proceed.\n"

		raw_input("> ")
		webbrowser.open(url5, new=new)

		print "So now you\'ve succeeded in convincing Omar to hit Mouzone."
		print "Your problem is solved right?"
		print "1. Yep!"
		print "2. Nope!"

		solved = raw_input("> ")

		if solved == "1":
			return 'game_over'
		if solved == "2":
			print "Too easy right? Seems that Omar decided to have a lil chat with"
			print "Brother Mouzone before he felt the need to finish him."
			print "Press RETURN to proceed."

		raw_input("> ")
		webbrowser.open(url6, new=new)
		return 'hospital'

class Hospital(Scene):

	def enter(self):
		print "So THAT didn't work. Brother Mouzone is laid up in a hospital bed after"
		print "taking a bullet from Omar. Why isn't he dead though? Obviously,"
		print "you decide to make a trip to the hospital to find out because you\'re"
		print "'concerned'. Press RETURN to proceed."

		raw_input("> ")
		webbrowser.open(url7, new=new)

		print "Well THAT wasn\'t the smartest thing to do. And now, Mouzone is looking"
		print "at you sideways for asking him who came at him. Time to go let Avon know"
		print "what went down."

		return 'jessup2'

class Jessup2(Scene):

	def enter(self):
		print "You\'re back at Jessup to let Avon know what happened to Brother Mouzone."
		print "I\'m sure he\'ll be in a great mood..."
		print "Press RETURN to proceed."

		raw_input("> ")
		webbrowser.open(url8, new=new)

		print "Bruh, safe to say having that much power went to your head a lil bit."
		print "While you succeeded in having D\'Angelo killed and you were able to"
		print "flex your business skills in getting Prop Joe\'s product in the towers,"
		print "you\'ve now created issues with Avon (his disappointment with you"
		print "was obvious during your last conversation with him), and oh yeah,"
		print "Omar has his sights set on you too... Press RETURN to proceed."

		raw_input("> ")
		webbrowser.open(url9, new=new)

		print "So with Avon coming home soon, and Omar looking for revenge,"
		print "can you hold on to what you\'ve been building since you became"
		print "Interim Boss #1???????"

class FuneralHome2(Scene):

	def enter(self):
		print "It's a new day in Baltimore. "
		
		return 'finished'



class Map(object):

	scenes = {
		'funeral_home': FuneralHome(),
		'jessup': Jessup(),
		'prop_joe': PropJoe(),
		'butchies': Butchies(),
		'hospital': Hospital(),
		'jessup2': Jessup2(),
		'funeral_home2': FuneralHome2(),
		'game_over': GameOver()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('funeral_home')
a_game = Engine(a_map)
a_game.play()