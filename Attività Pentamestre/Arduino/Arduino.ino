struct PacchettoSensore 
{
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char valoreSensore[4];
  char vuoto[16];
};

const char ID[] = "AB";
const char MITTENTE[] = "P001";
const char DESTINATARIO[] = "P002";
const char TIPO[] = "S1";
const char VUOTO[] = "----------------";

void setup() 
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  PacchettoSensore p;

  int valore = analogRead(A0);

  memcpy(p.id, ID, 2);
  memcpy(p.mittente, MITTENTE, 4);
  memcpy(p.destinatario, DESTINATARIO, 4);
  memcpy(p.tipo, TIPO, 2);
  memcpy(p.vuoto, VUOTO, 16);

  sprintf(p.valoreSensore, "%04d", valore);

  Serial.write((byte*)&p, sizeof(p));

  delay(1000);
}
