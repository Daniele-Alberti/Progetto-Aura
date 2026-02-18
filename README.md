# Progetto Aura

## Descrizione
Progetto integrato di automazione che combina sensori Arduino, comunicazione tra microcontrollori, controllo motori e visualizzazione dati web. Il sistema acquisisce dati sensoriali, li trasmette tra dispositivi Arduino, aziona un motore in base ai valori rilevati, salva i dati in formato JSON tramite Python e li visualizza attraverso un'interfaccia HTML.

## Architettura del Sistema

```
Sensore Arduino → Arduino Ricevente → Motore
                        ↓
                    Python (JSON)
                        ↓
                    HTML (Visualizzazione)
```

## Componenti

### Arduino (Arduino/)
- **Arduino.ino**: Sketch per la comunicazione tra i due Arduino e il controllo del motore
  - Arduino 1: Legge i dati dal sensore e li trasmette
  - Arduino 2: Riceve i dati e aziona il motore in base ai valori

### Python (main.py)
- Riceve i dati dagli Arduino
- Salva i dati in formato JSON
- Gestisce la persistenza dei dati e la comunicazione con l'interfaccia web

### Interfaccia Web
- **index.html**: Pagina principale per la visualizzazione dei dati
- **index.htm**: Alternativa della pagina principale
- Visualizza i dati salvati in tempo reale
- Interfaccia responsiva per il monitoraggio del sistema

## Requisiti

### Hardware
- 2x Arduino (configurati per la comunicazione seriale/I2C/SPI)
- Sensore compatibile con Arduino
- Motore e driver di controllo
- Cavi di collegamento

### Software
- Arduino IDE
- Python 3.x
- Browser moderno (Chrome, Firefox, Edge)

## Installazione

1. **Arduino**:
   - Carica `Arduino/Arduino.ino` su entrambi i dispositivi Arduino
   - Configura la comunicazione tra i due Arduino
   - Collega il sensore al primo Arduino e il motore al secondo

2. **Python**:
   - Installa le dipendenze necessarie (se presenti in requirements.txt)
   - Configura la porta seriale per la comunicazione con gli Arduino

3. **Web Interface**:
   - Apri `index.html` in un browser web
   - Assicurati che Python sia in esecuzione per l'aggiornamento dei dati

## Funzionamento

1. Il primo Arduino legge continuamente i dati dal sensore
2. I dati vengono trasmessi al secondo Arduino tramite comunicazione seriale/wireless
3. Il secondo Arduino aziona il motore in base ai valori ricevuti
4. Python intercetta i dati e li salva in formato JSON
5. L'interfaccia HTML legge il file JSON e visualizza i dati in tempo reale

## Struttura dei Dati JSON

```json
{
  "timestamp": "2026-02-18T10:30:00",
  "sensore_value": 45.5,
  "motore_speed": 120,
  "stato": "attivo"
}
```

## Utilizzo

```bash
python main.py
```

Poi aprire `index.html` nel browser per visualizzare i dati in tempo reale.

## Configurazione

- Modifica iParametriArduino nel file `.ino` per adattare i valori di soglia e velocità del motore
- Configura le porte seriali e i baudrate nel file `main.py` secondo il tuo setup
- Personalizza lo stile e il layout in `index.html`

## Troubleshooting

- **Connessione Arduino non riconosciuta**: Verifica i driver USB e la porta COM corretta
- **Dati non salvati in JSON**: Assicurati che Python abbia i permessi di scrittura nella cartella
- **Interfaccia web vuota**: Controlla che `main.py` sia in esecuzione e che il JSON sia aggiornato

## Autore
Progetto sviluppato come parte del corso TPS

## Licenza
MIT

## Note
- Assicurati che gli Arduino comunicano correttamente prima di attivare il motore
- Testa il sistema in modalità manuale prima di automatizzare completamente
