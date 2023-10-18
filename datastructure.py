# list mutable

fruits =["mangoes","oranges","bananas",3,25]
num =[1,3,76,-2,33,8,9,5]
rep=num*2

print(fruits)
fruits[1]="Apples"
print(f"i love eating {fruits[1]}")
print(num)
print(rep)

# Tuples immutable ordered
cars=("toyota", "mercedz","nissan")
print(cars[0])
tup=cars*3
print(tup)
print(tup.count("nissan"))

# sets unordered (doesnt have index)
days={"monday","tuesday","wednesday","thursday","friday"}
print(days)

# dictionaries
staff_details={"Name":"Dume", "Age":26, "Company":"Rubys", "Gender":"Male"}
print(f"Age %d"%staff_details["Age"])
print(f"Company %s"%staff_details["Company"])
print(f"Gender %s"%staff_details["Gender"])
