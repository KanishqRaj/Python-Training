def write_certificate():
    with open("student_names.txt" , "r")as f:
        student_names = [line.strip() for line in f.readlines() if line.strip()]

    content = "This is certify {name} has successfully completed the course"

    for n in student_names:
        certificate = content.format(name = n)
        filename = f"{n}_Certificate.txt"
        with open(filename,"w") as f:
            f.write(certificate)

write_certificate()



