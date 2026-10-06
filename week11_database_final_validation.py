import pandas as pd

print("=== Week 11 Database Final Validation ===")

# Load database sample data
students = pd.read_csv("students_sample_v2.csv")
tutors = pd.read_csv("tutors_sample_v2 (1).csv")
subjects = pd.read_csv("subjects_sample_v2 (1).csv")
sessions = pd.read_csv("sessions_sample_v2.csv")
attendance = pd.read_csv("attendance_sample_v2.csv")

# Check record counts
print("\nRecord Counts:")
print("Students:", len(students))
print("Tutors:", len(tutors))
print("Subjects:", len(subjects))
print("Sessions:", len(sessions))
print("Attendance:", len(attendance))

# Validate session relationships
missing_tutors = sessions[
    ~sessions["Tutor_ID"].isin(tutors["Tutor_ID"])
]

missing_subjects = sessions[
    ~sessions["Subject_ID"].isin(subjects["Subject_ID"])
]

# Validate attendance relationships
missing_students = attendance[
    ~attendance["Student_ID"].isin(students["Student_ID"])
]

missing_sessions = attendance[
    ~attendance["Session_ID"].isin(sessions["Session_ID"])
]

print("\nRelationship Validation:")
print("Missing Tutor references:", len(missing_tutors))
print("Missing Subject references:", len(missing_subjects))
print("Missing Student references:", len(missing_students))
print("Missing Session references:", len(missing_sessions))

# Validate session duration
sessions["Duration_Minutes"] = pd.to_numeric(
    sessions["Duration_Minutes"],
    errors="coerce"
)

invalid_duration = sessions[
    sessions["Duration_Minutes"].isna()
    | (sessions["Duration_Minutes"] <= 0)
]

print("\nSession Duration Validation:")
print("Invalid duration records:", len(invalid_duration))

# Attendance summary
attendance_summary = (
    attendance["Status"]
    .value_counts()
    .reset_index()
)

attendance_summary.columns = ["Status", "Count"]

print("\nAttendance Summary:")
print(attendance_summary)

# Calculate attendance rate
present_count = (attendance["Status"] == "Present").sum()
total_attendance = len(attendance)

attendance_rate = (present_count / total_attendance) * 100

print("\nAttendance Rate:")
print(round(attendance_rate, 2), "%")

# Calculate average session duration
average_duration = sessions["Duration_Minutes"].mean()

print("\nAverage Session Duration:")
print(round(average_duration, 2), "minutes")

# Final validation result
total_errors = (
    len(missing_tutors)
    + len(missing_subjects)
    + len(missing_students)
    + len(missing_sessions)
    + len(invalid_duration)
)

print("\nFinal Validation Result:")

if total_errors == 0:
    print("PASS - All database validation checks completed successfully.")
else:
    print("REVIEW REQUIRED - Validation errors were found.")

print("\n=== Week 11 Validation Complete ===")
