class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

class Student:
    def __init__(self, name, subjects, marks):
        self.name = name
        self.scores = [Score(subject, mark) for subject, mark in zip(subjects, marks)]

    
    def __str__(self):
        result = f"Student {self.name} has the following scores:\n"
        for score in self.scores:
            result += f"{score.subject}: {score.marks}\n"
        return result

    
    def average(self):
        total_marks = sum(score.marks for score in self.scores)
        return total_marks / len(self.scores)

def classAverage(students):
    subject_scores = {}
    subject_counts = {}
    
    
    for student in students:
        for score in student.scores:
            if score.subject not in subject_scores:
                subject_scores[score.subject] = 0
                subject_counts[score.subject] = 0
            subject_scores[score.subject] += score.marks
            subject_counts[score.subject] += 1
    
    
    class_averages = []
    for subject, total_marks in subject_scores.items():
        avg = total_marks / subject_counts[subject]
        class_averages.append(f"{subject}:{round(avg)}")
    
    return class_averages


s1 = Student('X', ['C1', 'C2', 'C3', 'C4'], [10, 20, 30, 80])
s2 = Student('Y', ['C1', 'C2'], [40, 50])
s3 = Student('Z', ['C2', 'C3'], [60, 70])


print(s1)
print(s1.average())

print(classAverage([s1, s2, s3]))
