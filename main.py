from turtledemo.penrose import start

lista_zadan = [
    ["nauka pythona", "23-8-2025", "do zrobienia"],
    ["ogar samochodu", "23-8-2025", "do zrobienia"]
]
do_zrobienia = 0
zrobione = 0
for nr,zadanie in enumerate(lista_zadan, start=1):
    print(f"{nr}. {zadanie[0]} {zadanie[1]} {zadanie[2]}")
    status = zadanie[2]

    if status == "do zrobienia":
        do_zrobienia += 1
    elif status == "zrobione":
        zrobione += 1
print(f"Do zrobienia: {do_zrobienia}")
print(f"Zrobione: {zrobione}")

wybor = input("Wybierz zadanie do odznaczenia zrobione: ")
nr = int(wybor)
lista_zadan[nr -1][2] = "zrobione"
do_zrobienia = 0
zrobione = 0

for nr,zadanie in enumerate(lista_zadan, start=1):
    status = zadanie[2].strip().lower()
    print(f"{nr}.{zadanie[0]} {zadanie[1]} {zadanie[2]}")
    if status == 'do zrobienia':
        do_zrobienia += 1
    elif status == 'zrobione':
        zrobione += 1
print(f"Do zrobienia: {do_zrobienia}")
print(f"Zrobione: {zrobione}")

while True:
    wybor1 = input(
        "Wybierz zadanie:\n"
        "1 - pokaż\n"
        "2 - dodaj\n"
        "3 - oznacz zrobione\n"
        "4 - statystyki\n"
        "0 - wyjście\n"
        "Twój wybór: "
    )
    if wybor1 == "0":
        break
    elif wybor1 == "1":
        for nr, zadanie in enumerate(lista_zadan, start=1):
            print(f"{nr}. {zadanie[0]} {zadanie[1]} {zadanie[2]}")
    elif wybor1 == "2":
        nazwa = input("Wpisz zadanie: ")
        data = input("Wpisz date: ")
        status = input("Wpisz status: ")
        lista_zadan.append([nazwa, data, status])
        print("dodano zadanie!")
    elif wybor1 == "3":
        do_zrobienia = 0
        zrobione = 0
        for nr, zadanie in enumerate(lista_zadan, start=1):
            print(f"{nr}. {zadanie[0]} {zadanie[1]} {zadanie[2]}")
        wybor = input("Wybierz zadanie do odznaczenia zrobione: ")
        nr = int(wybor)
        lista_zadan[nr - 1][2] = "zrobione"
        for nr, zadanie in enumerate(lista_zadan, start=1):
            status = zadanie[2].strip().lower()
            print(f"{nr}.{zadanie[0]} {zadanie[1]} {zadanie[2]}")
            if status == 'do zrobienia':
                do_zrobienia += 1
            elif status == 'zrobione':
                zrobione += 1
        print(f"Do zrobienia: {do_zrobienia}")
        print(f"Zrobione: {zrobione}")
        for nr, zadanie in enumerate(lista_zadan, start=1):
            print(f"{nr}. {zadanie[0]} {zadanie[1]} {zadanie[2]}")
    elif wybor1 == "4":
        do_zrobienia = 0
        zrobione = 0
        wszystkie = len(lista_zadan)
        for zadanie in lista_zadan:
            status = zadanie[2].strip().lower()
            if status == 'do zrobienia':
                do_zrobienia += 1
            elif status == 'zrobione':
                zrobione +=1
            else:
                print("Nieznany status: ", status)
        print(f"Wszystkie: {wszystkie}")
        print(f"Do zrobienia: {do_zrobienia}")
        print(f"Zrobione: {zrobione}")
        if wszystkie >0:
            procent = (zrobione/wszystkie) * 100
            round(2)
            print(f"Progres: {procent}", f"%")
        else:
            print("Brak zadań na liście.")




