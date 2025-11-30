def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    top_line = []
    bottom_line = []
    dashes = []
    answers = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem should have two operands and one operator."

        operand1, operator, operand2 = parts

        # Check operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate width of the problem
        width = max(len(operand1), len(operand2)) + 2

        # Arrange the problem
        top_line.append(operand1.rjust(width))
        bottom_line.append(operator + operand2.rjust(width - 1))
        dashes.append('-' * width)

        # Calculate answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers.append(answer.rjust(width))

    # Join the parts
    arranged_problems = '    '.join(top_line) + '\n' + \
                        '    '.join(bottom_line) + '\n' + \
                        '    '.join(dashes)

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

# Test the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print("\n")
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

