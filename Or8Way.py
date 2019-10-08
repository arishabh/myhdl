from myhdl import block, always_comb

@block
def Or8Way(inp_a, inp_b, inp_c, inp_d, inp_e, inp_f, inp_g, inp_h, out):
    @always_comb
    def f():
        out.next = inp_a or inp_b or inp_c or inp_d or inp_e or inp_f or inp_g or inp_h
    return f

# replace 5 empty lists with your tests
tests = [
    # ....inputs.....  output
    [0,0,0,0, 0,0,0,0, 0],
    [0,1,0,0, 0,0,0,0, 1],
    [0,0,0,0, 1,1,1,1, 1],
    [0,0,0,0, 0,0,0,1, 1],
    [1,1,1,1, 1,1,1,1, 1],
]
