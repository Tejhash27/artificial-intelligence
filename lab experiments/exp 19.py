import os
from pyswip import Prolog

def setup_prolog_file():
    """Generates the Prolog source file dynamically."""
    prolog_content = """
    % --- Database Facts ---
    teaches(dr_smith, cse101).
    teaches(prof_davis, mat202).
    teaches(dr_jones, phy301).
    teaches(prof_clark, cse101).

    enrolled(arjun, cse101).
    enrolled(arjun, mat202).
    enrolled(priya, mat202).
    enrolled(priya, phy301).
    enrolled(rahul, cse101).
    enrolled(ananya, phy301).

    % --- Custom Query Rules ---
    student_teacher(Student, Teacher, SubCode) :-
        enrolled(Student, SubCode),
        teaches(Teacher, SubCode).

    student_course_load(Student, SubCode, Teacher) :-
        enrolled(Student, SubCode),
        teaches(Teacher, SubCode).

    classmate(Student1, Student2, SubCode) :-
        enrolled(Student1, SubCode),
        enrolled(Student2, SubCode),
        Student1 \\= Student2.
    """
    with open("school_db.pl", "w") as f:
        f.write(prolog_content.strip())

def decode_atom(value):
    """Utility helper to translate raw byte atoms from Prolog into clean Python strings."""
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return str(value)

def run_queries():
    # 1. Initialize Prolog Engine and load the database file
    prolog = Prolog()
    prolog.consult("school_db.pl")

    print("=" * 65)
    print("      STUDENT-TEACHER-SUB-CODE PROLOG RELATION ENGINE")
    print("=" * 65)

    # 2. Query 1: Find who teaches Arjun for course code 'cse101'
    student_query = "arjun"
    course_query = "cse101"
    print(f"Finding teachers for student '{student_query.capitalize()}' in course [{course_query.upper()}]:")
    
    q1_results = list(prolog.query(f"student_teacher({student_query}, Teacher, {course_query})"))
    for res in q1_results:
        teacher = decode_atom(res['Teacher'])
        print(f" -> Professor: {teacher.replace('_', ' ').title()}")
    print("-" * 65)

    # 3. Query 2: Get complete course schedule and professors for Priya
    target_student = "priya"
    print(f"Fetching full course load profiles for student '{target_student.capitalize()}':")
    
    q2_results = list(prolog.query(f"student_course_load({target_student}, SubCode, Teacher)"))
    for res in q2_results:
        sub_code = decode_atom(res['SubCode']).upper()
        teacher = decode_atom(res['Teacher']).replace('_', ' ').title()
        print(f" -> Class: {sub_code} | Instructor: {teacher}")
    print("-" * 65)

    # 4. Query 3: Find all classmates of Arjun in 'mat202'
    classmate_source = "arjun"
    target_class = "mat202"
    print(f"Finding classmates of '{classmate_source.capitalize()}' in course [{target_class.upper()}]:")
    
    q3_results = list(prolog.query(f"classmate({classmate_source}, Classmate, {target_class})"))
    if q3_results:
        # Avoid duplicate printing if multiple relationships match the exact same target pair
        seen = set()
        for res in q3_results:
            classmate_name = decode_atom(res['Classmate']).capitalize()
            if classmate_name not in seen:
                seen.add(classmate_name)
                print(f" -> peer: {classmate_name}")
    else:
        print(" -> No other classmates found enrolled in this section.")
        
    print("=" * 65)

if __name__ == "__main__":
    setup_prolog_file()
    run_queries()
