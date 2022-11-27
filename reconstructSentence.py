#This program reads two text file and combines/reconstru the contents to produce a complete output of:
#   This is the companion site for the book Exploring BeagleBone: Tools and Techniques for
#   Building with Embedded Linux Second Edition by Derek Molloy.
#
import sys


# Opens input1 and input2 file
f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")
# read full lines of each files
file1 = f1.readline()
file2 = f2.readline()

#strip newline from each string
file1.strip()
file2.strip()


# splits string into a list of words
line1 = file1.split()
line2 = file2.split()

# reads length of each line
length1 = len(line1)
length2 = len(line2)

print
print ("line1: ", line1)
print
print ("line1 length: ", length1)
print 
print
print ("line2: ", line2)
print
print ("line2 length: ", length2)
print


# Decrement lengths to index of the last element
length1 -= 1
length2 -= 1

#output of the new combined lines
out = []

# adds items to the list until either inputs is empty of contents
while ((length1 > 0) | (length2 > 0)):
    out.append(line1[length1])
    out.append(line2[length2])
    length1 -= 1
    length2 -= 1

# combines remaining contents
while (length1 >= 0):
    out.append(line1[length1])
    length1 -= 1

while (length2 >= 0):
    out.append(line2[length2])
    length2 -= 1

# prints the output
print ("The new line is: ", out)
print

# output of file
f3 = open("output.txt","w")
for i in out:
    f3.write(i + " ")