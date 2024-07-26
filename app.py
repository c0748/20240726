import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(8, 3))

plt.plot(df["Date"], df["Aomori"], label="Aomori")
plt.plot(df["Date"], df["Shimane"], label="Shimane")

plt.title("青森島根のコロナ感染者数")
plt.xlabel("日付")
plt.ylabel("感染者数")

plt.xticks(rotation=45)
plt.legend()

plt.show()
