from math import pi

#Skapa en metod som, när den anropas, skriver ut "Hello, World" 32 gånger. Använd en loop (while eller for) för att sköta upprepningen. Döp metoden till "Hello32".


def Hello32():
    print("Hello World")

for i in range(32):
    Hello32()
    
#Skapa en metod som anropas med en integer som parameter. Skriv ut kvadraten av denna integer.
def Squared(x):
    return x*x

print(Squared(1))
print(Squared(2))
print(Squared(3))


#Skapa en metod som anropas med två doubles eller floats som parametrar. Metoden ska returnera resultatet av den ena parametern multiplicerad med den andra. Döp metoden till "Multi".
def Multi(a,b):
    return a*b

print(Multi(1.5,2.5))
print(Multi(3.5,4.5))
print(Multi(5.5,6.5))



#Skapa en metod för att räkna ut arean på en rätvinklig triangel. Den ska ta emot två doubles eller floats och returnera samma datatyp. Döp metoden till "RightTriangleArea".

def RightTriangleArea(c,b):
    return c*b/2

print(RightTriangleArea(1,2))
print(RightTriangleArea(3,4))
print(RightTriangleArea(5,6))


#Skapa en metod som, på motsvarande sätt, räknar ut arean för en cirkel.
def CirlceArea(r):
    return pi*r*r

print(CirlceArea(1))
print(CirlceArea(2))
print(CirlceArea(3))


#Skapa en metod som hämtar in tal från användaren via konsollen (Scanner). Skapa en loop inuti metoden som inte avslutas förrän användaren skrivit in något som är ett tal. Metoden ska returnera en int som är det tal användaren skrivit in. Metoden ska inte ta emot några parametrar. Döp metoden till GetNumberInput.

def GetNumberInput():
    while True:
        try:
            user_input = input("Skriv in ett tal: ")
            if user_input.isdigit():
                return int(user_input)  
            else:
                print("Ogiltigt, vänligen skriv in ett tal")
        except Exception as e: 
            print(f"Ett fel inträffade: {e}")


print(f"Du skrev in: {GetNumberInput()}")


##Skapa en metod som du döper till GetChoice och som tar emot tre strings som parametrar. Skriv ut de tre stringvärdena så att användaren ser dem. Metoden ska sedan låta användaren välja mellan de tre, t.ex. genom att skriva 1, 2 eller 3. Metoden ska inte avslutas innan användaren skrivit in ett giltigt svar. Metoden ska returnera en int som motsvarar användarens val.
#Förbättra: Gör så att metoden istället tar emot en string-array som parameter. Använd en loop för att skriva ut de olika stringvärdena och bygg om metoden så att den inte bara fungerar för tre alternativ utan för det antal som stoppas in i arrayen; om man t.ex. stoppar in en string-array med fyra värden så ska användaren få välja mellan fyra olika alternativ.

def GetChoice(choices):
    for i, choice in enumerate(choices):
        print(f"{i+1}: {choice}")
    
    choice = int(input(f"Välj ett utav valen (1-{len(choices)}):"))
    return choice
    
choices = []
print("Vänligen skriv in dina val (skriv ""klar"" när du är klar): ")
while True:
    choice = input()
    if choice == "klar":
        break   
    elif choice.strip():
        choices.append(choice)
    
    
print(f"Du valde val nummer {GetChoice(choices)}")
