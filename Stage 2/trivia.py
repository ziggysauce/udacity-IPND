'''
Author: Daniel Nguyen
Udacity: Intro To Programming
Class 3: Code Your Own Quiz
Project: Fill-in-the-Blanks Quiz (Trivia Game)
'''

#Prompt user for answers
blanks = ["\n__1__ = ","\n__2__ = ","\n__3__ = ","\n__4__ = ","\n__5__ = ",]
placeholder = ["__1__", "__2__", "__3__", "__4__", "__5__", ]
newlist = []

#Trivia text for each category and difficulty level
#Implemented dictionary to store text for each round
trivia1 = {0:"\nFirst Round:\nTo you young science knowledge seekers, here are some random facts to help you gain breadth for your intellect. The planet __1__ is closest to the Sun and the smallest planet in our solar system. The diatomic element __2__ is what humans breathe in order to survive. In an ecosystem, an __3__ is an organism that only consumes plants. DNA, or deoxyribonucleicacid, is made up of four different nucleotides: adenine, thymine, cytosine, and __4__. The __5__ is a biome described as the coldest, with little biotic diversity and short growing seasons.",
1:"\nRound 2:\nTo you young sports knowledge seekers, here are some random facts to help you gain breadth for your intellect. The 2008 Summer Olympics was hosted in __1__ where swimmer Michael Phelps won a gold medal in all of his events. Though Spanish, Rafael Nadal is the all-time leading winner of the __2__ Open in men's singles. The sport __3__ is considered America's pastime. Though __4__ didn't make the varsity squad for his high school basketball team sophomore year, he went on to become one of the greatest basketball players of all time. As of 2017, Tom Brady has the most __5__ wins as a quarterback.",
2:"\nRound 3:\nTo you young superhero knowledge seekers, here are some random facts to help you gain breadth for your intellect. Clark Kent, also known as __1__ , was raised in Smallville, Kansas. Gotham City harbors the vigilante __2__ who is sometimes referred to as the Dark Knight. While DC Comics is a major comic book publisher with several famous heroes, one incredibly popular superhero, Spiderman, is part of __3__ Comics. The most recent DC Comics film to receive high praise for a female hero was __4__  Woman, played brilliantly by Gal Gadot. Disney created the __5__ which is a whole family of superheroes who fight crime.",
3:"\nFinal Round:\nTo you young singer/song knowledge seekers, here are some random facts to help you gain breadth for your intellect. The singer Beyonce is married to famous hip hop artist __1__ Z. Taylor Swift made a huge statement in the music industry with the release of her album __2__ being her first pop genre album after switching from country music that she was known for. Michael Jackson created the hit song '__3__' most noted for it's music video featuring zombies. In 2009, __4__ released his first album after being discovered on youtube by Usher. In 1998, singer __5__ became famous with her hit single '...Baby One More Time'."}

trivia2 = {0:"\nFirst Round:\nTo you experienced science knowledge seekers, here are some random facts to help you gain breadth for your intellect. The __1__ is the largest human organ. Scientists refer to __2__ as a degree of disorder or randomness in a system. When a thunderstorm occurs, the sky is full of __3__ clouds. A __4__ is a single- or multi-cellular oganism whose cells contain a nucleus enclosing the organism's genetic material. The phospholipid bilayer consists of many phospholipids that have a phosphate head and a __5__ lipid tail consisting of two fatty acid chains.",
1:"\nRound 2:\nTo you experienced sports knowledge seekers, here are some random facts to help you gain breadth for your intellect.In 1930, __1__ was the first country to win the World Cup. As of 2016, Floyd __2__ Jr. currently has an undefeated boxing record. Pele is one of the most prolific __3__ goalscorers it soccer history. Usain Bolt stunned the world in the 2008 Summer Olympic Games when he ran the __4__ meter dash in under 10 seconds, setting a new world record. The team with the most Stanley Cup wins of all time are the __5__.",
2:"\nRound 3:\nTo you experienced superhero knowledge seekers, here are some random facts to help you gain breadth for your intellect. Lex Luthor uses __1__ to weaken and almost kill Superman in several adaptations of their stories. Batman's arch nemesis is the __2__. The __3__ is one of the most famous X-Men because of his ability to repair his body and survive longer lengths of time than most other heroes. Comic-book writer __4__ Lee has appeared in several Marvel films as a cameo appearance. Batman's sidekick __5__ is the leader of the Teen Titans.",
3:"\nFinal Round:\nTo you experienced singer/song knowledge seekers, here are some random facts to help you gain breadth for your intellect. The song 'Carry on my __1__ Son' made famous by Kansas is featured in Guitar Hero. The movie __2__ features one of Celine Dion's famous hits 'My Heart Will Go On'. The track 'Hey Jude' is one of the most popular songs made famous by the __3__. The popular 90's boy band Backstreet Boys released their album __4__ in 1995 which received high praise by the public. Elvis Presley became known as the __5__ of Rock n' Roll before dying due to a drug overdose at age 42."}


