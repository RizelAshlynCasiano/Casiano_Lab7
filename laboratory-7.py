name = str(input("Name: "))
sec = str(input("Section: "))

prelim = float(input("Enter the Preliminary Period Grade: "))
if prelim < 40 or prelim > 100:
    print("ERROR! Your grade is invalid. Please try again later.")
else:
    midterm = float(input("Enter the Midterm Period Grade: "))
    if midterm < 40 or midterm > 100:
        print("ERROR! Your grade is invalid. Please try again later.")
    else:
        finals = float(input("Enter the Final Period Grade: "))
        if finals < 40 or finals > 100:
            print("ERROR! Your grade is invalid. Please try again later.")
        else:
            final_grade = round((prelim * 0.3333) + (midterm * 0.3333) + (finals * 0.3333))
            
            if 99 <= final_grade <= 100:
                grade_points, description = 1.00, "Excellent"
            elif 96 <= final_grade <= 98:
                grade_points, description = 1.25, "Outstanding"
            elif 93 <= final_grade <= 95:
                grade_points, description = 1.50, "Superior"
            elif 90 <= final_grade <= 92:
                grade_points, description = 1.75, "Very Good"
            elif 87 <= final_grade <= 89:
                grade_points, description = 2.00, "Good"
            elif 84 <= final_grade <= 86:
                grade_points, description = 2.25, "Satisfactory"
            elif 81 <= final_grade <= 83:
                grade_points, description = 2.50, "Fairly Satisfactory"
            elif 78 <= final_grade <= 80:
                grade_points, description = 2.75, "Fair"
            elif 75 <= final_grade <= 77:
                grade_points, description = 3.00, "Passed"
            elif final_grade < 75:
                grade_points, description = 5.00, "Failed"
            else:
                grade_points, description = None, "Invalid grade"
                
            print(f"Final Grade: {final_grade}")
            print(f"Grade Points: {grade_points}")
            print(f"General Description: {description}")