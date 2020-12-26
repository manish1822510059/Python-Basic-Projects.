#when only one condition fullfil use 

subs = 1000
likes = 400
comments = 500

cheakers = [subs>200,likes>100,comments>50]

if all(cheakers):
    print('Great Content')