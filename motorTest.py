from motor import Motor
from time import sleep

# # front left
enablePin_num  = 0   # 1,2EN (Pin  1 of L293 1)
logicPin1_num  = 1   # 1A    (Pin  2 of L293 1) 
logicPin2_num  = 2   # 2A    (Pin  7 of L293 1)

# # front right
# enablePin_num  = 19  # 3,4EN (Pin  9 of L293 1)
# logicPin1_num  = 20  # 3A    (Pin 10 of L293 1) 
# logicPin2_num  = 21  # 4A    (Pin 15 of L293 1)

# # back left
# enablePin_num  = 13   # 1,2EN (Pin  1 of L293 2)
# logicPin1_num  = 14   # 1A    (Pin  2 of L293 2) 
# logicPin2_num  = 15   # 2A    (Pin  7 of L293 2)

# # back right
# enablePin_num  = 16  # 3,4EN (Pin  9 of L293 2)   orange
# logicPin1_num  = 17  # 3A    (Pin 10 of L293 2)   blue
# logicPin2_num  = 18  # 4A    (Pin 15 of L293 2)   white

motor = Motor(enablePin_num, logicPin1_num, logicPin2_num)

velocities = [ 0.00, 0.50, 1.00, 0.50, 0.00, -0.50, -1.00, -0.50 ]
while True: 
	for velocity in velocities:
		print(f"setting velocity: {velocity}")
		motor.setVelocity(velocity)
		sleep(1)