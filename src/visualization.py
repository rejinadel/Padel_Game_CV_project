import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# STYLE (IMPORTANT FOR BEAUTY)

sns.set_style("whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"

# LOAD DATA

CSV_PATH = r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\output\shot_events.csv"
OUTPUT_DIR = r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\output"

df = pd.read_csv(CSV_PATH).drop_duplicates()
df = df.sort_values("frame")
df["index"] = range(len(df))


# KPIs

total = len(df)
fh = len(df[df["shot_type"] == "Forehand"])
bh = len(df[df["shot_type"] == "Backhand"])


# FIGURE (CLEAN LAYOUT)

fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor("#f5f7fa")

plt.suptitle(
    "SHOT ANALYSIS DASHBOARD",
    fontsize=22,
    fontweight="bold",
    color="#2c3e50"
)


# KPI BOXES (TOP ROW)
ax1 = plt.subplot2grid((3, 6), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 6), (0, 2), colspan=2)
ax3 = plt.subplot2grid((3, 6), (0, 4), colspan=2)

for ax in [ax1, ax2, ax3]:
    ax.axis("off")
    ax.set_facecolor("#ffffff")

ax1.text(0.5, 0.5, f"{total}\nTOTAL SHOTS",
         ha="center", va="center", fontsize=16, fontweight="bold")

ax2.text(0.5, 0.5, f"{fh}\nFOREHAND",
         ha="center", va="center", fontsize=16, color="green", fontweight="bold")

ax3.text(0.5, 0.5, f"{bh}\nBACKHAND",
         ha="center", va="center", fontsize=16, color="blue", fontweight="bold")

# BAR CHART
ax4 = plt.subplot2grid((3, 6), (1, 0), colspan=3)

sns.countplot(x="shot_type", data=df, palette=["#2ecc71", "#3498db"], ax=ax4)

ax4.set_title("Shot Count Comparison", fontsize=14, fontweight="bold")
ax4.set_xlabel("")
ax4.set_ylabel("Count")
# DONUT CHART

ax5 = plt.subplot2grid((3, 6), (1, 3), colspan=3)

counts = df["shot_type"].value_counts()

ax5.pie(
    counts,
    labels=counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#2ecc71", "#3498db"]
)

centre = plt.Circle((0, 0), 0.60, fc="white")
fig.gca().add_artist(centre)

ax5.set_title("Shot Distribution", fontsize=14, fontweight="bold")


# SHOTS OVER TIME (FULL WIDTH)
ax6 = plt.subplot2grid((3, 6), (2, 0), colspan=6)

sns.scatterplot(
    x="index",
    y="shot_type",
    hue="shot_type",
    palette=["#2ecc71", "#3498db"],
    data=df,
    ax=ax6
)

ax6.set_title("Shots Over Time", fontsize=14, fontweight="bold")
ax6.set_xlabel("Time Progression")
ax6.set_ylabel("Shot Type")


# SAVE

output_path = os.path.join(OUTPUT_DIR, "shot_dashboard.png")

plt.tight_layout()
plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())

plt.show()

print("DASHBOARD SAVED:", output_path)