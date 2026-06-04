def countdown(count):
    if count <= 0:
        print("Invalid Count Value")
        return
    
    print("Countdown:")
    while count > 0:
        print(count)
        count -= 1

def main():
    count = 5
    countdown(count)

main()