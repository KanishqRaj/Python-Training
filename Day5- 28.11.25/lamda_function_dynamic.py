generate_line = lambda user : f"Hello {user}, How are you?"

def write_dynamic_line(user , filename):
    with open(filename, 'w') as f:
        f.write(generate_line(user))

write_dynamic_line("Kanishq", "user.txt")