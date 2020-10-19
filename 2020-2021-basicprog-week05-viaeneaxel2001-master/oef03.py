MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
MIT = {"1MIT": 58, "2MIT": 36}
Devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

# print(f"{MIT}")


# element ophalen uit een dictionary
print(f"{MIT.get('2MIT')}")
print(f"{MIT['2MIT']}")

# nieuw element toevoegen aan een dictionary
MIT["3MIT"] = 67
print(f"{MIT}")

# nieuw element met dezelfde key toevoegen aan dictionary
MIT["3MIT"] = 1000
print(f"{MIT}")

# checken of een waarde al in gebruik is
if 1000 in MIT.values():
    print("Value bestaat al")
else:
    print(f"Value bestaat nog niet")