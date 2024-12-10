import random

# Skapa en string-array med namnen på fem olika leksaker.
leksaker = ["Lego", "Docka", "Boll", "Teddybjörn", "Racerbil"]

# Skriv en for-loop (eller foreach-loop) som skriver ut namnet på varje leksak på en egen rad.
for leksak in leksaker:
    print(leksak)

#Skapa en string-array med namnen på fem av dina klasskamrater.
namn = ["Tådor", "Blublig", "Slevis", "Zuttengren", "Hassan"]
#Skapa en integer-array med fem värden mellan 0 och 10.
betyg = [5, 2, 4, 9, 8]

#Komplettera for-loopen så att den på varje rad skriver ut något liknande "Pelle ger Barbie betyget 5". Använd dina klasskamraters namn, leksakernas namn och värdena från int-arrayen.
for i in range(len(namn)):
    print(f"{namn[i]} ger {leksaker[random.randint(0,len(leksaker)-1)]} {betyg[random.randint(0,len(betyg)-1)]} utav 10")
    
#Skapa en tom string-lista som heter "cities".
cities = [""]

#Skapa en loop där du varje gång loopen körs hämtar en string från användaren med hjälp av en Scanner. Lägg till den string du får från användaren till cities-listan. Avbryt loopen om användaren skriver "exit".
while True:
    city = input("Skriv namnet på en stad: ")
    if city != "exit":
        cities.append(city)
    if city == "exit":
        break
#Skapa en loop som ligger efter den ovanstående. Den här loopen ska skriva ut alla strings som finns sparade i cities-listan.
print("Sparade städer:")
for city in cities: 	
    print(city)

    
        
    


