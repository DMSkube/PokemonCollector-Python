# This program records user-inputted quantities in 5 user-selected 
# categories and prints them for the user to see.

# Variables
again = True # Loop Condition
quantity = 0
bulb_quantity = 0
pid_quantity = 0
butt_quantity = 0
sand_quantity = 0

while again == True:
#Menu
	print("Welcome to the CS 110 Pokemon Go Shop!")
	print("Which Pokemon would you like to collect?")
	print("\t1. Bulbasaur\n\t2. Pidgey\n\t3. Butterfree\n\t4. Sandslash\n\t5. Exit")
	choice = (int(input("Please enter your choice (1-5): ")))
	print("")

#Bulbasaur
	if choice == 1:
		quantity = int(input("How many Bulbasaur's would you like to collect?: "))
		bulb_quantity = bulb_quantity + quantity
		print("")
		print("Okay. You have collected", quantity, "more Bulbasaur's.")
		# Quantity entered will remain until re-entered. But re-entry is nessecary to continue.
		# So a quantity will only repeat if intended.
		print("")

# Pidgey
	elif choice == 2:
		quantity = int(input("How many Pidgey's would you like to collect?: "))
		pid_quantity = pid_quantity + quantity
		print("")
		print("Okay. You have collected", quantity, "more Pidgey's.")
		print("")

# Butterfree
	elif choice == 3:
		quantity = int(input("How many Butterfree's would you like to collect?: "))
		butt_quantity = butt_quantity + quantity
		print("")
		print("Okay. You have collected", quantity, "more Butterfree's.")
		print("")

# Sandslash
	elif choice == 4:
		quantity = int(input("How many Sandslash's would you like to collect?: "))
		sand_quantity = sand_quantity + quantity
		print("")
		print("Okay. You have collected", quantity, "more Sandslash's.")
		print("")

# Exit	
	elif choice == 5:
			print("You have collected", bulb_quantity, "Bulbasaur's,", pid_quantity,
				"Pidegy's,", butt_quantity, "Butterfree's and ", sand_quantity, "Sandslash's.")
			again = False
# Invalid Entry
	else:
		print("Please enter a number from 1 to 5.")
		print("")
		print("")
		