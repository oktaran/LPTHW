from sys import argv
# from os.path import exists

_, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# indata = open(from_file).read()

# read
src_fd = open(from_file, 'r')
src_data = src_fd.read()

# write
dst_fd = open(to_file, 'w')
dst_fd.write(src_data)

# close
src_fd.close()
dst_fd.close()

# with open(from_file, 'r') as indata:
#     data = indata.read()
#
# print(data)

# indata = open(from_file).read()


# # print(f"The input file is {len(indata)} bytes long")
#
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# open(to_file, 'w').write(indata)




# print("Alright, all done.")

# out_file.close()
# in_file.close()
