from myhdl import Signal, block, always_comb

@block
def Mux16(select, inp_a, inp_b, out):
    inp = [inp_a, inp_b]
    @always_comb
    def f():
        out.next = inp[select]
    return f

# replace 5 empty lists with your tests
tests = [
  [0, 10, 40, 10],
  [1, 300, 200, 200],
  [1, 300, 200, 200],
  [1, 300, 200, 200],
  [1, 300, 200, 200],
]
