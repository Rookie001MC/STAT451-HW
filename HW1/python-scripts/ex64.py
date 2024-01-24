import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "viscosity": [20.4, 30.2, 89.4, 252.6],
        "wear": [
            [58.8, 30.8, 27.3, 29.9, 17.7, 76.5],
            [44.5, 47.1, 48.7, 41.6, 32.8, 18.3],
            [73.3, 57.1, 66.0, 93.8, 133.2, 81.1],
            [30.6, 24.2, 16.6, 38.9, 28.7, 23.6],
        ],
    }
)

# Calculate the coefficient of variation for the sample at each viscosity.
# Then compare the results and comment.
df_results = pd.DataFrame(
    {
        "viscosity": df["viscosity"],
        "mean": df["wear"].apply(lambda x: sum(x) / len(x)),
        "standard_deviation": df["wear"].apply(
            lambda x: (sum([(i - sum(x) / len(x)) ** 2 for i in x]) / (len(x) - 1))
            ** (1 / 2)
        ),
        "sample_coefficient_of_variation": df["wear"].apply(
            lambda x: 100
            * (
                (sum([(i - sum(x) / len(x)) ** 2 for i in x]) / (len(x) - 1)) ** (1 / 2)
                / (sum(x) / len(x))
            )
        ),
    },
)

print(df_results)

# Construct a comparative boxplot of the data and comment on interesting features.
for i in range(len(df["wear"])):
    plt.boxplot(df["wear"][i], positions=[df["viscosity"][i]])
plt.xlabel("Viscosity")
plt.ylabel("Wear")
plt.show()
