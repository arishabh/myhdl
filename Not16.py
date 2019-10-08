from myhdl import Signal, block, always_comb

@block
def Not16(inp, out):
    @always_comb
    def f():
        out.next = not inp
    return f

# replace 5 empty lists with your tests
tests = [
  [1,0],
  [0,1],
  [1,0],
  [0,1],
  [1,0],
]
