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


class Rock:
    def __init__(self, weight):
        self.__weight = weight

    def GetWeight(self):
        return self.__weight


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
    def DrinkCoffee(self):
        print(f"{self.GetName()} is drinking coffee")

    def AttendMeeting(self):
        print(f"{self.GetName()} is attending a meeting")

    def DoSpreadSheets(self):
        print(f"{self.GetName()} is doing spreadsheets")


class Bluecollar(Worker):
    def Build(self):
        print(f"{self.GetName()} is building")

    def Repair(self):
        print(f"{self.GetName()} is repairing")

    def Destroy(self):
        print(f"{self.GetName()} is destroying")


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
    def __init__(self, name: str, price: float, vram: int):
        super().__init__(name, price)
        self.vram = vram

    def __str__(self):
        return f"Graphics Card: {self.name}, Price: ${self.price} VRAM: {self.vram}GB"


class HardDrives(Hardware):
    def __init__(self, name: str, price: float, storage: int):
        super().__init__(name, price)
        self.storage = storage

    def __str__(self):
        return f"Hard Drive: {self.name}, Price: ${self.price}, Storage: {self.storage}GB"


def main_menu():
    while True:
        print("\nHuvudmeny:")
        print("1. Bokprogram")
        print("2. Stenprogram")
        print("3. Arbetsprogram")
        print("4. Hårdvaruprogram")
        print("5. Avsluta")

        choice = input("Välj ett program (1-5): ")

        if choice == '1':
            book_program()
        elif choice == '2':
            rock_program()
        elif choice == '3':
            worker_program()
        elif choice == '4':
            hardware_program()
        elif choice == '5':
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val, försök igen.")


def book_program():
    print("\n Bookprogram \n")
    book1 = Book("Harry Potter", 320)
    book2 = Book("The 48 Laws of Power", 1337)
    book3 = Book("Sagan Om Ringen", 560)

    book1.TurnPage()
    print(book1.GetCurrentPage())
    print(book1.GetName())
    print(book1.GetPages())


def rock_program():
    print("\n Rockprogram \n")
    rockList = []
    amount = int(input("Hur många stenar ska skapas (int): "))

    for i in range(amount):
        weight = input("Ange vikten på din sten: ")
        rockList.append(Rock(weight))

    print("Stenar skapade:")
    for rock in rockList:
        print(f"Sten vikt: {rock.GetWeight()}")


def worker_program():
    print("\n Workerprogram \n")
    worker1 = Worker("Pelle", 25)
    worker1.SetWage(30000)
    print(worker1.GetName(), worker1.GetAge(), worker1.GetWage())

    whitecollar = Whitecollar("Anna", 30)
    whitecollar.SetWage(40000)
    whitecollar.DrinkCoffee()

    bluecollar = Bluecollar("Karl", 40)
    bluecollar.SetWage(35000)
    bluecollar.Build()


def hardware_program():
    print("\n Hardware \n")
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

            more = input(
                "Vill du lägga till en annan hårdvara? (j/n): ").lower()
            if more != 'j':
                break
        except ValueError:
            print("Ogiltig inmatning, försök igen.")

    print("\nLagrad hårdvara:")
    for hardware in storedHardwares:
        print(hardware)


main_menu()
