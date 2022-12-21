import re

from sympy import Symbol
from sympy.solvers import solve

HUMAN = "humn"
ROOT = "root"


def solve_p1(commands) -> int:
    equations = [x.replace(":", " =") for x in commands]
    while True:
        for equation in equations:
            try:
                exec(equation)
                return int(eval("root"))
            except NameError:
                continue


def solve_p2(commands) -> int:
    root = [x for x in commands if x.startswith(ROOT)][0]
    equations = [x.replace(":", " =") for x in commands if not x.startswith(HUMAN) and not x.startswith(ROOT)]
    equations = {x.split(" = ")[0]: x.split(" = ")[1] for x in equations}
    solved = {}
    while equations:
        equations = solve_partial(equations, solved)

    last_equations = re.findall(r"\b\w{4}\b", root)
    equality = f"{solved[last_equations[1]]} - {solved[last_equations[2]]}"
    return solve(equality, Symbol(HUMAN))[0]


def solve_partial(equations, solved):
    updated_equations = {}
    for lhs, rhs in equations.items():
        rhs_vars = re.findall(r"[a-z]{4}", rhs)
        if rhs_vars:
            if all(rhs_var == HUMAN for rhs_var in rhs_vars):
                solved[lhs] = rhs
            else:
                for rhs_var in rhs_vars:
                    if rhs_var in solved:
                        rhs = rhs.replace(rhs_var, f"({solved[rhs_var]})")
                updated_equations[lhs] = rhs
        else:
            solved[lhs] = str(int(eval(rhs)))
    return updated_equations
