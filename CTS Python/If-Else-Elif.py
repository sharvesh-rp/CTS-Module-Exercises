def assign_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Grade A"
    elif score >= 75:
        return "Grade B"
    else:
        return "Grade C"


def main():
    score = float(input("Enter the score (0-100): "))
    print("Your Grade Is:", assign_grade(score))

main()