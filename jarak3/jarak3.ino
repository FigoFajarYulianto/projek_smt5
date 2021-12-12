#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
const int trigPin = 5;
const int echoPin = 6;
int led = 7;
int BUTTON_PIN = 8;
int buttonState = 0;
int piezo=10;
long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
  lcd.backlight();
lcd.init();
pinMode(led, OUTPUT);
   pinMode(BUTTON_PIN, INPUT);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
pinMode(piezo, OUTPUT);

}

void loop() {
buttonState = digitalRead(BUTTON_PIN);
  Serial.println(buttonState);

  if(buttonState == LOW){
    digitalWrite(led, HIGH);
  }else{
    digitalWrite(led,LOW);
  }

  // put your main code here, to run repeatedly:
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

duration = pulseIn(echoPin, HIGH);
  distance= (duration*0.034)/2; // memperkiraan jarak
if(distance >=6 || distance <=0){
  lcd.setCursor (0,0);
  lcd.println("Letakan Telur");
}
else{
  lcd.setCursor (0,0);
  lcd.println("Telur Terdeteksi");

}
if (distance <=5
){
  digitalWrite(piezo,HIGH);
  delay(20);
  digitalWrite(piezo,LOW);
  delay(100);
}

else{
  digitalWrite(piezo,LOW);
}
}
