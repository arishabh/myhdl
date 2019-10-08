from myhdl import Signal, block, always_comb

@block
def DMux8Way(select, inp, out_a, out_b, out_c, out_d, out_e, out_f, out_g, out_h):
    all_out = [out_a,out_b, out_c, out_d, out_e, out_f, out_g, out_h]
    all_out[select]
    @always_comb
    def f():
        (i for i in all_out).next = Signal(0)
        all_out[select].next = inp
    return f

# replace 5 empty lists with your tests
tests = [
  [0,  65535,   65535,0,0,0,  0,0,0,0],
  [7,  722,     0,0,0,0,      0,0,0,722],
  [5,  50,      0,0,0,0,      0,50,0,0],
  [1,  1,       0,1,0,0,      0,0,0,0],
  [3,  999,     0,0,0,999,    0,0,0,0],
]
