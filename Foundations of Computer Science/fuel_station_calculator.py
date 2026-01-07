#USER INPUT
fuel = input("What type of fuel that the customer bought (DIESEL, PREMIUM, UNLEADED, KEROSENE)? \n")

#DIESEL
if fuel == "DIESEL":
	liters = int(input("How many liters of fuel bought?\n"))
	payment = int(input("How much is the customer's payment?\n"))
	costoverall = liters * 66.50
	change = payment - costoverall
	roundedchange = round(change, 2) #from freecodecamp
	if roundedchange < 0:
		print ("Attention! The customer needs to pay an additional Php " + str(roundedchange*-1))
	else: 
		print ("The customer's change is Php " + str(roundedchange))

#PREMIUM
elif fuel == "PREMIUM":
	liters = int(input("How many liters of fuel bought?\n"))
	payment = int(input("How much is the customer's payment?\n"))
	costoverall = liters * 71.45
	change = payment - costoverall
	roundedchange = round(change, 2) #from freecodecamp
	if roundedchange < 0:
		print ("Attention! The customer needs to pay an additional Php " + str(roundedchange*-1))
	else: 
		print ("The customer's change is Php " + str(roundedchange))
		
#UNLEADED
elif fuel == "UNLEADED":
	liters = int(input("How many liters of fuel bought?\n"))
	payment = int(input("How much is the customer's payment?\n"))
	costoverall = liters * 69.36
	change = payment - costoverall
	roundedchange = round(change, 2) #from freecodecamp
	if roundedchange < 0:
		print ("Attention! The customer needs to pay an additional Php " + str(roundedchange*-1))
	else: 
		print ("The customer's change is Php " + str(roundedchange))
		
#KEROSENE
elif fuel == "KEROSENE":
	liters = int(input("How many liters of fuel bought?\n"))
	payment = int(input("How much is the customer's payment?\n"))
	costoverall = liters * 67.56
	change = payment - costoverall
	roundedchange = round(change, 2) #from freecodecamp
	if roundedchange < 0:
		print ("Attention! The customer needs to pay an additional Php " + str(roundedchange*-1))
	else: 
		print ("The customer's change is Php " + str(roundedchange))
		
#WRONG INPUT
else: 
	print ("Sorry, you inputed an invalid type of fuel.")
	
	
#John Rafael P. Belotindos
#G-1L
#This code calculates the price of fuel based on the number of liters bought.
