# MENU DRIVEN FILE HANDLING PROGRAM

# Function to create a new file and write text into it
def create_file():
    f = open("C:\\Users\\Dhruv\\Desktop\\p\\textfile.txt", "w")
    content = input("Enter text to write:\n")
    f.write(content)
    f.close()
    print("File created and data written.")

# Function to open and display content of the file
def open_file():
    try:
        f = open("C:\\Users\\Dhruv\\Desktop\\p\\textfile.txt", "r")
        data = f.read()
        print("File content:\n", data)
        f.close()
    except:
        print("File not found.")

# Function to append new data to the existing file
def append_data():
    try:
        f = open("C:\\Users\\Dhruv\\Desktop\\p\\textfile.txt", "a")
        content = input("Enter text to append:\n")
        f.write("\n" + content)
        f.close()
        print("Data appended.")
    except:
        print("File not found.")

# Function to perform counting tasks:
# 1. Lines starting with W or H
# 2. Total number of words
# 3. Words starting with T/t
# 4. Words that are 5 letters long
def count_functions():
    try:
        f = open("C:\\Users\\Dhruv\\Desktop\\p\\textfile.txt", "r")
        lines = f.readlines()
        f.close()

        wh_lines = 0
        total_words = 0
        t_words = 0
        five_letter_words = 0

        for line in lines:
            if line.strip().startswith(('W','w','H','h')):
                wh_lines += 1

            words = line.strip().split()
            total_words += len(words)

            for word in words:
                if word.lower().startswith('t'):
                    t_words += 1
                if len(word) == 5:
                    five_letter_words += 1

        # Displaying the results
        print("Lines starting with W or H:", wh_lines)
        print("Total words:", total_words)
        print("Words starting with T/t:", t_words)
        print("5-letter words:", five_letter_words)

    except:
        print("File not found.")

# Function to copy from source.txt to target.txt
# It skips lines that start with '@'
def copy_file():
    try:
        src = open("C:\\Users\\Dhruv\\Desktop\\p\\source.txt", "r")
        tgt = open("C:\\Users\\Dhruv\\Desktop\\p\\target.txt", "w")
        
        for line in src:
            if not line.startswith("@"):
                tgt.write(line)

        src.close()
        tgt.close()
        print("Copied to target.txt without '@' lines.")
    except:
        print("source.txt not found.")

# --------- MAIN MENU LOOP ----------
while True:
    print("\n***** MENU *****")
    print("1. Create a file ‘textfile.txt’")
    print("2. Open an existing file")
    print("3. Append new data")
    print("4. Count functions (All)")
    print("5. Copy source.txt to target.txt (skip lines with @)")
    print("6. Exit")

    ch = input("Enter choice (1-6): ")

    if ch == '1':
        create_file()
    elif ch == '2':
        open_file()
    elif ch == '3':
        append_data()
    elif ch == '4':
        count_functions()
    elif ch == '5':
        copy_file()
    elif ch == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
