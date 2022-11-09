from game_data import data
import random
from art import logo, vs

Compare_A = random.choice(data)
Against_B = random.choice(data)


def get_data(Compare_A, Against_B):
    return f"Compare A: {Compare_A['name']}, a {Compare_A['description']}, from {Compare_A['country']}", f"Against B: {Against_B['name']}, a {Against_B['description']}, from {Against_B['country']}."


def check(Compare_A, Against_B):
    if Compare_A['follower_count'] > Against_B['follower_count']:
        return True
    elif Compare_A['follower_count'] < Against_B['follower_count']:
        return False
    else:
        return "Both has Same followers"


count = 0
flag = True

print(get_data(Compare_A, Against_B)[0])
print(vs)
print(get_data(Compare_A, Against_B)[1])

while (flag):
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
        if check(Compare_A, Against_B):
            count += 1
            print(f"You're right! Current score: {count}.")
        else:
            flag = False
            print(f"Sorry, that's wrong. Final score: {count}")
    elif choice == 'B':
        if check(Compare_A, Against_B) == False:
            count += 1
            print(f"You're right! Current score: {count}.")
        else:
            flag = False
            print(f"Sorry, that's wrong. Final score: {count}")
    if flag:
      new_Compare_A = Compare_A
      Against_B = random.choice(data)  
      print(get_data(new_Compare_A, Against_B)[0])
      print(vs)
      print(get_data(new_Compare_A, Against_B)[1])
