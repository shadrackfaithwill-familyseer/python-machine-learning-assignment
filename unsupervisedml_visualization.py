
import matplotlib.pyplot as plt

# Create a scatter plot
plt.figure(figsize=(8, 5))

# Display each customer cluster in a different colour
for cluster in range(3):
    spending = [
        data[i][0] for i in range(len(data))
        if clusters[i] == cluster
    ]

    visits = [
        data[i][1] for i in range(len(data))
        if clusters[i] == cluster
    ]

    plt.scatter(
        spending,
        visits,
        label=f"Cluster {cluster}",
        s=100
    )

# Add chart title and labels
plt.title("Customer Segmentation Using K-Means")
plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")

# Display legend and grid
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Display the scatter plot
plt.show()