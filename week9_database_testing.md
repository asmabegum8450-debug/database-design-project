# Week 9 Database Testing

## Purpose

This document records testing performed on the tutoring center database data and relationships.

## Testing Areas

### 1. Session Data Testing

Tested the session dataset using Python and Pandas.

Results:
- Total sessions: 40
- Missing Session_ID: 0
- Missing Tutor_ID: 0
- Missing Subject_ID: 0
- Missing Duration: 0
- Invalid Duration: 0

### 2. Attendance Data Testing

Tested the attendance dataset using Python and Pandas.

Results:
- Total attendance records: 40
- Missing Session_ID: 0
- Missing Student_ID: 0
- Missing Status: 0
- Present records: 34
- Absent records: 6

### 3. Database Relationship Testing

Tested whether foreign-key ID values in related tables matched existing records.

Results:
- Missing Tutor references: 0
- Missing Subject references: 0
- Missing Session references: 0
- Missing Student references: 0

## Results

The testing confirmed that the sample session and attendance data did not contain missing required IDs or invalid session durations. The relationship testing also confirmed that the Tutor, Subject, Session, and Student references matched records in their related tables.

## Next Steps

Continue improving database queries and testing additional data relationships as the project develops.
