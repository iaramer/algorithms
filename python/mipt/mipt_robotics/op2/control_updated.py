#!/usr/bin/env python
import asyncio
import websockets
import json

from pid_updated import PID

# TODO: Initialize the pid variable.
# steering_pid = PID(0.053, 0.0, 0.0)


# steering_pid = PID(0.03, 0.00004, 40.0) # pozdno povorachivaet
# steering_pid = PID(0.03, 0.00004, 30.0) # nachal povorachivat
# steering_pid = PID(0.03, 0.00004, 25.0) - # huzhe

# steering_pid = PID(0.03, 0.00006, 30.0) # povernul best
# steering_pid = PID(0.03, 0.00006, 35.0) # ne povernul
# steering_pid = PID(0.03, 0.00006, 27.0) # povernul
# steering_pid = PID(0.045, 0.00006, 40.0) # povernul
pid = PID(0.1, 0.00001, 50.0)
pid_throttle = PID(0.6, 0, 1)


# Checks if the SocketIO event has JSON data.
# If there is data the JSON object in string format will be returned,
# else the empty string "" will be returned.
def get_data(message):
    try:
        start = message.find("[")
        end = message.rfind("]")
        return message[start:end + 1]
    except:
        return ""


async def handle_telemetry(websocket, msg_json):
    cte = msg_json[1]["cte"]
    speed = msg_json[1]["speed"]
    angle = msg_json[1]["steering_angle"]

    cte = float(cte)
    speed = float(speed)
    angle = float(angle)

    print("CTE: ", cte, ", speed: ", speed, ", angle: ", angle)

    # TODO: Calculate steering value here, remember the steering value is
    # [-1, 1].
    # NOTE: Feel free to play around with the throttle and speed.
    # Maybe use another PID controller to control the speed!

    pid.UpdateError(cte)
    steer_value = pid.get_control()

    max_speed = 80
    max_angle = 25
    max_throttle = 0.3
    target_speed = max(0.0, max_speed * (1.0 - abs(angle / max_angle * cte) / 4))
    target_speed = min(100.0, target_speed)
    pid_throttle.UpdateError(speed - target_speed)
    throttle_value = min(max_throttle, 0.7 + pid_throttle.get_control())

    response = {
        'steering_angle': steer_value,
        'throttle': throttle_value
    }

    print("throttle ", throttle_value, "Steer value ", steer_value, "cte ", cte)
    msg = "42[\"steer\"," + json.dumps(response) + "]"

    await websocket.send(msg)


async def echo(web_socket, path):
    async for message in web_socket:
        if len(message) < 3 \
                or message[0] != '4' \
                or message[1] != '2':
            return

        s = get_data(message)
        msg_json = json.loads(s)

        event = msg_json[0]
        if event == "telemetry":
            await handle_telemetry(web_socket, msg_json)
        else:
            msg = "42[\"manual\",{}]"
            await web_socket.send(msg)


def main():
    start_server = websockets.serve(echo, "localhost", 4567)
    print('Server  started  at  localhost:4567')

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
