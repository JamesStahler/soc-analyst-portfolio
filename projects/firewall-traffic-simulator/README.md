# Firewall Traffic Simulator

An in-progress Python project that simulates network connection attempts, evaluates them against simple IP-and-port rules, records allow/block decisions, and summarizes traffic activity.

## Current Features

- Generates simulated private IPv4 source addresses
- Selects common destination ports
- Applies combined IP and blocked-port rules
- Logs allow and block decisions
- Counts total allowed and blocked connections
- Identifies top-talking source addresses
- Alerts when a configured blocked address reaches an activity threshold
- Summarizes blocked IP-and-port combinations

## Run the Project

```bash
python firewall_checker.py
```

The script prints simulated connection activity and a security summary to the terminal. It also appends connection decisions to `FireWall.log`.

A representative output file is included as `sample_firewall.log`.

## Rule Logic

Traffic is blocked only when both conditions are true:

1. The generated source IP appears in `firewall_rules`.
2. The generated destination port appears in `blocked_port_list`.

All other simulated traffic is allowed by default.

## Skills Demonstrated

- Python functions and control flow
- Dictionaries, lists, tuples, and counters
- File-based logging
- Rule evaluation
- Threshold-based alerting
- Traffic aggregation and summary reporting
- Security-oriented problem solving

## Project Status

This project is under active development. Planned improvements include configurable rules, structured logging, input validation, reproducible test data, improved separation of concerns, and automated tests.

## Important Note

This is an educational traffic and firewall-rule simulation. It does not inspect live network traffic, modify an operating-system firewall, or provide production security enforcement.
