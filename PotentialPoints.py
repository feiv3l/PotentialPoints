import numpy as np
import pandas as pd

df = pd.read_csv ("testTable2.csv")
df.drop_duplicates(subset ="PLAYER",
                      inplace = True)




df['AVG'] = pd.to_numeric(df['AVG'], errors='coerce')
df = df.replace(np.nan, 0, regex=True)
print(df)
print(df.dtypes)

df.sort_values(by='AVG',ascending=False,inplace=True)




## Potential Points
potPoints=[]
potTeam=[]
## Relevante Spalten behalten
df=df[['PLAYER','TYPE','AVG']]

# Dataframe Filtern --> Top5 pro Team zum Testen
## Positionsspalte erstellen

df['Position']=""

df['Position']=df['PLAYER'].str[-2:]
df.loc[df['PLAYER'].str[-1:]=="K", 'Position'] = 'K'

### Filtern und Zählen
franchises=df['TYPE'].unique()

for t in franchises:
    teamlist=(df[df.TYPE == t])

    flex=pd.DataFrame()
    #Liste für jede Position erstellen RB,WR,TE,QB,FLEX,K,DEF und danach wo notwendig 2 (qb1) spieler zum Flex pool zuweisen
    #QB
    QB=teamlist[teamlist.Position == 'QB'].head(1)
    try:
        flex=pd.concat([flex, teamlist[teamlist.Position=='QB'].iloc[[1]]])
    except:
        pass
    ##RB
    RB=teamlist[teamlist.Position == 'RB'].head(2)
    try:
        flex=pd.concat([flex, teamlist[teamlist.Position=='RB'].iloc[2:]])
    except:
        pass
    ##WR
    WR=teamlist[teamlist.Position == 'WR'].head(3)
    try:
        flex=pd.concat([flex, teamlist[teamlist.Position=='WR'].iloc[3:]])
    except:
        pass
    ##TE
    TE=teamlist[teamlist.Position == 'TE'].head(1)
    try:
        flex=pd.concat([flex, teamlist[teamlist.Position=='TE'].iloc[1:]])
    except:
        pass
    ## K
    K=teamlist[teamlist.Position == 'K'].head(1)

    ## DEF
    ST=teamlist[teamlist.Position == 'ST'].head(1)

    ##Flex
    flex.sort_values(by='AVG',ascending=False)
    flex=flex.iloc[[0,1]]

    team=pd.concat([QB,RB,WR,TE,K,ST,flex])

    ## Punkte addieren
    teamsum=pd.to_numeric(team['AVG']).sum()
    ##raussschreiben
    potPoints.append(
        
            {  
                'Team': t,
                'Potential Points':  teamsum
            }
        )

    potTeam.append(
        
            {  
                'Team': t,
                'Potential Team':  team
            }
        )    

print(potPoints)
print(potTeam)



### Abspeichern


