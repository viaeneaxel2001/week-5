def print_tuple(naam, tuple):
    for item in tuple:
        print(f"{item} zit op positie {tuple.index(item)} ")


tuple1 = ("1MIT", "2MIT")
print_tuple("lijst van de beste opleiding", tuple1)
