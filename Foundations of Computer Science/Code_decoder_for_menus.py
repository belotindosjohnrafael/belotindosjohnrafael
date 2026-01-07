# Belotindos, John Rafael P.
# G-1L
# This code determines the ice cream flavor and toppings that your customers have chosen for the day.
# Maraschino Cherries combined with Chocolate chips or any other toppings cannot exist because the code limit is 128.


def determine_toppings(top, i): #This code determines the toppings that the ice cream have.
	Sprinkles=1
	Marshmallows=2
	Strawberry_syrup=4
	Almonds=8
	Blueberries=16
	Chocolate_chips=32
	Coconut_shavings=64
	Maraschino_cherries=128
	o=top
	print("Customer",i,"toppings:")
	if o==128:
		print("\tMaraschino Cherries")
	if 128>top>=64:
		print("\tCoconut shavings")
		o=top-64
	if 64>o>=32:
		print("\tChocolate chips")
		o-=32
	if 32>o>=16:
		print("\tBlueberries")
		o-=16
	if 16>o>=8:
		print("\tAlmonds")
		o-=8
	if 8>o>=4:
		print("\tStrawberry syrup")
		o-=4
	if 4>o>=2:
		print("\tMarshmallows")
		o-=2
	if o==1:
		print("\tSprinkles")
	
def determine_flavor(flavor,i): #This block of code determines the flavor of the ice cream
	if flavor%2==0:
		print("The ice cream flavor is chocolate.")
	else:
		print("The ice cream flavor is vanilla.")
	determine_toppings(flavor, i)
	
def check_valid_code(customers): #This block of code checks if the customer code is valid.
	for i in range(1,customers+1):
		print("\n============= CUSTOMER",i,"=============")
		code=int(input("Code: "))
		while 0>code>128:
			print("The customer code ranges from 1 to 128. Ask the cashier again.")
			code=int(input("Code: "))
		determine_flavor(code,i)
	
	print("\n====================================","\nFinished processing orders for the day. We did it!")

def check_valid_customers(q): #This block of code checks if the number of customers are valid.
	if q<=10:
		check_valid_code(q)
	else:
		print("You can only have 1-10 customers on a given day. Try again.")
		main()

def main(): #This part gets the number of customers
	num_of_customers=int(input("How many customers do you have? "))
	check_valid_customers(num_of_customers)

main() #this part initiates the program
	
	

	
