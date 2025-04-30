typedef enum {est0, est1, est2, est3} Estados;
Estados compuerta = est0;
#define Ptrig 7
#define Pecho 6
long distancia1;
long tiempo1;
int inicio=2;
int bomba1=3;
int bomba2=4;
int bocina=5;
int ledrojo=8;
int ledverde=9;
int ledbomba1=10;
int ledbomba2=11;
int nivel=13;
void setup() {
 Serial.begin(9600);
 pinMode(Ptrig,OUTPUT);
 pinMode(Pecho,INPUT);
 pinMode(inicio, INPUT);
 pinMode(bomba1, OUTPUT);
 pinMode(bomba2, OUTPUT);
 pinMode(bocina, OUTPUT);
 pinMode(ledrojo, OUTPUT);
 pinMode(ledverde, OUTPUT);
 pinMode(ledbomba1, OUTPUT);
 pinMode(ledbomba2, OUTPUT);
 pinMode(nivel,OUTPUT);
}


void loop (){
  switch(compuerta){
    case est0:
    sensor();
    digitalWrite(ledrojo,HIGH);
    digitalWrite(ledverde,LOW);
    digitalWrite(bomba1,LOW);
    digitalWrite(bomba2,LOW);
    digitalWrite(nivel,LOW);
    if(digitalRead(inicio)== HIGH){
      digitalWrite(ledverde,HIGH);
      digitalWrite(ledrojo,LOW);
      Serial.print("PREPARANDO INICIO");
      delay(1000);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(400);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(400);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(400);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(400);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(400);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(400);
      digitalWrite(bocina,HIGH);
      delay(400);
      digitalWrite(bocina,LOW);
      delay(1000);
      digitalWrite(ledbomba1,HIGH);
      digitalWrite(bomba1,HIGH);
      Serial.print("  BOMBA 1 ACTIVA");
      delay(15000);
      digitalWrite(ledbomba1,LOW);
      digitalWrite(bomba1,LOW);
      delay(5000);
    compuerta=est1;
 
  }
  else {compuerta = est0;}
  break;  


  case est1:
  digitalWrite(ledbomba2,HIGH);
  digitalWrite(bomba2,HIGH);
  Serial.print("BOMBA 2 ACTIVA");
  Serial.print("sensor");
  sensor();
  if (distancia1<10){
    compuerta=est2;
  }
  else {compuerta =est1;}
  break;
 
 case est2:
 if (distancia1<12){
    Serial.print("NIVEL LLEGO A TOPE");
    digitalWrite(nivel,HIGH);
    digitalWrite(ledbomba2,LOW);
    digitalWrite(bomba2,LOW);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    delay(400);
    digitalWrite(bocina,HIGH);
    delay(400);
    digitalWrite(bocina,LOW);
    compuerta=est0;
    }
   else{compuerta=est2;}
   delay(500);
}
}

void sensor() {
  digitalWrite(7,LOW);
  delayMicroseconds(2);
  digitalWrite(7,HIGH);
  delayMicroseconds(5);

  tiempo1 = pulseIn(6,HIGH) 
  ditancial = int(0.017 * tiempo1)

 Serial.println("distancia 1 ");
 Serial.println("distancia 1");
 Serial.println("cm");


 delay(200);
}
