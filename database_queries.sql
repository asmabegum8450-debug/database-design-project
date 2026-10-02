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
