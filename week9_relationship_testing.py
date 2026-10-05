import pandas as pd

students = pd.read_csv("students_sample_v2.csv")
tutors = pd.read_csv("tutors_sample_v2 (1).csv")
subjects = pd.read_csv("subjects_sample_v2 (1).csv")
sessions = pd.read_csv("sessions_sample_v2.csv")
attendance = pd.read_csv("attendance_sample_v2.csv")

missing_tutors = sessions.loc[
    ~sessions["Tutor_ID"].isin(tutors["Tutor_ID"]),
    "Tutor_ID"
].nunique()

missing_subjects = sessions.loc[
    ~sessions["Subject_ID"].isin(subjects["Subject_ID"]),
    "Subject_ID"
].nunique()

missing_sessions = attendance.loc[
    ~attendance["Session_ID"].isin(sessions["Session_ID"]),
    "Session_ID"
].nunique()

missing_students = attendance.loc[
    ~attendance["Student_ID"].isin(students["Student_ID"]),
    "Student_ID"
].nunique()

print("Relationship Testing Results")
print("----------------------------")
print("Missing Tutor references:", missing_tutors)
print("Missing Subject references:", missing_subjects)
print("Missing Session references:", missing_sessions)
print("Missing Student references:", missing_students)
