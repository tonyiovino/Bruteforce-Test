chiave = 999877

print("Contenuto bloccato.")
tentativo = input("Inserire la chiave: ")

if (tentativo == chiave):
    print("Contenuto sbloccato.\nChiave inerita GIUSTA!")

else:
    print("Contenuto bloccato.\nChiave inserita SBAGLIATA!")
    print("1: Avvia il bruteforce (Trova la chiave);\n2: Lascia perdere ed esci dal programma.")
    scelta = input()

    if (scelta == 1):
        for tentativo in range(0, 999999):
            if tentativo == chiave:
                break
        if tentativo == chiave:
            print("Chiave: ", tentativo)

        else:
            print("Nessuna chiave trovata.")

    elif (scelta == 2):
        print("Arrivederci.")

    else:
        print("Per favore digitare un numero corrispondente alle scelte.")
