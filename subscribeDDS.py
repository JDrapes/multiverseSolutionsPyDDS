import time
import sys
import rti.connextdds as dds
import rti.asyncio
import asyncio #Need both
from interfaces import DDS

#Participant
participant = dds.DomainParticipant(domain_id=1)

#Topics
componentHealth_topic = dds.Topic(participant, "ComponentHealth", DDS.Metrics.ComponentHealth)
objectInfo_topic = dds.Topic(participant, "ObjectInfo", DDS.Detection.ObjectInfo)
detectionData_topic = dds.Topic(participant, "DetectionData", DDS.Detection.DetectionData)
weaponInfo_topic = dds.Topic(participant, "WeaponInfo", DDS.Weapon.WeaponInfo)
fireWeapon_topic = dds.Topic(participant, "FireWeapon", DDS.Weapon.FireWeapon)
scanInstruction_topic = dds.Topic(participant, "ScanInstruction", DDS.Scanning.ScanInstruction)
scanResponse_topic = dds.Topic(participant, "ScanResponse", DDS.Scanning.ScanResponse)
trackData_topic = dds.Topic(participant, "TrackData", DDS.Tracking.TrackData)
IFFRequest_topic = dds.Topic(participant, "IFFRequest", DDS.IFF.IFFRequest)
IFFResponse_topic = dds.Topic(participant, "IFFResponse", DDS.IFF.IFFResponse)
command_topic = dds.Topic(participant, "Command", DDS.misc.Command)
radarSafety_topic = dds.Topic(participant, "RadarSafety", DDS.safety.RadarSafety)
IRSafety_topic = dds.Topic(participant, "IRSafety", DDS.safety.IRSafety)

#Readers
componentHealth_reader = dds.DataReader(participant.implicit_subscriber, componentHealth_topic)
objectInfo_reader = dds.DataReader(participant.implicit_subscriber, objectInfo_topic)
detectionData_reader = dds.DataReader(participant.implicit_subscriber, detectionData_topic)
weaponInfo_reader = dds.DataReader(participant.implicit_subscriber, weaponInfo_topic)
fireWeapon_reader = dds.DataReader(participant.implicit_subscriber, fireWeapon_topic)
scanInstruction_reader = dds.DataReader(participant.implicit_subscriber, scanInstruction_topic)
scanResponse_reader = dds.DataReader(participant.implicit_subscriber, scanResponse_topic)
trackData_reader = dds.DataReader(participant.implicit_subscriber, trackData_topic)
IFFRequest_reader = dds.DataReader(participant.implicit_subscriber, IFFRequest_topic)
IFFResponse_reader = dds.DataReader(participant.implicit_subscriber, IFFResponse_topic)
command_reader = dds.DataReader(participant.implicit_subscriber, command_topic)
radarSafety_reader = dds.DataReader(participant.implicit_subscriber, radarSafety_topic)
IRSafety_reader = dds.DataReader(participant.implicit_subscriber, IRSafety_topic)

#Creating global data holders, these act as data pointers essentially, I wrote this code coming from a C++ background so excuse any weird-ness
componentHealth_ReceivedData = DDS.Metrics.ComponentHealth
objectInfo_ReceivedData = DDS.Detection.ObjectInfo
detectionData_ReceivedData = DDS.Detection.DetectionData
weaponInfo_ReceivedData = DDS.Weapon.WeaponInfo
fireWeapon_ReceivedData = DDS.Weapon.FireWeapon
scanInstruction_ReceivedData = DDS.Scanning.ScanInstruction
scanResponse_ReceivedData = DDS.Scanning.ScanResponse
trackData_ReceivedData = DDS.Tracking.TrackData
IFFRequest_ReceivedData = DDS.IFF.IFFRequest
IFFResponse_ReceivedData = DDS.IFF.IFFResponse
command_ReceivedData = DDS.misc.Command
radarSafety_ReceivedData = DDS.safety.RadarSafety
IRSafety_ReceivedData = DDS.safety.IRSafety

#Async updater for ComponentHealth
async def update_componentHealth():
    async for data in componentHealth_reader.take_data_async():
        global componentHealth_ReceivedData 
        componentHealth_ReceivedData = data

#Async updater for ObjectInfo
async def update_objectInfo():
    async for data in objectInfo_reader.take_data_async():
        global objectInfo_ReceivedData 
        objectInfo_ReceivedData = data

#Async updater for DetectionData
async def update_detectionData():
    async for data in detectionData_reader.take_data_async():
        global detectionData_ReceivedData 
        detectionData_ReceivedData = data

