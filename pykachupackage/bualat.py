import random
import emoji
from getname import random_name

def hero_num():
    hero_number = random.randint(1, 100)
    print(emoji.emojize (f"\n Your hero number is: {hero_number} :dizzy:"))

def hero_name():
    hero_alias = random_name('superhero')
    print(emoji.emojize(f" Your hero nickname is: {hero_alias} :khanda:"))
