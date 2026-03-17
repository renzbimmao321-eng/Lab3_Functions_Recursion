# grades.py

def compute_average(scores):
    return sum(scores) / len(scores)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def generate_remark(grade):
    if grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Good"
    elif grade == "C":
        return "Satisfactory"
    elif grade == "D":
        return "Needs Improvement"
    else:
        return "Failed"