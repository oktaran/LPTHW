from sys import argv                        # imports argv module from sys package

script, filename = argv #                   # assigns argument values

# txt = open(filename)                      # assigns variable for opening the file
#
# print(f"Here's your file {filename}:")    # prints text in "" and name of file
# print(txt.read())                         # reads and prints out the file content
# txt.close()                               # closes file descriptor txt

print("Type the filename again:")           # prints text in ""
file_again = input("> ")                    # requests to type in the file name

txt_again = open(file_again)                # opens a file

print(txt_again.read())                     # reads and prints out the file content
txt_again.close()                           # closes file descriptor txt_again

# print(type(txt_again))
