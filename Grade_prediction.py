import pickle
import numpy as np


def predict_single(student, dv, model):
    X = dv.transform([student])
    y_pred = model.predict(X)
    return y_pred
    

with open('lar.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
    

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

prediction = predict_single(person, dv, model)

print('Student Grade', prediction)
