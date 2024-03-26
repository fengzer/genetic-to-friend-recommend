import random

def generate_expression(depth):
    operators = ['+', '-', '*', '/', '//', '**', '%']
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '%': 2, '**': 3}
    def get_last_operator(expr):
        for i in range(len(expr) - 1, -1, -1):
            if expr[i] in operators or (i > 0 and expr[i-1:i+1] == '**'):
                return expr[i-1:i+1] if expr[i-1:i+1] == '**' else expr[i]
        return ''
    def generate_node(current_depth):
        if current_depth == 0:
            return str(random.randint(1, 9))
        else:
            left = generate_node(current_depth - 1)
            right = generate_node(current_depth - 1)
            operator = random.choice(operators)

            if current_depth > 1:
                left_operator = get_last_operator(left)
                right_operator = get_last_operator(right)
                if left_operator and precedence[left_operator] < precedence[operator]:
                    left = f'({left})'
                if right_operator and precedence[right_operator] < precedence[operator]:
                    right = f'({right})'
            return f'{left} {operator} {right}'
    return generate_node(depth)
print(generate_expression(3))