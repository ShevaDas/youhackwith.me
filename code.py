#!/usr/bin/env python
# coding: utf-8

import web
import random
render = web.template.render('templates/')

urls = (
  '/', 'index',
  '/credits', 'Credits'
)

tech = ["iOS", "Android", "Windows phone", "Xbox", "Kinect", "Playstation", "Wii U", "Arduino", "Oculus Rift", "Angular.js", "Backbone.js", "Node.js", "Javascript", "Python", "Pebble", "Apple Watch", "Facebook", "Ruby on Rails", "Mac", "Windows", "Linux", "command line", "HTML5/CSS3", "Lego Mindstorm", "assembly language", "Visual Basic", "Brainf*ck", "COBOL", "Fortran", "LISP", "Turing complete", "chatbot", "useless", "crappy", "awesome", "server-side", "client-side", "Java", "esoteric", "barely functional", "Raspberry Pi"]
action1 = ["ordered a pizza", "called my mom", "texted my math teacher", "wrote an epic novel", "composed an ode", "punched a kitten", "baked a pie", "turned off all the lights", "reinvented the wheel", "parsed the entire internet", "took over the world", "wrote a fanfic", "bought me a beer", "rewrote itself in Haskell", "swore profusely", "made 2000 consecutive API calls", "brought about the robot revolution", "sent Obama one of my selfies", "broke all of Asimov's Laws", "freed us from this dream world", "took me back to the future", "showed me how deep the rabbit-hole goes", "summoned an ancient god", "spoiled Breaking Bad", "started a cold fusion reaction", "electrocuted my user", "created a new paradigm", "hacked the NSA", "spewed business jargon", "deleted all my files", "crashed my computer","disrupted an industry","built another app", "passed the Turing test", "went into an endless loop", "failed horribly"]
event = ["the clock struck midnight", "my phone rang", "I fell asleep", "I woke up", "my mom called", "Opening Ceremonies began", "Opening Ceremonies ended", "the hackathon ended", "my teammate sneezed", "someone farted", "lunch was served", "someone divided by 0", "the hackathon venue changed", "we were demoing the app", "I made a new Tweet", "I ate too many cookies", "drank too much Red Bull", "my bus broke down"]
stuff = ["the ordr.in API", "my Unhackathon t-shirt", "some free food", "a can of Red Bull", "my pillow", "my laptop", "someone else's laptop", "my brain", "a soldering iron", "fabric paint", "a Cosi napkin", "my swag", "a board game", "an off-brand tablet", "a Linux server", "a Windows 95 machine", "the power of the gods", "an unholy combination of caffeine and pure sugar", "my nerd skills", "computing know-how", "my love for obscure trivia", "my extensive video game collection", "entirely too much technology", "the iPhone 6 Plus"]
action2 = ["asked a mentor for help", "curled up in a ball and cried", "fell asleep", "ate a snack", "saved the world", "started from scratch", "copy/pasted from StackOverflow", "drank more Red Bull", "bought a gyro", "learned how to pronounce \"gyro\"", "started a liveblog", "took a selfie", "went home early", "fixed all the bugs", "broke everything", "implemented Unicode support", "added support for IE6", "played some board games", "pirated Photoshop", "panicked", "used simple math", "wrote a do-while loop", "found a new venue for the hackathon", "stayed awake for 72 hours straight", "embraced the void", "discovered the answer to life, the universe, and everything", "discovered the question to the answer of life, the universe, and everything", "made an obscure reference", "rebooted my server", "changed my business model entirely"]
denouement = ["made a new friend", "saved the day", "was given a big hug", "became a legend", "got a job offer", "got kicked out of the hackathon", "won the hackathon", "tripped over my own shoelace", "built the best app ever", "built the worst app ever", "had an awesome time", "nearly died", "learned a new skill", "finally went to bed", "discovered coding wasn't right for me", "went out in a blaze of glory", "got my travel reimbursement", "discovered that friendship is magic"]
aesop = ["Hackathons are hard.", "I love hackathons.", "Technology is fun.", "Use your powers for good.", "What am I doing with my life?", "It’s only Saturday night.", "It's not even Saturday night!", "And it will all happen again next year.", "Sarcasm is hard.", "This may or may not have happened.", "High-five your superiors at your own peril.", "Smashburger is good.", "I'm definitely coming back next year.", "I'm definitely not coming back next year."]

def random_tech():
   rtech = random.choice(tech)
   # vowels, yo
   if rtech[:1].lower() in ("a", "e", "i", "o", "u", "h", "x") and rtech != "useless":
     rtech = "an " + rtech
   else:
     rtech = "a " + rtech
   return rtech

def random_phrase(phrase_list):
  rphrase = random.choice(phrase_list)
  return rphrase

def is_aesop():
  chance = random.randint(1,10)
  if chance == 1 or chance == 10:
    return random_phrase(aesop)

class index:
    def GET(self):
        rtech = random_tech()
	raction1 = random_phrase(action1)
	revent = random_phrase(event)
	rstuff = random_phrase(stuff)
	raction2 = random_phrase(action2)
	rdenouement = random_phrase(denouement)
	raesop = is_aesop()
	return render.index(rtech, raction1, revent, rstuff, raction2, rdenouement, raesop)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 
