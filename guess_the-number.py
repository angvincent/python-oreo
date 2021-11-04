#     guess the number game
#     generates new number after you guessed correctly

def intro():
    print('''

 #################################################   
 # Welcome to guess the number game!             #
 # The computer will generate a random number.   #                                          
 # You will start with a score of 100, if your   #
 # score becomes 0, you lose. Everytime you      #
 # guessed correctly +10 points will be added    #
 # to your score. Good Luck!                     #
 #################################################   
    
    ''')
intro()


def loading_bar():
    progressbar_width = 20 
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * progressbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (progressbar_width+1)) # return, start of line after:  '['

    for i in range(progressbar_width):
        time.sleep(0.2) # duration set
        # diplays sign, updates bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # ends progress bar


import random
import time
import sys

score = 100
sec = random.randint(1, 10)


while(1):
    flag = True
    while flag:
        user = (input('\n Guess a number between 1 and 10: '))
        if user.isdigit():   # user has to input a whole number (int)
            user = int(user)
            flag = False
        else:
            print('\n Type digit!\n')
    if score <= 0:
        print('\n You lost! ** Game Over **\n') # if score becomes 0, game lost.
        break
    else:
        score_new = abs(sec - user)
        score = score - score_new  ## calculates the distance between the user input and the random number,
                                   ## then removes it from the score     

    if user > 10:
        print('U guessed to high')
    elif user < 1:
        print('To low')
        
    if user == sec:
        print('\n Well done! Your score is', score)
        score = score + 10 #  if user guessed correctly - +10 points 
        
        if user == sec:
            print('New number is being generated, you keep your score!')
            sec = random.randint(1, 10)  #   generates new num
            loading_bar()

    else:
        print('Try again')



            

