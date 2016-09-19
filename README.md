# simple-python-night

PDX Python at Simple

# what

I think I want to work on a stack-based VM rather than my existing
register-based VM in appendixc.

# How to use

Currently the way to invoke the interpreter is by running
[src/machine.py](src/machine.py). It will read a file [prog.ivm](prog.ivm) from
the root directory and output some debug information when it's finished.

```
~/simple-python-night$ cat prog.ivm
PUSH x
PUSH 5
SET_VAR
PUSH 4
GET_VAR x
ADD
~/simple-python-night$ python src/machine.py
PROGRAM:
	PUSH x
	PUSH 5
	SET_VAR
	PUSH 4
	GET_VAR x
	ADD
STACK:
	[9]
FRAMES:
	[{'x': '5'}]
~/simple-python-night$ 
```

# Instructions

The current list of instructions is quite short and can't do much except basic
arithmetic.

```
ADD: Add numbers on the stack.
MUL: Multiply numbers on the stack.
SUB: Subtract numbers on the stack.
DIV: Divide numbers on the stack.
XOR: Exclusive or numbers on the stack.

PUSH: Push element on the stack.
POP: Pop element off of the stack.
SET_VAR: Pop last two elements off the stack. The first element popped off is
the value to set the second element popped off to.
GET_VAR: Push the value associated with the operand onto the stack.
NOP: No operation.
```

Currently none of the instructions have any extra operands except `GET_VAR`,
although I plan on giving mathematical operators such as `ADD`, `MUL`, etc. the
ability to take an operand (possibly more than one). The operand would be a
number of elements to apply the operator to. Potential (future) example:

```
PUSH 1
PUSH 2
PUSH 3
ADD 3
```

The above would pop all three elements and push the value 6 onto the stack.
There's no real reason for this, I just think it would be kind of fun.
