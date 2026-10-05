# Week 8 - Join-Based Database Analysis

## Overview

For Week 8, I expanded the database analysis by developing SQL queries that use JOIN operations. The new queries connect related tables to provide more useful information about tutoring sessions, tutors, subjects, and student attendance.

## Query 4 - Sessions with Tutor and Subject Information

This query joins the sessions table with the tutors and subjects tables. It displays the session ID, tutor name, and subject name.

The query demonstrates how related tables can be combined using foreign key relationships.

## Query 5 - Attendance with Student Information

This query joins the attendance table with the students table. It displays the student ID, student name, and attendance status.

This makes the attendance information easier to understand because the student's name is displayed instead of only the student ID.

## Query 6 - Total Sessions by Tutor

This query joins the tutors and sessions tables and counts the number of sessions associated with each tutor.

The results are grouped by tutor name and ordered from the tutor with the most sessions to the tutor with the fewest sessions.

## Testing and Review

The SQL queries were reviewed against the database table structure and foreign key relationships. The JOIN conditions use the matching Tutor_ID, Subject_ID, and Student_ID fields between the related tables.

The queries were also reviewed for correct SQL syntax, JOIN conditions, GROUP BY usage, and COUNT aggregation.

## Development Progress

The Week 8 work expands the project's database analysis capabilities beyond the basic aggregate queries developed in Week 7. The new JOIN queries allow information from multiple related tables to be analyzed together.

## Next Steps

Future work can include additional analytical queries using multiple tables, filtering, aggregation, and more detailed attendance and tutoring-session analysis.
