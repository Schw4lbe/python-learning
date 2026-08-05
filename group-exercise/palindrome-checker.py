"""
-----------------------------------------------------------
Aufgabe 2: Palindrome Checker
-----------------------------------------------------------
Ziel:
- Erstellt eine Funktion, die überprüft, ob ein eingegebener Text ein Palindrom ist.
- Dabei sollen alle Zeichen außer Buchstaben ignoriert werden.
- Groß- und Kleinschreibung sollen nicht unterschieden werden.
- Eine leere Zeichenkette (nach Entfernen der Nicht-Buchstaben) gilt nicht als Palindrom.

Schritte:
1. Schreibt die Funktion `is_palindrome(text)`:
   - Entfernt alle Zeichen, die keine Buchstaben sind.
   - Wandelt den verbleibenden Text in Kleinbuchstaben um.
   - Vergleicht den bereinigten Text mit seiner umgekehrten Version (Tipp: Slicing [::-1]).
   - Gibt True zurück, wenn der Text ein Palindrom ist, sonst False.
2. Testet eure Funktion mit Beispielen:
   - Beispiel: "Mystic, citsym!" sollte als Palindrom erkannt werden.
"""

import requests
import json

input_string: str = input("enter word: ")
string_reversed: str = input_string[::-1]

response = requests.get(
    f"https://freedictionaryapi.com/api/v1/entries/en/{input_string}"
)

response_reversed = requests.get(
    f"https://freedictionaryapi.com/api/v1/entries/en/{string_reversed}"
)

data = json.loads(response.text)
data_reversed = json.loads(response_reversed.text)

print(data)
print(data_reversed)

has_entries: bool = len(data["entries"]) > 0
has_entries_reversed: bool = len(data_reversed["entries"]) > 0

print(has_entries == has_entries_reversed)
