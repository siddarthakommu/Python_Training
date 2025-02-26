students = [("Alice", 85), ("Bob", 92), ("Charlie", 67)]

def get_grade(score):
    if score >= 90: return 'A'
    elif score >= 80 and score < 90: return 'B'
    elif score >= 70 and score < 80: return 'C'
    elif score < 70: return 'F'

print({name: get_grade(score) for name, score in students})