const int switchPin = 8;
const int yellow = 2;
const int greenLED = 3;

int switchState = 0;

void setup() {
  pinMode(switchPin, INPUT);
  pinMode(yellow, OUTPUT);
  pinMode(greenLED, OUTPUT);
}

void loop() {
  switchState = digitalRead(switchPin);

  if (switchState == HIGH) {
    digitalWrite(yellow, HIGH);
    digitalWrite(greenLED, LOW);

    delay(5); 

    digitalWrite(yellow, LOW);
    digitalWrite(greenLED, LOW);
  }
  else {
    digitalWrite(yellow, LOW);
    digitalWrite(greenLED, HIGH);

    delay(5); 
    
    
    digitalWrite(yellow,LOW);
    digitalWrite(greenLED,LOW);
  }
}