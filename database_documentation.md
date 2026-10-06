# Week 6: Database Data Dictionary

## Project Overview

This database is designed for a tutoring center. It stores information about students, tutors, subjects, tutoring sessions, and attendance. The tables are connected through shared identifiers so that SQL queries can be used to analyze tutoring activity and attendance.

## Students

The Students table stores information about students who use the tutoring center.

| Field        | Description                        |
| ------------ | ---------------------------------- |
| student_id   | Unique identifier for each student |
| student_name | Name of the student                |
| email        | Student email address              |

The `student_id` is used to identify each student and connect students to tutoring sessions and attendance records.

## Tutors

The Tutors table stores information about tutors who provide tutoring services.

| Field      | Description                                          |
| ---------- | ---------------------------------------------------- |
| tutor_id   | Unique identifier for each tutor                     |
| tutor_name | Name of the tutor                                    |
| subject_id | Identifier for the subject associated with the tutor |

The `tutor_id` identifies each tutor and is used to connect tutors to tutoring sessions.

## Subjects

The Subjects table stores information about subjects offered by the tutoring center.

| Field        | Description                        |
| ------------ | ---------------------------------- |
| subject_id   | Unique identifier for each subject |
| subject_name | Name of the subject                |

The `subject_id` identifies each subject and connects subjects to tutoring sessions.

## Sessions

The Sessions table stores information about scheduled tutoring sessions.

| Field        | Description                                      |
| ------------ | ------------------------------------------------ |
| session_id   | Unique identifier for each tutoring session      |
| student_id   | Identifier for the student attending the session |
| tutor_id     | Identifier for the tutor providing the session   |
| subject_id   | Identifier for the subject being taught          |
| session_date | Date of the tutoring session                     |

The Sessions table connects students, tutors, and subjects. It provides the main structure for analyzing tutoring activity.

## Attendance

The Attendance table records whether students attended their scheduled tutoring sessions.

| Field             | Description                                        |
| ----------------- | -------------------------------------------------- |
| attendance_id     | Unique identifier for an attendance record         |
| session_id        | Identifier for the related tutoring session        |
| attendance_status | Indicates whether the student attended the session |

The `session_id` connects attendance records to the Sessions table.

## Database Relationships

The tables are connected using identifiers:

* `Students.student_id` connects students to their tutoring sessions.
* `Tutors.tutor_id` connects tutors to tutoring sessions.
* `Subjects.subject_id` connects subjects to tutoring sessions.
* `Sessions.session_id` connects sessions to attendance records.
* The Sessions table brings together students, tutors, and subjects for each tutoring session.

These relationships allow SQL queries to combine information from multiple tables and analyze tutoring activity, subjects, tutors, and attendance.

## Purpose of the Data Dictionary

This data dictionary provides a reference for the database structure and explains the purpose of each table and field. It will make future SQL queries, testing, troubleshooting, and database maintenance easier.
