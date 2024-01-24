import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {
        "class": [
            "81 - <83",
            "83 - <85",
            "85 - <87",
            "87 - < 89",
            "89 - <91",
            "91 - <93",
            "93 - <95",
            "95 - <97",
            "97 - <99",
        ],
        "frequency": [6, 7, 17, 30, 43, 28, 22, 13, 3],
    }
)


# a. Construct a histogram based on relative frequencies and comment on any interesting features.
total_freq = sum(df["frequency"])
print(total_freq)

df["relative_frequency"] = df["frequency"].apply(lambda x: x / total_freq)

plt.bar(df["class"], df["relative_frequency"])
plt.xlabel("Class")
plt.ylabel("Relative Frequency")
plt.show()
