import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\Muttaki\Desktop\analysis gov\undo\data-resource_2024_06_25_Table-22 Advances Distributed by DivisionsDistricts and Areas(UrbanTotal).csv"
df = pd.read_csv(file_path, skiprows=2)
df.columns = df.columns.str.strip()
if 'Division/District/Area' in df.columns:
    df = df.rename(columns={'Division/District/Area': 'District'})
elif 'Unnamed: 0' in df.columns:
    df = df.rename(columns={'Unnamed: 0': 'District'})

df = df.dropna(subset=['District'])
def dataset_summary(df):
    print("===== Dataset Summary =====")
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")
    if 'District' in df.columns:
        print(f"Unique Divisions/Districts: {df['District'].nunique()}")
        print("Sample Districts:", df['District'].dropna().unique()[:10])
    total_cols = [c for c in df.columns if 'Total' in c]
    print(f"Available Quarters: {len(total_cols)}")
    print("Sample Quarters:", total_cols[:5])
def plot_grand_total(df):
    if 'District' not in df.columns:
        print("'District' column missing.")
        return

    grand_total = df[df['District'].str.upper() == 'GRAND TOTAL'].iloc[:, 2:].filter(like='Total')
    if grand_total.empty:
        print("No Grand Total row found.")
        return

    quarters = grand_total.columns
    values = grand_total.values.flatten()

    plt.figure(figsize=(10, 6))
    plt.plot(quarters, values, marker='o')
    plt.title('Bangladesh Advances Tracker (2018–2024): Grand Total')
    plt.xlabel('Quarter')
    plt.ylabel('Advances (Crore Tk)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def plot_urban_rural(df, division="BARISHAL DIVISION"):
    if 'District' not in df.columns:
        print("'District' column missing.")
        return
    division_df = df[df['District'].str.upper().str.contains(division.upper(), na=False)]
    urban_cols = [col for col in df.columns if 'URBAN' in col.upper() and 'TOTAL' not in col.upper()]
    rural_cols = [col for col in df.columns if 'RURAL' in col.upper() and 'TOTAL' not in col.upper()]

    if division_df.empty:
        print(f"No data found for {division}. Check spelling or CSV content.")
        return
    if not urban_cols or not rural_cols:
        print("Urban/Rural columns not found in dataset.")
        print("Columns available:", df.columns.tolist()[:20])
        return

    quarters = [col.split(',')[0] for col in urban_cols]
    urban_values = division_df[urban_cols].values.flatten()
    rural_values = division_df[rural_cols].values.flatten()

    plot_df = pd.DataFrame({
        'Quarter': quarters * 2,
        'Advances': list(urban_values) + list(rural_values),
        'Type': ['Urban'] * len(quarters) + ['Rural'] * len(quarters)
    })

    if plot_df.empty:
        print(f"No valid data to plot for {division}.")
        return

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Quarter', y='Advances', hue='Type', data=plot_df)
    plt.title(f'Bangladesh Advances Tracker (2018–2024): Urban vs. Rural in {division}')
    plt.xlabel('Quarter')
    plt.ylabel('Advances (Crore Tk)')
    plt.xticks(rotation=45)
    plt.legend(title='Area')
    plt.tight_layout()
    plt.show()
def plot_yoy_growth(df, division="DHAKA DIVISION"):
    if 'District' not in df.columns:
        print("'District' column missing.")
        return

    division_df = df[df['District'].str.upper().str.contains(division.upper(), na=False)]
    if division_df.empty:
        print(f"No data found for {division}.")
        return

    total_cols = [col for col in df.columns if 'Total' in col]
    totals = division_df[total_cols].values.flatten()

    if len(totals) < 5:
        print("Not enough data to compute YoY growth.")
        return

    yoy_growth = [(totals[i+4] / totals[i] - 1) * 100 for i in range(len(totals) - 4)]
    quarters_yoy = total_cols[4:]  # start from 2019Q1

    plt.figure(figsize=(10, 6))
    plt.plot(quarters_yoy, yoy_growth, marker='o', color='purple')
    plt.title(f'Bangladesh Advances Tracker (2018–2024): YoY Growth in {division}')
    plt.xlabel('Quarter')
    plt.ylabel('YoY Growth Rate (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def plot_top_divisions(df, top_n=5):
    if 'District' not in df.columns:
        print("'District' column missing.")
        return

    total_cols = [col for col in df.columns if 'Total' in col]
    if not total_cols:
        print("No Total columns found.")
        return

    latest_col = total_cols[-1]
    division_totals = df[df['District'].str.upper().str.contains("DIVISION", na=False)][['District', latest_col]]

    if division_totals.empty:
        print("No division-level data found.")
        return

    top_divs = division_totals.sort_values(latest_col, ascending=False).head(top_n)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=latest_col, y='District', data=top_divs, palette="viridis")
    plt.title(f"Top {top_n} Divisions by Advances ({latest_col})")
    plt.xlabel("Advances (Crore Tk)")
    plt.ylabel("Division")
    plt.tight_layout()
    plt.show()
def plot_qoq_growth(df):
    grand_total = df[df['District'].str.upper() == 'GRAND TOTAL'].iloc[:, 2:].filter(like='Total')
    if grand_total.empty:
        print(" No Grand Total row found.")
        return

    quarters = grand_total.columns
    values = grand_total.values.flatten()

    qoq_growth = [(values[i+1] / values[i] - 1) * 100 for i in range(len(values)-1)]

    plt.figure(figsize=(10, 6))
    plt.bar(quarters[1:], qoq_growth, color='teal')
    plt.title("Quarter-over-Quarter Growth (Grand Total)")
    plt.xlabel("Quarter")
    plt.ylabel("QoQ Growth (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def plot_heatmap(df):
    if 'District' not in df.columns:
        print("'District' column missing.")
        return

    division_df = df[df['District'].str.upper().str.contains("DIVISION")].iloc[:, 2:].filter(like='Total')
    if division_df.empty:
        print(" No division-level data found for heatmap.")
        return

    division_df.index = df[df['District'].str.upper().str.contains("DIVISION")]['District']

    plt.figure(figsize=(12, 6))
    sns.heatmap(division_df, cmap="YlGnBu", linewidths=0.5)
    plt.title("Advances Heatmap (Divisions vs Quarters)")
    plt.xlabel("Quarter")
    plt.ylabel("Division")
    plt.tight_layout()
    plt.show()
dataset_summary(df)
plot_grand_total(df)
plot_urban_rural(df, "BARISHAL DIVISION")
plot_yoy_growth(df, "DHAKA DIVISION")
plot_top_divisions(df, top_n=5)
plot_qoq_growth(df)
plot_heatmap(df)
