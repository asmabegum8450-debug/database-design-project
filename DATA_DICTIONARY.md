# Tutoring Center Database — Data Dictionary

This document describes the **logical** database design currently summarized in the README. It is a reference for implementation and review, **not** a claim that the following columns already exist in a deployed schema. Confirm names, types, and constraints against the actual SQL schema before implementation.

## Entities and responsibilities

| Entity | Purpose | Suggested identifier | Relationships |
| --- | --- | --- | --- |
| Students | Represents learners receiving tutoring | `student_id` | Referenced by Attendance |
| Tutors | Represents tutors leading sessions | `tutor_id` | Referenced by Sessions |
| Subjects | Represents subjects covered by tutoring | `subject_id` | Referenced by Sessions |
| Sessions | Represents scheduled tutoring sessions | `session_id` | References Tutors and Subjects; referenced by Attendance |
| Attendance | Records which student attended which session | `attendance_id` or composite key | References Students and Sessions |

## Proposed field dictionary

These are **suggested fields** to validate against the project schema, not verified existing columns.

| Table | Field | Suggested role | Meaning |
| --- | --- | --- | --- |
| Students | `student_id` | Primary key | Unique student identifier |
| Tutors | `tutor_id` | Primary key | Unique tutor identifier |
| Subjects | `subject_id` | Primary key | Unique subject identifier |
| Sessions | `session_id` | Primary key | Unique tutoring session identifier |
| Sessions | `tutor_id` | Foreign key → Tutors | Tutor responsible for the session |
| Sessions | `subject_id` | Foreign key → Subjects | Subject taught in the session |
| Attendance | `attendance_id` | Optional primary key | Unique attendance record if using a surrogate key |
| Attendance | `student_id` | Foreign key → Students | Student attending |
| Attendance | `session_id` | Foreign key → Sessions | Session attended |

## Relationship rules

- One tutor can lead many sessions; each session references one tutor in this proposed model.
- One subject can be associated with many sessions; each session references one subject.
- One student can attend many sessions and one session can have many students. Attendance is the junction table that represents this many-to-many relationship.
- Foreign keys should reference existing parent records to prevent orphaned attendance or session records.
- To prevent duplicate attendance, enforce a unique constraint on `(student_id, session_id)` when the business rule permits only one attendance record per student per session.
- If Attendance uses the pair `(student_id, session_id)` as a composite primary key, a separate `attendance_id` is not required.

## Validation checklist

- [ ] Compare every proposed column name with the real schema or CSV headers.
- [ ] Verify data types, nullability, and primary/foreign key constraints.
- [ ] Confirm whether Sessions can have multiple tutors or subjects.
- [ ] Confirm whether Attendance needs status, timestamp, or other fields.
- [ ] Check uniqueness of primary keys and attendance pairs.
- [ ] Check that all foreign key values resolve to parent records.
- [ ] Update this dictionary to reflect verified implementation details.

## Example questions supported by this model

1. Which students attended a particular tutoring session?
2. How many sessions did each tutor lead?
3. Which subjects had the most sessions?
4. How many distinct students attended sessions for each subject?

Related tracking issue: #17.
