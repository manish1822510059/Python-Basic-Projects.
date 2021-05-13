from tabulate import tabulate
data = [["Name","Place","Gender"],["Manish","Noida","Male"],["Hritika","New Delhi","Male"],["pooja","Greater Noida","Female"]]

# print(tabulate(data))
# print(tabulate(data,headers="firstrow"))
# print(tabulate(data,headers="firstrow",tablefmt='grid'))
print(tabulate(data,headers="firstrow",tablefmt='fancy_grid'))
