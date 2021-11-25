#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print ("Welcome to the tip calculator.\n")
numBill = float(input("How much is your bill? $ "))
numCus = int(input("How many people will split the bill? "))
numPer = int(input("What percentage do you want to leave as a tip? "))
numBill1 = numBill + (float(numBill) / 100 * float(numPer))
numRes = numBill1 / float(numCus)
numRes = round(numRes,2)
print ("Each person should pay: $" + str(numRes))