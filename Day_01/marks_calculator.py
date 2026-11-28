def main():
    name=input("Enter the name of the student: ")
    total_subjects=int(input("Enter the total number of subjects: "))
    if total_subjects <= 0:
        print("Total subjects must be greater than zero.")
        return
    max_marks = float(input("Enter maximum marks per subject: "))
    if max_marks <= 0:
        print("Maximum marks per subject must be greater than zero.")
        return
    marks=[]
    for i in range(total_subjects):
        mark=float(input(f"Enter mark {i+1}: "))
        if mark < 0 or mark > max_marks:
            print(f"Mark must be between 0 and {max_marks}.")
            return
        marks.append(mark)
    total=sum(marks)
    average=total/len(marks)
    percentage=(total/(total_subjects*max_marks))*100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    print(f"Student: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")
    print(f"percentage:{percentage:.2f}%")
    print(f"Grade: {grade}")
if __name__ == "__main__":
    main()