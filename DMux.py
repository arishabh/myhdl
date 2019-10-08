from myhdl import Signal, block, always_comb

@block
def DMux(select, inp, out_a, out_b):
    all_out = [out_a,out_b]
    all_out[select]
    @always_comb
    def f():
        (i for i in all_out).next = Signal(0)
        all_out[select].next = inp
    return f

# replace 5 empty lists with your tests
tests = [
  [0,  65535,   65535,0],
  [1,  722,     0,722],
  [0,  9,       9,0],
  [1,  1,       0,1],
  [1,  999,     0,999],
]
