import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path


cartella = Path(__file__).parent

cd_data = pd.read_csv(cartella / "candy-data.csv")
cd_vendite = pd.read_csv(cartella / "candy-vendite.csv")

#Esplorazione 

print(cd_data.shape)
print(cd_vendite.shape)
print("")
print(cd_data.columns)
print("")
print(cd_vendite.columns)

print("")

print(cd_data.describe())
print(cd_vendite.describe())

print(cd_data.isnull().sum())
print(cd_vendite.isnull().sum())

print("Duplicati cd_data:", cd_data.duplicated().sum())
print("Duplicati cd_vendite:", cd_vendite.duplicated().sum())

#Non sono presenti duplicati ne valori nulli 

print(cd_vendite.head(20))
#print(cd_vendite.describe())

#merged_df = pd.merge(cd_data,cd_vendite, on="competitorname")
#print(merged_df.head(20))

#Analizziamo le vendite di caramelle per area 
vendite_per_area = cd_vendite.groupby("area_vendita")["unita_vendute"].sum()
giacenza_per_area = cd_vendite.groupby("area_vendita")["giacenza_magazzino"].sum()
budget_marketing_euro = cd_vendite.groupby("area_vendita")["budget_marketing_euro"].sum()

print("Vendite per area")
print(vendite_per_area)
print("")
print("Giacenza per area")
print(giacenza_per_area)
print("")
print("Budget_marketing per area")
print(budget_marketing_euro)
print("")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

# Vendite per area
ax1.bar(vendite_per_area.index, vendite_per_area.values)
ax1.set_title("Vendite per Area")
ax1.set_xlabel("Area")
ax1.set_ylabel("Unità Vendute")

# Giacenza per area
ax2.bar(giacenza_per_area.index, giacenza_per_area.values)
ax2.set_title("Giacenza per Area")
ax2.set_xlabel("Area")
ax2.set_ylabel("Unità in Magazzino")

# Budget marketing per area
ax3.bar(budget_marketing_euro.index, budget_marketing_euro.values)
ax3.set_title("Budget Marketing per Area")
ax3.set_xlabel("Area")
ax3.set_ylabel("Budget (€)")

ax1.grid()
ax2.grid()
ax3.grid()

plt.tight_layout()
plt.show()



#Analizziamo le percentuali di zucchero presenti nei prodotti delle aziende 
caramelle_zucchero = cd_data.sort_values(
    by="sugarpercent",
    ascending=False
)

#print(caramelle_zucchero[["competitorname", "sugarpercent"]])

caramelle_zucchero = caramelle_zucchero[caramelle_zucchero["sugarpercent"] > 0.9]


plt.figure()

plt.bar(caramelle_zucchero["competitorname"], caramelle_zucchero["sugarpercent"])

plt.xlabel("Nome della caramella")
plt.ylabel("Percentuale di zucchero")
plt.title("Caramelle con sugarpercent > 0.9")


plt.tight_layout()
plt.show()