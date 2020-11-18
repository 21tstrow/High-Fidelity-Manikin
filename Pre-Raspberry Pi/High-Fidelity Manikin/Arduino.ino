int light_left = 0;
int light_right = 0;// store the current light value
bool mouth_on = false; 
bool fingernails_led_left = false;
bool fingernails_led_right = false;
bool fingernails_led = false;

'''
###In setup()
char cTMP;
int beePin=12;

Serial.begin(9600);
while (Serial.available()>0) cTMP=Serial.read();  // flush the buffer

####Then somewhere in loop()

if (Serial.available) > 0) {
    if (serIn=='A') {
      digitalWrite(beePin,HIGH); delay(2000); digitalWrite(beePin,LOW);
      delay(2000);
      digitalWrite(beePin,HIGH); delay(2000); digitalWrite(beePin,LOW);
    }

}
'''
void setup() {
    setup_led_eyes_left();
    setup_led_eyes_right();
    setup_mouth();
    setup_fingernails();
}
void loop() {
    loopInput();
    loop_led_eyes_left();
    setup_led_eyes_right();
    loop_mouth();
    loop_fingernails();
}

void setup_led_eyes_left() {
    // put your setup code here, to run once:
    Serial.begin(9600); //configure serial to talk to computer
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT); 
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    
}

void loop_led_eyes_left() {
    // put your main code here, to run repeatedly:
    light_left = analogRead(A0); // read and save value from PR
    
    Serial.println(light_left); // print current light value
 
    if(light_left > 450) { // If it is bright...
        Serial.println("bright!");
        digitalWrite(2,LOW); 
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
    }
    else if(light_left > 229 && light_left < 451) { // If it is average light...
        Serial.println("Little Bright!");
        digitalWrite(2,HIGH); 
        digitalWrite(3,LOW);
        digitalWrite(4,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,LOW);
    }
    else { // If it's dark...
        Serial.println("Dark!");
        digitalWrite(2,HIGH); 
        digitalWrite(3,HIGH);
        digitalWrite(4,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,HIGH);
    }
    delay(1000); // don't spam the computer!
}

void setup_led_eyes_right() {
    // put your setup code here, to run once:
    Serial.begin(9600); //configure serial to talk to computer
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
    pinMode(11, OUTPUT);
    
}

void loop_led_eyes_right() {
    // put your main code here, to run repeatedly:
    light_right = analogRead(A1); // read and save value from PR
    
    Serial.println(light_right); // print current light value
 
    if(light_right > 450) { // If it is bright...
        Serial.println("bright!");
        digitalWrite(7,LOW); 
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
        digitalWrite(11,LOW);
    }
    else if(light_right > 229 && light_right < 451) { // If it is average light...
        Serial.println("Little Bright!");
        digitalWrite(7,HIGH); 
        digitalWrite(8,LOW);
        digitalWrite(9,HIGH);
        digitalWrite(10,HIGH);
        digitalWrite(11,LOW);
    }
    else { // If it's dark...
        Serial.println("Dark!");
        digitalWrite(7,HIGH); 
        digitalWrite(8,HIGH);
        digitalWrite(9,HIGH);
        digitalWrite(10,HIGH);
        digitalWrite(11,HIGH);
    }
    delay(1000); // don't spam the computer!
}

// Mouth
void setup_mouth() {
    pinMode(2,OUTPUT);
}

void loop_mouth() {
    if (mouth_on == true){
        digitalWrite(2,HIGH);
    }
    else {
        digitalWrite(2,LOW);
    }
}

// Fingernails
void setup_fingernails() {
    pinMode(3,OUTPUT); // right hand
    pinMode(4,OUTPUT);
    pinMode(5,OUTPUT);
    pinMode(6,OUTPUT);
    pinMode(7,OUTPUT); //  
    pinMode(8,OUTPUT); // left hand
    pinMode(9,OUTPUT);
    pinMode(10,OUTPUT);
    pinMode(11,OUTPUT);
    pinMode(12,OUTPUT); // 
}

void loop_fingernails() {
    if ((fingernails_led_right == true) && (fingernails_led_left == false) && (fingernails_led == false)){
        digitalWrite(3,HIGH);
        digitalWrite(4,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,HIGH);
        digitalWrite(7,HIGH);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
        digitalWrite(11,LOW);
        digitalWrite(12,LOW);
    }
    else if ((fingernails_led_left == true) && (fingernails_led_right == false) && (fingernails_led == false)){
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,HIGH);
        digitalWrite(9,HIGH);
        digitalWrite(10,HIGH);
        digitalWrite(11,HIGH);
        digitalWrite(12,HIGH);
    }
    else if (fingernails_led == true) {
        digitalWrite(3,HIGH);
        digitalWrite(4,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,HIGH);
        digitalWrite(7,HIGH);
        digitalWrite(8,HIGH);
        digitalWrite(9,HIGH);
        digitalWrite(10,HIGH);
        digitalWrite(11,HIGH);
        digitalWrite(12,HIGH);
    }
    else if ((fingernails_led_right == true) && (fingernails_led_left == true)) {
        digitalWrite(3,HIGH);
        digitalWrite(4,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,HIGH);
        digitalWrite(7,HIGH);
        digitalWrite(8,HIGH);
        digitalWrite(9,HIGH);
        digitalWrite(10,HIGH);
        digitalWrite(11,HIGH);
        digitalWrite(12,HIGH);
    }
}


//serial needs to be set to a valid port input based on the arduino and raspberry config
void loopInput(){
  String inputString = serial.readString()
  if ((inputString.length() > 17) && (inputString.remove(17).equals("speaker play file"))){
    speakerPlay(inputString.substring(18))
  } 
}




//The String str is the file name
void speakerPlay(String str){
  music.play(str)
}