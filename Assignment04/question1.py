#function for calculating total no. of denominations and printing output
#-------------------------------------------------------------------------------------------------------------------------
def output(d50, d25, d20, d10, d5, d1) :

    #calculating total no. of denominations
    total_denomination = d50 + d25 + d20 + d10 + d5 + d1
    total_denomination = int(total_denomination) #typecasting variable to int

    #printing output
    print("Minimum number of denominations to provide change the above amount of money is",total_denomination)
    print("Note of 50 units =",d50)
    print("Note of 25 units =",d25)
    print("Note of 20 units =",d20)
    print("Note of 10 units =",d10)
    print("Note of 5 units =",d5)
    print("Note of 1 units =",d1)
#-------------------------------------------------------------------------------------------------------------------------


#taking amount of money from the user
#-------------------------------------------------------------------------------------------------------------------------
print("Enter the Amount of Money : ")     #just printing a message
money = input()     #input money
money = int(money)      #typecasting variable to int
#-------------------------------------------------------------------------------------------------------------------------


#calculating denominations for all units
#-------------------------------------------------------------------------------------------------------------------------
denomination50 = int(0)  #typecasting variable to int
denomination25 = int(0)  #typecasting variable to int
denomination20 = int(0)  #typecasting variable to int
denomination10 = int(0)  #typecasting variable to int
denomination5 = int(0)   #typecasting variable to int
denomination1 = int(0)   #typecasting variable to int

#calculating no. of note of 50 units
denomination50 = int(money/50)
remaining_money = money - denomination50*50 #calculating remaining money
remaining_money = int(remaining_money) #typecasting variable to int

#calculating no. of note of 1 unit
denomination1 = int(remaining_money%5)
remaining_money = remaining_money - denomination1 #calculating remaining money
remaining_money = int(remaining_money) #typecasting variable to int

#calculating no. of note for other unit's note then calling output function for printing output
if remaining_money == 45 :
    denomination20 = 1
    denomination25 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 40 :
    denomination20 = 2
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 35 :
    denomination10 = 1
    denomination25 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 30 :
    print("there are two solutions :")
    print("\n1st Solution :-")
    denomination20 = 1
    denomination10 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)
    print("\n2st Solution :-")
    denomination20 = 0
    denomination10 = 0
    denomination25 = 1
    denomination5 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 25 :
    denomination25 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 20 :
    denomination20 = 1
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 15 :
    denomination10 = 1
    denomination5 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 10 :
    denomination10 = 1
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

elif remaining_money == 5 :
    denomination5 = 1 
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

else :
    output(denomination50, denomination25, denomination20, denomination10, denomination5, denomination1)

#-------------------------------------------------------------------------------------------------------------------------
