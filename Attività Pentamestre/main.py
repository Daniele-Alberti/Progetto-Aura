import serial
import struct
import datetime as dt

arduino = serial.Serial("COM4", 9600)

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

    while True:
        seriale = arduino.read(32)
        dati = struct.unpack("2s 4s 4s 2s 4s 16s", seriale)

        id = dati[0].decode()
        mittente = dati[1].decode()
        destinatario = dati[2].decode()
        tipo = dati[3].decode()
        valoreSensore = dati[4].decode()
        vuoto = dati[5].decode()
        
        print(f"id: {id}")
        print(f"mittente: {mittente}")
        print(f"destinatario: {destinatario}")
        print(f"tipo: {tipo}")
        print(f"valore sensore: {valoreSensore}")
        print(f"vuoto: {vuoto}")

        file = open("Attività Pentamestre/index.html", "w")
        dato = f"\t\t\t<tr><td>{dt.datetime.now()}</td><td>{valoreSensore}</td></tr>"
        stringagrossa = intestazioneHtml + dato + chiusuraHtml
        file.write(stringagrossa)
        file.close()