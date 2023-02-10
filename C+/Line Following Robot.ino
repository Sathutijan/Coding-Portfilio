/* Author: Sathu. K and Thanushkanth. S
 * Teacher: Mr. Rai
 * Date: January 24th, 2023
 * 
 * Description: This program will allow the robot to follow the black line using the ir sensors as input and based of those
 * values the 2 DC motors will rotate in a certain direction and speed by the H bridge to stay on the black line to successfully
 * complete a lap around the track in the most time effiecnt way. There are constant blinking lights and blinking lights when
 * turning. The push button acts as a start top switch for the robot.
 */


// initialize variable for middle blue LED as an integer, which is connected to pin 7 on the circuit
const int flashLED = 7;

// initialize variable for right LED as an integer, which is connected to pin 3 on the circuit
const int rightLED = 3;

// initialize variable for left LED as an integer, which is connected to pin 4 on the circuit
const int leftLED =4;

// Initialize variable to set the left led state in a off position
int stateLeftLED = LOW; 

// Initialize variable to set the right led state in a off position
int stateRightLED = LOW;

// Initialize variable to set the middle blue led state in a off position
int stateFlashLED = LOW;

// A variable that hold time are unsigned long as it will be too big to store in the int function

unsigned long flashLastMillis = 0; // will store the last time middle blue LED state was updated
unsigned long rightLastMillis = 0; // will store the last time right LED state was updated
unsigned long leftLastMillis = 0; // will store the last time left LED state was updated

// 100ms interval in which the middle bllue LED will blink at
const long flashInterval = 100;

// 50ms interval in which the the left and right led will blink at
const long turnInterval = 50;

// initialize variable for the push button as an integer, which is connected to pin 12 on the circuit
const int pushButton   = 12;  

// initialize variable for motor1A as an integer, which is connected to pin 9 on the circuit
const int motor1A      = 9;  
// initialize variable for motor2A as an integer, which is connected to pin 8 on the circuit
const int motor2A      = 8; 
// initialize variable for motor3A as an integer, which is connected to pin 10 on the circuit
const int motor3A      = 10; 
// initialize variable for motor4A as an integer, which is connected to pin 11 on the circuit
const int motor4A      = 11; 

// These lines define and initialize constants for the speed of the left and right motors.
const int leftMotorspeed = 6;
const int rightMotorspeed = 5;

// These lines define constants for the pins connected to the left and right IR sensors. These sensors are used to detect the line.
const int leftIRsensor  = 13;
const int rightIRsensor = 2;

//These lines define variables for the speed of the right and left motors. 
//These variables can be adjusted to control the speed of the robot.

int rightWheelSpeed = 241; // Controlled by the right enable pin
int leftWheelSpeed = 255; // Controlled by the left enable pin 
 
// define variables for the speed of the left and right wheels when the robot is turning.
int leftTurningSpeed = 255; // Controlled by the left enable pin
int rightTurningSpeed = 255; // Controlled by the right enable pin
 
// define variables for the speed of the left and right wheels when the robot is moving in backward direction. 
int leftBackwardSpeed = 215;
int rightBackwardSpeed = 210;   

int pushbuttoncounter = 0; //Creates a variable to keep count of button presses
int stateofbutton =  0; //Creates a variable to see the current state of the button
int previousButtonState = 0; //Creates a varaible to see the previous state of the button

  

void setup() {

// The flashLED, rightLED and leftLED pins are set as OUTPUT, which allows the robot to
// control the state of these LEDs.
pinMode(flashLED, OUTPUT);
pinMode(rightLED, OUTPUT);
pinMode(leftLED, OUTPUT);


// The motor1A, motor2A, motor3A and motor4A pins are set as OUTPUT,
// which allows the robot to control the speed and direction of the motors.
pinMode(motor1A, OUTPUT);
pinMode(motor2A, OUTPUT);
pinMode(motor3A, OUTPUT);
pinMode(motor4A, OUTPUT);


// The pushButton pin is set as INPUT, which allows the robot to read the state of the push button.
pinMode(pushButton, INPUT);

// The leftIRsensor and rightIRsensor pins are set as INPUT, which allows the robot to read the state of the IR sensors.
pinMode(leftIRsensor, INPUT);
pinMode(rightIRsensor, INPUT);
  
}

