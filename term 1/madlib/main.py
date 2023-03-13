# Landon Bowcutt
# 9/20/2022
# madlib


# imports


# globals
OGTEXT = """
We wanted to (believe) there was no
No hell on (earth) worse than what we know
But every day just seems to (worsen)
We weren't (prepared) at all
Now we must rise to this (occasion)
Devoid of all (consideration)
When every day's a waking (nightmare)
We're waiting for the fall

(Waging) war with every single passing day
We will march to (victory) no matter what the cost
I could see the fear as it was (plaguing) all our eyes
Let's set aside our (weaknesses) and cross the line
Any way you (break) it down
We've still no answers not yet
These (devils) seem to (massacre) so easily
We'll stand and (fight)
We're never (backing) down

We'll offer up
We'll offer up
We'll (sacrifice)
Until our (hearts) have (stopped)
With our own hands
We'll take a stand
And carve a path
Into our (future)
We'll offer up
We'll offer up
We'll (sacrifice)
Until our (hearts) have (stopped)
With our own hands
We'll take a stand
And live to see another day
"""

OGTEXT2 = """
Are you the food? No we are the hunters!

Crimson Bow and arrow

Not knowing the name of the trampled flower
Birds that have fallen from the sky tire of waiting upon the wind
Prayers won't change anything
Only the resolve to fight can change the present

You pigs who sneer at our will to step over corpses and march onwards
Enjoy the peace of livestock false prosperity "freedom" of the dying wolves that hunger!

The humiliation of entrapment is our cue to counterattack
Beyond the castle walls lies a hunter killing his prey
With a surging killer impulse scorching his body, he pierces the dusk scarlet
With a crimson arrow

Drawing his bow, he takes after his target; he won't let it escape
Releasing his arrow, he closes upon it; he won't let it escape
He bends his bow to its limits, the string on the verge of snapping
He'll release it, time and time again, until his target draws its last breath

What truly kills a prey are not tools nor your skills at using it
But your own sharp killing intent

We are the hunter -> passionate as flames!
We are the hunter -> cold as ice!
We are the hunter -> pour your heart and soul into your arrow!
We are the hunter -> boldly go forth and pierce through everything!

Attack on the Titans.
The boy from back then will soon take up the sword.
Who only laments his powerlessness won't be able to change anything.
The boy from back then will soon take up the black sword.
Hate and rage are a double-edged blade.
Soon, one day, he will bare his fangs against fate.

Ones that could hope to change anything
Are ones who could bear to abandon anything
Without bearing any risk at all, how could you hope to attain anything?

Foolish assumptions they are but mere phantasms right now, we could do with even reckless courage
The advance guards of freedom betting on their offensive
Victory to the charging slaves!

All this absurdity forced upon us are our cue to attack
Deprived of his horizon, Eren yearns for freedom
With relentless killer impulse assailing his body, he carries violet to dusk-
With an arrow from Hades"""

OGTEXT2 = OGTEXT2.replace("hunter","(hunter)")
OGTEXT2 = OGTEXT2.replace("arrow","(arrow)")
OGTEXT2 = OGTEXT2.replace("prey","(prey)")
OGTEXT2 = OGTEXT2.replace("sword","(sword)")
OGTEXT2 = OGTEXT2.replace("escape","(escape)")
OGTEXT2 = OGTEXT2.replace("fangs","(fangs)")
OGTEXT2 = OGTEXT2.replace("kills","(kills)")
OGTEXT2 = OGTEXT2.replace("killing","(killing)")
OGTEXT2 = OGTEXT2.replace("hades","(hades)")
OGTEXT2 = OGTEXT2.replace("killer","(killer)")

OGTEXT3 ="""
I learned the reason to become strong
Take me and go

I feel dizzy by the muddy flashback
Heart tenses, hands shake
That means you have something you want to grab hold of
That's all

The scent of night (I'll spend all thirty nights)
Even if I stare at the sky (Staring into the sky)
The only thing you can change is yourself
That's all

I learned the reason to become strong
Take me and go

Dreams that you can't erase no matter what
An unstoppable "now"
If you can become stronger for someone
Thank you, sadness
I learned why I lost when I was beaten up by the world
Bloom, crimson lotus
Shine the fate

The sound of lightning pierced my ears
Is there anything you can protect just by being nice? I know
Good and evil are entangled in water, divine punishment that can see clear hypocrisy
(Tell me why, tell me why, tell me why, tell me ... I don't need you!)
One flower that continues to struggle for blossom is more beautiful than a gem

Road full of sharp thorns
It will only appear for me who means it
Don't easily get rid of your dreams, even dreams that can't be protected
This red lotus heart is rooted and lives in this blood

Hidden secrets will disappear because they are scattered
A heartbreaking wind scream that tore it apart
A person's laughter and cry
Everyone wants happiness

dreams that you can't erase no matter what
An unstoppable "now"
If you can become stronger for someone
Thank you, sadness
I learned why I lost when I was beaten up by the world
Bloom, crimson lotus
Shine the fate

Shine the fate
"""



