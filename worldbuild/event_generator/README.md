# Event Generation

event_gen is a flexible way to manage world events through simple CSV files.

## Quick Start
Events are functions in your code that are executed, such as light changes, NPC triggers, weather changes.

There are 4 CSV files that can be modified to randomly schedule these events.

```
- events_daily.csv
- events_weekly.csv
- events_seasonal.csv
- events_annual.csv
```

Each CSV file contains a frequency and an event ID

The events.csv file has the event ID and a description

The event_actions.csv file maps action(s) to events when they are triggered (these actions are functions in the code)
