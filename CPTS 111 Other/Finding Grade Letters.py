grade_as_percent = float(input("Enter a grade[%]: "))

if grade_as_percent >= 100:
    print("You received an 'A+'")
elif grade_as_percent < 100 and grade_as_percent >= 93:
    print("You received an 'A'")
elif grade_as_percent < 93 and grade_as_percent >= 90:
    print("You received an 'A-'")
elif grade_as_percent < 90 and grade_as_percent >= 87:
    print("You received a 'B+'")
elif grade_as_percent < 87 and grade_as_percent >= 84:
    print("You received a 'B'")
elif grade_as_percent < 84 and grade_as_percent >= 80:
    print("You received a 'B-'")
elif grade_as_percent < 80 and grade_as_percent >= 77:
    print("You received a 'C+'")
elif grade_as_percent < 77 and grade_as_percent >= 74:
    print("You received a 'C'")
elif grade_as_percent < 74 and grade_as_percent >= 70:
    print("You received a 'C-'")
elif grade_as_percent < 70 and grade_as_percent >= 67:
    print("You received a 'D+'")
elif grade_as_percent < 67 and grade_as_percent >= 64:
    print("You received a 'D'")
elif grade_as_percent < 64 and grade_as_percent >= 60:
    print("You received a 'D-'")
elif grade_as_percent < 60:
    print("You received an 'F'")
