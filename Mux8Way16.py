from myhdl import Signal, block, always_comb

@block
def Mux8Way16(select, inp_a, inp_b, inp_c, inp_d, inp_e, inp_f, inp_g, inp_h, out):
    inp = [inp_a, inp_b, inp_c, inp_d, inp_e, inp_f, inp_g, inp_h]
    @always_comb
    def f():
        out.next = inp[select]
    return f

# replace 5 empty lists with your tests
tests = [
  [0, 10, 40, 0,0,0,0,0,0,0, 10],
  [1, 300, 200, 0,0,0,0,0,0,0, 200],
  [1, 300, 200, 0,0,0,0,0,0,0, 200],
  [1, 300, 200, 0,0,0,0,0,0,0, 200],
  [1, 300, 200, 0,0,0,0,0,0,0, 200],
]

