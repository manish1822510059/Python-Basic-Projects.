import random
import os
passlen = int(input("Enter the Length of Password: "))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!~@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print(p)
value  = "Your Generated password is:",p
with open('workfile1.txt','w')as f:
    s=str(value)
    f.write(s)