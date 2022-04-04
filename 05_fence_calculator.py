# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":
    
    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost_per_m= num_check("Cost_per_m: ")

    # Calulate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Calculate the cost of the fencing (perimeter x price / meter)
    cost_of_fencing = perimeter * cost_per_m

    # Output the perimeter and cost of the fencing
    print()
    print("Perimeter: {:.2f} units".format(perimeter))
    print("Cost_per_m: {:.2f} units".format(cost_per_m))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit. ")
    
    print()
    print("-" * 30)
    print()

print()
print("Thanks for using the Fencing cost calculator")

        
    
    