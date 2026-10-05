Week 10 Database Query Development
Overview

This week I developed and tested Python/Pandas queries against the tutoring center database sample data. The purpose was to generate useful summaries from the Students, Tutors, Subjects, Sessions, and Attendance data.

Queries Developed
1. Sessions by Tutor

The query groups session records by Tutor_ID and counts the number of sessions associated with each tutor. This helps identify tutor activity levels within the sample dataset.

2. Sessions by Subject

The query groups session records by Subject_ID and counts the number of sessions for each subject. This provides a summary of which subjects have the most session activity.

3. Average Session Duration

The average session duration was calculated using the Duration_Minutes field.

Result: 58.5 minutes

4. Attendance Summary

The attendance records were grouped by Status.

Results:

Present: 34

Absent: 6

5. Attendance Rate

The attendance rate was calculated by dividing the number of Present records by the total number of attendance records.

Attendance Rate: 85.0%

Testing Result

The Week 10 query script executed successfully after matching the query to the actual database column name, Duration_Minutes. The completed script generated session summaries by tutor and subject, calculated the average session duration, summarized attendance status, and calculated the overall attendance rate.

Conclusion

The queries provide useful reports for evaluating tutoring center activity. The results show an average session length of 58.5 minutes and an 85% attendance rate in the sample data. These queries can be used as a foundation for additional database reporting and analysis.
