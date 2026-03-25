import pandas as pd
import Player as Pl

# URL of the CSV file (example)
url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/gws/merged_gw.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(url)
print(df.columns)


Sample=df.sort_values(by='name')
name_list=Sample.loc[::38,'name'].values

#I create a list of classes below for easier access.
players=[Pl.Player(name) for name in name_list]


#num=0
relevantPlayers=[player for player in players if player.starts>13 and player.TotalPoints>50]

name_list=[player.name for player in relevantPlayers]  #shortened nameList




Pts=[]
for player in relevantPlayers:
    Pts.append((player.name, player.TotalPoints))

Pts.sort(key=lambda x: x[1],reverse=True)
#normal sort uses the names so this sorts it instead using the 2nd item (the scores)
del player

Best11=[]
for i in range(11):
    Best11.append(Pts[i])



#weekly points part


def setweek(GW):
        players = [Pl.Player(name,GW) for name in name_list]
        return players


def ReturnWeeklyPts(GW):
    players=setweek(GW) #creates a copy of players with data from that GW
    Weeklypts = []
    for player in players:
        Weeklypts.append((player.name, player.gwPoints))
    Weeklypts.sort(key=lambda x: x[1], reverse=True)
    BestWeekly=[]
    for i in range(11):
        BestWeekly.append(Weeklypts[i])
    del i
    return BestWeekly


#did it in a dif way cause it requires setweek










