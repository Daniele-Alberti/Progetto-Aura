import serial
import struct
import datetime as dt
import json
import tkinter as tk

arduino = serial.Serial("COM4", 9600)

def LetturaSensore():
    label.config(text="Lettura Aura in corso...")
    startButton.config(state=tk.DISABLED)

    seriale = arduino.read(32)
    dati = struct.unpack("2s 4s 4s 2s 4s 16s", seriale)

    valoreSensore = dati[4].decode()

    tempo = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    salva_json(tempo, valoreSensore)
    genera_html()

    window.after(1000, LetturaSensore)

def salva_json(data, valore):

    try:
        with open("db.json", "r") as f:
            dati = json.load(f)
    except:
        dati = []

    dati.append({
        "data": data,
        "valore": valore
    })

    with open("db.json", "w") as f:
        json.dump(dati, f, indent=4)

def cancella_json():
    with open("db.json", "w") as f:
        json.dump([], f, indent=4)
    label.config(text="Aura azzerata")
    startButton.config(state=tk.NORMAL)


def genera_html():

    try:
        with open("db.json", "r") as f:
            dati = json.load(f)
    except:
        dati = []

    righe = ""

    for d in reversed(dati[-5:]):
        righe += f"<tr><td>{d['data']}</td><td>{d['valore']}</td></tr>"

    html = intestazioneHtml + righe + chiusuraHtml

    with open("index.html", "w") as f:
        f.write(html)

window = tk.Tk()
window.title("Lettura sensore")
window.geometry("500x200")
startButton = tk.Button(window, text="Aura input", command=LetturaSensore)
startButton.pack(pady=20)
label = tk.Label(window, text="Aspetto Aura input...")
label.pack(pady=20)
cleanButton = tk.Button(window, text="Azzera Aura", command=cancella_json)
cleanButton.pack(pady=10)


intestazioneHtml = """
<html>
<head>
<title>Lettura Aura</title>
<style>
    body {
        font-family: Arial, sans-serif;
        font-size: 24px;
    }
    table {
        border-collapse: collapse;
        width: 80%;
        margin: 20px auto;
        font-size: 24px;
    }
    th, td {
        border: 1px solid black;
        padding: 10px;
        text-align: center;
    }
    h1 {
        text-align: center;
        font-size: 36px;
    }
</style>
</head>
<body>
<h1>Tabella Aura</h1>
<table>
<tr>
<th>Data</th>
<th>Valore sensore</th>
</tr>
"""

chiusuraHtml = """
</table>
</body>
</html>
"""


if __name__ == "__main__":
    window.mainloop()