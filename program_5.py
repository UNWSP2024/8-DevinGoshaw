# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def main():
    print('if you want to stop press enter')
    courses={}
    while True:
        courseID=input('enter course ID:')
        if courseID=="":
            break
        
        courseName=input('enter course name: ').strip()
        courses[courseID]=courseName
    
    subject= input('enter a subject to search for (example COS):').strip().upper()
    print(f"\nCourses with subject '{subject}':")
    found = False
    for course_id, course_name in courses.items():
        if course_id.upper().startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True

    if not found:
        print("No courses found for that subject")


if __name__=="__main__":
    main()