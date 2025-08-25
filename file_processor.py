def process_file():
    #Asking user for the input filename
    filename = input("Enter the name of the file to process: ")

    try:
        #Trying to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        #Counting words
        words = content.split()
        word_count = len(words)

        #Converting text to uppercase
        content_upper = content.upper()

        #Writing processed text + word count to output.txt
        with open("output.txt", "w") as outfile:
            outfile.write("Processed Text:\n")
            outfile.write(content_upper + "\n\n")
            outfile.write(f"Word Count: {word_count}\n")

        #Printing success message
        print("Success! The modified content has been saved in 'output.txt'.")

    except FileNotFoundError:
        print("Eror: The file you entered does not exist.")
    except PermissionError:
        print("Error: Permission denied while trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Running the program
process_file()
