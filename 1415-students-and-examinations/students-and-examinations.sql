SELECT students.student_id, students.student_name, subjects.subject_name, COUNT(examinations.subject_name) AS attended_exams
FROM students
JOIN subjects
LEFT JOIN examinations
ON students.student_id = examinations.student_id AND subjects.subject_name = examinations.subject_name
GROUP BY students.student_id, subjects.subject_name
ORDER BY student_id ASC, subject_name ASC;