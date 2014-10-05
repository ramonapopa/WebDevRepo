#!/usr/bin/python
import sys

def delta(xi, xf):
    return abs(xi-xf)

def get_exp_atoms(num, nums, rest):

    if sum(rest) == num:
        yield rest
    elif sum(rest) > num:
        if delta(sum(rest[:-1]), num) >= delta(sum(rest), num):
            yield rest
        else:
            yield rest[:-1]
    elif nums == []:
        pass
    else:
        for r in get_exp_atoms(num, nums[:], rest + [nums[0]]):
            yield r
        for r in get_exp_atoms(num, nums[1:], rest):
            yield r

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    nums = [int(x) for x in sys.stdin.readline().split()]
    nums.sort()

    # Find the first exact solution, else find all aproximate solutions
    total_sum = 0
    sol = []
    best_sol = []
    min_delta = sys.maxint

    solutions = [s for s in get_exp_atoms(num, nums, [])]
    for s in solutions:
        total_sum = sum(s)
        if total_sum == num:
            sol = s
            break

        if delta(total_sum, num) < min_delta:
            min_delta = delta(total_sum, num)
            best_sol = s

    expr = {}
    if not sol:
        sol = best_sol

    for op in sol:
        count = sol.count(op)
        expr[str(op)] = count

    # construct the arithmetic expression
    expr_str = ""
    for op in expr.keys():
        expr_str += op
        if expr[op] > 1:
            expr_str += "*" + str(expr[op])
        expr_str += " + "

    expr_str = expr_str[:-3]
    print expr_str
