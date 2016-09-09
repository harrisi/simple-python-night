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

# I think this will be over engineered for two hours of time to spend.
class vm(object):
    def __init__(self, prog): # optional delimiter?
        self.prog = prog

ops = {'ADD': operator.add,
       'SUB': operator.sub,
       'MUL': operator.mul,
       'DIV': operator.truediv}


def read_instr(prog):
    prog_list = prog.split('\n') # split program into instructions (seperated by
                                 # line)
    stack = []
    op_left = 0
    for inst in prog_list:
        cur_inst = inst.split()
        if inst in ops:
            stack.append(ops[cur_inst[0]](stack.pop(), stack.pop()))
        elif cur_inst[0] == 'PUSH':
            stack.append(int(cur_inst[1]))
        elif cur_inst[0] == 'POP':
            stack.pop()
    return stack

if __name__ == '__main__':
    # read instructions, but for now I would rather just execute a static
    # program, for quick progression.
    print(program)
    print(read_instr(program))

