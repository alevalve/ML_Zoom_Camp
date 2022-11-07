import json
import requests

url = 'http://localhost:8080'

person = {"school": "GP",
"sex"          :                "M",
"age"          :                18,
"address"      :             "U",
"famsize"      :        "GT3",
"Pstatus"      :          "A",
"Fedu"         :                4,
"Mjob"         :         "at_home",
"Fjob"         :       "teacher",
"reason"       :         "course",
"guardian"     :       "mother",
"traveltime"   :          4,
"studytime"    :         4,
"failures"     :       0,
"schoolsup"    :      "no",
"famsup"       :      "no",
"paid"         :     "yes",
"activities"   :     "no",
"nursery"      :  "yes",
"higher"       :  "yes",
"internet"     :  "no",
"romantic"     : "no",
"famrel"       :  4,
"freetime"     :   3,
"goout"        :  4,
"Walc"         : 5,
"health"       : 5,
"absences"     :4,
"G2"           :10}

url = 'http://127.0.0.1:9696/prediction'
response = requests.post(url, json = person)
print(response.json())