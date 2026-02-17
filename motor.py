from machine import Pin, PWM
from time import sleep


class Motor:
	# enablePin: connect to L293, pin "1,2EN" (pin7)    
	# logicPin1 = connect to L293, pin "1A" (pin 1)   
	# logicPin2 = connect to L293, pin "2A" (pin 2)
	
	#login pins are digital, and control the direction
	#    1,0 forward, 0,1 backward
	#    if logic pins match (both 0s or both 1s), then the motor stops (preferred stop to use enable pin tho)
	
	#enable pin = PWM controlled speed
	
	# controlling speed
	#    Option 1 (preferred): apply PWM to enable pin, while using logic pins as digital pins to only control direction
	#    Option 2: apply PWM to logic pins.  Not recommended
	
	# stopping
	#    Option 1 (preferred): apply PWM 0 to enable pin
	#    Option 2: make logic pins match (set both to 0, or set both to 1)

	
	velocity = 0.0  # [-1, 1], -1 = full speed back, 0 stop, +1 full speed forward
	
	def __init__(self, enablePin_num, logicPin1_num, logicPin2_num) -> None:
		self.enablePin = PWM(Pin(enablePin_num))
		self.enablePin.freq(1000)
		self.logicPin1 = Pin(logicPin1_num, Pin.OUT)
		self.logicPin2 = Pin(logicPin2_num, Pin.OUT)
		
		self.logicPin1.value(0)
		self.logicPin2.value(0)
		self.enablePin.duty_u16(0)
		self.velocity = 0.0
	
	def setVelocity(self, velocity):
		
		print(f"Motor - setVelocity {self.velocity} => {velocity}")
		if( self.velocity == velocity ):
			print("    no change in speed, just return")
			return
		
		if( velocity > 0 ):
			self.logicPin1.value(1)
			self.logicPin2.value(0)
		if( velocity < 0 ):
			self.logicPin1.value(0)
			self.logicPin2.value(1)

		
		speed = abs(velocity)
		self.enablePin.duty_u16( round(speed*65535) )
		
		self.velocity = velocity
	
	def jumpstartCheck(self, newVelocity):
		oldVelocity = self.velocity
		if ( oldVelocity == 0 and newVelocity > 0 ):
			return False
		
		if( newVelocity > 0 ):
			self.enablePin.duty_u16( +65535 )
		if( newVelocity < 0 ):
			self.enablePin.duty_u16( -65535 )
		
		return True