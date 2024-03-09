usr = input("Enter the numbers you want to sum up to: ")

#Handle any error
usr.strip()
if not usr.isdigit() or int(usr) <= 0:
    print("Enter a valid user input")
    exit(0)

sum = 0
for i in range(0,int(usr) + 1):
    sum += i

print(f"The sum is {sum}")

