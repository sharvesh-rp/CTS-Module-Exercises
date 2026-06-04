def net_salary_calculator(gross_salary, tax_rate):
    if gross_salary < 0:
        return "Gross Salary Cannot Be Negative"
    # Catch invalid tax rates first
    if tax_rate < 0 or tax_rate > 100:
        return "Tax rate must be between 0 and 100"
    # If both inputs are valid, calculate the net salary
    tax_amount = (tax_rate / 100) * gross_salary
    net_salary = gross_salary - tax_amount
    return net_salary
def main():
    gross_salary = float(input("Enter Gross Salary: "))
    tax_rate = float(input("Enter Tax Rate: "))

    result = net_salary_calculator(gross_salary, tax_rate)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Net Salary: {result:.2f}")
main()