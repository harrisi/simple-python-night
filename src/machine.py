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

# I think this will be over engineered for two hours of time to spend.
class vm(object):
    def __init__(self, prog): # optional delimiter?
        self.prog = prog

ops = {'ADD': operator.add,
       'SUB': operator.sub,
       'MUL': operator.mul,
       'DIV': operator.truediv}

def PUSH(operands):
    # this requires reading an operand. Doing this in general means either
    # reading the actual input as a stream or passing all operands to all
    # functions. I think that's a reasonable solution, actually.
    global stack
    stack.append(int(operands[0]))

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
        if cur_inst[0] in ops:
            stack.append(ops[cur_inst[0]](stack.pop(), stack.pop()))
        elif cur_inst[0] in instructions:
            instructions[cur_inst[0]](cur_inst[1:])
        else:
            print('unknown instruction!')

if __name__ == '__main__':
    # read instructions, but for now I would rather just execute a static
    # program, for quick progression.
    print(program)
    read_instr(program)
    print(stack)
