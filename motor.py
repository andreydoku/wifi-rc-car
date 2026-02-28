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

	
	velocity = 0.0  # [-1, 1], 
	# +1 = full speed forward
	#  0 = stop, 
	# -1 = full speed back
	
	#enable pins are donnected to PWM pins, which are 16bit (0-65535), 
	# so to convert from velocity to duty cycle, do: duty = speed * 65535
	
	def __init__(self, name, enablePin_num, logicPin1_num, logicPin2_num) -> None:
		self.name = name
		self.enablePin = PWM(Pin(enablePin_num))
		self.enablePin.freq(1000)
		self.logicPin1 = Pin(logicPin1_num, Pin.OUT)
		self.logicPin2 = Pin(logicPin2_num, Pin.OUT)
		
		self.logicPin1.value(0)
		self.logicPin2.value(0)
		self.enablePin.duty_u16(0)
		self.velocity = 0.0
	
	def setVelocity(self, velocity):
		
		print(f"  {self.name} - setVelocity {self.velocity} => {velocity}")
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
	
	def kickstartCheck(self, newVelocity):
		oldVelocity = self.velocity
		oldSpeed = abs(oldVelocity)
		newSpeed = abs(newVelocity)
		
		changingDirection = (oldVelocity * newVelocity < 0)
		
		# print(f"    {self.name} - kickstartCheck, speed change: {oldSpeed} => {newSpeed}")
		
		# going down in speed, don't need a kickstart
		# only if going up in speed, and was previously stopped, and we're going up to something slow, then kickstart
		
		if( newSpeed == 0 ):
			# print("      not kickstarting because we're stopping the motor, not starting it")
			return False
		
		if( not changingDirection ):
			if ( newSpeed <= oldSpeed ):
				# print("      not kickstarting because we're not going up in speed")
				return False
			
			if( oldSpeed != 0 ):
				# print("      not kickstarting because we were already moving at a nonzero speed")
				return False
			
			if( newSpeed >= 0.4 ):
				# print("      not kickstarting because we're going up to a reasonably high speed, so we probably don't need it")
				return False
		
		if( changingDirection ):
			if( newSpeed >= 0.4 ):
				# print("      not kickstarting because we're going up to a reasonably high speed, so we probably don't need it")
				return False
		
		
		if( newVelocity > 0 ):
			self.logicPin1.value(1)
			self.logicPin2.value(0)
		if( newVelocity < 0 ):
			self.logicPin1.value(0)
			self.logicPin2.value(1)
		kickstartSpeed = 0.4
		self.enablePin.duty_u16( round(kickstartSpeed*65535) )
		
		return True