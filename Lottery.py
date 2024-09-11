import random
listt=[]
print("_________________________________")
print("Win a Lottery and check your luck")
print("_________________________________")
name=input("Enter your name: ")
print("_________________________________")
lottery_number= random.randint(0,20)
print(f"Hi {name} Your lottery number is : {lottery_number}")
print("_________________________________")
print("lucky dip of 20 lottery tickets..... processing")
for i in range(20):
    listt.append(random.randint(0, 20))
print("_________________________________")
print("Check your luck among 5 lotteries......")
prize=random.sample(listt,5)
print("And the winners are:",prize)
if lottery_number in prize:
    print("_________________________________")
    print(":::::::Hurray!! you have won the lottery:::::")
else:
    print("_________________________________")
    print(":::::::OOPS Better luck next time::::::::::")
