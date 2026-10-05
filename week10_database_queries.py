import pandas as pd

# Load the database sample data
students = pd.read_csv("students_sample_v2.csv")
tutors = pd.read_csv("tutors_sample_v2 (1).csv")
subjects = pd.read_csv("subjects_sample_v2 (1).csv")
sessions = pd.read_csv("sessions_sample_v2.csv")
attendance = pd.read_csv("attendance_sample_v2.csv")

print("=== Week 10 Database Query Development ===")

# Query 1: Count sessions by tutor
sessions_by_tutor = (
    sessions.groupby("Tutor_ID")
    .size()
    .reset_index(name="Session_Count")
    .sort_values("Session_Count", ascending=False)
)

print("\nSessions by Tutor:")
print(sessions_by_tutor)

# Query 2: Count sessions by subject
sessions_by_subject = (
    sessions.groupby("Subject_ID")
    .size()
    .reset_index(name="Session_Count")
    .sort_values("Session_Count", ascending=False)
)

print("\nSessions by Subject:")
print(sessions_by_subject)

# Query 3: Calculate average session duration
average_duration = sessions["Duration_Minutes"].mean()

print("\nAverage Session Duration:")
print(round(average_duration, 2), "minutes")

# Query 4: Count attendance by status
attendance_summary = (
    attendance["Status"]
    .value_counts()
    .reset_index()
)

attendance_summary.columns = ["Status", "Count"]

print("\nAttendance Summary:")
print(attendance_summary)

# Query 5: Calculate attendance rate
total_attendance = len(attendance)
present_count = (attendance["Status"] == "Present").sum()

attendance_rate = (present_count / total_attendance) * 100

print("\nAttendance Rate:")
print(round(attendance_rate, 2), "%")

print("\n=== Query Development Complete ===")
