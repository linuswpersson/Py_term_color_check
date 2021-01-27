import colorama
from colorama import init, Fore, Back, Style

## Strängar som används vid utskrivning av brädet
box = (" ---","|"," |", " --- ")


## Arrayer som representerar tre rader av rutor på spelplanen där:
## X = kryss
## pw = vit pessant
## pb = svart pesant
## g = giant
row1 = ["X", 0, "g", "pw", "pb", "pb"]
row2 = [0, "pw", 0, 0, "pw", "pb"]
row3 = ["X", 0, 0, "pb", "pb", "X"]


## En rad av rutor representeras i denna protoryp-design som tre rader av tecken i terminalen. Endast den mittersta kan variera beroende på
## pjäser eller kryss, så den läses av och raden printas ut i sin helhet i tre omgångar dynamiskt.
## proof of concept för senare designer.

## Note: de röda kryssen är för en finare bild i prototypningen, det är inte baserat på kundens önskemål. :)
def print_row(row):
    for x in row:
        print(Fore.BLACK + Back.BLUE + box[0], end='')
    print(Fore.BLACK + Back.BLUE + " ")

    print(Fore.BLACK + Back.BLUE + box[1], end='')
    for x in row:
        if x == 'g':
            print(Fore.WHITE + Back.BLUE + " G", end='')
        elif x == 'pw':
            print(Fore.WHITE + Back.BLUE + " p", end='')
        elif x == 'pb':
            print(Fore.BLACK + Back.BLUE + " p", end='')
        elif x == 'X':
            print(Fore.RED + Back.BLUE + " X", end='')
        else:
            print(Fore.BLACK + Back.BLUE + "  ", end='')
        print(Fore.BLACK + Back.BLUE + box[2], end='')

    print()

    for x in row:
        print(Fore.BLACK + Back.BLUE + box[0], end='')
    print(Fore.BLACK + Back.BLUE + " ")


## En enkelt exempel på hur colorama fungerar
def print_square_black(str):
    print(Fore.BLACK + Back.BLUE + " --- ")
    print(Fore.BLACK + Back.BLUE + "| ", Fore.BLACK + Back.BLUE + str, Fore.BLACK + Back.BLUE + " |", sep='')
    print(Fore.BLACK + Back.BLUE + " --- ")

## En enkelt exempel på hur colorama fungerar
def print_square_white(str):
    print(Fore.BLACK + Back.BLUE + " --- ")
    print(Fore.BLACK + Back.BLUE + "| ", Fore.WHITE + Back.BLUE + str, Fore.BLACK + Back.BLUE + " |", sep='')
    print(Fore.BLACK + Back.BLUE + " --- ")



def main():
    init(autoreset=True)

    print("Test 1: printa ut ensam ruta med ett svart p med en blå bakgrund.")
    print_square_black("p")

    print("Test 2: printa ut ensam ruta med ett vitt G med en blå bakgrund.")
    print_square_white("G")

    print()

    print("Test 3: Printa ut tre rader av ett bräde dynamiskt från en datatyp som representerar pjäsernas och kryssens position.")
    print_row(row1)
    print_row(row2)
    print_row(row3)





if __name__ == "__main__":
    main()
