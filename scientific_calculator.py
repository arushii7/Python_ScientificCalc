import math
def main():
    print("Simple Scientific Calculator")
    print("Operations: +, -, *, /, ** (power), sqrt, sin, cos, tan, log, ln, pi, e")
    print("Enter 'quit' to exit.")
    while True:
        expression = input("Enter expression: ")
        if expression == 'quit':
            break
        try:
            result = eval_expression(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
def eval_expression(expression):
    constants = {
        'pi': math.pi,
        'e': math.e,}
    math_functions = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log10,
        'ln': math.log,
        'sqrt': math.sqrt,}
    eval_scope = {**constants, **math_functions}
    result = eval(expression, eval_scope)
    return result
if __name__ == "__main__":
    main()
