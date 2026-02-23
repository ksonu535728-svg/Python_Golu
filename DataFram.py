import pandas as pd 

data=[
[101,"Sonu","Cricket",80],
[102,"Kalu Bhai","Football",87],
[103,"Shubham","HOckey",90],
[104,"Neha","Badminton",90]
]

df=pd.Dataframe(data,columns=["Player ID","Name","Sport","Score:"])

print(df)