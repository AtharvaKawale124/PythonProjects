
basic =int(input("Enter Basic pay="))

hra =(basic*10 /100)
da =(basic*130 /100)
ta =(basic* 5/100)

total =hra +da +ta

pt=(total*2/100)
gross=total+pt

print("HRA=" ,hra)
print("DA=" ,da)
print("TA=" ,ta)
print("************************")
print("Total Salary=" ,total)
print("************************")
print("Gross Salary=" ,gross)

if gross<=10000:
    print("GRADE C employee.")

elif 10000<gross<=25000:
    print("GRADE B employee.")

else:
    print("GRADE A employee.")