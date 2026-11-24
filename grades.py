def get_grade(score):
    if score>100 or score < 0 :
        return("Yanlis bal")
    if score >= 91:
        return("A")
    elif score >= 81:
        return("B")
    elif score >= 71 :
        return("C")
    elif score >= 61 :
        return("D")
    elif score >= 51 :
        return("E")
    else:
        return("F")
def make_report(students):
    report = {}
    for name, score in students.items():
        report[name] = get_grade(score)
    return report
students = {"Aysel": 95, "Murad": 72, "Elvin": 48}
print(make_report(students))
