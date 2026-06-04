def grade_decider(mark):
    if mark < 0:
        return "Marks Cannot Be Negative"
    elif mark > 100:
        return "Marks Cannot Be Greater Than 100"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"
    
def main():
    mark = float(input("Enter Your Mark : "))
    print(grade_decider(mark))

main()