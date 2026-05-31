import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Logger connected successfully!")
        client.subscribe("sensors/temperature")
    else:
        print(f"Failed to connect! Error code: {rc}")

def on_message(client, userdata, msg):
    print(f"[LIVE] {msg.payload.decode()}")

def on_disconnect(client, userdata, rc):
    print(f"Disconnected! Code: {rc}")

client = mqtt.Client()
client.username_pw_set("myuser", "mypassword123")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("localhost", 1883)
client.loop_forever()