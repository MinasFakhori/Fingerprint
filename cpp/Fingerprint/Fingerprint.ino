#include <Adafruit_Fingerprint.h>
#include "config.h"
#include "password.h"
#include "dual_devices.h"
#include <Keyboard.h>



SoftwareSerial mySerial(FINGERPRINT_MODULE_TXD_PIN, FINGERPRINT_MODULE_TOUCH_PIN);




Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);


// This is for the device reset button on/off
const int fingerprintOnPin = FINGERPRINT_ON_PIN;
bool fingerprint_used = false;
int fingerprintButtonState = 0;
int lastButtonState = 0;
int buttonState = LOW;


// This is for device swtiching
int ledDeviceState; 
bool isDevice;
int lastDeviceState;
int deviceState;
int switchDevicePin;
int switchDeviceLedPin;


void setup() {

  if (DUAL_DEVICES){
  isDevice = false;
  ledDeviceState = LOW;
  lastDeviceState = 0;
  deviceState = 0;
  switchDevicePin = SWITCH_DEVICE_PIN;
  switchDeviceLedPin = SWITCH_DEVICE_LED_PIN;

  pinMode(switchDevicePin, INPUT);
  pinMode(switchDeviceLedPin, OUTPUT);
} 


  pinMode(fingerprintOnPin, INPUT);

  Keyboard.begin();
  finger.begin(57600);
}

void loop() {
  fingerprintButtonState = digitalRead(fingerprintOnPin);

  if (fingerprintButtonState != lastButtonState) {
    if (fingerprintButtonState == HIGH) {
      buttonState = (buttonState == LOW) ? HIGH : LOW;
      if (buttonState == HIGH && fingerprint_used) {
        fingerprint_used = false;
      } else {
        fingerprint_used = true;
      }
         delay(180);
    }
  }


  if (DUAL_DEVICES){
    deviceState = digitalRead(switchDevicePin);
  if (deviceState != lastDeviceState) {
    if (deviceState == HIGH) {

      ledDeviceState = (ledDeviceState == LOW) ? HIGH : LOW;

      if (ledDeviceState == HIGH) {
        digitalWrite(switchDeviceLedPin, HIGH);
        isDevice = true; 
     
      } else {
      digitalWrite(switchDeviceLedPin, LOW);
       isDevice = false; 
       
      }
      delay(180);
    }

  }
  } 

  if (!fingerprint_used){
    getFingerprintID();
  }

  lastButtonState = fingerprintButtonState;
}



uint8_t getFingerprintID() {
  uint8_t p = finger.getImage();
  
  if (p == FINGERPRINT_OK) {
    p = finger.image2Tz();
    if (p == FINGERPRINT_OK) {
      p = finger.fingerFastSearch();
      if (p == FINGERPRINT_OK && !fingerprint_used) {
        Serial.print("Found ID #"); Serial.print(finger.fingerID);
        Serial.print(" with confidence of "); Serial.println(finger.confidence);
        if (!isDevice){
          Keyboard.print(PASSWORD1);
        }else{
           Keyboard.print(PASSWORD2);
        }
        Keyboard.press(KEY_RETURN);
        delay(100);
        Keyboard.release(KEY_RETURN);
        fingerprint_used = true;
        return FINGERPRINT_OK;
      }
    }
  }

  return p;
}