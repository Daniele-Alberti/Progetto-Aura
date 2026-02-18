int pin = 0;
int ritardo = 833;
int offset = 416;
int messaggio[8];
void setup() 
{
  pinMode(pin, INPUT);
  Serial.begin(1200);
}

void loop() 
{
  if (digitalRead(pin) == 0 && Serial.available() == 0) 
  {
    delayMicroseconds(ritardo + offset);
    for (int i = 0; i < 8; i++) 
    {
      messaggio[i] = digitalRead(pin);
      delayMicroseconds(ritardo);
    }
    for (int i = 8; i > 0; i--) 
    {
      Serial.print(messaggio[i]);
    }
  }
}
