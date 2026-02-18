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

### Arduino
- Arduino 1: Legge i dati dal sensore e li trasmette
- Arduino 2: Riceve i dati e aziona il motore in base ai valori

### Python
- Riceve i dati dagli Arduino
- Salva i dati in formato JSON
- Gestisce i dati e la comunicazione con l'interfaccia web

### Interfaccia Web
- Visualizza i dati salvati

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
