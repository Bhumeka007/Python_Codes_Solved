import random
"""print(random.random())
print(random.randint(3,8))"""
verbs = ["goes","cooks","shoots","faints","chews","screams","loves"]
nouns = ["bear","lion","mother","baby","sister","BTS","car","book"]
adverbs = ["handily","lovely","sweetly","sourly","forcefully"]
articles = ["I","a","the","that","this"]

def sentence():
    A = random.choice(articles)
    N = random.choice(nouns)
    V = random.choice(verbs)
    Ad= random.choice(adverbs)

    OurSen = A+" "+N+" "+V+" "+Ad+"."
    OurSen = OurSen.capitalize()

    print(OurSen)
