import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv("data/sales.csv")

# 日付処理
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

# 売上計算
df["sales"] = df["amount"] * df["price"]

# 月別集計
summary = df.groupby("month")["sales"].sum()

# Excel出力
summary.reset_index().to_excel("monthly_sales.xlsx", index=False)

# グラフ作成
summary.plot(kind="bar")
plt.title("Monthly Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()
