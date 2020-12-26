#when many condition fullfil use all.

subs = 1000
likes = 400
comments = 500

condition = [subs>150,likes>150,comments>50]

if all(condition):
    print('Great Content')