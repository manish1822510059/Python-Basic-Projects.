#User Email Address
Email = input("Enter Your Email Address?:").strip()
#slice out The User Name
user_name = Email[:Email.index("@")]


#slice out the Domain name
domain_name = Email[Email.index("@")+1:]

#Seprate Message
res = "Your Username is '{}' and Your Domain Name is '{}'".format(user_name,domain_name)

#result 

print(res)
