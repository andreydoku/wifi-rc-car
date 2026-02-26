from motor import Motor
from time import sleep

# TODO - define these in an organized json structure
# {
# 	topLeftMotor: {
# 		enablePin: 0,
# 		logicPin1: 1,
# 		logicPin2: 2
# 	},
# 	...
# }

# that or call constructor by explicitly definint parameters
# something like = Car(x=5, y=4)


# # front left
frontLeftMotor_enablePin_num  = 6   # 1,2EN (Pin  1 of L293 1)
frontLeftMotor_logicPin1_num  = 7   # 1A    (Pin  2 of L293 1) 
frontLeftMotor_logicPin2_num  = 8   # 2A    (Pin  7 of L293 1)

# # front right
frontRightMotor_enablePin_num  = 19  # 3,4EN (Pin  9 of L293 1)
frontRightMotor_logicPin1_num  = 20  # 3A    (Pin 10 of L293 1) 
frontRightMotor_logicPin2_num  = 21  # 4A    (Pin 15 of L293 1)

# # back left
backLeftMotor_enablePin_num  = 13   # 1,2EN (Pin  1 of L293 2)
backLeftMotor_logicPin1_num  = 14   # 1A    (Pin  2 of L293 2) 
backLeftMotor_logicPin2_num  = 15   # 2A    (Pin  7 of L293 2)

# # back right
backRightMotor_enablePin_num  = 16  # 3,4EN (Pin  9 of L293 2)   orange
backRightMotor_logicPin1_num  = 17  # 3A    (Pin 10 of L293 2)   blue
backRightMotor_logicPin2_num  = 18  # 4A    (Pin 15 of L293 2)   white


class Car:
	
	def __init__(self) -> None:
		
		self.frontLeftMotor  = Motor(frontLeftMotor_enablePin_num, frontLeftMotor_logicPin1_num, frontLeftMotor_logicPin2_num)
		self.frontRightMotor = Motor(frontRightMotor_enablePin_num, frontRightMotor_logicPin1_num, frontRightMotor_logicPin2_num)
		self.backLeftMotor   = Motor(backLeftMotor_enablePin_num, backLeftMotor_logicPin1_num, backLeftMotor_logicPin2_num)
		self.backRightMotor  = Motor(backRightMotor_enablePin_num, backRightMotor_logicPin1_num, backRightMotor_logicPin2_num)
		
	def setMotors(self, frontLeftV, frontRightV, backLeftV, backRightV ):
		
		print(f"Car - setMotors {frontLeftV} {frontRightV} {backLeftV} {backRightV}")
		# self.jumpStartCheck( frontLeftV, frontRightV, backLeftV, backRightV )
		
		self.frontLeftMotor.setVelocity( frontLeftV )
		self.frontRightMotor.setVelocity( frontRightV )
		self.backLeftMotor.setVelocity( backLeftV )
		self.backRightMotor.setVelocity( backRightV )
	
	def setFrontLeftMotor( self, frontLeftV ):
		self.frontLeftMotor.setVelocity( frontLeftV )
	
	
	
	
	def jumpStartCheck(self, frontLeftV, frontRightV, backLeftV, backRightV):
		
		flJumpstarted = self.frontLeftMotor.jumpstartCheck( frontLeftV )
		frJumpstarted = self.frontRightMotor.jumpstartCheck( frontRightV )
		blJumpstarted = self.backLeftMotor.jumpstartCheck( backLeftV )
		brJumpstarted = self.backRightMotor.jumpstartCheck( backRightV )
		
		if( flJumpstarted or frJumpstarted or blJumpstarted or brJumpstarted ):
			sleep(0.1)