def write_multiple_lines(stud_id,reg_no):
    data = f"""
    Hi, Student
    Your ID is {stud_id}
    Your Registration Number is {reg_no}
    """
    with open("student.txt", "w")as f:
        f.write(data)

write_multiple_lines(1232,"TUEC102")
