def age_calculator(age):
    if age < 0:
        return "Age Cannot Be Negative"
    else:
        return "Next Year Your Age Will Be " + str(age + 1)
    
def main():
    age = int(input("Enter Your Age: "))
    print(age_calculator(age))

main()
