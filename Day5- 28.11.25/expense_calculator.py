def generate_report(*args):
    total = 0
    expense_lines = []
    for name, amount in args:
        expense_lines.append(f"{name} Rs{amount}")
        total += amount

    report_content = f"""
    This report contains the total expenses details
    Expenses : {expense_lines}
    Total Expenses : {total:.2f}
    """

    with open("report.txt" , "w") as f:
        f.write(report_content)

generate_report(
    ("Lunch" , 150),
    ("Travel" , 500),
    ("Clothing" , 100),
    ("Snacks" , 200),

)
