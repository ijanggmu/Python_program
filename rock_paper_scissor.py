import random
def comp_choice():
    ran_num=random.randint(1,3)
    option={1:'rock',2:'paper',3:'scissor'}
    choice=option[ran_num]
    return choice
def user_choice():
    user_input=input("Enter rock paper or scissor\n")
    user_input=user_input.lower()
    return user_input
def result(user_pick,comp_pick):
    if user_pick==comp_pick:
        return "draw"
    elif user_pick=="rock" and comp_pick=="scissor":
        return "win"
    elif user_pick=="scissor" and comp_pick=="paper":
        return "win"
    elif user_pick=="paper" and comp_pick=="rock":
        return "win"
    else:
        return"lose"
comp=comp_choice()
while True:
    user=user_choice()
    if user in['rock','paper','scissor']:
        break
res=result(user,comp)
print(f'your pick:{user}')
print(f'computer pick:{comp}')
print(f'result:{res}')