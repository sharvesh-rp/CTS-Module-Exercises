import math 
def areacalculator(radius):
    if radius < 0:
        return "Radius Cannot Be Zero"
    else:
        return (math.pi)*(radius*radius)
    
def main():
    radius = float(input("Enter Radius : "))
    print(f"{areacalculator(radius):.2f}")

main()


