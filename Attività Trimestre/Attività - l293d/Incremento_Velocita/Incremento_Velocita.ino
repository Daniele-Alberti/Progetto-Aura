int enablePin = 9;
int IN1 = 7;
int IN2 = 8;

void setup() {
  pinMode(enablePin, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
}

void loop() {
  for (int speed = 0; speed <= 255; speed++) {
    analogWrite(enablePin, speed);
    delay(30);
  }

  for (int speed = 255; speed >= 0; speed--) {
    analogWrite(enablePin, speed);
    delay(30);
  }
}
