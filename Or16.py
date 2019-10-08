from myhdl import Signal, block, always_comb

@block
def Or16(inp_a, inp_b, out):
    @always_comb
    def f():
        out.next = inp_a or inp_b
    return f

# replace 5 empty lists with your tests
tests = [
  [0,1,1],
  [0,0,0],
  [1,1,1],
  [1,0,1],
  [1,1,1],
]
