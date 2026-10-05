import pandas as pd

sessions = pd.read_csv("sessions_sample_v2.csv")

print("Total sessions:", len(sessions))
print("Missing Session_ID:", sessions["Session_ID"].isna().sum())
print("Missing Tutor_ID:", sessions["Tutor_ID"].isna().sum())
print("Missing Subject_ID:", sessions["Subject_ID"].isna().sum())
print("Missing Duration:", sessions["Duration_Minutes"].isna().sum())
print("Invalid Duration:", (sessions["Duration_Minutes"] <= 0).sum())
