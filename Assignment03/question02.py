#Function for swaping two values in a list
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def swap(puzzle,index1,index2) :
    temp = puzzle[index1]
    puzzle[index1] = puzzle[index2]
    puzzle[index2] = temp
    return 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function for counting inversed pair for checking the problem solvable or not
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Inversion_Count(input_puzzle,maping) :
	inversion_count = 0
	blank_space = 0
	for i in range(0, 9) :
		for j in range(i + 1, 9) :
			if maping[input_puzzle[j]] != blank_space and maping[input_puzzle[i]] != blank_space and maping[input_puzzle[i]] > maping[input_puzzle[j]] :
				inversion_count += 1
	return inversion_count
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function for checking the problem is solvable or not
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Is_Solvable(input_puzzle,desired_puzzle) :
	maping = [0, 1, 2, 3, 4, 5, 6, 7, 8]  
	desired_copy = desired_puzzle.copy()

	for i in range(2) :
		if int(desired_copy.index(0)) < 6 :
			blank_pos = desired_copy.index(0)
			desired_copy[blank_pos] = desired_copy[blank_pos + 3]
			desired_copy[blank_pos + 3] = 0
		else :
			break

	for i in range(2) :
		if int(desired_copy.index(0)) < 8 :
			blank_pos = desired_copy.index(0)
			desired_copy[blank_pos] = desired_copy[blank_pos + 1]
			desired_copy[blank_pos + 1] = 0
		else :
			break
	for i in range(8) :
		maping[desired_copy[i]] = i+1
		
	inversion_count = Inversion_Count(input_puzzle,maping)

	if inversion_count % 2 == 0 :
		return 1
	else :
		return 0 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function for printing list in array format of 3X3
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Print_in_Matrix_format(puzzle) :
	print(puzzle[0]," ",puzzle[1]," ",puzzle[2])
	print(puzzle[3]," ",puzzle[4]," ",puzzle[5])
	print(puzzle[6]," ",puzzle[7]," ",puzzle[8])
	return 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function for calculating Heuristic value(using this for checking function is solved or not)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Heuristic_Count(input_puzzle,desired_puzzle) :
	c = 0
	for i in range(9) :
		if input_puzzle[i] != 0 and input_puzzle[i] != desired_puzzle[i] :
			c += 1
	return c
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function for calculating min steps for solving any problem(when level parameter is 0). I using this function for checking which move is best
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def check_solve(input_puzzle,desired_puzzle,level) :
    h = Heuristic_Count(input_puzzle,desired_puzzle)
    temp_puzzle = input_puzzle.copy()
    while(h>0) :
        blank_pos = int(temp_puzzle.index(0))
        level += 1
        can_move = []
        if(level>10) :
            return level 
        if blank_pos == 0 :
            can_move = [1, 3]
        elif blank_pos == 1 :
            can_move = [0, 2, 4]
        elif blank_pos == 2 :
            can_move = [1, 5]
        elif blank_pos == 3 :
            can_move = [0, 4, 6]
        elif blank_pos == 4 :
            can_move = [1, 3, 5, 7]
        elif blank_pos == 5 :
            can_move = [2, 4, 8]
        elif blank_pos == 6 :
            can_move = [3, 7]
        elif blank_pos == 7 :
            can_move = [4, 6, 8]
        elif blank_pos == 8 :
            can_move = [5, 7]
        check_value = 15
        h_value = 10
        stored_puzzle = temp_puzzle.copy()
        for i in range(len(can_move)) :
            duplicate_puzzle = temp_puzzle.copy()

            swap(duplicate_puzzle,blank_pos,can_move[i])

            temp_check_value = check_solve(duplicate_puzzle,desired_puzzle,level)
            temp_h_value = Heuristic_Count(duplicate_puzzle,desired_puzzle)

			#checking for best move    
            if temp_check_value <= check_value :
                h_value = temp_h_value
                check_value = temp_check_value
                stored_puzzle = duplicate_puzzle.copy()
        temp_puzzle = stored_puzzle.copy()
        h = h_value
    return level
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Function for solving the puzzle and printing each step
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------		
def solve(input_puzzle,desired_puzzle) :
    h = Heuristic_Count(input_puzzle,desired_puzzle)
    level = 0
    while(h>0) :
        blank_pos = int(input_puzzle.index(0))
        level += 1
        can_move = []  #list for storing movable locations
        if blank_pos == 0 :
            can_move = [1, 3]
        elif blank_pos == 1 :
            can_move = [0, 2, 4]
        elif blank_pos == 2 :
            can_move = [1, 5]
        elif blank_pos == 3 :
            can_move = [0, 4, 6]
        elif blank_pos == 4 :
            can_move = [1, 3, 5, 7]
        elif blank_pos == 5 :
            can_move = [2, 4, 8]
        elif blank_pos == 6 :
            can_move = [3, 7]
        elif blank_pos == 7 :
            can_move = [4, 6, 8]
        elif blank_pos == 8 :
            can_move = [5, 7]
        check_value = 15
        h_value = 10
        stored_puzzle = input_puzzle.copy()
        for i in range(len(can_move)) :
            duplicate_puzzle = input_puzzle.copy()

            swap(duplicate_puzzle,blank_pos,can_move[i])   #call to swap function

            temp_check_value = check_solve(duplicate_puzzle,desired_puzzle,level)  #function call to check_solve function for checking best move
            temp_h_value = Heuristic_Count(duplicate_puzzle,desired_puzzle)

			#checking for best move   
            if temp_check_value <= check_value :
                h_value = temp_h_value
                check_value = temp_check_value
                stored_puzzle = duplicate_puzzle.copy()

		#printing each step
        print("Step -",level)
        print("--------------------------------------------")
        Print_in_Matrix_format(input_puzzle)
        print("    ||\n    ||\n    \/")
        input_puzzle = stored_puzzle.copy()
        h = h_value
        Print_in_Matrix_format(input_puzzle)
        print("--------------------------------------------\n\n")


    return 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

				
#taking initial matrix
print("Enter the initial matrix put 0 to the blank space(input one digit at a time) :")
input_puzzle   =  []
for i in range(9) :
	t = int(input())
	input_puzzle.append(t)

#taking desired matrix
print("Enter the goal matrix put 0 to the blank space(input one digit at a time) :")
desired_puzzle =  []
for i in range(9) :
	t = int(input())
	desired_puzzle.append(t)

#Checking problem solvable or not
if Is_Solvable(input_puzzle,desired_puzzle) == 0 :
	print("This input_puzzle is unsolvable.")
else :
    print("\nIt is Solvable",)
    print("We can solve this in",check_solve(input_puzzle,desired_puzzle,0),"steps\n")
    solve(input_puzzle,desired_puzzle)     #function call for solving the problem
    