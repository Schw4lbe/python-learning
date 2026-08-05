"""
-----------------------------------------------------------
Aufgabe 1: Mystic Code Breaker – Caesar-Chiffre
-----------------------------------------------------------
Ziel:
- Erstellt zwei Funktionen, um einen Text mittels Caesar-Chiffre zu verschlüsseln und wieder zu entschlüsseln.
- Jeder Buchstabe soll um einen bestimmten Shift (zwischen 1 und 25) verschoben werden.
- Groß- und Kleinschreibung bleiben erhalten.
- Nicht-alphabetische Zeichen (z. B. Leerzeichen, Zahlen, Satzzeichen) bleiben unverändert.

Schritte:
1. Schreibt die Funktion `caesar_encrypt(text, shift)`:
   - Lest den zu verschlüsselnden Text und den Verschiebungswert ein.
   - Überprüft, ob der Shift ein Integer zwischen 1 und 25 ist; falls nicht, soll eine
   sinnvolle Fehlermeldung ausgegeben werden.
   - Iteriert über jeden Buchstaben des Textes:
     - Für Großbuchstaben: Verschiebt den Buchstaben innerhalb des Bereichs A–Z.
     - Nicht-Buchstaben werden unverändert übernommen.
     - Für Kleinbuchstaben: Verschiebt den Buchstaben innerhalb des Bereichs a–z.
   - Fügt die verschlüsselten Zeichen zu einem neuen String zusammen und gebt diesen zurück.
2. Schreibt die Funktion `caesar_decrypt(cipher, shift)`:
   - Diese Funktion führt den umgekehrten Prozess durch, sodass aus dem verschlüsselten Text
   wieder der Originaltext entsteht.
3. Testet eure Funktionen mit einem Beispiel:
   - Beispiel: Text = "Mystic Realm" und Shift = 3.
   - Überprüft, ob die Entschlüsselung den ursprünglichen Text ergibt.
"""

import string


class Text:
    UPPER: str = string.ascii_uppercase
    LOWER: str = string.ascii_lowercase
    SHIFT_RANGE_MIN: int = 1
    SHIFT_RANGE_MAX: int = 25

    def __init__(self):
        self.shift: int
        self.text: str
        self.encrypted_text: str


def init_ceasar_chiffre():
    text = Text()
    set_params(text)
    while True:
        menu_select: str = user_menu_select()
        if menu_select == "e":
            toggle_encryption(text, menu_select)
            break

        elif menu_select == "d":
            toggle_encryption(text, menu_select)
            break


def set_params(text: Text):
    text.text = input("input text: ")
    text.shift = validate_shift_input(text)


def toggle_encryption(text: Text, select: str):
    shift = text.shift * (-1) if select == "d" else text.shift
    result: str = ""
    for char in text.text:
        if char.isupper():
            start_index: int = text.UPPER.index(char)
            end_index: int = (start_index + shift) % len(text.UPPER)
            result += result.join(text.UPPER[end_index])

    print(result)
    text.encrypted_text = result


def validate_shift_input(text: Text) -> int:
    while True:
        try:
            user_input_shift: int = int(input("select shift: "))
        except ValueError:
            print("select int")
            continue

        if (
            user_input_shift < text.SHIFT_RANGE_MIN
            or user_input_shift > text.SHIFT_RANGE_MAX
        ):
            print(
                f"pls select value between {text.SHIFT_RANGE_MIN} - {text.SHIFT_RANGE_MAX}"
            )
            continue
        else:
            return user_input_shift


def user_menu_select() -> str:
    while True:
        user_input: str = input("pls select decode (d) or encrypt (e): ")
        if user_input == "d":
            return user_input
        elif user_input == "e":
            return user_input
        else:
            print("select valid option.")
            continue


def main():
    init_ceasar_chiffre()


if __name__ == "__main__":
    main()
