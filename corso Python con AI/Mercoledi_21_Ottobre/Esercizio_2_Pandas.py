import pandas as pd 

df_ball = pd.read_csv("ballon_dor_rankings.csv")

#Rimozione duplicati se presenti 
df_ball = df_ball.drop_duplicates()
df_ball = df_ball.dropna()

print("")
print(df_ball.info())
print("")

#Vincitori del pallone d'oro
df_vincitori = df_ball[df_ball["Rank"] == "1st"]

print("I primi 5 vincitori del pallone d'oro sono: \n ", df_vincitori.head() , "\n")
print("Gli ultimi  5 vincitori del pallone d'oro sono: \n ", df_vincitori.tail())

#Secolo in cui  è stato vinto, True se nel 2000 , False altrimenti 

df_vincitori["Secolo"] = df_vincitori["Year"] >= 2000


#definizione dataset con vittorie del real madrid 

df_real_madrid = df_vincitori[df_vincitori["Club"] == "Real Madrid"]

#occorrenze di vittorie del real madrid 
print(" ")
print("Il numero di palloni d'oro ottenuti da squadre che giocavano nel Real Madrid è: ", (df_vincitori["Club"] == "Real Madrid").sum())

#occorrenze di vittorie da parte di Lionel Messi 

print(" ")
df_messi = df_vincitori[df_vincitori["Player"].str.startswith("Lionel")]

print("Lionel Messi ha vinto: ", len(df_messi), "palloni d'oro")