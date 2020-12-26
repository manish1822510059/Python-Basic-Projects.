#using set and key to count most repeted value in list

a = [1,3,4,6,8,2,14,1,7,8,2,5,9,4,12]
print(a)
most = max(set(a),key= a.count)
print(most)