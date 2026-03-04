import serial
import struct
import datetime as dt
import json
import tkinter as tk

arduino = serial.Serial("COM4", 9600)

def LetturaSensore():
    seriale = arduino.read(32)
    dati = struct.unpack("2s 4s 4s 2s 4s 16s", seriale)

    id = dati[0].decode()
    mittente = dati[1].decode()
    destinatario = dati[2].decode()
    tipo = dati[3].decode()
    valoreSensore = dati[4].decode()
    vuoto = dati[5].decode()
    
    labelvalore.configure(text=f"Data lettura: {dt.datetime.now()}\tValore: {valoreSensore}")
    window.after(100, LetturaSensore)

    html = open("index.html", "w")
    dato = f"\t\t\t<tr><td>{dt.datetime.now()}</td><td>{valoreSensore}</td></tr>"
    stringagrossa = intestazioneHtml + dato + chiusuraHtml
    html.write(stringagrossa)
    html.close()

    data_json = {"data": str(dt.datetime.now()), "valore": valoreSensore}
    with open("db.json", "a") as json_file:
        json_file.write(json.dumps(data_json) + "\n")
    json_file.close()
    

window = tk.Tk()
window.title("Lettura sensore")
window.geometry("1500x500")
labelvalore = tk.Label(window, text="Valore: ", font=("Arial", 20))
labelvalore.grid(column=0, row=1)
button = tk.Button(window, text="Avvia lettura", command=LetturaSensore)
button.grid(column=0, row=0)


intestazioneHtml = """
<html>
    <head>
        <title>Lettura sensore</title>
    </head>
    <body>
        <h1>Tabella valori</h1>
        <table>
            <tr>
                <td>data</td>
                <td>valore sensore</td>
            </tr>
"""
chiusuraHtml = """
		</table>
	</body>
</html>
"""

if __name__ == "__main__":

    window.mainloop()
        
        