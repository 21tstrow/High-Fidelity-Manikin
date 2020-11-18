import serial

#Breath Sounds: http://faculty.etsu.edu/arnall/www/public_html/heartlung/breathsounds/contents.html

#Heart Sounds: https://www.easyauscultation.com/heart-sounds-audio
'''
ser = serial.Serial("/dev/ttyUSB9",9600)
''
To Read:
    linein = ser.readline()

 To Write:
    ser.write("A")
''


#The following is experimental and may not work
def useButton(button):
 if button = "moanMale1":
   feed(speaker, 'moanMale1.wav')

def feed(operation, dataType):
  if operation == "speaker":
    fileName = main.findImage(dataType)
    ser.write("speaker play file:" + fileName)
  if operation == 
'''