trivia3 = {0:"\nFirst Round:\nTo you expert science knowledge seekers, here are some random facts to help you gain breadth for your intellect. The __1__ is the smallest bone found in the human body. The Raphus cucullatus is the scientific name for a __2__ which is an extinct flightless bird. An __3__ collision describes two objects that collide and do not separate from one another. Physical anthropologists have declared Lucy within the genus __4__ after numerous years of research on her fossil remains. When sea otters consume sea urchins, which in turn results in an increase of kelp forests, this is known as a top-down __5__ effect.",
1:"\nRound 2:\nTo you expert sports knowledge seekers, here are some random facts to help you gain breadth for your intellect. The oldest college football program began at __1__ University. The first World Athletics Championship was held in __2__. Pete Sampras was seeded 12 when he won his first __3__ Open. In 1954, __4__ Bannister was the first runner to officially break the four-minute mile with a time of 3:59.4. Tiger Woods was named Sports Illustrated __5__ of the Year in 1996",
2:"\nRound 3:\nTo you expert superhero knowledge seekers, here are some random facts to help you gain breadth for your intellect. The Green Arrow, also known as Oliver Queen, is the vigilante protector of __1__ City. The New York City antagonist __2__ goes by the name of Wilson Fisk and rivals Daredevil and Spiderman in several stories. The __3__ Realm is home to King Odin and his warriors. Odin's son wields an all-powerful hammer that is named __4__ and has magical properties accessed only by it's master. Raphael uses the Twin __5__ as his weapon of choice to defeat enemies.",
3:"\nFinal Round:\nTo you expert singer/song knowledge seekers, here are some random facts to help you gain breadth for your intellect. Disney's animated film Frozen features a girl named Elsa who is voiced by singer __1__ Menzel, also famous for her work on Broadway. Famous rapper __2__ died in 1996 and was believed to be a victim of a drive-by shooting. Artist __3__ suffered a tragic death in 2001 during the 911 terrorist plane hijack attacks. Ray Charles is a famous musician known mostly for playing the __4__ as a blind individual. In 2014, Calvin Harris became the first electric music artist to perform at __5__."}

#Trivia answers
#Implemented dictionary to store answers for each round
answers1 = {0:['Mercury','oxygen','herbivore','guanine','tundra'],
1:['Beijing','French','baseball','Michael Jordan','Super Bowl'],
2:['Superman','Batman','Marvel','Wonder','Incredibles'],
3:['Jay','1989','Thriller','Justin Bieber','Britney Spears']}

answers2 = {0:['skin','entropy','cumulonimbus','eukaryote','hydrophobic'],
1:['Uruguay','Mayweather','Brazilian','100','Montreal Canadiens'],
2:['kryptonite','Joker','Wolverine','Stan','Robin'],
3:['Wayward','Titanic','Beatles','Millennium','King']}

answers3 = {0:['stapes','dodo','inelastic','Australopithecus','cascade'],
1:['Rutgers','Helsinki','US','Roger','Sportsman'],
2:['Star','Kingpin','Asgard','Mjolnir','Sai'],
3:['Idina','Tupac','Aaliyah','piano','Coachella']}

def win(points):
    """
    Completion of Game
    Show point total and description based on points accumulated
    """
    print "\nCongratulations " + username + "! You scored " + str(points) + " points."
    if points > 90:
        print "You're a trivia God!\n"
    elif points > 80:
        print "You've played a lot of Sporcle.\n"
    elif points > 40:
        print "Looks like you're the local bar's weekly trivia player\n"
    elif points > 0:
        print "You won, but just barely.\n"
    else:
        print "Unfortunately however, that means you simply got through it.\n"

