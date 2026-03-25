import pandas as pd
import Player as Pl

# URL of the CSV file (example)
url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/gws/merged_gw.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(url)

P1=df[df['name'] == 'Kyle Walker']
P2=df[df['name'] == 'Erling Haaland']
P3=df[df['name'] == 'Cole Palmer']
P4=df[df['name'] == 'Bukayo Saka']
P5=df[df['name'] == 'Mohammed Salah']
P6=df[df['name'] == 'Virgil Van Dijk']
P7=df[df['name'] == 'Antoine Semenyo']
P8=df[df['name'] == 'Bruno Fernandes']
P9=df[df['name'] == 'Chris Wood']
P10=df[df['name'] == 'Rasmus Højlund']
P11=df[df['name'] == 'Phil Foden']
P12=df[df['name'] == 'Mason Mount']
P13=df[df['name'] == 'Micky van de Ven']
P14=df[df['name'] == 'Pedro Porro']
P15=df[df['name'] == 'William Saliba']
P16=df[df['name'] == 'Kevin De Bruyne']
P17=df[df['name'] == 'Ibrahima Konaté']
P18=df[df['name'] == 'Declan Rice']
P19=df[df['name'] == 'Cody Gakpo']
P20=df[df['name'] == 'Alejandro Garnacho']
P21=df[df['name'] == 'Anthony Elanga']
P22=df[df['name'] == 'Marc Guéhi']
P23=df[df['name'] == 'Ollie Watkins']
P24=df[df['name'] == 'Bryan Mbeumo']
P25=df[df['name'] == 'Liam Delap']
P26=df[df['name'] == 'Bruno Guimarães']

#A shorter DF of just relevant players below
Sample=pd.concat([P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,P19,P20,P21,P22,P23,P24,P25,P26],ignore_index=True)