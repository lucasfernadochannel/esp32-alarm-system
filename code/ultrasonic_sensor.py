from machine import Pin, time_pulse_us
from time import sleep_us

class ultrasonic_sensor:
    """
    This code works with the HC-SR04 ultrasonic sensor.
    The sensor range is between 2cm and 4m (0.8in to 157in);
    """
    def __init__(self, trigger_pin, echo_pin, echo_timeout = 30000):
        """
        trigger_pin: It's used to send the wave sound to the target object
        echo_pin: It's used to detect the bounced back wave (echo)
        echo_timeout: The time limit the echo pin will wait (in milliseconds)
        """
        self.trigger = Pin(trigger_pin, mode = Pin.OUT, pull = None)
        self.echo = Pin(echo_pin, mode = Pin.IN, pull = None)
        self.echo_timeout = echo_timeout
        self.trigger.value(0)
        
    
    def send_pulse(self):
        self.trigger.value(0) # Turn off the emitter
        sleep_us(5)
        self.trigger.value(1) # Turn on the emitter
        sleep_us(10)
        self.trigger.value(0)
        try:
            return time_pulse_us(self.echo, 1, self.echo_timeout)
        except OSError as ex:
            if ex.args[0] == 110: # Timeout
                raise OSError('Object out of range')
            raise ex
        
        
    def distance(self):
        """
        Get the distance in centimeters.
        """
        return (self.send_pulse() / 2) / 29.1
