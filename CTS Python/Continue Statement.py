def continuestatement(num):
    sum = 0
    if num < 0:
        return "Negative Values Will Not Be Allowed"
    elif num > 0:
        for i in range(1,num+1):
            if i % 2 == 0:
                continue
            sum += i
    return sum

def main():
    num = int(input("Enter a positive integer : "))
    result = continuestatement(num)
    if result:
        print("The sum of odd numbers from 1 to", num, "is : ", result)

main()