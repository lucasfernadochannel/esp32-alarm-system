"""
Use the following information according to your e-mail server.
If you use another e-mail provider, you'll need to search for
its SMTP server settings and apply them on this code.

========== For GMAIL ==========
SMTP Server: smtp.gmail.com
SMTP port (TLS): 587
SMTP port (SSL): 465
SMTP TLS/SSL required: yes

========= For OUTLOOK =========
SMTP Server: smtp.office365.com
SMTP Port: 587
SMTP TLS/SSL Required: Yes

===== For LIVE or HOTMAIL =====
SMTP Server: smtp.live.com
SMTP Port: 587
SMTP TLS/SSL Required: Yes
"""

# This file runs when board finishes executing boot.py
from ultrasonic_sensor import ultrasonic_sensor
from time import sleep_ms
from umail import SMTP
from machine import Pin, PWM

def send_email(provider, sender_email, sender_name, sender_app_password, recipient_email, subject, message):
    provider = provider.lower()
    if (provider == 'gmail'):
        smtp = SMTP('smtp.gmail.com', 465, ssl = True)
    elif (provider == 'outlook'):
        smtp = SMTP('smtp.office365.com', 587, ssl = True)
    elif (provider == 'live' or provider == 'hotmail'):
        smtp = SMTP('smtp.live.com', 587, ssl = True)
        
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write('From:' + sender_name + '<' + sender_email + '>\n')
    smtp.write('Subject:' + subject + '\n')
    smtp.write(message)
    smtp.send()
    smtp.quit()
    
    return None


hcsr04 = ultrasonic_sensor(trigger_pin = 25, echo_pin = 26)
buzzer_pin = Pin(19, Pin.OUT)
# Define melody notes (frequency in Hz)
melody = [262, 262, 392, 392, 440, 440, 392, 349, 349, 330, 330, 294, 294, 262,
          392, 392, 349, 349, 330, 330, 294, 392, 392, 349, 349, 330, 330, 294,
          262, 262, 392, 392, 440, 440, 392, 349, 349, 330, 330, 294, 294, 262]

# Define melody durations (in milliseconds)
durations = [200, 200, 200, 200, 200, 200, 400, 200, 200, 200, 200, 200, 200, 400,
             200, 200, 200, 200, 200, 200, 400, 200, 200, 200, 200, 200, 200, 400,
             200, 200, 200, 200, 200, 200, 400, 200, 200, 200, 200, 200, 200, 400]
provider = 'YOUR_EMAIL_PROVIDER'
sender_email = 'YOUR_EMAIL'
sender_name = 'YOUR_APP_PASSWORD_NAME'
password = 'YOUR_APP_PASSWORD' # This is the app password not the e-mail password
recipient_email = 'THE_RECIPIENT_EMAIL'
subject = 'SUBJECT'
message = 'MESSAGE'
while True:
    distance_cm = hcsr04.distance()
    print(f'Distance: {distance_cm}cm | {distance_cm / 2.54}in')
    if (distance_cm >= 0 and distance_cm <= 50):
        # Play melody
        for note, duration in zip(melody, durations):
            buzzer = PWM(buzzer_pin, freq=note, duty=512)
            sleep_ms(duration)
            buzzer.deinit()
            sleep_ms(50)  # Pause between notes
        send_email(provider, sender_email, sender_name, password, recipient_email, subject, message)
        print('E-mail has been sent')
    sleep(0.1)
    
