#Function for Solving Josephus Problem using list
#------------------------------------------------------------------------------------------------------------------------
def solve_josephus(person_list, k) :

    killer_index = 0     #variable for storing index of killer  
    killer_index = int(killer_index)     #typecasting variable to int

    step = 1      #variable for storing killing no.
    step = int(step)     #typecasting variable to int

    #loop runs untill only one person remaining
    while(len(person_list)!=1) :
        killed_index = (killer_index + k)%len(person_list)     #calculating the index of killed person
        killed_index = int(killed_index)     #variable for storing killed person index  #typecasting variable to int

        killer = person_list[killer_index]     #variable for storing name of killer
        killed = person_list[killed_index]     #variable for storing name of killed person

        #here I printing the killing step who is killer and who is killed 
        if killer_index == killed_index :
            print("Killing no.",step," : ",killer," kills  himself",)
        else :  
            print("Killing no.",step," : ",killer," kills ",killed)

        person_list.remove(killed)     #removing the person from the list who is killed 

        killer_index = killed_index % len(person_list)     #storing the next killer index
        killer_index = int(killer_index)     #typecasting variable to int

        step = step + 1     #incrementing the killing counter by 1

    print("\nWinner : ",person_list[0]," is the last person alive.",)     #printing the name of last person alive
#------------------------------------------------------------------------------------------------------------------------

#taking the no. of total person
print("Enter the number of persons standing : ")     #just printing a message
n = input()     #input n
n = int(n)     #typecasting variable to int

#taking the skip no.
print("Enter the skip number : ")     #just printing a message
k = input()      #input k
k = int(k)     #typecasting variable to int

person_list = []     #created list for storing names of persons

#creating person name(person followed by no. like person1 , person2) and storing them to person list
for i in range(1,n+1) :
    person = "Person"     #initial name
    person_number = "% s" % i     #person no.
    person_name = person + person_number     #creating person name
    person_list.append(person_name)     #storing person name in person list

print("\nLets start the Killing Game :\n")   #just printing a message

#function call to function "solve_josephus" for solving the person
solve_josephus(person_list, k)    