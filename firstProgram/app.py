
#***************************#
# Writen By Ravi Damodaran  #
# Python while loop Tutorial#
# Working with while loop   #
#***************************#

# i =1
#
# while i<=10:
#     print(i)
#     i+=1
#
# print("Done with loop")

secret_word="ravi"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while secret_word !=guess and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("Enter your guess: ")
        guess_count+=1
    else:
        out_of_guesses=True

    if guess != secret_word:
        print("Sorry Wrong Guess")
if out_of_guesses:
    print("You lost the game")
else:
    print("you win !")













