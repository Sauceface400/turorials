value = 0
score = value

print("What is the capital city of Malaysia?")
question_1 = input("a)KL\nb)JB\nc)KB\n:")

if question_1.lower() == "a":
    print("correct")
    value = value + 1
else:
    print("Wrong the answer is KL")

print("When did melaya gain independance from the British?")
question_2 = input("a)16sept1963\nb)21sept1980\nc)31Aug1957\n:")

if question_2.lower() == "c":
    print("correct")
    value = value + 1
else:
    print("Wrong the answer is 31Aug 1957")

print("What is Parameswara islamic name")
question_3 = input("a)Tun Tebat\nb)Iskandar Shah\nc)Ong Ling Lwok\n:")

if question_3.lower() == "b":
    print("correct")
    value = value + 1
else:
    print("Wrong the answer is Iskandar Shah")

print("How many state's are there in Malaysia")
question_4 = input("a)13\nb)10\nc)1\n:")

if question_4.lower() == "a":
    print("correct")
    value = value + 1
else:
    print("Wrong the answer is 13")

print("You've got 4 out of " + str(value))


if value == 4:
    print("genuis")
elif 0 < value < 4:
    print("average")