void loop() {

stateofbutton = digitalRead(pushButton); //Updates the variable to read pushbutton 


  if (stateofbutton != previousButtonState) { //If the current state of the button does not equal to the previous state of the button,
                                              //which in short means if the button has been pressed, it will do the code below. Else, it 
                                              //it will do nothing and continue to line 130 and below. 

    if (stateofbutton == 1) { //If the state of the button equals to 1, it will do the code below
      pushbuttoncounter++; //increases the push button counter by 1 
      
    }

    else {     //Else if the state of button does not equal to 1, meaning 0, it will do the code below (nothing). 

      // Doesn't add anything (you can remove this else statement but its just for understanding).
      
    }
    
  }

  previousButtonState = stateofbutton; //saves the recent state of the button as the last state 
                                       //the next time the loop runs

 /*If pushbuttoncounter value divided by 2 gives us a REMAINDER VALUE that does equal to 0, robot
    will stay off, doing nothing and than looping back. If anything else, meaning remainder value does 
    not equal to 0, robot will follow the code below the else statement. */    

  if (pushbuttoncounter % 2 == 0) { 
        
    // The Led on the left,right and flash LED will be set to low
      digitalWrite(leftLED,LOW);
      digitalWrite(rightLED,LOW);
      digitalWrite(flashLED,LOW);

// All motors will be set in a low postion to make the robot stop
      digitalWrite(motor1A,LOW);
      digitalWrite(motor2A,LOW);                       
      digitalWrite(motor3A,LOW);
      digitalWrite(motor4A,LOW);
      
  }

  
  else {

// The first two lines read the state of the left and right IR sensors and store the values
// in the variables "leftsensorValue" and "rightsensorValue" respectively.
    int leftsensorValue = digitalRead(leftIRsensor);
    int rightsensorValue = digitalRead(rightIRsensor);
    
// initializes a variable "flashRecentMillis" to store the current value of the millis() function.
   unsigned long flashRecentMillis = millis();

// The following block of code is a conditional statement that checks if the time elapsed since the
// last execution of this block is greater than or equal to the value of the "flashInterval" variable.

  if (flashRecentMillis - flashLastMillis >= flashInterval){
    
// If the condition is true, the "flashLastMillis" variable is updated to the current value of millis().
    flashLastMillis = flashRecentMillis;

// The next conditional statement checks the current state of the flash LED, if it's LOW,
// it sets it to HIGH otherwise it sets it to LOW.
    if (stateFlashLED == LOW) {
      stateFlashLED = HIGH;    
    }
    else {
      stateFlashLED = LOW;
    }
// This line writes the current state of the flash LED to the flashLED pin.
  digitalWrite(flashLED, stateFlashLED);
  }

// This code is a conditional statement that checks the values of the 
// "rightsensorValue" and "leftsensorValue" variables to determine the robot's
// position on the line.

// If both "rightsensorValue" and "leftsensorValue" are equal to 1, it means that the robot is on the line.

    if((rightsensorValue == 1) && (leftsensorValue == 1))
    {
// If the conditional statement is true the following lines of code turn off the right and left LED, 
// this might be indicating the robot is on the line.

      digitalWrite(rightLED,LOW);
      digitalWrite(leftLED,LOW);

// It then sets the state of the motor1A and motor3A pins to HIGH and the state of the
// motor2A and motor4A pins to LOW,  this makes the robot move forward.
      digitalWrite (motor1A,HIGH);
      digitalWrite(motor2A,LOW);                       
      digitalWrite (motor3A,HIGH);
      digitalWrite(motor4A,LOW);

// The next lines set the speed of the left and right motors using the 
// "analogWrite" function, which sets the speed of the motors to the values
// stored in the "leftWheelSpeed" and "rightWheelSpeed" variables respectively.

      analogWrite(leftMotorspeed, leftWheelSpeed);
      analogWrite(rightMotorspeed, rightWheelSpeed);
    

      }

//  If the "rightsensorValue" is equal to 1 and "leftsensorValue"
// is equal to 0, it means that the robot is on the right side of the line.
    else if((rightsensorValue == 1) && (leftsensorValue == 0))
    {

// If the conditional statement is true the following lines of code turn off
// the left LED, indicating that the robot is on the right side of the line.
      digitalWrite(leftLED,LOW);
      
// It then sets the state of the motor1A pin to LOW, motor2A pin to HIGH,
// motor3A pin to HIGH and motor4A pin to LOW, which makes the robot turn left.
      digitalWrite(motor1A,LOW);
      digitalWrite(motor2A,HIGH);                       
      digitalWrite(motor3A,HIGH);
      digitalWrite(motor4A,LOW);

// The next lines set the speed of the left and right motors using the "analogWrite"
//function, which sets the speed of the left motors to the value stored in the 
//"leftBackwardSpeed" variable and the speed of the right motors to the value stored in
//the "rightTurningSpeed" variable.
    
      analogWrite(leftMotorspeed, leftBackwardSpeed);
      analogWrite(rightMotorspeed, rightTurningSpeed);

// The following block of code is a conditional statement that checks if the time elapsed
// since the last execution of this block is greater than or equal to the value of the 
// "turnInterval" variable.

          unsigned long rightRecentMillis = millis();

      if (rightRecentMillis - rightLastMillis >= turnInterval){
        
// If the condition is true, the "rightLastMillis" variable is updated to the current value of millis().
        rightLastMillis = rightRecentMillis;

// The next conditional statement checks the current state of the right LED, 
// if it's LOW, it sets it to HIGH otherwise it sets it to LOW.

        if (stateRightLED == LOW) {
          stateRightLED = HIGH;    
        }
        else {
          stateRightLED = LOW;
        }
// This line writes the current state of the right LED to the rightLED pin
      digitalWrite(rightLED, stateRightLED);
    
 
          }

    }


// if the "rightsensorValue" is equal to 0 and "leftsensorValue" is equal to 1,
// it means that the robot is on the left side of the line.    
    else if((rightsensorValue == 0) && (leftsensorValue == 1))
    {
// If the condition is true the following code runs and turns off the right LED, this indicates
// the robot is on the left side of the line.

      digitalWrite(rightLED,LOW);
      
// It then sets the state of the motor1A pin to HIGH, motor2A pin to LOW, 
// motor3A pin to LOW and motor4A pin to HIGH,this makes the robot turn right.
  
      digitalWrite(motor1A,HIGH);
      digitalWrite(motor2A,LOW);                       
      digitalWrite(motor3A,LOW);
      digitalWrite(motor4A,HIGH);

// The next lines set the speed of the left and right motors using
// the "analogWrite" function, which sets the speed of the left motors to
// the value stored in the "leftTurningSpeed" variable and the speed of 
// the right motors to the value stored in the "rightBackwardSpeed" variable.

      analogWrite (leftMotorspeed, leftTurningSpeed);
      analogWrite (rightMotorspeed, rightBackwardSpeed);

// The following block of code is a conditional statement that checks if
// the time elapsed since the last execution of this block is greater than or
// equal to the value of the "turnInterval" variable.

         unsigned long leftRecentMillis = millis();

    if (leftRecentMillis - leftLastMillis >= turnInterval){
      
// If the condition is true, the "leftLastMillis" variable is updated to the current value of millis().
    leftLastMillis = leftRecentMillis;

// The next conditional statement checks the current state of the left LED, if it's LOW,
// it sets it to HIGH otherwise it sets it to LOW.
    if (stateLeftLED == LOW) {
      stateLeftLED = HIGH;    
    }
    else {
      stateLeftLED = LOW;
    }
// This line writes the current state of the left LED to the leftLED pin.
  digitalWrite(leftLED, stateLeftLED);

   
    }

      }
// If all the if and else if statements are false the following code will run
    else
    { 

// The Led on the left and right side will be set to low
      digitalWrite(leftLED,LOW);
      digitalWrite(rightLED,LOW);

// All motors will be set in a low postion to make the robot stop
      digitalWrite(motor1A,LOW);
      digitalWrite(motor2A,LOW);                       
      digitalWrite(motor3A,LOW);
      digitalWrite(motor4A,LOW);
      
      }

  }
}






  


 











 
