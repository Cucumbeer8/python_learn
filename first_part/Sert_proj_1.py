def arithmetic_arranger(problems, show_answers=False):
    error = rules(problems)
    if error:
        return error

    return draw_problem(problems, show_answers)

def rules(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        part = problem.split()
        if not((part[1] == '+' or part[1] == '-')):
            return "Error: Operator must be '+' or '-'."
        elif not(part[0].isdigit()) or not(part[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        elif len(part[0]) > 4 or len(part[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'


def draw_problem(problems, show_answers):
    first_line = []
    second_line = []
    dashes_line = []
    result_line = []

    for problem in problems:
        part = problem.split()

        opperand1, operator, opperand2 = part[0], part[1], part[2]

        if operator == '+':
            result = str(int(opperand1) + int(opperand2))
        else:
            result = str(int(opperand1) - int(opperand2))

        width = max(len(opperand1), len(opperand2)) + 2
        first_line.append(' '*(width - len(opperand1)) + opperand1)
        second_line.append(operator + ' '*(width - len(opperand2) - 1) + opperand2)
        dashes_line.append('-'*width)
        result_line.append(' '*(width - len(result)) + result)

    problems_result = '\n'.join([
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(dashes_line)
    ])

    if show_answers:
        problems_result += '\n' + '    '.join(result_line)

    return problems_result



print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')