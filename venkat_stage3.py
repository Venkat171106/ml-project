name, m1, m2, m3 = input("Enter: ").split(", ")

m1 = int(m1)
m2 = int(m2)
m3 = int(m3)

total = m1 + m2 + m3
percentage = (total / 300) * 100

print(name)
print("Total:", total, "/300")
print("Percentage:", round(percentage,1), "%")

# print grade directly
if percentage >= 75:
    print("Grade is A")

elif percentage >= 60:
    print("Grade is B")

elif percentage >= 40:
    print("Grade is C")

else:
    print("Grade is F")
