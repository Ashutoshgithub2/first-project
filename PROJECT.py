def is_prime(n):
    num = n
    flag = False
    if num == 1:
        print(num, "is not prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is composite number")
            return 1
        else:
            print(num, "is prime number")
            return 2
a,b = input().split(",")
pcount=0
ccount=0
for i in range(int(a), int(b) + 1):
    p=is_prime(i)
    if p==1:
        ccount+=1
    else:
        pcount+=1
print("count:",pcount,"prime and",ccount,"composite numbers in the range")

