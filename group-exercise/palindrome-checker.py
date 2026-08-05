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


def main():
    print("Hello from group-exercise!")


if __name__ == "__main__":
    main()
