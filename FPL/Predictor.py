from Base import name_list

import pandas as pd


#These scrape live for every match and must be updated for every game week, helpful fir identifying player availability
#player data not available in normal csv
url="https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/players_raw.csv"
df2 = pd.read_csv(url)
status=df2[["status",'first_name','second_name']]
status['full_name']=status['first_name']+' '+status['second_name']
status=status[status["full_name"].isin(name_list)]
status=status[['status','full_name']]
print(status)

Prob_play=df2[["chance_of_playing_this_round",'first_name','second_name']]
Prob_play['full_name']=Prob_play['first_name']+' '+Prob_play['second_name']
Prob_play=Prob_play[Prob_play["full_name"].isin(name_list)]
Prob_play=Prob_play[['chance_of_playing_this_round','full_name']]
print(Prob_play)

Prob_play2=df2[["chance_of_playing_next_round",'first_name','second_name']]
Prob_play2['full_name']=Prob_play2['first_name']+' '+Prob_play2['second_name']
Prob_play2=Prob_play2[Prob_play2["full_name"].isin(name_list)]
Prob_play2=Prob_play2[['chance_of_playing_next_round','full_name']]
print(Prob_play2)
#do not exist for older game weeks sadly
#Def_contri=df2[["defensive_contribution",'first_name','second_name']]
#Def_contri['full_name']=Def_contri['first_name']+' '+Def_contri['second_name']
#Def_contri=Def_contri[Def_contri["full_name"].isin(name_list)]
#Def_contri=Def_contri[['defensive_contribution','full_name']]
#print(Def_contri)


