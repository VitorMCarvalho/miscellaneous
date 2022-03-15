const int buzzer = 2; //buzzer to arduino pin 2
const int ponto = 250;
const int traco = 1000; 
int Letras[26][6] = {{ponto,traco,0,0,0,0}, //a
                    {traco,ponto,ponto,ponto,0,0}, //b
                    {traco,ponto,traco,ponto,0,0}, //c
                    {traco,ponto,ponto,ponto,0,0}, //d
                    {ponto,0,0,0,0,0}, //e
                    {ponto,ponto,traco,ponto,0,0}, //f
                    {traco,traco,ponto,0,0,0}, //g
                    {ponto,ponto,ponto,ponto,0,0}, //h
                    {ponto,ponto,0,0,0,0}, //i
                    {ponto,traco,traco,traco,0,0}, //j
                    {traco,ponto,traco,0,0,0}, //k
                    {ponto,traco,ponto,ponto,0,0}, //l
                    {traco,traco,0,0,0,0}, //m
                    {traco,ponto,0,0,0,0}, //n
                    {traco,traco,traco,0,0,0}, //o
                    {ponto,traco,traco,ponto,0,0}, //p
                    {traco,traco,ponto,traco,0,0}, //q
                    {ponto,traco,ponto,0,0,0}, //r
                    {ponto,ponto,ponto,0,0,0}, //s
                    {traco,0,0,0,0,0}, //t
                    {ponto,ponto,traco,0,0,0}, //u
                    {ponto,ponto,ponto,traco,0,0}, //v
                    {ponto,traco,traco,0,0,0}, //w
                    {traco,ponto,ponto,traco,0,0}, //x
                    {traco,ponto,traco,traco,0,0}, //y
                    {traco,traco,ponto,ponto,0,0} //z
                    };
int Numeros[10][6] = {{traco,traco,traco,traco,traco,0}, //0
                      {ponto,traco,traco,traco,traco,0}, //1
                      {ponto,ponto,traco,traco,traco,0}, //2
                      {ponto,ponto,ponto,traco,traco,0}, //3
                      {ponto,ponto,ponto,ponto,traco,0}, //4
                      {ponto,ponto,ponto,ponto,ponto,0}, //5
                      {traco,ponto,ponto,ponto,ponto,0}, //6
                      {traco,traco,ponto,ponto,ponto,0}, //7
                      {traco,traco,traco,ponto,ponto,0}, //8
                      {traco,traco,traco,traco,ponto,0} //9
                     };
int especiais[8][6] = {{ponto,traco,ponto,traco,ponto,traco}, //.
                    {traco,traco,ponto,ponto,traco,traco}, //,
                    {ponto,ponto,traco,traco,ponto,ponto}, //?
                    {ponto,ponto,traco,traco,ponto,0}, //!
                    {ponto,traco,ponto,ponto,traco,ponto}, //"
                    {ponto,traco,traco,traco,traco,ponto}, //'
                    {traco,ponto,ponto,ponto,traco,0},//=
                    {traco,traco,traco,ponto,ponto,ponto}//:
                    };
void setup(){
 
  pinMode(buzzer, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);

}

void loop(){
 if(Serial.available()>0){
  char N = Serial.read();
  Serial.println(N);
  somluz(N - 'a');
  } 
 }

 void somluz(int ordem){
   if(ordem <=25 && ordem >=0){
    for(int i = 0; i<6; i++){
      if(Letras[ordem][i] !=0 ){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(Letras[ordem][i]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500); 
      }
      else{
        delay(1000);
        break;
      }
     }
    }
    else if(ordem<= -40 && ordem >= -49){
            for(int j = 0; j<6; j++){
              if(Numeros[ordem+49][j] !=0 ){
                tone(buzzer, 500);
                digitalWrite(LED_BUILTIN, HIGH);
                delay(Numeros[ordem+49][j]);
                noTone(buzzer);     // Stop sound...
                digitalWrite(LED_BUILTIN, LOW);
                delay(500); 
              }
              else{
                delay(1000);
                break;
              }
            }
           }
    else if(ordem == -51){ // ponto
      for(int j = 0; j<6; j++){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(especiais[0][j]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
      }
      delay(1000);
    }
    else if(ordem == -53){ //virgula
      for(int j = 0; j<6; j++){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(especiais[1][j]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
      }
      delay(1000);
    }
    else if(ordem == -64){ //exclamação
      for(int j = 0; j<6; j++){
        if(especiais[ordem][j] !=0 ){
          tone(buzzer, 500);
          digitalWrite(LED_BUILTIN, HIGH);
          delay(especiais[3][j]);
          noTone(buzzer);     // Stop sound...
          digitalWrite(LED_BUILTIN, LOW);
          delay(500);
        }
        else{
          delay(1000);
          break;
        }
      }
    }
    else if(ordem == -34){ //interrogação
      for(int j = 0; j<6; j++){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(especiais[2][j]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
      }
      delay(1000);
    }
    else if(ordem == -63){ //aspas
      for(int j = 0; j<6; j++){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(especiais[4][j]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
      }
      delay(1000);
    }

    else if(ordem == -58){ //apostrofe
      for(int j = 0; j<6; j++){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(especiais[5][j]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
      }
      delay(1000);
    }
    else if(ordem == -36){ //igualdade
      for(int j = 0; j<6; j++){
        if(especiais[ordem][j] !=0 ){
          tone(buzzer, 500);
          digitalWrite(LED_BUILTIN, HIGH);
          delay(especiais[6][j]);
          noTone(buzzer);     // Stop sound...
          digitalWrite(LED_BUILTIN, LOW);
          delay(500);
        }
        else{
          delay(1000);
          break;
        }
      }
    }
    else if(ordem == -39){ //doispontos
      for(int j = 0; j<6; j++){
        tone(buzzer, 500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(especiais[7][j]);
        noTone(buzzer);     // Stop sound...
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
      }
      delay(1000);
    }
      
    
    else{
      delay(500);
      }
 }
