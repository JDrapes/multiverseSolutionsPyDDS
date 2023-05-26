import time
import sys
import rti.connextdds as dds
from interfaces import DDS

class ddsWriter:

#Participant
    participant = dds.DomainParticipant(domain_id=0)

    #Topics    
    scanInstruction_topic = dds.Topic(participant, "ScanInstruction", DDS.Scanning.ScanInstruction)
    scanResponse_topic = dds.Topic(participant, "ScanResponse", DDS.Scanning.ScanResponse)
    
    #Writers
    scanInstruction_writer = dds.DataWriter(participant.implicit_publisher, scanInstruction_topic)
    scanResponse_writer = dds.DataWriter(participant.implicit_publisher, scanResponse_topic)
   
    #ScanInstruction - Can write it as a 1 liner or assign things after, or mix.
    #scanInstruction_data = DDS.Scanning.ScanInstruction(radarSetting = 1, manualScanSetting = 2)
    scanInstruction_data = DDS.Scanning.ScanInstruction
    scanInstruction_data.radarSetting = 1
    scanInstruction_data.manualScanSetting = 1

    #ScanResponse
    scanResponse_data = DDS.Scanning.ScanResponse
    scanResponse_data.ZoneNumber = 3;