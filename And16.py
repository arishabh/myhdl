from myhdl import Signal, block, always_comb

@block
def And16(inp_a, inp_b, out):
    @always_comb
    def f():
        out.next = inp_a and inp_b
    return f

# replace 5 empty lists with your tests
tests = [
  [1,1,1],
  [0,1,0],
  [10,5,5],
  [1,1,1],
  [1,1,1],
]
