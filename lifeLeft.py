#This program calculates the years, weeks and days you have left 
#It depends on how old are you, and the operations are based on the period of life of 90 years

yearsOld = int(input("How old are you? "))

yearsLeft = 90-yearsOld
monthsLeft = yearsLeft*12
daysLeft = yearsLeft * 365

answer = f"You have {yearsLeft} years left, {monthsLeft} months left, {daysLeft} days left."
print(answer)