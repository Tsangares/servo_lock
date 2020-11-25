import time
import RPi.GPIO as pi

class Servo:
    def __init__(self,pin,freq):
        pi.setwarnings(False)
        Servo.clean()
        self.percent = 0
        self.pin = pin
        self.freq = freq
        self.deg = 360
        pi.setmode(pi.BCM)
        pi.setup(pin,pi.OUT)
        self.pwm = pi.PWM(pin,freq)
    def start(self):
        print("Servo started")
        self.pwm.start(0)
    def stop(self):
        self.pwm.stop()
        Servo.clean()
    def clean():
        pi.cleanup()
    def duty(self):
        return self.percent
    def setDuty(self,percent):
        self.pwm.ChangeDutyCycle(percent)
        self.duty = percent
    def frequency(self):
        return self.freq
    def setFreq(self,freq):
        self.pwm.ChangeFrequency(freq)
        self.freq = freq

    def position(self):
        return self.duty,self.deg
    
    def setPosition(self,deg,delay=0):
        distance = abs(self.deg - deg)
        sleep = distance/60*.5+delay
        self.setDuty(deg/18 + 2)
        print(f'Moving to {deg} degrees, duty {self.duty:.0f}%, sleeping for {sleep:.1f} sec.')
        self.deg = deg
        time.sleep(sleep+delay)
    
    def go(self,deg,delay=0):
        return self.setPosition(deg,delay)

def lock(args):
    p=Servo(args.pin,50)
    p.start()
    p.go(90)
    p.go(90)
    p.stop()
    
def unlock(args):
    p=Servo(args.pin,50)
    p.start()
    p.go(0)
    p.go(0)
    p.stop()

def move(args):
    p=Servo(args.pin,50)
    p.start()
    p.go(args.angle)
    p.stop()
    
if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Control display for escrow.')
    
    subparsers = parser.add_subparsers(help='Choose a prompt.')

    lockParse = subparsers.add_parser('lock', help='Move servo to lock position')
    lockParse.add_argument('--pin',type=int, help='The data GPIO pin for the servo',default=19)
    
    lockParse.set_defaults(func=lock)
    
    unlockParse = subparsers.add_parser('unlock', help='Move servo to unlock position')
    unlockParse.add_argument('--pin',type=int, help='The data GPIO pin for the servo',default=19)
    unlockParse.set_defaults(func=unlock)
    
    move = subparsers.add_parser('move', help='Move servo to a specific position')
    move.add_argument('angle',type=int, help='angle in degrees to move the servo.')
    move.add_argument('--pin',type=int, help='The data GPIO pin for the servo',default=19)
    move.set_defaults(func=move)

    args = parser.parse_args()
    args.func(args)
