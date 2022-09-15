#! /usr/bin/perl

################################################
#
# PERL script to generate a randomized string.
#
################################################

# storing alphabets to use in variable alphabets
$file = $ARGV[0];
# opening $file
open(FILE,"<","$file") or die "File '$file' can't be opened" ;
$alphabets = <FILE>;
# closing $file
close (FILE);
chomp $alphabets;

# taking max. repeatation of an alphabet
$count = $ARGV[1];

# taking length of string
$length = $ARGV[2];

# Calculating total no of alphabets entered 
$total_alphabets = length($alphabets);

# variable for tracking how many character are remaining to print
$remaining_length = $length;

# variable for storing previous random alphabet generated
# it is used to avoid consecutive generation of same alphabet
$previous_char = "@";

# variable for storing our ans string
$ans_string = "" ;

# case where no string can be generated 
if($total_alphabets == 1 )
{
    # case where no string can be generated 
    if($count < $length)
    {
        print "No string possible\n" ;
    }

    # case where only 1 string possible we dont need rand() function
    else
    {
    	print "Only possible string is -\n" ;
        $only_char = substr($alphabets, 0, 1);
        for ($loop = 0 ; $loop < $length ; $loop++)
        {
            print "$only_char" ;
        }
        print "\n" ;
    }
}

else
{
    # runs loop till we get string of our desired length
    while ($remaining_length >= 1)
    {
        # generating random no to choose an alphabet we call that alphabet as new_random_char
        $random_no_alphabet = int(rand($total_alphabets));

        # generating random no for how many times this new_random_char will repeated
        $random_no_times = int(rand($count)) + 1 ;

        # selecting new_random_char from entered set of alphabets
        $new_random_char = substr($alphabets, $random_no_alphabet, 1);

        # checking new_random_char with previous_char 
        if("$new_random_char" ne "$previous_char") 
        {
            #updating previous_char
            $previous_char = $new_random_char ;

	        # avoiding the case when random no. generated greater than remaining_length
	        $random_no_times = ($random_no_times >= $remaining_length ? $remaining_length : $random_no_times) ;
	    
            # printing
	        print "\nRandom generated character is = $new_random_char\n" ;
	        print "No. of times we will repeat this character = $random_no_times\n" ;
            # loop for printing new_random_char
            for ($loop = 0 ; $loop < $random_no_times ; $loop++)
            {
                # condition for managing strinh length
                if($loop < $remaining_length)
                {
                    $ans_string = $ans_string.$new_random_char ;
                }
            }

            #updating remaining_length
            $remaining_length = $remaining_length - $random_no_times;
            print "Now our string becomes = $ans_string\n" ;
        }
    }
    print "\nFinal string = $ans_string";
    print "\n" ;
}
