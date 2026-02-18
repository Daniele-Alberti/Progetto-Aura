int enablePin = 9;
int IN1 = 7;
int IN2 = 8;

void setup() {
  Serial.begin(9600);
  pinMode(enablePin, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  Serial.println("Inserisci velocità (0-255): ");
}

void loop() {
  if (Serial.available()) {
    int speed = Serial.parseInt();
    speed = speed, 0, 255;

    analogWrite(enablePin, speed);
    Serial.print("Velocità impostata a: ");
    Serial.println(speed);
  }
}
