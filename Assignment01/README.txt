
Name - Ravi Lahare
Roll No. - 210101086
Assignment - 01


-----------------------------------------------------------------------------------------------------------------
Question - 01
-----------------------------------------------------------------------------------------------------------------
input file     : INVENTORY.txt
code file      : question01.awk  
                 (for creating report)
output file    : output01.txt
command to run : awk -f question01.awk INVENTORY.txt  
                 (to show report in terminal)
                 awk -f question01.awk INVENTORY.txt > output01.txt
                 (for getting output in a file)
description    : I created a awk script(question01.awk) to generate report of structured
                 data like (INVENTORY.txt).
                 Explanation of Code:
                 in line 1-6 i just printed the headers using <print "---" ;> & i uses BEGIN{}
                 in line 7-12 i jus created variables and assigned values to them 
                         {$1,$2,$3,$4,$4} the data is readed from input file
                 in line 13-16 i uses the if else condition and calculated the order Amount
                 in line 17-23 i just printed the content of report using <printf("");>
                         and uses the suitable format specifiers like %d, %f, %s, %c, %5.2f etc..
                 in line 24-27 i just printed the ending part using <print "";> & i uses END{}



-----------------------------------------------------------------------------------------------------------------
Question - 02
-----------------------------------------------------------------------------------------------------------------
input file     : EMPLOYEE.txt
code file      : question02.sh 
                 (for creating payroll register)
output file    : output02.txt
command to run : ./question02.sh 
                 (to show payroll register in terminal)
                 ./question02.sh > output02.txt
                 (for getting output in a file)
note           : first of all we have to make question02.sh to be executable
command to make file executable : chmod +x question02.sh
formula for overtime pay : for work time greater than 40 and exempt is N  
                            = (pay rate)*(hours worked-40)*1.5
                           for other case = 0
formula for base pay     : when overtime pay is 0     = (pay rate)*(hours worked)
                           when overtime pay is not 0 = (pay rate)*40
formula for total pay    : base pay + overtime pay
description              : I created bash script(question02.sh) to generate payroll register
                           using input file(EMPLOYEE.txt).
                           Explanation of Code:
                           in line 1-4 i just printed the heading using echo
                           in line 7 i make a while loop to run through each line of EMPLOYEE.txt
                                   and storing contents of line in data1 data2 ... data5
                                   this loop if from 9-56
				   in line 9-13 i created variable and assigned values to them
                           inside loop i created if else condition for exempt==Y 
                           	inside else condition i further created if else condition for hours worked > 40
						for all case i calculated base pay, overtime pay and total pay using
                                    above formulas and printed the content of payroll register
                           for making calculations i used awk tool using piping,uses printf in awk
                           in line 58 just printed END.
-----------------------------------------------------------------------------------------------------------------
