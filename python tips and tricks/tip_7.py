# square of odd no only single line of code



# odd_squares = []
# for i in range(11):
#     if i % 2 == 1:
#         odd_squares.append(i**2)
odd_squares = [i**2 for i in range(11) if i%2==1]
print(odd_squares)
