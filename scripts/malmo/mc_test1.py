# mc_test1.py

import sys
import os

malmo_path = 'T:\\user\\dev\\src\\python\\Malmo\\Python_Examples'

sys.path.append(malmo_path)

try:
    import MalmoPython
    print('imported Malmo ok')
except ImportError:
    print('cant import MalmoPython - check path')

    
agent_host = MalmoPython.AgentHost()
agent_host.setObservationsPolicy(MalmoPython.ObservationsPolicy.LATEST_OBSERVATION_ONLY)

print(agent_host)

print('Environment ok - TODO - specify and run mission')

"""
my_mission = MalmoPython.MissionSpec()
my_mission_record = MalmoPython.MissionRecordSpec()
agent_host.startMission( my_mission, my_mission_record )
"""
