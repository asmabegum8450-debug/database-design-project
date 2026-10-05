-- Week 3 Database Development
-- SQL queries for the tutoring database project

-- 1. View all students
SELECT *
FROM students;

-- 2. Count the number of students
SELECT COUNT(*) AS total_students
FROM students;

-- 3. Find all Mathematics students
SELECT Student_ID, Name, Email, Major, Year
FROM students
WHERE Major = 'Mathematics';

-- 4. Count attendance records by status
SELECT Status, COUNT(*) AS total_records
FROM attendance
GROUP BY Status;

-- 5. Find students who were absent
SELECT Student_ID, Session_ID, Comments
FROM attendance
WHERE Status = 'Absent';

-- 6. View sessions with their dates and durations
SELECT Session_ID, Tutor_ID, Subject_ID, Date, Start_Time, Duration_Minutes
FROM sessions
ORDER BY Date;

-- 7. Find sessions that lasted at least 60 minutes
SELECT Session_ID, Tutor_ID, Subject_ID, Date, Duration_Minutes
FROM sessions
WHERE Duration_Minutes >= 60;

-- 8. View tutors and their subject expertise
SELECT Tutor_ID, Name, Email, Subject_Expertise
FROM tutors;

-- 9. View subjects and course codes
SELECT Subject_ID, Subject_Name, Course_Code
FROM subjects;

-- 10. Find subjects with their course codes
SELECT Subject_Name, Course_Code
FROM subjects
ORDER BY Subject_Name;
-- Week 5 Query Testing

-- 11. Count attendance records by status
SELECT Status, COUNT(*) AS Attendance_Count
FROM attendance
GROUP BY Status
ORDER BY Attendance_Count DESC;
-- Week 7: Additional Database Analysis Queries

-- Query 1: Count total students
SELECT COUNT(*) AS total_students
FROM students;

-- Query 2: Count total tutors
SELECT COUNT(*) AS total_tutors
FROM tutors;

-- Query 3: Count total subjects
SELECT COUNT(*) AS total_subjects
FROM subjects;

-- Query 4: Count sessions by subject
SELECT subject_id, COUNT(*) AS total_sessions
FROM sessions
GROUP BY subject_id
ORDER BY total_sessions DESC;

-- Query 5: Count attendance records by status
SELECT attendance_status, COUNT(*) AS total_records
FROM attendance
GROUP BY attendance_status
ORDER BY total_records DESC;

-- Week 8: Join-Based Database Analysis

-- Query 4: Sessions with tutor and subject information
SELECT
    sessions.Session_ID,
    tutors.Name AS Tutor_Name,
    subjects.Subject_Name
FROM sessions
JOIN tutors
    ON sessions.Tutor_ID = tutors.Tutor_ID
JOIN subjects
    ON sessions.Subject_ID = subjects.Subject_ID;

-- Query 5: Attendance with student information
SELECT
    attendance.Student_ID,
    students.Name AS Student_Name,
    attendance.Status
FROM attendance
JOIN students
    ON attendance.Student_ID = students.Student_ID;

-- Query 6: Total sessions by tutor
SELECT
    tutors.Name AS Tutor_Name,
    COUNT(sessions.Session_ID) AS Total_Sessions
FROM tutors
JOIN sessions
    ON tutors.Tutor_ID = sessions.Tutor_ID
GROUP BY tutors.Name
ORDER BY Total_Sessions DESC;
