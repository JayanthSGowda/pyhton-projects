import json

with open('weatherdata.json') as file:
    data = json.load(file)

# for hour in range(10):
#     print(f'code = {data["data"][0]["weather"]["code"]}')
#     # print(f'rain = {data["data"][0]["precip"]}')

code_list = [day["weather"]["code"] for day in data["data"]][:12]
# twelve_hours = code_list[:12]
it_rains = False
for n in code_list:
    if n < 700:
        it_rains = True

if it_rains:
    print("Bring an umbrella")
