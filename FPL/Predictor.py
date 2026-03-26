import pandas as pd

from Base import name_list


url="https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/players_raw.csv"
df2 = pd.read_csv(url)
status=df2[["status",'first_name','second_name']]
status['full_name']=status['first_name']+' '+status['second_name']
status=status[status["full_name"].isin(name_list)]
status=status[['status','full_name']]
print(status)