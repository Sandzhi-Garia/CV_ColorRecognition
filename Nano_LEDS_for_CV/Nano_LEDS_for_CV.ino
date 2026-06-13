
// constants won't change. Used here to set a pin number:
const int RED = 9;
const int YELLOW = 6;
const int GREEN = 10;
const int BLUE = 11;  // the number of the LED pin

// Variables will change:
int ledState = LOW;  // ledState used to set the LED

void setup() {
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
    String recieved = Serial.readStringUntil('\n');
  int pins[4] = {BLUE, YELLOW, GREEN, RED};

  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);

  for (int i = 0; i <4; i++){
    if (recieved[i] =='1'){
      digitalWrite(pins[i], HIGH);
    }

  }
  }
}

