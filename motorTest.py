from time import sleep


def motorTest(car):
	velocities = [ 0.00, 0.50, 1.00, 0.50, 0.00, -0.50, -1.00, -0.50 ]
	while True: 
		for velocity in velocities:
			car.setMotors( velocity, 0, 0, 0 )
			sleep(1)
		for velocity in velocities:
			car.setMotors( 0, velocity, 0, 0 )
			sleep(1)
		for velocity in velocities:
			car.setMotors( 0, 0, velocity, 0 )
			sleep(1)
		for velocity in velocities:
			car.setMotors( 0, 0, 0, velocity )
			sleep(1)

def motorTest2(car):
	v = 0.5
	while True:
		setMotorsWithSleep(car, v, v, 0, 0, 1)
		setMotorsWithSleep(car, 0, 0, v, v, 1)
		setMotorsWithSleep(car, v, 0, v, 0, 1)
		setMotorsWithSleep(car, 0, v, 0, v, 1)


def setMotorsWithSleep(car, frontLeftV, frontRightV, backLeftV, backRightV, sleepTime):
	car.setMotors( frontLeftV, frontRightV, backLeftV, backRightV )
	sleep(sleepTime)