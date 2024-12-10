import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Download the dataset
path = kagglehub.dataset_download("abcsds/pokemon")
dataset_path = f"{path}/Pokemon.csv"  # Update with actual file name if necessary
pokemon_data = pd.read_csv(dataset_path)

# Step 2: Clean and Prepare Data
pokemon_data["Total"] = pokemon_data["HP"] + pokemon_data["Attack"] + pokemon_data["Defense"] + \
                        pokemon_data["Sp. Atk"] + pokemon_data["Sp. Def"] + pokemon_data["Speed"]

# Step 3: Graphs

# 1. Distribution of Pokémon by Type (Scatter plot using circles in XY plane)
plt.figure(figsize=(12, 8))
type_counts = pokemon_data["Type 1"].value_counts()
plt.scatter(range(len(type_counts)), type_counts.values, s=type_counts.values * 50, alpha=0.6, edgecolors="w")
for i, (x, y) in enumerate(zip(range(len(type_counts)), type_counts.values)):
    plt.text(x, y + 3, type_counts.index[i], ha='center')  # Adjusted to place labels above the circles
plt.title("Distribution of Pokémon by Type (Circle Scatter)")
plt.xlabel("Type Index")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 2. Top 10 Most Powerful Pokémon (Bar Chart)
top_10 = pokemon_data.nlargest(10, "Total").sort_values("Total", ascending=False)
plt.figure(figsize=(14, 6))
sns.barplot(x="Total", y="Name", data=top_10, palette="viridis")
plt.title("Top 10 Most Powerful Pokémon")
plt.xlabel("Total Stats")
plt.ylabel("Pokémon Name")
plt.tight_layout()
plt.show()

# 3. Ranking of Pokémon by HP (Scatter Plot with Names)
plt.figure(figsize=(12, 8))
sns.scatterplot(x="HP", y="Total", hue="Type 1", size="HP", data=pokemon_data, sizes=(20, 200), alpha=0.7)
for _, row in pokemon_data.iterrows():
    plt.text(row["HP"], row["Total"], row["Name"], fontsize=8, alpha=0.7)  # Added Pokémon names
plt.title("Ranking of Pokémon by HP vs Total Stats")
plt.xlabel("HP")
plt.ylabel("Total Stats")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type 1")
plt.tight_layout()
plt.show()

# 4. Pokémon Distribution by Generation (Bar Chart with Generation Names)
generation_names = {
    1: "Generation I",
    2: "Generation II",
    3: "Generation III",
    4: "Generation IV",
    5: "Generation V",
    6: "Generation VI",
}
pokemon_data["Generation Name"] = pokemon_data["Generation"].map(generation_names)

plt.figure(figsize=(10, 6))
sns.countplot(x="Generation Name", data=pokemon_data, palette="Set2", order=generation_names.values())
plt.title("Pokémon Distribution by Generation")
plt.xlabel("Generation")
plt.ylabel("Count")
plt.xticks(rotation=45)  # Rotate for better readability
plt.tight_layout()
plt.show()
