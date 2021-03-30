# Event Generation

event_gen is a flexible way to manage world events through simple CSV files.

## Quick Start
Events are generated randomly according to specified CSV files, and a table 
is produced with chance of events occurring at a given day/time.

When an event is triggered, it uses the action_id to call functions in your code 
that are executed, such as light changes, NPC triggers, weather changes.

There are 4 CSV files that can be modified to randomly schedule these events.

```
- events_daily.csv
- events_weekly.csv
- events_seasonal.csv
- events_annual.csv
```

Each CSV file contains a frequency and an event ID


The event_chance.csv file generated can be loaded to Unreal Engine and accessed as per below

![ue4_BP_GameEvents_LoadEventsForDay](https://github.com/acutesoftware/worldbuild/blob/master/doc/ue4_BP_GameEvents_LoadEventsForDay_20210330.PNG)
ue4_BP_GameEvents_LoadEventsForDay_20210330.PNG





