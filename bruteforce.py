f =open(".ijdg.dat", "r")
string = f.readline()
ijdg = int(string)

print("Contenuto bloccato.")
tentativo = input("Inserire la chiave: ")

if tentativo == ijdg:
    print("Contenuto sbloccato.\nChiave inserita GIUSTA!")

else:
    print("Contenuto bloccato.\nChiave inserita SBAGLIATA!")
    print("1: Avvia il bruteforce (Trova la chiave);\n2: Lascia perdere ed esci dal programma.")
    scelta = input()
    
    if scelta == 1:
        for tentativo in range(0, 999999):
            if tentativo == ijdg:
                break
        if tentativo == ijdg:
            print("Chiave: ", tentativo)

        else:
            print("Nessuna chiave trovata.")

    elif scelta == 2:
        print("Arrivederci.")

    else:
        print("Per favore digitare un numero corrispondente alle scelte.")
