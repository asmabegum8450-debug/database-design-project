# Week 5 Query Testing

## Attendance Query Test

### Query Tested

```sql
SELECT Status, COUNT(*) AS Attendance_Count
FROM attendance
GROUP BY Status
ORDER BY Attendance_Count DESC;


Test Data

The query was tested using attendance_sample_v2.csv.

Test Result
Status	Attendance Count
Present	34
Absent	6
### Result

The query executed successfully and correctly grouped the attendance records by status and counted the number of records for each status.
