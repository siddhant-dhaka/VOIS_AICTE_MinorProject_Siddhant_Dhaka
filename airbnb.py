# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "/mnt/data/1730285881-Airbnb_Open_Data.xlsx"
df = pd.read_excel(file_path)

# Preview dataset
print("Data Preview:")
print(df.head(), "\n")
print("Columns:", df.columns, "\n")

# --- 1️⃣ Booking Patterns ---
print("=== Booking Patterns Analysis ===")
# Assuming dataset includes columns: 'last_review', 'neighbourhood', 'availability_365', 'minimum_nights'

# Convert review date to datetime and extract month
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
df['month'] = df['last_review'].dt.month

# Identify peak booking months
booking_pattern = df['month'].value_counts().sort_index()
print("Bookings by Month:\n", booking_pattern)

plt.figure(figsize=(10,5))
sns.barplot(x=booking_pattern.index, y=booking_pattern.values, palette="viridis")
plt.title("Peak Booking Seasons by Month")
plt.xlabel("Month")
plt.ylabel("Number of Bookings")
plt.show()

# --- 2️⃣ Pricing Strategies ---
print("=== Pricing Strategies Analysis ===")
# Analyze pricing by neighborhood and room type
pricing_summary = df.groupby(['neighbourhood', 'room_type'])['price'].mean().reset_index()
print("Average Price by Neighborhood and Room Type:\n", pricing_summary.head())

plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='room_type', y='price', showfliers=False)
plt.title("Price Distribution by Room Type")
plt.ylabel("Price ($)")
plt.xlabel("Room Type")
plt.show()

# --- 3️⃣ Guest Preferences ---
print("=== Guest Preferences Analysis ===")
# Assuming features like 'number_of_reviews', 'reviews_per_month', 'room_type'
guest_pref = df.groupby('room_type')[['number_of_reviews', 'reviews_per_month']].mean().reset_index()
print("Guest Preference Indicators:\n", guest_pref)

plt.figure(figsize=(10,5))
sns.barplot(data=guest_pref, x='room_type', y='number_of_reviews', palette="magma")
plt.title("Average Number of Reviews by Room Type")
plt.ylabel("Average Reviews")
plt.xlabel("Room Type")
plt.show()

# --- 4️⃣ Host Performance ---
print("=== Host Performance Analysis ===")
# Assuming columns like 'host_id', 'host_name', 'availability_365', 'number_of_reviews', 'reviews_per_month'

host_perf = df.groupby('host_id').agg({
    'number_of_reviews':'sum',
    'reviews_per_month':'mean',
    'availability_365':'mean',
    'price':'mean'
}).reset_index()

top_hosts = host_perf.sort_values(by='number_of_reviews', ascending=False).head(10)
print("Top 10 Performing Hosts:\n", top_hosts)

plt.figure(figsize=(12,6))
sns.barplot(data=top_hosts, x='host_id', y='number_of_reviews', palette="coolwarm")
plt.title("Top 10 Hosts by Total Reviews")
plt.xlabel("Host ID")
plt.ylabel("Total Reviews")
plt.show()

print("\nAnalysis Completed ✅")
