# Eduard

# import
import random

# data
part1=["Putin", "Hillary", "Obama", "Fake News", "Mexico", "Arnold Schwarzenegger", "Democrats"]
part2=["no talen", "on the way down", "really poor numbers", "nasty tone", "looking like a fool", "bad hombre"]
part3=["got destroyed by my ratings.", "regged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4=["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]

# random range vorbereiten
random.seed()

# output
print(random.choice(part1) + " " + random.choice(part2) + " " + random.choice(part3) + " " + random.choice(part4) + ".")
