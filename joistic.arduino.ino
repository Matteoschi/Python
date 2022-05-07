

void setup() {
  Serial.begin(9600);

  


}

void loop() {
  int c = fnz();
  Serial.print(c);
  Serial.print("                                counter   ");
  int x = analogRead(A5);
  int y = analogRead(A1);
  int clic = analogRead(A3);
  Serial.print("     x");
  Serial.println(x);
  Serial.print("clic  ");
  Serial.print(y);
  Serial.print("                y  ");
  Serial.print(clic);
  Serial.print(c);

}
int fnz(){
  int static counter = 0;
  counter++;
  return counter;
}
