import operator

program = '''PUSH 1
PUSH 2
ADD
PUSH 5
ADD
PUSH 2
SUB
PUSH -1
MUL'''

# ugly silly global stack because why bother
stack = []

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
                'POP':  POP}

def read_instr(prog):
    prog_list = prog.split('\n') # split program into instructions (seperated by
                                 # line)
    global stack
    op_left = 0
    for inst in prog_list:
        cur_inst = inst.split()
        cur_operator = cur_inst[0]
        if cur_operator in ops:
            ops[cur_operator](cur_inst[1:])
            #stack.append(ops[cur_inst[0]](stack.pop(), stack.pop()))
        elif cur_inst[0] in instructions:
            instructions[cur_operator](cur_inst[1:])
        else:
            print('unknown instruction!')

if __name__ == '__main__':
    # read instructions, but for now I would rather just execute a static
    # program, for quick progression.
    print(program)
    read_instr(program)
    print(stack)
