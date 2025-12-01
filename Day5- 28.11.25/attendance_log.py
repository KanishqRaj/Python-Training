from datetime import datetime
def mark_attendance(*students):
    status = input("Enter status (Present/Absent): ").strip() if len(students) > 0 else "Present"

    with open("attendance.log", "a", encoding="utf-8") as file:
        for student in students:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp} | {student} | {status}\n"
            file.write(entry)
            print(f"Marked {status}: {student}")

    print("Attendance logged successfully!")


print("Enter student names (comma-separated) or press Enter to finish:")
while True:
    names_input = input("Students: ").strip()
    if not names_input:
        break

    students = [name.strip() for name in names_input.split(",")]
    mark_attendance(*students)
