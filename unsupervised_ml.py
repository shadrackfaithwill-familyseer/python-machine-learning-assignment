from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# customer data
# Columns: Monthly Spending (KES), Monthly Visits
data = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]
]

# 3. Scale the customer data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 4. Create the K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# 5. Train the model and assign clusters
clusters = kmeans.fit_predict(scaled_data)

# 6. Display the cluster assigned to each customer
print("CUSTOMER CLUSTER ASSIGNMENTS")
print("-" * 35)

for i, cluster in enumerate(clusters):
    print(f"Customer {i + 1}: Cluster {cluster}")

# 7. Display the total number of customers in each cluster
print("\nTOTAL CUSTOMERS IN EACH CLUSTER")
print("-" * 35)

for cluster in range(3):
    count = sum(clusters == cluster)
    print(f"Cluster {cluster}: {count} customers")

