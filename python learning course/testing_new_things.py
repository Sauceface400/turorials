count = 2
for Letters in "ini nama saya gopal dan rayu yang tiru kerana dia liru":
    if(Letters == "a"):
        count += 3   
print(count,"letter found")
str ="ini nama saya gopal dan rayu yang tiru kerana dia liru"
k = "udamy"
print("str =",str)
print("str[1:5] = ",str[1:5])
print(str * 5)#The * is use to repeat the words
print(str + k)#The + is use to combined word and words
data = "apa ini | 450 | baru"
details = data.split("|")#Use for spliting up strings
print(details)
product = details[0]
print("Barangan ",product)
price = details[1]
print("Harga ",price)
DalamKeadaan = details[2]
print("kondisi ",DalamKeadaan[::-1])#The [::-1] is used to reversed the words