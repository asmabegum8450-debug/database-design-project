import pandas as pd

attendance = pd.read_csv("attendance_sample_v2.csv")

print("Total attendance records:", len(attendance))
print("Missing Session_ID:", attendance["Session_ID"].isna().sum())
print("Missing Student_ID:", attendance["Student_ID"].isna().sum())
print("Missing Status:", attendance["Status"].isna().sum())
print("Attendance statuses:")
print(attendance["Status"].value_counts())
