import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student names and marks
students = ["Aman", "Priya", "Rahul", "Neha", "Rohan"]

maths = [85, 92, 67, 78, 88]
science = [90, 89, 72, 85, 76]
english = [78, 95, 80, 88, 82]

print("=" * 40)
print("       STUDENT PERFORMANCE ANALYZER")
print("=" * 40)

# Convert marks into NumPy arrays
maths_array = np.array(maths)
science_array = np.array(science)
english_array = np.array(english)

# Calculate average marks for each subject
maths_average = np.mean(maths_array)
science_average = np.mean(science_array)
english_average = np.mean(english_array)

print("\nSUBJECT STATISTICS")
print("-" * 25)

print("Maths Average:", round(maths_average, 2))
print("Science Average:", round(science_average, 2))
print("English Average:", round(english_average, 2))

print("\nHIGHEST AND LOWEST MARKS")
print("-" * 25)

print("Maths - Highest:", np.max(maths_array))
print("Maths - Lowest:", np.min(maths_array))

print("Science - Highest:", np.max(science_array))
print("Science - Lowest:", np.min(science_array))

print("English - Highest:", np.max(english_array))
print("English - Lowest:", np.min(english_array))

# Create a  Dataframe
data = {
    "Student": students,
    "Maths": maths,
    "Science": science,
    "English": english
}

df = pd.DataFrame(data)

# Calculate each student's average using Pandas
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Assign a performance category
def get_performance(average):
    if average >= 85:
        return "Excellent"
    elif average >= 75:
        return "Good"
    else:
        return "Needs Improvement"


df["Performance"] = df["Average"].apply(get_performance)

print("\nCOMPLETE STUDENT REPORT")
print("-" * 40)
print(df.to_string(index=False, formatters={"Average": "{:.2f}".format}))

# Find the top-performing student
top_student_index = df["Average"].idxmax()
top_student = df.loc[top_student_index]

print("\nTOP PERFORMER")
print("-" * 25)
print("Name:", top_student["Student"])
print("Average:", round(top_student["Average"], 2))

# Find students who need improvement
print("\nSTUDENTS NEEDING IMPROVEMENT")
print("-" * 30)

low_performers = df[df["Average"] < 75]

if low_performers.empty:
    print("No students in this category.")
else:
    print(low_performers[["Student", "Average"]].to_string(index=False))

# Save the report as a CSV file
df.to_csv("student_results.csv", index=False)

print("\nStudent report saved to student_results.csv")

# Graph 1: Average marks by subject
subjects = ["Maths", "Science", "English"]
subject_averages = [
    maths_average,
    science_average,
    english_average
]

plt.figure(figsize=(8, 5))
plt.bar(subjects, subject_averages)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# Graph 2: Average marks by student
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Average"])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# Graph 3: Compare subject marks for each student
df.plot(
    x="Student",
    y=["Maths", "Science", "English"],
    kind="bar",
    figsize=(9, 5)
)

plt.title("Subject-wise Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend(title="Subjects")
plt.tight_layout()
plt.show()

print("\nProject completed successfully!")