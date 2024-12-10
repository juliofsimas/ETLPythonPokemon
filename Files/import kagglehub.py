import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Download the latest version of the dataset
path = kagglehub.dataset_download("abcsds/pokemon")

# Step 2: Load the dataset
# Assuming the dataset is a CSV file, typically 'pokemon.csv'
dataset_path = f"{path}/pokemon.csv"  # Replace 'pokemon.csv' with the actual file name
pokemon_data = pd.read_csv(dataset_path)

# Step 3: Explore the dataset
print(pokemon_data.head())  # Inspect the first few rows
print(pokemon_data.info())  # Understand data types and null values

# Step 4: Create Principal Graphs

# 1. Distribution of Pokémon by Type
plt.figure(figsize=(10, 6))
sns.countplot(y="Type 1", data=pokemon_data, order=pokemon_data["Type 1"].value_counts().index)
plt.title("Distribution of Pokémon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type 1")
plt.tight_layout()
plt.show()

# 2. Relationship between Attack and Defense
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Attack", y="Defense", hue="Legendary", data=pokemon_data)
plt.title("Attack vs Defense with Legendary Status")
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.tight_layout()
plt.show()

# 3. Average Stats by Primary Type
stats_cols = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
type_stats = pokemon_data.groupby("Type 1")[stats_cols].mean().sort_values("Attack", ascending=False)

type_stats.plot(kind="bar", figsize=(12, 6), stacked=True)
plt.title("Average Stats by Primary Type")
plt.xlabel("Primary Type")
plt.ylabel("Average Stats")
plt.legend(title="Stat Categories")
plt.tight_layout()
plt.show()

# 4. Count of Legendary vs Non-Legendary Pokémon
plt.figure(figsize=(8, 6))
sns.countplot(x="Legendary", data=pokemon_data)
plt.title("Legendary vs Non-Legendary Pokémon")
plt.xlabel("Legendary Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
