def split_bill(total_bill,people):
    if (people <= 0) and (total_bill <= 0):
        return "Number Of People And Total Bill Amount Must Be Greater Than Zero"
    else:
        return total_bill // people
    
def main():
    total_bill = int(input("Enter Total Bill Amount : "))
    people = int(input("Enter Number Of People : "))
    print(split_bill(total_bill,people))

main()