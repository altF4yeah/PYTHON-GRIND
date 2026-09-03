# converting Numbers to roman numerals

print("-"*50)
print("This program can convert numbers to roman numerals")
print("-"*50)


print()
roman = [
    (1000,"M"),
    (900,"CM"),
    (500,"D"),
    (400,"CD"),
    (100,"C"),
    (90,"XC"),
    (50,"L"),
    (40,"XL"),
    (10,"X"),
    (9,"IX"),
    (5,"V"),
    (4,"IV"),
    (1,"I")
]


num = int(input("Enter the number you want to convert: "))
result = ""
for val, sym in roman:
    while num >= val:
        result += sym
        num -= val

print(result)