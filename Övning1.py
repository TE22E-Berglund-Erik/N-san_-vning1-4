import random

# Skapa en if-sats som skriver ut "Hello, World!" ifall 6 är större än eller lika med 3.
if 6 >= 3:
    print("Hello World")

# Skapa en kod som först hämtar in ett användarnamn från användaren via en Scanner. Gör sedan en if-sats som skriver ut "Welcome!" Ifall användarnamnet är lika med "noname".
# Komplettera föregående kod så att både användarnamn och lösenord efterfrågas. "Welcome" ska skrivas ut enbart om användarnamnet är lika med "noname" och lösenordet är "nopass". Om någon av
användarnamn = input("Skriv in ditt användarnamn: ")
lösenord = input("Skriv in ditt lösenord: ")
if användarnamn == "noname" and lösenord == "nopass":
    print("Welcome!")
else:
    print("Wrong username or password")

# Skriv en loop som skriver ut "Hello, World" 32 gånger. Välj själv om det ska vara en for-loop eller en while-loop.
for i in range(32):
    print("Hello world")

rättLösen = "pass1234"
while lösenord != rättLösen:
    lösenord = input("Skriv in ditt lösenord: ")
    if lösenord == rättLösen:
        print("Korrekt lösen angavs")
    else:
        print("Fel lösen, försök igen!")

# Skriv en loop som körs 5 gånger. Varje gång loopen körs ska användaren skriva in ett tal. Om talet är högre än 5, skriv ut "högre än 5!". Observera att du måste konvertera talet från en String till en int för att kunna göra jämförelsen.
for i in range(5):
    user_input = int(input("Ange ett tal: "))
    if user_input > 5:
        print("högre än 5!")

# Skriv en loop som körs så länge användaren skriver in en string som inte kan konverteras till en int.
while True:
    user_input = input("Skriv in ett tal som kan konverteras: ")
    try:
        int_value = int(user_input)
        print(f"Du skrev in talet: {int_value}")
        break
    except ValueError:
        print("Inmatningen var inte ett giltigt heltal. Försök igen.")

# Skriv en loop som genererar ett slumpmässigt tal mellan 0 och 10 och ber användaren gissa talet.
# Loopen ska fortsätta tills användaren gissar rätt.
randint = random.randint(0, 10)
while True:
    guess = int(input("Gissa ett tal mellan 0 och 10: "))
    if guess > randint:
        print("För högt")
    elif guess < randint:
        print("För lågt")
    else:
        print("Korrekt!")
        break
