// the setup function runs once when you press reset or power the boardint le
int ledPin1 = 8;
int ledPin2 = 9;
int ledPin = 10;
void setup() {
  // initialize digital pin ledPin as an output.
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin1,OUTPUT);
  pinMode(ledPin2,OUTPUT);
  
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(ledPin, HIGH);
  delay(3000);  
  digitalWrite(ledPin1, HIGH);// wait for a second
  delay(3000); 
  digitalWrite(ledPin, LOW);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, HIGH);// turn the LED off by making the voltage LOW
  delay(3000);        
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin1, HIGH);
  delay(3000);  
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin, HIGH);
  // wait for a second
}
