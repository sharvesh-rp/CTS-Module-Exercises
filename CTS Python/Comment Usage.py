def commentprogram(base,salary): #Defines a function called commentprogram that takes two parameters: base and salary
    
    if base and salary <= 0: #Checks if either base or salary is less than 0

        return "Error: Base and salary must be positive" #Returns an error message if either base or salary is less than 0
    
    return base + salary #Returns Total Salary

def main():

    base = float(input("Enter The Base Salary: ")) #Prompts The User To Enter The Base Salary And COnverts It To A Float
    salary = float(input("Enter The Salary: ")) #Prompts The User To Enter The Salary And COnverts It To A Float

    total_salary = commentprogram(base, salary) #Calls The commentprogram Function With The Base And Salary As Arguments And Stores The Result In total_salary
    print("Total Salary:", total_salary) #Prints The Total Salary

main() #Calls The main Function To Execute The Program