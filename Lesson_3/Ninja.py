from Lesson_1.character import Character

import random

class Ninja(Character):

   def __init__(self, name, hp, damage, armor):

       Character.__init__(self, name, hp, damage, armor)

   def count_addition_damage(self):

       return (self.max_hp - self.hp) / self.max_hp * self.damage

   def attack(self, target):

       if random.randint(1, 100) > 50:
           target.take_damage(self.damage + self.count_addition_damage())

           else:

           print('Ниндзя увернулся от удара!')

   def take_damage(self, damage):

       if random.randint(1, 100) > 50:

           self.hp -= damage

       else:

           print('Ниндзя увернулся от удара!')
