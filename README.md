This database tracks tutoring sessions at a Student Learning Center. It includes five entities: Students, Tutors, Subjects, Sessions, and Attendance. Sessions link to Tutors and Subjects, while Attendance connects Students to Sessions, allowing multiple students per session. This design supports tasks such as scheduling, attendance tracking, and reporting. Primary and foreign keys enforce data consistency, and the relationships support queries such as session participation by subject or tutor workload. The database ensures that all stakeholders—students, tutors, staff, and faculty—can easily view, record, and analyze tutoring activity.
## Database Relationships

The database uses primary keys and foreign keys to connect the five main entities.

- Students are connected to Attendance through `student_id`.
- Sessions are connected to Tutors through `tutor_id`.
- Sessions are connected to Subjects through `subject_id`.
- Attendance connects Students to Sessions through `student_id` and `session_id`.
- A session can have multiple students through the Attendance table.
- A tutor can conduct multiple tutoring sessions.
- A subject can be associated with multiple tutoring sessions.

These relationships help maintain data consistency and support queries for attendance, tutoring sessions, subjects, and tutor activity.
