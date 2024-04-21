#import modules
from  random import randrange as r
# ask how many questions user wants
no_questions = int(input('How many questions do you want?: '))
#set score start at zero
score = 0
#loop through number of questions
for q in range(no_questions):
    num1,num2 = r(1,11),r(1,11)
    ans = num1 * num2
    u_ans =int(input(f'{num1} X {num2} = '))
    if u_ans == ans:
        score += 1
print(f'Thank you for playing! \nYou got {score} out of {no_questions} {round(score/no_questions*100)}%')