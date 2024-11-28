def read_and_write_file():
    try:
        # ask the user to input file name
        input_filename = input("Enter the name of the file to read: ")
        
        #open the file and read
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # write the content (convert to uppercase or lowercase)
        write_content = content.upper()
        
        # write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(write_content)
        
        print(f"Modified content has been written to {output_filename}")
       
    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except PermissionError:
         print("Error: You do not have permission to read this file.")
         
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    
#call the function
read_and_write_file()