#Program polega na kodowaniu oraz dekodowaniu szyfru Cezara. Program umożliwia dowolną zmianę tekstu, oraz liczby przesunięcia. Funkcja caesar_cipher sprawdza czy chcemy kodować lub dekodować i za pomocą pętli for oraz znalezionego indexu w liscie alfabetu zamienia litery o odpowiednio liczbę przesunięcia. Program sprawdza również czy został wpisany tekst oraz czy wpisane przesunięcie jest liczbą.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
menu_number = 0
text = ""
shift = 0

def caesar_cipher(code, text, shift):
    new_text = ""
    if(text == "" or shift == "" or shift == 0):
            print("Nie ma czego szyfrować albo o ile przesunąć")
            return
    if(code == "encrypt"):
        shift = +shift
    elif(code == "decrypt"):
        shift = -shift
    for letter in text:
        if(letter == " "):
            new_text += " "
        else:
            index = alphabet.index(letter)
            new_text += alphabet[index + shift]
    return new_text
    
while(menu_number != 5):
    print("1 - Wpisz tekst")
    print("2 - Liczba do przesunięcia")
    print("3 - Kodowanie")
    print("4 - Dekodowanie")
    print("5 - Zakończenie programu")
    
    menu_number = int(input("Wybierz numer w menu: "))
    
    if(menu_number == 1):
        text = input("Wpisz jakikolwiek tekst: ")
    elif(menu_number == 2):
        try:
            shift = int(input("Wpisz liczbę całkowitą służącą do przesunięcia liter: "))
        except ValueError:
            print("To nie jest liczba!")
    elif(menu_number == 3):
        print(f"Zakodowany tekst: {caesar_cipher('encrypt', text, shift)}")
        text = caesar_cipher("encrypt", text, shift)
    elif(menu_number == 4):
        print(f"Zdekodowany tekst: {caesar_cipher('decrypt', text, shift)}")
        text = caesar_cipher("decrypt", text, shift)
        
        