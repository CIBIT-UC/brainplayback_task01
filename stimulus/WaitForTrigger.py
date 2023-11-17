from psychopy import core, parallel
import serial

#initialise ports
serialPort = serial.Serial("COM2", baudrate=57600, bytesize=8, parity='N', stopbits=1, timeout=0.0001)

serialPort.flushInput();
serialPort.flushOutput()

#time out period
timer = core.CountdownTimer(5)
while timer.getTime() > 0:
  nCharsToGet = serialPort.inWaiting()
  if (nCharsToGet)>0:
      # number of incoming bytes.
      message = serialPort.read(nCharsToGet)
      #read the current characters
      print(message)
      break
