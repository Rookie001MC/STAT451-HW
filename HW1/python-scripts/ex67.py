import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

list_M = [3.7, 3.4, 3.7, 4.0, 3.9, 3.8, 3.4, 3.6, 3.1, 4.0, 3.4, 3.8, 3.5]
list_F = [3.8, 2.6, 3.2, 3.0, 4.3, 3.5, 3.1, 3.1, 3.2, 3.0]
df = pd.DataFrame(columns=["M", "F"], index=range(len(list_M)))


for x in range(len(list_M)):
    df.loc[x, "M"] = list_M[x]

for x in range(len(list_F)):
    df.loc[x, "F"] = list_F[x]

# b) Calculate a 10% trimmed mean for each of the two samples, and compare to other measures of center.
# For the male sample, the interpolation method must be used.

print(df)

print("Mean of M: ", df["M"].mean())
print("Mean of F: ", df["F"].mean())

print("Median of M: ", df["M"].median())
print("Median of F: ", df["F"].median())

print("Sorted M: ", sorted(list_M))
print(f"There are {len(list_M)} elements in the list, 10")
print("Trimmed mean of M: ", stats.trim_mean(list_M, 0.1))

print("Sorted F: ", sorted(list_F))
print("Trimmed mean of F: ", stats.trim_mean(list_F, 0.1))
