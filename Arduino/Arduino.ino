struct PacchettoSensore {
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char valoreSensore[4];
  char vuoto[16];
};

void setup() {
  #define ID = "AB"
  #define MITTENTE = "P001"
  #define DESTINATARIO = "P002"
  #define TIPO = "S1"
  #define VUOTO = "----------------"
  
  pinMode(A0, INPUT);

  Serial.begin(9600);
}

void loop() {
  PacchettoSensore p;

  int valore = analogRead(A0);

  delay(1000);
}
