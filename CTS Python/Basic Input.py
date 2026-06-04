def greet(name):

    if(name == " "  or name == "" or name.isdigit()):
        return "Please Enter A Valid Name"
    else:
        return "Hello " + name + "!"
    
def main():

    name = input("What Is Your Name? : ")
    print(greet(name))

main()