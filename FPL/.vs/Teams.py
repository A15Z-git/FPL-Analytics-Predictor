import pandas as pd
import requests
import re
import json


df=pd.read_excel(r"C:\ML and Kaggle\FPL project\24-25\24-25 understat.xlsx")

url24="https://understat.com/league/EPL/2024"

#I do not really get Json stuff, but since its really just a one time download before match
#Not the most important. Real setting I'd run into problem if source site changed,
#but this exact code is unlikely to change+if database significantly changed I'd have to manually edit anyways.

df.to_csv("understat_2024_detailed.csv", index=False)

#For newly promoted teams we use Rel 1 2 and 3 for standardization, with name fixed inside
class Team:
    def __init__(self,team, GW=38, year=24-25):
        self.team=team
        self.GW=GW
        self.year=year

        self.Data=df[df['Team']==self.team]

        self.xG=self.Data["xG"].item()/38
        self.xGA=self.Data["yG"].item()/38
        self.goals=self.Data["goals"].item()/38
        self.ga=self.Data["ga"].item()/38








