#%%
from utils import load

raw = load("day8.txt", split="\n")[:-1]

proc = [[(u := x.split())[0], int(u[1])] for x in raw]
# %%


def execute(program, acc, curr):
    cmd, n = program[curr]
    if cmd == "acc":
        acc += n
        curr += 1
    elif cmd == "jmp":
        curr += n
    elif cmd == "nop":
        curr += 1
    else:
        raise ValueError("WTF")
    return acc, curr


def run(program, acc=0, curr=0):
    passed = set()
    while True:
        if curr in passed:
            break
        else:
            passed.add(curr)
        if curr == len(program):
            return acc, True

        acc, curr = execute(program, acc, curr)
    return acc, False


print(run(proc))
# %%
import copy

passed = set()


def swap(test, loc):
    if test[loc][0] == "jmp":
        test[loc][0] = "nop"
    elif test[loc][0] == "nop":
        test[loc][0] = "jmp"
    else:
        raise ValueError


test = copy.deepcopy(proc)
acc = 0
curr = 0
while True:
    if curr in passed:
        raise Exception
    passed.add(curr)

    # Change
    if proc[curr][0] in ["jmp", "nop"]:
        swap(test, curr)
    else:
        acc, curr = execute(proc, acc, curr)
        continue

    # Test
    out, ok = run(test, acc, curr)
    if ok:
        print(out)
        break
    else:
        swap(test, curr)
        acc, curr = execute(test, acc, curr)
# %%

# %%
