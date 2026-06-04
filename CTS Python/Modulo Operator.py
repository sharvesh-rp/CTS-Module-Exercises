def oddoreven(num):
    if(num < 0) or (type(num) != int):
        return "Please enter a positive integer."
    elif(num % 2 == 0):
        return "Even"
    else:
        return "Odd"
    
def main():
    num = int(input("Enter a positive integer : "))
    print(oddoreven(num))

main()