# Given 3 positive integers, find the sum of all numbers between the first two that are a multiple of the third. eg. Given "1, 10, 2", the expected output is "20". --> 2,4,6,8 - 20
# 3 positive integers; 1,36,6 --> 6,12,18,24 --> sum of multiples = 60

# count = 0
# for i in range(1,36): 
#     if i == 36:
#         count += 1 
# print(count)
a=0
b=10
c=2
sum = 0
for i in range (a,b,c):
    print(i)
    sum += i
print(sum) 
# range already lists multiples of c (idk why)
# += means sum +1 
