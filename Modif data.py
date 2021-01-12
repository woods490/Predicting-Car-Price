import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv(r'C:\Users\Acer\Downloads\cars_data.csv')
data = data.fillna(data.mean())

print(data["body-style"].value_counts())
print(data["make"].value_counts())
print(data["fuel-type"].value_counts())
cleanup_strings = {"body-style": {"sedan": 1, "hatchback": 2, "wagon": 3, "hardtop": 4, "convertible": 5},
                   "make": {"toyota":1, "nissan": 2, "mazda":3, "honda":4, "mitsubishi": 5, "subaru": 6,
                            "volkswagen":7, "peugot": 8, "volvo":9, "dodge": 10, "bmw": 11, "mercedes-benz":12,
                            "plymouth": 13, "saab": 14, "audi":15, "porsche": 16, "alfa-romero": 17, "chevrolet": 18,
                            "jaguar": 19, "isuzu": 20, "renault": 21, "mercury": 22},
                   "fuel-type": {"gas":1, "diesel":2}}
data = data.replace(cleanup_strings)
data.to_csv(r'C:\Users\Acer\Downloads\cars_data_modified.csv')
