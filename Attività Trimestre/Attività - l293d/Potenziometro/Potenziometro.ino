int enablePin = 9;
int IN1 = 7;
int IN2 = 8;
int potPin = A0;

void setup() {
  pinMode(enablePin, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);
  int speed = map(potValue, 0, 1023, 0, 255);

  analogWrite(enablePin, speed);

  Serial.print("Potenziometro: ");
  Serial.print(potValue);
  Serial.print("    Velocità motore: ");
  Serial.println(speed);

  delay(50);
}
