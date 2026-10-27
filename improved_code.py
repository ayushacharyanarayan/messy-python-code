"""Student result calculator (AFTER: cleaned-up version of messy_code.py)."""

STUDENTS = [
    {"name": "Amit", "marks": [78, 85, 90]},
    {"name": "Riya", "marks": [92, 88, 95]},
    {"name": "Karan", "marks": [45, 50, 38]},
    {"name": "Sneha", "marks": [67, 72, 60]},
]

# (minimum average, grade) checked from highest to lowest
GRADE_BOUNDARIES = [(90, "A"), (75, "B"), (60, "C"), (40, "D")]
LOWEST_GRADE = "F"


def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks)


def get_grade(average):
    """Return the grade letter for a given average."""
    for minimum, grade in GRADE_BOUNDARIES:
        if average >= minimum:
            return grade
    return LOWEST_GRADE


def build_report(student):
    """Return a dictionary with total, average and grade for one student."""
    marks = student["marks"]
    average = calculate_average(marks)
    return {
        "name": student["name"],
        "total": sum(marks),
        "average": average,
        "grade": get_grade(average),
    }


def print_report(report):
    print(
        f"Name: {report['name']} Total: {report['total']} "
        f"Average: {round(report['average'], 2)} Grade: {report['grade']}"
    )


def main():
    reports = [build_report(student) for student in STUDENTS]

    for report in reports:
        print_report(report)

    class_average = sum(r["average"] for r in reports) / len(reports)
    topper = max(reports, key=lambda r: r["average"])

    print(f"Class average: {round(class_average, 2)}")
    print(f"Topper: {topper['name']} with {round(topper['average'], 2)}")


if __name__ == "__main__":
    main()
