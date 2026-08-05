"""-----------------------------------------------------------
Aufgabe 3: Anagram Investigator
-----------------------------------------------------------
Ziel:
- Erstellt eine Funktion, die zwei Texte daraufhin überprüft, ob sie Anagramme sind.
- Dabei sollen Leerzeichen ignoriert und beide Texte in Kleinbuchstaben umgewandelt werden.
- Zwei leere Zeichenketten gelten nicht als Anagramme.

Schritte:
1. Schreibt die Funktion `are_anagrams(str1, str2)`:
   - Entfernt aus beiden Texten alle Leerzeichen.
   - Wandelt beide Texte in Kleinbuchstaben um.
   - Sortiert die Zeichen beider Texte (Tipp: Nutzt dazu die Funktion sorted()).
   - Vergleicht die sortierten Listen; stimmen diese überein, so handelt es sich um Anagramme.
2. Testet eure Funktion:
   - Beispiel: "Mystic" und "mytsic" sollten als Anagramme erkannt werden.
"""

string1: str = input("enter word: ")
string2: str = input("enter word: ")

string_list1: list = []
string_list2: list = []


def is_anagram(str1: str, str2: str) -> bool:
    global string1, string2
    string1 = str1.replace(" ", "").lower()
    string2 = str2.replace(" ", "").lower()
    print(string1, string2)

    string_list1 = sorted(string1)
    string_list2 = sorted(string2)

    if string_list1 == string_list2:
        print("is anagram")
        return True
    else:
        print("is not anagram")
        return False


is_anagram(string1, string2)
