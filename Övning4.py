# Skapa klassen Book. Den ska ha de publika variablerna name och pages. Skapa tre instanser av book och ge varje instans ett eget namn och antal sidor.
class Book:

    def __init__(self, name, pages):
        self.__name = name
        self.__pages = pages
        self.__currentPage = 0

    def TurnPage(self):
        self.__currentPage += 1

    def GetCurrentPage(self):
        return self.__currentPage

    def GetName(self):
        return self.__name

    def GetPages(self):
        return self.__pages


book1 = Book("Harry Potter", 320)
book2 = Book("The 48 Laws of Power", 1337)
book3 = Book("Sagan Om Ringen", 560)

book1.TurnPage()
print(book1.GetCurrentPage())
print(book1.GetName())
print(book1.GetPages())


# Skapa klassen Rock. Den behöver ha den privata variabeln weight och en konstruktor. Konstruktorn ska ta emot en vikt och spara denna i den privata variabeln weight. Klassen behöver också en metod som du döper till GetWeight. Den metoden ska inte ta emot några parametrar, men returnera värdet som weight har. Skriv kod som låter användaren ange hur många stenar som ska skapas, och som sedan skapar så många instanser av klassen Rock. Varje instans ska stoppas in i listan rockList. Innan varje sten skapas så ska programmet fråga användaren hur mycket stenen ska väga, och den informationen ska sedan stoppas in i den nya instansen genom dess konstruktor.
class Rock:
    def __init__(self, weight):
        self.__weight = weight

    def GetWeight(self):
        return self.__weight


rockList = []
amount = int(input("Hur många stenar ska skapas (int)"))

for i in range(amount):
    weight = input("Ange vikten på din sten: ")
    rockList.append(Rock(weight))


# Skapa basklassen Worker som har de variablerna name, age och wage som alla är protected. Name och Age ska ges värden genom klassens konstruktor. Wage börjar på 0 men det ska finnas en metod som heter SetWage som bestämmer lönens värde. Dessutom ska det finnas metoder som heter GetName, GetAge och GetWage. De ska returnera värdet som sparats i name, age respektive wage.Skapa klasserna BlueCollar och WhiteCollar som ärver från Worker-klassen. BlueCollar ska ha metoderna Build, Repair och Destroy. WhiteCollar ska ha metoderna DrinkCoffee, AttendMeeting och DoSpreadsheets. De här metoderna behöver inte ha något innehåll eller returnera något; om du vill kan du låta dem printa något roligt när de körs. Skapa en instans vardera av Worker, WhiteCollar och BlueCollar. Se till så att det går att köra SetWage, GetWage, GetName och GetAge för alla instanser.
class Worker:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._wage = 0

    def SetWage(self, wage):
        self._wage = wage

    def GetName(self):
        return self._name

    def GetAge(self):
        return self._age

    def GetWage(self):
        return self._wage


class Whitecollar(Worker):
    def __init__(self, name, age):
        super().__init__(name, age)

    def DrinkCoffee(self):
        print(f"{self.GetName()} is drinking coffee")

    def AttendMeeting(self):
        print(f"{self.GetName()} is attending a meeting")

    def DoSpreadSheets(self):
        print(f"{self.GetName()} is doing spreadsheets")


class Bluecollar(Worker):
    def __init__(self, name, age):
        super().__init__(name, age)

    def Build(self):
        print(f"{self.GetName()} is building")

    def Repair(self):
        print(f"{self.GetName()} is repairing")

    def Destroy(self):
        print(f"{self.GetName()} is destroying")


worker1 = Worker("Pelle", 25)


# Skapa basklassen Hardware som ska beskriva olika hårdvarudelar i en dator. Hardware-klassen ska beskriva några egenskaper som är gemensamma för olika sorters hårdvara, till exempel namn och pris. Gör så att dessa egenskaper ska anges i konstruktorn och sparas i privata variabler. Skapa också metoder för att hämta informationen som sparas i de privata variablerna. Skapa subklasser för hårddiskar, processorer och grafikkort. De ska alla ärva från Hardware. Se till så att varje klass sparar några nya variabler som är unika för just den typ av hårdvara klassen beskriver, t.ex. att processorklassen sparar information om antal kärnor och processorns klockhastighet. Se till så att de nya variablerna är privata och har metoder som används för att bestämma deras värden och hämta ut värdena igen.
class Hardware:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Hardware: {self.name}, Price: ${self.price}"


class Processors(Hardware):
    def __init__(self, name: str, price: float, cores: int, ghz: float):
        super().__init__(name, price)
        self.cores = cores
        self.ghz = ghz

    def __str__(self):
        return f"Processor: {self.name}, Price: ${self.price}, Cores: {self.cores}, GHz: {self.ghz}"


class GraficCards(Hardware):
    def __init__(self, name: str, price: float, ghz: float, vram: int):
        super().__init__(name, price)
        self.ghz = ghz
        self.vram = vram

    def __str__(self):
        return f"Graphics Card: {self.name}, Price: ${self.price}, Cores: {self.cores}, GHz: {self.ghz}, VRAM: {self.vram}GB"


class HardDrives(Hardware):
    def __init__(self, name: str, price: float, storage: int):
        super().__init__(name, price)
        self.storage = storage

    def __str__(self):
        return f"Hard Drive: {self.name}, Price: ${self.price}, Storage: {self.storage}GB"


differentparts = {
    1: "Processor",
    2: "Graphics Card",
    3: "Hard Drive"
}

storedHardwares = []

while True:
    try:
        for i, part in differentparts.items():
            print(f"{i} {part}")
        choice = int(input(f"Ange ett nummer (1-{len(differentparts)}): "))
        if choice < 1 or choice > len(differentparts):
            print("Ogiltig inmatning, försök igen.")
            continue

        print(f"Du valde: {differentparts[choice]}")

        if choice == 1:  
            name = input("Ange namnet på processorn: ")
            price = float(input("Ange priset på processorn: "))
            cores = int(input("Ange antalet kärnor: "))
            ghz = float(input("Ange klockfrekvensen (GHz): "))
            storedHardwares.append(Processors(name, price, cores, ghz))

        elif choice == 2:  
            name = input("Ange namnet på grafikkortet: ")
            price = float(input("Ange priset på grafikkortet: "))
            ghz = float(input("Ange klockfrekvensen (GHz): "))
            vram = int(input("Ange mängden VRAM (GB): "))
            storedHardwares.append(GraficCards(name, price, ghz, vram))

        elif choice == 3:  
            name = input("Ange namnet på hårddisken: ")
            price = float(input("Ange priset på hårddisken: "))
            storage = int(input("Ange lagringsutrymme (GB): "))
            storedHardwares.append(HardDrives(name, price, storage))

        more = input("Vill du lägga till en annan hårdvara? (j/n): ").lower()
        if more != 'j':
            break

    except ValueError:
        print("Ogiltig inmatning, ange ett giltigt nummer.")


print("\nLagrad hårdvara:")
for hardware in storedHardwares:
    print(hardware)



    