def pointscale(section,cycle,points,tries,guess,trivia,answers):
    """
    Points generator
    Inputs points from question
    Outputs total points
    """
    if tries == 0:
        points = points + 5
        print "Total points: " + str(points)
    elif tries == 1:
        points = points + 4
        print "Total points: " + str(points)
    elif tries == 2:
        points = points + 3
        print "Total points: " + str(points)
    elif tries == 3:
        points = points + 2
        print "Total points: " + str(points)
    elif tries == 4:
        points = points + 1
        print "Total points: " + str(points)
    tries = 0
    return begin(section,cycle,points,tries,guess,trivia,answers)

def correct(section,cycle,points,tries,guess,trivia,answers):
    """
    Correct Answer
    Inputs guess
    Outputs correct answer into trivia text
    """
    newlist.append(guess)
    print "Correct"
    trivia[section] = trivia[section].replace(placeholder[cycle], guess)
    cycle = cycle + 1
    return pointscale(section,cycle,points,tries,guess,trivia,answers)

def incorrect(section,cycle,points,tries,guess,trivia,answers):
    """
    Incorrect Answer
    Inputs guess
    Outputs correct answer after 5 tries
    """
    print "Sorry, '" + guess + "' was incorrect."
    tries = tries + 1
    if tries == len(blanks):
        print "You've ran out of attempts!"
        print "The correct answer was '" + answers[section][cycle] + "'"
        trivia[section] = trivia[section].replace(placeholder[cycle], answers[section][cycle])
        cycle = cycle + 1
        if cycle == len(blanks):
            section = section + 1
            if section == len(trivia):
                return win(points)
            cycle = 0
            return pointscale(section,cycle,points,tries,guess,trivia,answers)
        else:
            return pointscale(section,cycle,points,tries,guess,trivia,answers)
    else:
        return begin(section,cycle,points,tries,guess,trivia,answers)

def begin(section,cycle,points,tries,guess,trivia,answers):
    """
    Start game with selected difficulty
    """
    if cycle == len(blanks):
        section = section + 1
        if section == len(trivia):
            return win(points)
        cycle = 0
    while section < len(trivia):
        while cycle < len(placeholder):
            while tries < len(blanks):
                print trivia[section]
                print "Attempt: " + str(tries + 1)
                guess = raw_input(blanks[cycle])
                if guess.lower() == answers[section][cycle].lower():
                    return correct(section,cycle,points,tries,guess,trivia,answers)
                else:
                    return incorrect(section,cycle,points,tries,guess,trivia,answers)

def start(diff):
    """
    Select difficulty
    """
    section, cycle, points, tries, guess = 0,0,0,0,0
    if diff == "novice":
        trivia, answers = trivia1, answers1
        return begin(section,cycle,points,tries,guess,trivia,answers)
    elif diff == "master":
        trivia, answers = trivia2, answers2
        return begin(section,cycle,points,tries,guess,trivia,answers)
    elif diff == "legend":
        trivia, answers = trivia3, answers3
        return begin(section,cycle,points,tries,guess,trivia,answers)

def intro():
    """
    Provide instructions for user
    """
    print "\nYou will have 5 attempts to guess the correct word(s) for each fill-in-the-blank.\nGetting the correct answer with fewer attempts rewards you with a higher point value per the following:\n1st Attempt = 5 points\n2nd Attempt = 4 points\n3rd Attempt = 3 points\n4th Attempt = 2 points\n5th Attempt = 1 point\nIncorrect   = 0 points\n"
    return start(diff)

#Prompt user for name
username = raw_input("What is your name? ")
print "\nHello " + username + ", welcome to Trivia Bonanza!"

#Prompt user for difficulty level until proper input selected
while True:
    difficulty = raw_input("Which stage of competition would you like to participate in?\n(Please type one of the following):\nNovice  |  Master  |  Legend\n")
    diff = difficulty.lower()
    if diff == "novice" or diff == "master" or diff == "legend":
        print "\nNow entering Trivia Bonanza for the " + diff.title()
        print intro()
        break
    else:
        print "\nSorry your response '" + difficulty + "' is not valid. Please try again."
