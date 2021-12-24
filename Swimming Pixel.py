import paho.mqtt.client as mqtt
import time
from time import sleep
from datetime import datetime
import mido

mqtt.Client.connected_flag=False #create flag in class
#define topics for all pixels
broker="localhost"
topic_1 = "MIDI/SP1"
topic_2= "MIDI/SP2"
topic_3 = "MIDI/SP3"
topic_4 = "MIDI/SP4"
topic_5= "MIDI/SP5"
topic_6= "MIDI/SP6"
topic_7= "MIDI/SP7"
topic_8= "MIDI/SP8"
topic_9= "MIDI/SP9"
topic_10= "MIDI/SP10"
topic_11= "MIDI/SP11"
topic_12= "MIDI/SP12"
topic_13= "MIDI/SP13"

port=1883
instrument = mido.get_input_names() #return input port name
inport = mido.open_input(instrument[0]) #open an input port

def on_connect (client,userdata,flags,rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("client is connected")
        connected=True
    else:
        print("connection failed Returned code=",rc)

def on_publish(client,userdata,result):
    print("data published ")
    pass
        
client = mqtt.Client("mqtt")             #create new instance
client.on_connect=on_connect  #bind call back function
print("Connecting to broker ",broker,port)
client.on_publish = on_publish #publish message to the topic
client.connect(broker)      #connect to broker

client.loop_start()
array_music_1 = []
array_music_2 = []
array_music_3 = []
array_music_4 = []
array_music_5 = []
array_music_6 = []
array_music_7 = []
previous_time = 0
average_velocity_SP1 = 0
average_velocity_SP2 = 0
average_velocity_SP3 = 0
average_velocity_SP4 = 0
average_velocity_SP5 = 0
average_velocity_SP6 = 0
average_velocity_SP7 = 0
    
if __name__ == "__main__":
    try:
        while True:
            client.loop_start()
            msg = inport.receive()
            note_onoff = msg.type #note_off or note_on
            note = msg.note #note value
            velocity = msg.velocity #how fast the note was struck or released
            total_velocity_1 = 0
            total_velocity_2 = 0
            total_velocity_3 = 0
            total_velocity_4 = 0
            total_velocity_5 = 0
            total_velocity_6 = 0
            total_velocity_7 = 0
            now = datetime.now().time()
            now_time = now.microsecond
            current_time = int(str(now_time)[:1])
            length_time = len(str(now_time))
            
            if length_time < 6:
                current_time = 10
            else:
                pass
                
            if client.connected_flag:
                if note in range (24, 36, 1):
                    if note_onoff == "note_on":
                        #add note and velocity to a list when music note starts
                        array_music_1.append([note,velocity])

                    else:
                        #remove note and velocity to a list when music note starts
                        array_music_1 = [subl for subl in array_music_1 if subl[0] != note]

                    for i in range (len(array_music_1)):
                        total_velocity_1  = total_velocity_1  + array_music_1[i][1]

                    #average value of 12 velocities
                    average_velocity_SP1 = total_velocity_1/12

                if note in range (36, 48, 1):
                    if note_onoff == "note_on":
                        array_music_2.append([note,velocity])

                    else:
                        array_music_2 = [subl for subl in array_music_2 if subl[0] != note]

                    for i in range (len(array_music_2)):
                        total_velocity_2  = total_velocity_2  + array_music_2[i][1]

                    average_velocity_SP2 = total_velocity_2/12

                if note in range (48, 60, 1):
                    if note_onoff == "note_on":
                        array_music_3.append([note,velocity])

                    else:
                        array_music_3 = [subl for subl in array_music_3 if subl[0] != note]

                    for i in range (len(array_music_3)):
                        total_velocity_3  = total_velocity_3  + array_music_3[i][1]

                    average_velocity_SP3 = total_velocity_3/12
                    
                if note in range (60, 72, 1):
                    if note_onoff == "note_on":
                        array_music_4.append([note,velocity])

                    else:
                        array_music_4 = [subl for subl in array_music_4 if subl[0] != note]

                    for i in range (len(array_music_4)):
                        total_velocity_4  = total_velocity_4  + array_music_4[i][1]

                    average_velocity_SP4 = total_velocity_4/12

                if note in range (72, 84, 1):
                    if note_onoff == "note_on":
                        array_music_5.append([note,velocity])

                    else:
                        array_music_5 = [subl for subl in array_music_5 if subl[0] != note]

                    for i in range (len(array_music_5)):
                        total_velocity_5  = total_velocity_5  + array_music_5[i][1]

                    average_velocity_SP5 = total_velocity_5/12

                if note in range (84, 96, 1):
                    if note_onoff == "note_on":
                        array_music_6.append([note,velocity])

                    else:
                        array_music_6 = [subl for subl in array_music_6 if subl[0] != note]

                    for i in range (len(array_music_6)):
                        total_velocity_6  = total_velocity_6  + array_music_6[i][1]

                    average_velocity_SP6 = total_velocity_6/12

                if note in range (96, 104, 1):
                    if note_onoff == "note_on":
                        array_music_7.append([note,velocity])

                    else:
                        array_music_7 = [subl for subl in array_music_7 if subl[0] != note]

                    for i in range (len(array_music_7)):
                        total_velocity_7  = total_velocity_7  + array_music_7[i][1]

                    average_velocity_SP7 = total_velocity_7/8
                    
                if (int(current_time) - int(previous_time)) == 2:
                    #publish message every 0.2 second
                    if current_time == 10:
                        current_time = 0
                    previous_time = current_time
                    client.publish(topic_1,average_velocity_SP1)
                    client.publish(topic_13,average_velocity_SP1)
                    client.publish(topic_2,average_velocity_SP2)
                    client.publish(topic_12,average_velocity_SP2)
                    client.publish(topic_3,average_velocity_SP3)
                    client.publish(topic_11,average_velocity_SP3)
                    client.publish(topic_4,average_velocity_SP4)
                    client.publish(topic_10,average_velocity_SP4)
                    client.publish(topic_5,average_velocity_SP5)
                    client.publish(topic_9,average_velocity_SP5)
                    client.publish(topic_6,average_velocity_SP6)
                    client.publish(topic_8,average_velocity_SP6)
                    client.publish(topic_7,average_velocity_SP7)                  
                    
            else:
                print("In wait loop")
                time.sleep(1)   

    except KeyboardInterrupt:
        print("connection failed")
        client.loop_stop()    #Stop loop 
        client.disconnect() # disconnect
        exit(1) #Should quit or raise flag to quit or retry
