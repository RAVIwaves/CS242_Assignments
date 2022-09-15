#! /bin/bash

#####################################
#
# bash script to back up files.
#
#####################################

# Validation part
#--------------------------------------------------------------------------------------------
# Checking first argument is passed or not
if [ -z "$1" ]
# if first argument not passed
then
    echo "⚠ ERROR..."
    echo "Message: no Arguments passed"
    echo "Coreect Arguments: <file> <folder>"
    exit 255 
fi

# Checking second argument is passed or not
if [ -z "$2" ]
# if second argument not passed
then
    echo "⚠ ERROR..."
    echo "Message: only one Argument passed"
    echo "Coreect Arguments: <file> <folder>"
    exit 255 
fi

files_list=$1    #list of files to be backup
target_folder=$2 #target folder where we have to store backup files

# Checking third argument is passed or not
if [ -z "$3" ]
then
    echo ""
# if third argument is passed
else
    echo "⚠ ERROR..."
    echo "Message: extra arguments are passed."
    echo "Coreect Arguments: <file> <folder>"
    exit 255
fi

# Checking first argument is an existing file or not
if [ -f "$files_list" ]  
then
    echo ""
# if first argument not an existing file
else
    echo "⚠ ERROR..."
    echo "Message: your first argument is not an existing file, it should be a existing file. "
    echo "Coreect Arguments: <file> <folder>"
    exit 255
fi

# Checking second argument is an existing directory or not
if [ -d "$target_folder" ]
then
    echo ""
# if second argument not an existing directory
else
    echo "⚠ ERROR..."
    echo "Message: your second argument is not an existing directory, it should be a existing directory. "
    echo "Coreect Arguments: <file> <folder>"
    exit 255
fi
#------------------------------------------------------------------------------------------------------------
           

# Backup part
# -----------------------------------------------------------------------------------------------------------
# loop runs through each line of files_list and scan filename
while IFS=" " read -r filename ;
do
    echo "copying $filename to $target_folder ....."
    cp /home/$filename $target_folder
    mv $target_folder$filename $target_folder$filename.bak
done < $files_list #inserting  files_list to be backup

# End
echo ":) Backup Done..."
#------------------------------------------------------------------------------------------------------------
