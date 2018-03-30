from sys import argv                                # install argv feature from sys package

script, input_file = argv                           # unpack argv values

def print_all(f):                                   # create function with one argument f
    print(f.read())                                 # function will read and print content of argument f

def rewind(f):                                      # create function with one argument f
    f.seek(0)                                       # function will set pointer to the beginning of the argument f

def print_a_line(line_count, f):                    # create function with 2 arguments
    print(line_count, f.readline(), end = "")       # function will read one line from the f argument and print it

current_file = open(input_file)                     # variable current_line is assigned to open input_file

print("First let's print the whole file:\n")        # print text in " "

print_all(current_file)                             # call function which will read and print the content of the current file

print("Now let's rewind, kind of like a tape.")     # print text in " "

rewind(current_file)                                # function will set pointer to the beginning of the current file

print("Let's print three lines:")                   # print text in " "

current_line = 1                                    # current line is assigned to 1
print_a_line(current_line, current_file)            # call function which will print line_count = current_line = 1 read line in the beggining of the file

current_line += 1                                   # current_line is assigned to be +1 from the current line
print_a_line(current_line, current_file)            # call function which will print current_line + 1 = 2 and read next line after previous operation

current_line += 1                                   # current_line is assigned to be +1 from the current line
print_a_line(current_line, current_file)            # call function which will print current_line + 1 = 3 and read next line after previous operation

current_file.close()
