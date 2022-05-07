#include <LiquidCrystal.h>
const int rs = 6, en = 7, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
const int sensoreled = A4;
const int triggerPort = 9;
const int echoPort = 10;
const int sensoretemperatura = A5;
void setup() {
  
//led

  pinMode(11, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(2, OUTPUT);
  
// sensore ulrasuoni
pinMode(triggerPort, OUTPUT);
pinMode(echoPort, INPUT);

Serial.print( "Sensore Ultrasuoni: ");
Serial.begin(9600);
}
int c = 0;
void loop() {

  //temperatura
  int temperatura= analogRead(sensoretemperatura);
  float voltage = (temperatura/1024.0) * 5.0;
  Serial.print("  gradi C°: ");
  float temperature = (voltage - .5) * 100;
  Serial.println(temperature);
// ledd
  int sensoreled = analogRead (A4);
    
  

 
//sensore ad ultrasuoni
digitalWrite( triggerPort, LOW );
digitalWrite( triggerPort, HIGH );
delayMicroseconds( 10 );
digitalWrite( triggerPort, LOW );
long durata = pulseIn( echoPort, HIGH );
long distanza = 0.035 * durata / 2;
Serial.print("distanza: ");
if( durata > 38000 ){
Serial.println("Fuori portata   ");
}
else{ 
Serial.print(distanza); 
Serial.println(" cm     ");
}
// lcd
  lcd.begin(16, 2); 
  lcd.print("distanza = "); 
  lcd.print(distanza);
  lcd.setCursor(1, 1);  
  lcd.print("temperatura ");
  lcd.print(temperature);

if(c >= 1){
  Serial.println("                                       ATTENZIONE è PASSATA UNA PERSONA");
  
  lcd.print(c);
  
}


if(distanza < 80){
 digitalWrite(11, LOW);
 digitalWrite(12, LOW);
 digitalWrite(13, HIGH);

 
}
else{
 digitalWrite(11, LOW);
 digitalWrite(12, LOW);
 digitalWrite(13, LOW);

}
 if(sensoreled > 550){
  Serial.print("attenzione       ");
  lcd.begin(16, 2); 
  lcd.print("non autorizzato "); 
  lcd.setCursor(1, 1);
  lcd.print("   chi sei ?   ");
  lcd.setCursor(2, 1);
  lcd.print(c);
  
  c++;
 }else{
  Serial.print("nessuno    ");
 }
 delay(150);


  

}
