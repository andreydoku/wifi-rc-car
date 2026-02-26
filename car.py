from motor import Motor
from time import sleep


pins = {
	"motorFL": {
		"enablePin_num": 6,		# 1,2EN (Pin  1 of L293_1)
		"logicPin1_num": 7,		# 1A    (Pin  2 of L293_1 ) 
		"logicPin2_num": 8		# 2A    (Pin  7 of L293_1)
	},
	"motorFR": {
		"enablePin_num": 19,	# 3,4EN (Pin  9 of L293_1)
		"logicPin1_num": 20,	# 3A    (Pin 10 of L293_1) 
		"logicPin2_num": 21		# 4A    (Pin 15 of L293_1)
	},
	"motorBL": {
		"enablePin_num": 13,	# 1,2EN (Pin  1 of L293_2)
		"logicPin1_num": 14,	# 1A    (Pin  2 of L293_2) 
		"logicPin2_num": 15		# 2A    (Pin  7 of L293_2)
	},
	"motorBR": {
		"enablePin_num": 16,	# 3,4EN (Pin  9 of L293_2)   orange
		"logicPin1_num": 17,	# 3A    (Pin 10 of L293_2)   blue
		"logicPin2_num": 18		# 4A    (Pin 15 of L293_2)   white
	}
}


class Car:
	
	def __init__(self) -> None:
		
		self.motorFL  = Motor(name="frontLeft", **pins["motorFL"])
		self.motorFR = Motor(name="frontRight", **pins["motorFR"])
		self.motorBL   = Motor(name="backLeft", **pins["motorBL"])
		self.motorBR  = Motor(name="backRight", **pins["motorBR"])
		
	def setMotors(self, vel_FL, vel_FR, vel_BL, vel_BR ):
		
		print(f"Car - setMotors {vel_FL}, {vel_FR}, {vel_BL}, {vel_BR}")
		# self.jumpStartCheck( vel_FL, vel_FR, vel_BL, vel_BR )
		
		self.motorFL.setVelocity( vel_FL )
		self.motorFR.setVelocity( vel_FR )
		self.motorBL.setVelocity( vel_BL )
		self.motorBR.setVelocity( vel_BR )
	
	def setFrontLeftMotor( self, vel_FL ):
		self.motorFL.setVelocity( vel_FL )
	
	
	
	
	def jumpStartCheck(self, vel_FL, vel_FR, vel_BL, vel_BR):
		
		flJumpstarted = self.motorFL.jumpstartCheck( vel_FL )
		frJumpstarted = self.motorFR.jumpstartCheck( vel_FR )
		blJumpstarted = self.motorBL.jumpstartCheck( vel_BL )
		brJumpstarted = self.motorBR.jumpstartCheck( vel_BR )
		
		if( flJumpstarted or frJumpstarted or blJumpstarted or brJumpstarted ):
			sleep(0.1)
	
	
	def getStatus(self):
		return {
			"FL": self.motorFL.velocity,
			"FR": self.motorFR.velocity,
			"BL": self.motorBL.velocity,
			"BR": self.motorBR.velocity,
		}