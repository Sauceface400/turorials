test1 = [1]
print(test1,'is',bool(test1))
apahalkau = 'giga is gay' 
print(apahalkau,'is',bool(apahalkau))
test1 = None
print(test1,'is',bool(test1))
test1 = 0.0
print(test1,'is',bool(test1))
test1 = []
print(test1,'is',bool(test1))
test1 = 0j
print(test1,'is',bool(test1))
africa = "continent"
print(africa,bool(africa))
gay = True 
jack = False
print (gay and jack)
print(gay or jack)
print (not True)
print(not False)
print (not (True or False))
print (not (True and False))
Catherine_throws_out_the_garbage = True
Catherine_Scores_straight_A = True
if Catherine_throws_out_the_garbage and Catherine_Scores_straight_A:
    print("she can go out with her friends")
print(not(Catherine_Scores_straight_A)and(Catherine_throws_out_the_garbage))
print(not(Catherine_Scores_straight_A) or (Catherine_throws_out_the_garbage))



MYR_USD = 0.23
MYR_IDR = 3300
MYR_KWD = 0.07
MYR_KW = 283.86
MYR_INR = 17


def money (currency):
    print(MYR_IDR * currency)
    print(MYR_KWD * currency)
    print(MYR_KW * currency)
    print(MYR_INR * currency)
        
def  money (currency):
    return {"MYR_IDR" : 3300, "MYR_KWD" : 0.07, "MYR_KW" : 283.86, "MYR_INR" : 17, "MYR_USD" : 0.23}[currency]
print (4*money("MYR_IDR")) #Currrency exchange rate shortcut