# functions


# main

def main():
    text3 = OGTEXT3

    words =["fate ","dreams ","stronger ","strong ","blood ","sadness ","thorns ","Bloom ","lotus ","crimson "]
    i = 0
    for word in words:
        text3 = text3.replace(word,"({"+str(i)+"})")
        i+=1

    vars = []
    for i in range(len(words)):
        x = input("Give me a word to Replace "+words[i])
        vars.append(x)

    text3 = str.format(text3,vars[0],vars[1],vars[2],vars[3],vars[4],vars[5],vars[6],vars[7],vars[8],vars[9])

    print(text3)

    # text2 =OGTEXT2
    #
    # hunter = input("give me a name of a type of person ")
    # arrow = input("give me a noun ")
    # prey = input("give me a noun or a verb ")
    # sword = input("give me a noun ")
    # escape = input("give me a verb ")
    # fangs = input("give me a noun ")
    # kills = input("give me a adjective ")
    # killing = input("give me a verb ")
    # hades = input("give me a me a name ")
    # killer = input("give me a name of a type of person ")
    #
    # text2 = text2.replace("(hunter)",hunter)
    # text2 = text2.replace("(arrow)", arrow)
    # text2 = text2.replace("(prey)", prey)
    # text2 = text2.replace("(sword)", sword)
    # text2 = text2.replace("(escape)", escape)
    # text2 = text2.replace("(fangs)", fangs)
    # text2 = text2.replace("(kills)", kills)
    # text2 = text2.replace("(killing)", killing)
    # text2 = text2.replace("(hades)", hades)
    # text2 = text2.replace("(killer)", killer)


    # believe = input ("i personally ")
    # earth = input ("Give me a name of a planet ")
    # prepared = input ("i am ________ for my flight ")
    # occasion = input ("whats the ")
    # consideration = input ("to put this into ")
    # nightmare = input ("i had a ")
    # waging = input ("we are ______ war ")
    # victory = input ("we have stolen their ")
    # plaguing = input ("the disease is ")
    # weaknesses = input ("show me your ")
    # break1 = input ("how did you _____ the wall ")
    # devils = input ("Give me a creature from the underworld ")
    # massacre = input ("Give me something very bloody ")
    # fight = input ("Give me something violent ")
    # backing = input("i was _______ my car in to the spot ")
    # sacrifice = input ("Give me something nobody want to do ")
    # hearts = input ("Give me a internal body part ")
    # stopped = input ("opposite of go ")
    # future = input ("past present and ")


#     text1= """
# We wanted to ("""+believe+""") there was no
# No hell on ("""+earth+""") worse than what we know
# But every day just seems to (worsen)
# We weren't ("""+prepared+""") at all
# Now we must rise to this ("""+occasion+""")
# Devoid of all ("""+consideration+""")
# When every day's a waking ("""+nightmare+""")
# We're waiting for the fall
#
# ("""+waging+""") war with every single passing day
# We will march to ("""+victory+""") no matter what the cost
# I could see the fear as it was ("""+plaguing+""") all our eyes
# Let's set aside our ("""+weaknesses+""") and cross the line
# Any way you ("""+break1+""") it down
# We've still no answers not yet
# These ("""+devils+""") seem to ("""+massacre+""") so easily
# We'll stand and ("""+fight+""")
# We're never ("""+backing+""") down
#
# We'll offer up
# We'll offer up
# We'll ("""+sacrifice+""")
# Until our ("""+hearts+""") have ("""+stopped+""")
# With our own hands
# We'll take a stand
# And carve a path
# Into our ("""+future+""")
# We'll offer up
# We'll offer up
# We'll ("""+sacrifice+""")
# Until our ("""+hearts+""") have ("""+stopped+""")
# With our own hands
# We'll take a stand
# And live to see another day
# """

   #print(text2)
main()

input()