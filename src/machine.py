# program = '''PUSH 1
# PUSH 2
# ADD
# PUSH 5
# ADD
# PUSH 2
# SUB
# PUSH -1
# MUL
# PUSH x
# PUSH 5
# SET_VAR
# PUSH 2
# GET_VAR x
# ADD
# ADD'''

# ugly silly global stack because why bother
stack = []

# This is dumb. I can't think of a really nice way to deal with scope, and it's
# almost eight!
frames = []

# Although I don't see why these would also need to have operands, I'm
# future-proofing at the cost of an unused parameter.
def ADD(operands):
   global stack
   # This indirection probably has no use, but, you know.
   res = int(stack.pop()) + int(stack.pop())
   stack.append(res)
   return res

def SUB(operands):
    global stack
    res = int(stack.pop()) - int(stack.pop())
    stack.append(res)
    return res

def MUL(operands):
    global stack
    res = int(stack.pop()) * int(stack.pop())
    stack.append(res)
    return res

def DIV(operands):
    global stack
    res = int(stack.pop()) / int(stack.pop())
    stack.append(res)
    return res

def XOR(operands):
    global stack
    res = int(stack.pop()) ^ int(stack.pop())
    stack.append(res)
    return res

def NOP(operands): # of course it's silly for NOP to take operands.
    pass

def SET_VAR(operands):
    global stack
    global frames
    var_val = stack.pop()
    var_name = stack.pop()
    # dealing with types?
    frames.append({var_name: var_val})

def GET_VAR(operands):
    global stack
    global frames
    var_name = operands[0]
    for frame in frames:
        if var_name in frame:
            PUSH(frame[var_name])

ops = {'ADD': ADD,
       'SUB': SUB,
       'MUL': MUL,
       'DIV': DIV,
       'XOR': XOR}

def PUSH(operands):
    # this requires reading an operand. Doing this in general means either
    # reading the actual input as a stream or passing all operands to all
    # functions. I think that's a reasonable solution, actually.
    global stack
    stack.append(operands[0])

def POP(operands):
    global stack
    return stack.pop()

instructions = {'PUSH': PUSH,
                'POP':  POP,
                'SET_VAR': SET_VAR,
                'GET_VAR': GET_VAR,
                'NOP': NOP}

def read_instr(prog):
    global stack
    op_left = 0
    for inst in prog:
        if inst is '': # hacky way of dealing with empty lines
            continue
        cur_inst = inst.split()
        cur_operator = cur_inst[0]
        if cur_operator in ops:
            ops[cur_operator](cur_inst[1:])
            #stack.append(ops[cur_inst[0]](stack.pop(), stack.pop()))
        elif cur_operator in instructions:
            instructions[cur_operator](cur_inst[1:])
        else:
            print('Unknown operator! Operator: ' + str(cur_operator))

# Let's see if I can write a weird REPL!
def REPL():
    pass

if __name__ == '__main__':
    # read instructions, but for now I would rather just execute a static
    # program, for quick progression.
    with open('prog.ivm', 'r') as f:
        program = f.read().splitlines()
        print('PROGRAM:')
        for line in program:
            print('\t' + str(line))
        read_instr(program)
        print('STACK:')
        print('\t' + str(stack))
        print('FRAMES:')
        print('\t' + str(frames))
