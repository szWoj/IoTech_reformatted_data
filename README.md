This is README file to instruct the user how to build and run a solution to IoTech Coding Exercise. The solution for this exercise has been written using Python.

1. Clone IOTechSystems github repository to your local machine by running:
    'git clone git@github.com:szWoj/IoTech_reformatted_data.git'
    on your terminal

2. Once the repository has been cloned, run devices_reformating.py file on your terminal by running the command: 'python3 devices_reformating.py'

After a successful run of the commands above, reformatted_data file is created with a solution of the IoTech Coding Exercise.
(please notice that the file 'devices_reformating.py' has been run before it was pushed on GitHub, so a new created file (reformatted_data) with the solution to the problem has been pused as well)

1. Data has been parsed from devices.json
2. uuid has been extracted from 'Info' field
3. For each device, sum of the sensor payloads has been calculated
4. Data has been formated to satisfy the schema (schema.json)
5. Data has been reformatted by 'Name' field
6. Reformatted data has been saved to a new 'reformatted_data' file