#Async updater for WeaponInfo
async def update_weaponInfo():
    async for data in weaponInfo_reader.take_data_async():
        global weaponInfo_ReceivedData 
        weaponInfo_ReceivedData = data

#Async updater for FireWeapon
async def update_fireWeapon():
    async for data in fireWeapon_reader.take_data_async():
        global fireWeapon_ReceivedData 
        fireWeapon_ReceivedData = data

#Async updater for ScanInstruction
async def update_scanInstruction():
    async for data in scanInstruction_reader.take_data_async():
        global scanInstruction_ReceivedData 
        scanInstruction_ReceivedData = data

#Async updater for ScanResponse
async def update_scanResponse():
    async for data in scanResponse_reader.take_data_async():
        global scanResponse_ReceivedData 
        scanResponse_ReceivedData = data

#Async updater for TrackData
async def update_trackData():
    async for data in trackData_reader.take_data_async():
        global trackData_ReceivedData 
        trackData_ReceivedData = data

#Async updater for IFFRequest
async def update_IFFRequest():
    async for data in IFFRequest_reader.take_data_async():
        global IFFRequest_ReceivedData 
        IFFRequest_ReceivedData = data

#Async updater for IFFResponse
async def update_IFFResponse():
    async for data in IFFResponse_reader.take_data_async():
        global IFFResponse_ReceivedData 
        IFFResponse_ReceivedData = data

#Async updater for Command
async def update_command():
    async for data in command_reader.take_data_async():
        global command_ReceivedData 
        command_ReceivedData = data

#Async updater for RadarSafety
async def update_radarSafety():
    async for data in radarSafety_reader.take_data_async():
        global radarSafety_ReceivedData 
        radarSafety_ReceivedData = data

#Async updater for IRSafety
async def update_IRSafety():
    async for data in IRSafety_reader.take_data_async():
        global IRSafety_ReceivedData 
        IRSafety_ReceivedData = data


#Custom async coroutines           
async def update_motorLogic():
    try:
        global scanInstruction_ReceivedData 
        #Could either have all motorlogic in 1 function like this or make routines for every "setting" - discuss with wider team
        if scanInstruction_ReceivedData.manualScanSetting == 1:
            print("Instructed to scan zone 1") 
        if scanInstruction_ReceivedData.manualScanSetting == 2:
            print("Instructed to scan zone 2")
        if scanInstruction_ReceivedData.manualScanSetting == 3:
            print("Instructed to scan zone 3")
    except Exception as e:
        print(f"Error in update_motorLogic(): {e}")


# Define the main loop coroutine
async def main_loop():
    #Tell the main thread to use the global variables
    global componentHealth_ReceivedData 
    global objectInfo_ReceivedData 
    global detectionData_ReceivedData 
    global weaponInfo_ReceivedData 
    global fireWeapon_ReceivedData 
    global scanInstruction_ReceivedData 
    global scanResponse_ReceivedData 
    global trackData_ReceivedData
    global IFFRequest_ReceivedData
    global IFFResponse_ReceivedData 
    global command_ReceivedData 
    global radarSafety_ReceivedData
    global IRSafety_ReceivedData 

    while True:
        print("Main loop doing nothing, print statements can be uncommented for debugging")
        #print(componentHealth_ReceivedData)
        #print(objectInfo_ReceivedData)
        #print(detectionData_ReceivedData)
        #print(weaponInfo_ReceivedData)
        #print(fireWeapon_ReceivedData)
        #print(scanInstruction_ReceivedData)
        #print(scanResponse_ReceivedData)
        #print(trackData_ReceivedData)
        #print(IFFRequest_ReceivedData)
        #print(IFFResponse_ReceivedData)
        #print(command_ReceivedData)
        #print(radarSafety_ReceivedData)
        #print(IRSafety_ReceivedData)


        await update_motorLogic() #Not sure the impact of this await keyword
        await asyncio.sleep(1)  # Simulating some work and slow thread so we can read it



# Create and run the event loop
loop = asyncio.get_event_loop()
#Add the async tasks to the task list
tasks = asyncio.gather(main_loop(), 
update_componentHealth(), 
update_objectInfo(), 
update_detectionData(), 
update_weaponInfo(), 
update_fireWeapon(), 
update_scanInstruction(), 
update_scanResponse(),
update_trackData(),
update_IFFRequest(),
update_IFFResponse(),
update_command(),
update_radarSafety(),
update_IRSafety(),
update_motorLogic()
)
#Now loop the task list
loop.run_until_complete(tasks)