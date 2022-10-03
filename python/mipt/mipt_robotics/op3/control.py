#!/usr/bin/env python

import asyncio
import json

import websockets
from pid import PID


steering_pid = PID(0.1, 0.00001, 50.0)

# Checks if the SocketIO event has JSON data.
# If there is data the JSON object in string format will be returned,
# else the empty string "" will be returned.
def getData(message):
	try:
		start = message.find("[")
		end = message.rfind("]")
		return message[start:end+1]
	except:
		return ""


async def handleTelemetry(websocket, msgJson):
	cte = msgJson[1]["cte"]
	speed = msgJson[1]["speed"]
	angle = msgJson[1]["steering_angle"]

	print("CTE: ", cte, ", speed: ", speed, ", angle: ", angle)
	
	steering_pid.UpdateError(cte)
	steer_value = steering_pid.TotalError()

	if steer_value < -1:
		steer_value = -1
	if steer_value > 1:
		steer_value = 1

	response = {}
	
	response["steering_angle"] = steer_value
	throttle = 0.2
	speed, cte = float(speed), float(cte)
	if abs(cte) > 1.2:
		throttle = 0.1
	response["throttle"] = throttle

	print("throttle ", throttle, "Steer value ", steer_value, "cte ", cte)

	msg = "42[\"steer\"," + json.dumps(response) + "]"

	await websocket.send(msg)


async def echo(websocket, path):
	async for message in websocket:
		if len(message) < 3 \
			or message[0] != '4' \
			or message[1] != '2':
			return

		s = getData(message);
		msgJson = json.loads(s)

		event = msgJson[0]
		if event == "telemetry":
			await handleTelemetry(websocket, msgJson)
		else:
			msg = "42[\"manual\",{}]"
			await websocket.send(msg)


def main():
	start_server = websockets.serve(echo, "localhost", 4567)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
	main()