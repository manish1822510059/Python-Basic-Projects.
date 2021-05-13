from tabulate import tabulate
data = [["Name","Place","Gender"],["Aman","NewDelhi","Male"],["Hritika","New Delhi","Male"]]

# print(tabulate(data))
# print(tabulate(data,headers="firstrow"))
# print(tabulate(data,headers="firstrow",tablefmt='grid'))
print(tabulate(data,headers="firstrow",tablefmt='fancy_grid'))