import claripy
import nose

def test_concrete():
    a = claripy.BVV(10, 32)
    b = claripy.BoolV(True)
    #c = claripy.BVS('x', 32)

    nose.tools.assert_is(type(claripy.backends.concrete.convert(a)), claripy.bv.BVV)
    nose.tools.assert_is(type(claripy.backends.concrete.convert(b)), bool)

    a = claripy.BVV(1337, 32)
    b = a[31:16]
    c = claripy.BVV(0, 16)
    nose.tools.assert_is(b, c)

    bc = claripy.backends.concrete
    d = claripy.BVV(-1, 32)
    nose.tools.assert_equal(bc.convert(d), 0xffffffff)

    e = claripy.BVV(2**32+1337, 32)
    nose.tools.assert_equal(bc.convert(e), 1337)


def test_concrete_fp():
    f = claripy.FPV(1.0, claripy.FSORT_FLOAT)
    nose.tools.assert_equal(claripy.backends.concrete.eval(f, 2), (1.0,))

if __name__ == '__main__':
    test_concrete()
    test_concrete_fp()
