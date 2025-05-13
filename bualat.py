import random
from getname import random_name

def hero_num():
    random_num = random.randint(1, 100)
    return random_num

def hero_name():
    hero_alias = random_name('superhero')
    return hero_alias

hero_number = hero_num()
hero_nickname = hero_name()

print(f"Your hero number is: {hero_number} "
      f"and your hero nickname is: {hero_nickname}"
)