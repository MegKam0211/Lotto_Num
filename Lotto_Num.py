import random

lottoNum = random.randint(10,99)#generate random 2 digit number
#print(lottoNum) #used to check if code is working correctly not part if the program
#check if its divisible to make sure they are whole numbers
lottoNum1 = int(lottoNum/10) #store first digit
lottoNum2 = lottoNum%10 #store second digit

guessNum = input("Enter 2 digit number guess for the lottery: ") #get guessed number from user
z = [int(d) for d in str(guessNum)]
guessNum1 = z[0] #store first digit
guessNum2 = z[1] #store second digit



# If the user's guess matches the lottery number exactly
if guessNum1 and guessNum2 == lottoNum1 and lottoNum2:
    print("Congratulations you have an exact match, you win R10 000.00")
# You c
# If the user's guess matches the lottery numbers, but are in the wrong order print out "Congratulations you have all digits, you win R5 000.00"
# (i.e. if the user enters 48 and the lottery number is 84)
elif (guessNum2 + guessNum1) or (guessNum1 + guessNum2)  == lottoNum1 and lottoNum2: 
        print("Congratulations you have all digits, you win R5 000.00")

# If the user guesses one digit correctly print out "Congratulations you have one correct digit, you win R1 000.00"
elif guessNum1 or guessNum2 == lottoNum1 or lottoNum2:
        print("Congratulations you have one correct digit, you win R1 000.00") 

#Else print out "Sorry no match"
else:
        print("Sorry no match")

# ##########################################################