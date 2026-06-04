def kgtolbs(kgs):
    
    if kgs < 0:
        return "Kilograms Cannot Be Negative"
    else:
        return kgs * 2.20462
    
def main():

    kgs = float(input("Enter The Weight In Kilograms: "))
    print(kgtolbs(kgs))

main()