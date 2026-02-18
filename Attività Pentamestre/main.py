import serial
import random

n1 = random.randint(0, 100)
n2 = random.randint(0, 100)
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
    file = open("index.html", "w")
    dato1 = f"<tr><td>2024-06-01 12:00:00</td><td>{n1}</td></tr>\n"
    dato2 = f"<tr><td>2024-06-01 12:01:00</td><td>{n2}</td></tr>\n"
    stringagrossa = intestazioneHtml + dato1 + dato2 + chiusuraHtml
    file.write(stringagrossa)
    file.close()