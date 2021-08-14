import random    #random module to be later used for random number generation

#variables declaration and initilization
guess = number = None     
correct = incorrect = 0
result = []
msg = ''


while 1:    #start of the infinit loop. user can break it by pressing -1
   number = random.randint(1, 10)     #generating random integer bw 1-10

   guess = input('Guess a number from 1 to 10. Press -1 to exit:\n')   #taking user input for guessing
   
   try:
      guess = int(guess)     #invalid input exception handling block to make the program robust

   except:
      print('You have made an invalid choice. \n')
      continue

   if guess > 10:            #user should enter value bw 1 and 10
      print('You have made an invalid choice. \n')
      continue

   elif guess == -1 :          #exit condition
      msg = 'You have chosen to exit'
      break

   elif guess == number :      #when the guess is true
      print('your guess was absolutely right\n')
      correct += 1
      result.append([guess, number])    #recording the result

   else :      #when the guess is false
       print('Keep Trying. The number was ', number)
       incorrect += 1
       result.append([guess, number])    #recording results


#printing results to user on console after breaking from the loop
print(msg)
print('Here are your results')

for i in range(len(result)):
   print('Number = ', result[i][0], '\t', 'Guess = ', result[i][1] )
   
print('*********************')
print(f"you made {correct} correct guesses while {incorrect} were incorrect")

