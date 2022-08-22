import pandas as pd

 
# making data frame from csv file
data = pd.read_csv("testTable2.csv")

# sorting by first name
data.sort_values("AVG", ascending=False)
 
# dropping ALL duplicate values
data.drop_duplicates(subset ="PLAYER",
                     keep = False, inplace = True)
 
# displaying data
print(data)