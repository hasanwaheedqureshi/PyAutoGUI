import pyautogui as pg
import time
import random

bad_adjectives = ["Terrible", "Horrible", "Dreadful", "Awful", "Abysmal", "Atrocious", "Ghastly", "Gruesome", "Hideous", "Repulsive", "Offensive", "Disgusting", "Nasty", "Vile", "Repugnant", "Foul", "Distasteful", "Unpleasant", "Annoying", "Irritating", "Frustrating", "Disappointing", "Boring", "Dull", "Tedious", "Monotonous", "Tiring", "Exhausting", "Draining", "Stressful", "Overwhelming", "Depressing", "Sad", "Miserable", "Gloomy", "Desolate", "Lonely", "Painful", "Agonizing", "Torturous", "Brutal", "Cruel", "Heartless", "Malicious", "Insulting", "Disrespectful", "Rude", "Arrogant", "Selfish", "Greedy", "Dishonest", "Corrupt", "Manipulative", "Lazy", "Incompetent", "Clumsy", "Unreliable", "Inconsiderate", "Thoughtless", "Ignorant", "Stupid", "Foolish", "Naive", "Gullible", "Careless", "Reckless", "Dangerous", "Unpredictable", "Chaotic", "Confusing", "Complicated", "Ambiguous", "Unclear", "Inconsistent", "Unfair", "Biased", "Prejudiced", "Discriminatory", "Offensive", "Hurtful", "Damaging", "Destructive", "Disruptive", "Divisive", "Hostile", "Aggressive", "Violent", "Hateful", "Envious", "Jealous", "Resentful", "Angry", "Frustrated", "Anxious", "Worried", "Nervous", "Stressed", "Overwhelmed", "Depressed", "Hopeless", "Desperate", "Suicidal", "Disappointed", "Regretful", "Guilty", "Ashamed", "Embarrassed", "Humiliated", "Insulted", "Offended", "Rejected", "Betrayed", "Abandoned", "Lonely", "Unloved", "Neglected", "Ignored", "Misunderstood", "Inadequate", "Insecure", "Inferior", "Worthless", "Useless", "Pointless", "Meaningless", "Empty", "Boring", "Dull", "Tedious", "Monotonous", "Tiring", "Exhausting", "Draining", "Stressful", "Overwhelming"]


time.sleep(3)

for i in range(1000):
    word = random.choice(bad_adjectives)
    pg.write("Aliyan you are" + word)
    time.sleep(0.5)
    pg.press("Enter")