import json, requests
url = 'https://api.opencovid.ca/'
response = requests.get(url)
data = json.loads(response.text)

url_two = 'https://api.opencovid.ca/other?stat=prov'
response_two = requests.get(url_two)
data_two = json.loads(response_two.text)
#for key in data['summary']:
  #for items in key:
    #print(items, ":", key[items])

def write_json():
  with open("data.json", "w") as w_file:
    json.dump(data, w_file)


def read_json():
  with open("data.json", "r") as r_file:
    json.dump(data, r_file)

  print(data)
  print(data["summary"][0]["active_cases"])

def exercise():

  alberta_pop = data_two["prov"][0]["pop"]
  alberta_province = data_two["prov"][0]["province"]
  
  print(alberta_province, ":",alberta_pop)

  british_pop = data_two["prov"][1]["pop"]
  britisih_province = data_two["prov"][1]["province_full"]
  
  print(britisih_province, ":",british_pop)

  for province in data_two["prov"]:
    for detail in province:
      print(detail, ":", data_two["prov"][detail]["province"])




exercise()