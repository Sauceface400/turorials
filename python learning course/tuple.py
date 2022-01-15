coordinates = ("k", "l")

print(coordinates)

def sayToName(name, age):
    print("Hello " +name+ " how are you doing " +str(age)+ " very old")
    if name == "Farhan":
        print("Hello sir how are you today")
    elif name == "Jannate":
        print("Hello miss how you/'re doing")
    elif age < 25:
        print(",and shall i say you'/re very young")

sayToName("Farhan",20)