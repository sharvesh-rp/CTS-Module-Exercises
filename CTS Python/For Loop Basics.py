def loop(num):
    if num < 0:
        return "Negative Numbers Are Not Allowed"
    if num == "":
        return "Number Limit Cannot Be Empty"
    
    for i in range(1,num):
        print(i, end = " ")

def main():
    num = int(input("Enter a number : "))
    loop(num)

main()