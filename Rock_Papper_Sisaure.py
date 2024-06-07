import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for papper or 2 for Scissors.\n"))
ia_choice = random.randint(0, 2)

if user_choice >= 3 or ia_choice < 0:
    print("You typed an invalid number, you lose !")
else:  
    print(game_images[user_choice])

    print(f"Computer chose:\n {game_images[ia_choice]}")
    if user_choice == 0 and ia_choice == 2:
        print("You win !")
    elif ia_choice == 0 and user_choice == 2: 
        print("You lose !")
    elif user_choice > ia_choice:
        print("You win !")
    elif ia_choice > user_choice:
        print("You lose !")
    elif user_choice == ia_choice: 
        print("It's a draw !")