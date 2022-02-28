for x in range (1, 151):
    print (x)



for y in range (5, 1001):
    if y%5 == 0:
        print(y)

for j in range (1, 101):
    if j%10==0:
        print ("Coding Dojo")
    
    elif j%5 ==0:
        print ("Coding")
    
    else:
        print(j)
        


sum= 0

for number in range (0, 500001):
    if number%2 != 0:
        sum += number

print(sum)

for j in range (2018, 0, -4):
    print(j)

print(0)


lowNum = 2
highNum= 9
mult = 3




for number in range (lowNum, highNum+1):
    if number%mult == 0:
        print(number)
