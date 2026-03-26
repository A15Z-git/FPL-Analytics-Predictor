import pandas as pd

# URL of the CSV file (example)
url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/gws/merged_gw.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(url)
class Player:
    def __init__(self, name, GW=38):
        #setup data
        self.name=name
        self.gw=GW
        self.Data=df[df['name']==self.name]
        self.gwData=self.Data[self.Data['GW']==self.gw]

        #Cumulative stats
        self.TotalPoints=self.Data['total_points'].sum()
        self.xP=self.Data['xP'].sum()
        self.assists=self.Data['assists'].sum()
        self.clean_sheets=self.Data['clean_sheets'].sum()
        self.creativity=self.Data['creativity'].sum() #replace with ICT index

        #more expected
        self.expected_assists=self.Data['expected_assists'].sum()
        self.expected_goal_involvements=self.Data['expected_goal_involvements'].sum()
        self.expected_goals=self.Data['expected_goals'].sum()
        self.expected_goals_conceded=self.Data['expected_goals_conceded'].sum()
        self.goals_conceded=self.Data['goals_conceded'].sum()
        self.goals_scored=self.Data['goals_scored'].sum()


        #GameWeek Stats
        self.gwPoints = self.gwData['total_points'].sum()
        self.starts=self.Data['starts'].sum()
        self.fixture=self.gwData['fixture'].item()

        #Player Details
        self.position = self.gwData['position'].item()
        self.team = self.gwData['team'].item()


#Erling_Haaland=Player('Erling Haaland')
#print(Erling_Haaland.team)


