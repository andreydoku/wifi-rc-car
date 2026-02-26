
import json
from cors import CORS
from motorTest import motorTest, motorTest2
import network
from machine import Pin
from microdot import Microdot
from time import sleep

from motor import Motor
from car import Car




print("START")


car = Car()
print("Car initialized")

onboardLed = Pin("LED", Pin.OUT) # onboard LED for Pico W

# motorTest2(car)



def connectToWifi():
    
	ssid = 'HingleMcCringle'
	password = '50cabbages'

	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)

	# might already be connected somehow.
	if wlan.isconnected() == False:
		wlan.connect(ssid, password)
		
	# Wait for connection.
	while wlan.isconnected() == False:
		print("trying to connect...")
		sleep(1)
		pass
	
	print('connected!')
	ipConfig = wlan.ifconfig() # returns (IP address , subnet mask , gateway , DNS server )
	print('IP address:', ipConfig[0])
	onboardLed.value(1)

connectToWifi()



app = Microdot()
cors = CORS(app, allowed_origins=['http://localhost:5173', "http://192.168.4.22:5173"], allowed_methods=["GET", "POST", "OPTIONS"])
# what fixed it: adding localhost above ^^^

@app.get('/api/status')
async def getStatus(request):
    
	response = {
		"frontLeft": car.frontLeftMotor.velocity,
		"frontRight": car.frontRightMotor.velocity,
		"backLeft": car.backLeftMotor.velocity,
		"backRight": car.backRightMotor.velocity,
	}
	headers = {
		'Content-Type': 'application/json', 
		"Access-Control-Allow-Origin": "*"
	}
	return json.dumps(response), 200, headers

@app.post('/api/motors')
async def setMotor(request):
    
	requestBody = request.json
	print(requestBody)
	
	frontLeftV = requestBody["frontLeft"]
	frontRightV = requestBody["frontRight"]
	backLeftV = requestBody["backLeft"]
	backRightV = requestBody["backRight"]
	
	
	car.setMotors( frontLeftV , frontRightV , backLeftV , backRightV )
	
	response = {
		"frontLeft": car.frontLeftMotor.velocity,
		"frontRight": car.frontRightMotor.velocity,
		"backLeft": car.backLeftMotor.velocity,
		"backRight": car.backRightMotor.velocity,
	}
	headers = {
		'Content-Type': 'application/json', 
		"Access-Control-Allow-Origin": "*",
		"Access-Control-Allow-Methods": "POST"
	}
	return json.dumps(response), 201, headers

print("starting server...")
app.run(debug=True)

