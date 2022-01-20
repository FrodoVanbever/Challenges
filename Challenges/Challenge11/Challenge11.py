import json
import pandas as pd

with open('./in.json') as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data)

df.to_excel('./uit.xlsx')