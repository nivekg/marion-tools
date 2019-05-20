import numpy

def unpack_1_bit(data, num_channels):
    real_pol0_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x80), 7), dtype="int8")
    imag_pol0_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x40), 6), dtype="int8")
    real_pol1_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x20), 5), dtype="int8")
    imag_pol1_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x10), 4), dtype="int8")
    real_pol0_chan1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x08), 3), dtype="int8")
    imag_pol0_chan1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x04), 2), dtype="int8")
    real_pol1_chan1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x02), 1), dtype="int8")
    imag_pol1_chan1=numpy.right_shift(numpy.bitwise_and(data, 0x01), dtype="int8")
    real_pol0=numpy.append(real_pol0_chan0, real_pol0_chan1)
    imag_pol0=numpy.append(imag_pol0_chan0, imag_pol0_chan1)
    real_pol1=numpy.append(real_pol1_chan0, real_pol1_chan1)
    imag_pol1=numpy.append(imag_pol1_chan0, imag_pol1_chan1)
    real_pol0[real_pol0==0]=-1
    imag_pol0[imag_pol0==0]=-1
    real_pol0[real_pol1==0]=-1
    imag_pol0[imag_pol1==0]=-1
    pol0=real_pol0+1J*imag_pol0
    pol1=real_pol1+1J*imag_pol1
    pol0=numpy.reshape(pol0, (-1, num_channels))
    pol1=numpy.reshape(pol1, (-1, num_channels))
    return pol0, pol1
    
def unpack_2_bit(data):
    pass

def unpack_4_bit(data, num_channels):
    pass

def read_header(file_object):
    pass
