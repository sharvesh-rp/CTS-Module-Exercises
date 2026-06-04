def breakloop(num):
    if num < 0:
        return "Negative Numbers Are Not Allowed"

    for i in range(1, num + 1):
        if i % 2 == 0:
            print("First even number:", i)
            break

def main():
    num = int(input("Enter a number : "))
    result = breakloop(num)
    if result:
        print(result)

main()