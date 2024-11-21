# Step 1: Create the Student Class
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    # Method to calculate the average of the student's scores
    def calculate_average(self):
        return sum(self.scores) / len(self.scores) 

    # Method to check if the student is passing all subjects (threshold of 40)
    def is_passing(self):
        return all(score >= 40 for score in self.scores)


# Step 2: Create the PerformanceTracker Class
class PerformanceTracker:
    def __init__(self):
        self.students = {}  # Dictionary to hold student names and their corresponding Student objects

    # Method to add a student and their scores to the tracker
    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students[name] = student

    # Method to calculate the class average (average score across all students)
    def calculate_class_average(self):
        total_scores = 0
        total_students = len(self.students)
        for student in self.students.values():
            total_scores += sum(student.scores)
        return total_scores / (total_students * len(student.scores)) if total_students > 0 else 0

    # Method to display the performance of each student
    def display_student_performance(self):
        for student in self.students.values():
            average = student.calculate_average()
            passing_status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name} | Average: {average:.2f} | Status: {passing_status}")


# Step 3: Input Handling Function
def get_student_data():
    while True:
        name = input("Enter student's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        # Input validation for scores
        scores = []
        for subject in ['Math', 'Science', 'English']:
            while True:
                try:
                    score = int(input(f"Enter {subject} score: "))
                    if score < 0 or score > 100:
                        print("Please enter a valid score between 0 and 100.")
                        continue
                    scores.append(score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        yield name, scores


# Step 4: Main Program
def main():
    tracker = PerformanceTracker()

    # Collecting data from user input
    for name, scores in get_student_data():
        tracker.add_student(name, scores)

    # Displaying the performance of all students
    print("\nStudent Performance Report:")
    tracker.display_student_performance()

    # Displaying the class average
    class_avg = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_avg:.2f}")


# Step 5: Error Handling and Edge Cases
if __name__ == '__main__':
    main()
