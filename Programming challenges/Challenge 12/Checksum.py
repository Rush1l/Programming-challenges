

def user_input():
    card = input("Enter card number: ")
    if len(card) < 16:
        print ('Too short')
        user_input()
    elif len(card) > 16:
        print ('Too long')
        user_input()
    else:
        return card


def PAN(card):
    number = card[6:15]
    return number

def checksum(card):
    digit = card[-1]
    return digit


def issuer(card):
    company = 0
    if card[0:2] == 37 or 34:
        company = ("American Express")
    elif card[0] == 3:
        company = ("JCB")
    elif card[0] == 4:
        company = ("Visa")
    elif 55>= card[0:2] >= 51: ##or =<55
        company == ("MasterCard")
    return company

def valid(card):
    s = (int(card[14])*2)+(int(card[12])*2)+(int(card[10])*2)+(int(card[8])*2)+(int(card[6])*2)+(int(card[4])*2)+(int(card[2])*2)+(int(card[0])*2)
    s = s + int(card[13]) + int(card[11])+int(card[9])+int(card[7])+int(card[5])+int(card[3])+int(card[1])
    check_digit = (10 - (s%10)) % 10
    if check_digit == card[15]:
        return "Valid card number entered"
    else:
        return "Invalid card number entered"
    
    
    
CARD = user_input()
pan = PAN(CARD)
brand = issuer(CARD)
check = valid(CARD)
print(f"Card number = {CARD}")
print(f"Issuer = {brand}")
print(check)
          






