i = 0
while i<10:
    print(i)
    i=i+1
print(i)
for i in range(10): #counts 1 by 1 from to to 9, not includes 10
    print(i)

for i in range(0,100,7): #multiples of 7 less than 100
    print(i)

for i in range(20):
    #add code here to print multiples of 7
    print(i*7)

for i in range(1,11):
    for j in range(i,11): # this can use variables
        print(f"{i}*{j}={i*j}")
    print()
