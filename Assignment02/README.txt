
Name - Ravi Lahare
Roll No. - 210101086
Assignment - 02


---------------------------------------------------------------------------------------------------------------------
Question - 01
---------------------------------------------------------------------------------------------------------------------
code file       : backup.scr.sh  
                 (for backup)

command to run  : sudo ./backup.scr.sh <filename> <directoryname>

note            : first of all we have to make code file executable

command to make
file executable : chmod +x backup.scr.sh

description     : <filename> - a file present which contains list of
                               files which we have to backup these files present in 
                               /home/ directory
			<directoryname> - a directory where we will store our backup files.
					      this argument should end with / 
			code file -> 1.first i done validation of arguments that exactly two arguments
					   are passed and first argument is an existing file and second
					   argument is an existing directory 
					 2.then i copied files using "cp" to our target directory
					 3.then i added .bak using  "mv" to this copied files
			commands and functions :
					 if [ -z "$1" ] -> for checking argument is passed or not
					 exit 225 -> for exit
					 echo "" -> for printing
					 if [ -f "$1" ] -> for checking argument is an existing file or not
					 if [ -d "$2" ] -> for checking argument is an existing directory or not
					 while IFS=" " read -r filename -> for runs through the each line of file
					 cp -> for copy
					 mv -> for renaming

-----------------------------------------------------------------------------------------------------------------------
Question - 02
-----------------------------------------------------------------------------------------------------------------------
code file       : rand_str_generator.pl
                 (for generating randomized string)

input file      : alphabets.txt

command to run  : ./rand_str_generator.pl alphabets.txt <count> <length>

note            : first of all we have to make code file executable

command to make
file executable : chmod +x rand_str_generator.pl

description     : alphabets.txt - a file which contains string of character without spaces.
                  <count> - max. repeatation of an alphabet
			<length> - length of string
			code file -> 1.first i opened file given in 1st argument and taken string present in it
					   and store it to variable named $alphabets
					 2.then i stored count and lenrth from 2nd and 3rd argument repectively.
					 3.then i calculated total no. of characters in string $alphabets
					 4.then i genenerated 2 random number
					   1st random no. between 0-(total_alphabet-1) for selecting random character
					   2nd random no. between 1-count for repeatation of random character
					 5.repetetely done step-4 till a get the string of desired length
					   in this i also insuring that no consecutive random character is same
					 6.i also checked for the case where no string can be generated or only 1 string possible
					   there are the case when alphabets.txt contains only one character.
			commands and functions :
					 $ARGV[] -> for acessing arguments
					 open(FILE,"<","$file") -> for opening file
					 close (FILE); -> for closing file
					 length() -> for calculating length of string
					 print "" -> for printing
					 $1 >= $2 ? $2 : $1 -> min. of $1 and $2
					 substr($string, n-1, 1) -> for nth element of string
					 int(rand(n)) -> generate random integer 0 - (n-1)
					 chomp ->  for to remove the last trailing newline from the input string.
					 

-----------------------------------------------------------------------------------------------------------------------
