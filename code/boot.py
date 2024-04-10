from network import WLAN, STA_IF
from machine import Pin
from time import sleep

# Local network credentials
ssid = 'YOUR_NETWORK_NAME'
password = 'YOUR_NETWORK_PASSWORD'

def connect_wifi(ssid, password):
  # Connect to local network (wi-fi)
  print("Connecting to wi-fi")
  built_in_led = Pin(2, Pin.OUT)
  
  station = WLAN(STA_IF)
  station.active(True)
  station.connect(ssid, password)
  
  while station.isconnected() == False:
      built_in_led.value(0)
      sleep(0.1)
      built_in_led.value(1)
      sleep(0.1)

  print(f'Board connected to {ssid}')
  return station
    
# Connect to your network
connect_wifi(ssid, password)
