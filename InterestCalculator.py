#User Data Input
MilkTeaWeeklyFrequency = input("How many times in a week do you buy milk tea?")
PriceOfMilkTea = input ("How much does milk tea typically cost?")

#Milk Tea Per year

MilkTeaCostPerWeek = int(MilkTeaWeeklyFrequency)*int(PriceOfMilkTea)
MilkTeaPerYear = (MilkTeaCostPerWeek*52)//1


#Formula for Future Value

#1 YEAR
x1 = (1+0.04)**1
y1 = x1-1
z1 = y1/0.04
FV1 = (MilkTeaPerYear*z1)//1

#5 YEARS
x2 = (1+0.04)**5
y2 = x2-1
z2 = y2/0.04
FV2 = (MilkTeaPerYear*z2)//1

#10 YEARS
x3 = (1+0.04)**10
y3 = x3-1
z3 = y3/0.04
FV3 = (MilkTeaPerYear*z3)//1

#20 YEARS
x4 = (1+0.04)**20
y4 = x4-1
z4 = y4/0.04
FV4 = (MilkTeaPerYear*z4)//1

#40 YEARS
x5 = (1+0.04)**40
y5 = x5-1
z5 = y5/0.04
FV5 = (MilkTeaPerYear*z5)//1



# yearly cost of milktea
b1 = MilkTeaPerYear*1
b2 = MilkTeaPerYear*5
b3 = MilkTeaPerYear*10
b4 = MilkTeaPerYear*20
b5 = MilkTeaPerYear*40

#Print
print ("The total amount you will spend on milk tea per year is Php " + str(MilkTeaPerYear))

print ("If you save this money every year in a high yield bank account earning 4% APY, you would have earned")

print ("Php " + str(int(FV1)) + " in 1 year" + " vs. " + "spending Php " + str(int(b1)))
print ("Php " + str(int(FV2)) + " in 5 year" + " vs. " + "spending Php " + str(int(b2)))
print ("Php " + str(int(FV3)) + " in 10 year" + " vs. " + "spending Php " + str(int(b3)))
print ("Php " + str(int(FV4)) + " in 20 year" + " vs. " + "spending Php " + str(int(b4)))
print ("Php " + str(int(FV5)) + " in 40 year" + " vs. " + "spending Php " + str(int(b5)))

#John Rafael P. Belotindos
#G1-L
#This code calculates your savings if you did not buy milk tea and instead put it in a savings account with 4% APY
