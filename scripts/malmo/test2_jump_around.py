# mc_test2.py

import sys
import os
import time
import random

malmo_path = 'T:\\user\\dev\\src\\python\\Malmo\\Python_Examples'
sys.path.append(malmo_path)
mission_file = os.path.join(os.getcwd(), 'mission1.xml')
import MalmoPython
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
    
agent_host = MalmoPython.AgentHost()
agent_host.setObservationsPolicy(MalmoPython.ObservationsPolicy.LATEST_OBSERVATION_ONLY)

# Set up a recording 
my_mission_record = MalmoPython.MissionRecordSpec(mission_file + ".tgz")
my_mission_record.recordRewards()
my_mission_record.recordMP4(48,400000)

with open(mission_file, 'r') as f:
    print ("Loading mission from %s" % mission_file)
    mission_xml = f.read()
    my_mission = MalmoPython.MissionSpec(mission_xml, True)
    
agent_host.startMission(my_mission, my_mission_record )

# Loop until mission starts:
print ("Waiting for the mission to start ",)
world_state = agent_host.getWorldState()
while not world_state.is_mission_running:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print ("Error:",error.text)


print( "Mission running ",)

total_reward = 0.0

# main loop:
while world_state.is_mission_running:
    try:
        # For manual commands on the keyboard
        #  nb = raw_input('Enter command: ')
        #  agent_host.sendCommand(nb)
        
        # Hardwired moves
        agent_host.sendCommand("move " + str(0.5*(random.random()*2-0.5)) )
        #agent_host.sendCommand("pitch " + str(0.2*(random.random()*2-1)) )
#        agent_host.sendCommand("pitch -1")
        agent_host.sendCommand("jump 1")
#        agent_host.sendCommand("attack 1")
#         agent_host.sendCommand("drop")
        agent_host.sendCommand( "turn " + str(0.5*(random.random()*2-1)) )
    except RuntimeError as e:
        print ("Failed to send command:",e)
        pass
    time.sleep(0.2)
    world_state = agent_host.getWorldState()
    print ("video,observations,rewards received:",world_state.number_of_video_frames_since_last_state,world_state.number_of_observations_since_last_state,world_state.number_of_rewards_since_last_state)
    for reward in world_state.rewards:
        print ("Summed reward:",reward.getValue())
        total_reward += reward.getValue()
    for error in world_state.errors:
        print ("Error:",error.text)


print ("Mission ended")
print ("Total reward = " + str(total_reward))


"""
my_mission = MalmoPython.MissionSpec()
my_mission_record = MalmoPython.MissionRecordSpec()
agent_host.startMission( my_mission, my_mission_record )
"""
