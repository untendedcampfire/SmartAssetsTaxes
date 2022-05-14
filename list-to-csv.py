import pandas as pd
import pickle
import numpy as np

with open("take_home_dump", "rb") as fp:
    take_home = pickle.load(fp)
with open("percentage_dump", "rb") as fp:
    percentage = pickle.load(fp)

p_list = [float(perc)/100 for perc in percentage]
tk_list = [int(tk.replace(",", "")) for tk in take_home]
# salary_list = np.arange(40000, 121000, 1000).tolist()
salary_range_lg = np.arange(20000, 200000, 100).tolist()
# salary_range_smol = np.arange(40000, 50000, 1000).tolist()

df = pd.DataFrame(
    {
        "Salary": salary_range_lg,
        "Tax Percentage": p_list,
        "Bi-Weekly Take home": tk_list
    }
)

# print(df)
with open("PAYCHECK.csv", "wb") as f:
    df.to_csv(f)

# print(len(salary_range_lg))
