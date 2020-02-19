# pandas 
# most popular library for table-data-analysis
# pandas and xlrd Pakete pip install
# zwei wichtige Objekte: Series, DataFrame
# DataFrame -> Tabelle
# 
import pandas as pd 

# read csv Datei
# df = pd.read_csv("astronauts.csv")
df = pd.read_csv("astronauts.csv", delimiter=',')

# print(f'\n')
# print(df)
# print(f'\n')
# print(df.head(3))
# print(f'\n')
# print(df.tail(3))

# # Die Länge des Datensatzes
# print(f'\n')
# print(len(df))

# auf eine bestimmte index zugreifen.
# print("Zugriff auf Index 0: \n")
# Index
# [0]  
#

# index location: iloc[x]
# print(df.iloc[0]) 
# print(f'\n')
# print(df["Name"])

#

# print(df.iloc[4:9])   [start:stop:step]
# print(df.iloc[::100]) # jede 100er Eintrag

# rows ausgeben
# print("Über alle Entries")
# for row in df.iterrows():
#     print(row)
#     print(f'\n')

# for row in df.iterrows():
#     # tupel-objekt
#     # pos= row[0] # in pos steht der erste Wert index
#     # print(pos)
#     # info= row[1] # info
#     # print(pos, info["Gender"])
#     print(row[0])
#     print(row[1]["Name"], row[1]["Gender"])
#     break # damit man nur einen Eintrag ausgelesen bekommt

# female_list = []
# for row in df.iterrows():
#     if row[1]["Gender"] == "Female":
#         female_list.append(row)
#         # print(f'{row[0]} - {row[1]["Name"]}: {row[1]["Gender"]}')

# print(len(female_list))
#     #break # damit man nur einen Eintrag ausgelesen bekommt

# rang = df.[df["Military Rank"]=='Colonel']
# for row in rang.iterrows():
#     print(row)

# rang = df[ (df["Gender"]=='Female') & (df["Military Rank"]=='Colonel')]  # Bedingungen bilden
# print(len(rang))
# for row in rang.iterrows():
#     print(row)
# print(df.sort_values("Name", ascending=True))


info = df.sort_values("Name", ascending=True)
# a = ["R", "r"]
# for element in info["Name"]:  
#     if element[0] in a:
#         print(element)

# beginnend mit Etwas
for element in info["Name"]:
    if element.startswith("Edward"):
        print(element)
        
# endend mit Etwas
for element in info["Name"]:
    if element.endswith("d"):
        print(element)