import csv

class Student:
    def __init__(self, sid, name, scores):
        self.sid = sid
        self.name = name
        self.scores = scores
        
    def get_average(self):
        return sum(self.scores.values()) / len(self.scores)

def generate_student_report(input_csv, output_txt):
    try:
        students = []
        subjects = ['Math', 'Physics', 'Chemistry', 'Biology']

        with open(input_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                scores = {sub: int(row[sub]) for sub in subjects}
                students.append(Student(row['StudentID'], row['Name'], scores))

        if not students:
            print("No data found in file.")
            return None

        total_students = len(students)
        subject_stats = {}
        for sub in subjects:
            all_scores = [s.scores[sub] for s in students]
            subject_stats[sub] = {
                'avg': sum(all_scores) / total_students,
                'max': max(all_scores),
                'min': min(all_scores)
            }

        all_averages = [s.get_average() for s in students]
        overall_class_avg = sum(all_averages) / total_students
        top_students = sorted(students, key=lambda x: x.get_average(), reverse=True)[:3]
        high_achievers = [s.name for s in students if any(score > 90 for score in s.scores.values())]

        with open(output_txt, 'w') as out:
            out.write("Student Performance Report\n")
            out.write("="*30 + "\n")
            out.write(f"Total Students: {total_students}\n")
            out.write(f"Overall Class Average: {overall_class_avg:.2f}\n\n")

            out.write("Subject wise analysis:\n")
            for sub, stats in subject_stats.items():
                out.write(f"{sub}: Avg: {stats['avg']:.2f}, High: {stats['max']}, Low: {stats['min']}\n")

            out.write("\nTop 3 Students:\n")
            for i, s in enumerate(top_students, 1):
                out.write(f"{i}. {s.name} ({s.get_average():.2f})\n")

            out.write("\nStudents scoring more than 90 in any subject:\n")
            out.write(", ".join(high_achievers) if high_achievers else "None")

        print(f"Report successfully generated: {output_txt}")

    except FileNotFoundError:
        print(f"Error: The file '{input_csv}' was not found.")

generate_student_report('student.csv', 'report.txt')
