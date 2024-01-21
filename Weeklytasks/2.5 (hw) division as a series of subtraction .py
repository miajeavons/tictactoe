# Implement division as a series of subtraction. The program should only deal with integers and report the remainder if there is one. eg. 10/2 => 10-2-2-2-2-2=0, 10 minus 2 five times so the division result is 5 with a remainder of 0
a = 10 
b = 2

# solution 1 
# for i in range(1,a):
#     a = a - b
#     if a -b < 0:
#         print (i)
#         print("remainder:", a)
#         break 

# solution 2
divisor = 0
while a - b >= 0:
    a-=b 
    divisor += 1
print ("remainder:",a)
print (divisor)

# >= means greater than or equal to
# -= means a = a-b
# += means divisor = divisor + 1