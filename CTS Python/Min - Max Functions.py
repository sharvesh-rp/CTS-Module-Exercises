def salary_checker(salary):
    for i in salary:
        if i<0:
            return "Invalid Salary"

    print("Highest Salary : " + str(max(salary)))
    print("Lowest Salary : " + str(min(salary)))

def main():
    salary = [50000, 75000, 62500, 95000]
    salary_checker(salary)

main()
    
