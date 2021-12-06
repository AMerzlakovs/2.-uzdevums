import re

x = input("Ievadiet tekstu: ")
text = re.sub(r'\{[^}]*\}', '', x)
print(text)