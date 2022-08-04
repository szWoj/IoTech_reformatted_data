import json
import re
import pprint




#Using context manager to load data
with open('devices.json') as f:
    data = json.load(f)

# Lists declaration 
name = []
type = []
info = []
uuid = []
total_sum = []
list_ = []
sorted_list = []

#Getting info from data which dont need to be manipulated
def get_device_info():
    for i in data['Devices']:
        name.append(i["Name"])
        type.append(i["Type"])
        info.append(i["Info"])


# Extracting the uuid from the Info field
def extract_the_uuid():
    for i in data['Devices']:
        uuid.append((re.findall(r"[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}",i["Info"]))[0])
        # print((re.findall(r"[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}",i["Info"]))[0])


# For each device, calculate sum of the sensor payloads
def sum_of_payloads():
    for i in data['Devices']:
        total_sum.append(i["Sensors"][0]["Payload"] + i["Sensors"][1]["Payload"])
        # print(i["Sensors"][0]["Payload"] + i["Sensors"][1]["Payload"])

#Calling above functions so lists get populated
get_device_info()
extract_the_uuid()
sum_of_payloads()


# Reformat the data so that it satisfies the schema
def populate_dict_to_match_schema():
    for i in range(len(data['Devices'])):
        list_.append({'Name': name[i], 'Type': type[i], 'Info': info[i], 'Uuid': uuid[i], 'PayloadTotal': total_sum[i]})

populate_dict_to_match_schema()


# Order the reformatted data by Name (ascending)
def get_name(list_):
    return list_.get('Name')

list_.sort(key=get_name)
pprint.pprint(list_)

# Writes the reformatted data to a new file in JSON format
with open("reformatted_data", "w") as outfile:
    json.dump(list_, outfile)
