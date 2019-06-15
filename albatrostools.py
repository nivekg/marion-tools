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
    del real_pol0
    del imag_pol0
    del real_pol1
    del imag_pol1
    pol0=numpy.reshape(pol0, (-1, num_channels))
    pol1=numpy.reshape(pol1, (-1, num_channels))
    return pol0, pol1
    
def unpack_2_bit(data, num_channels):
    real_pol0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0xC0), 6), dtype="int8")
    imag_pol0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x30), 4), dtype="int8")
    real_pol1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x0C), 2), dtype="int8")
    imag_pol0=numpy.asarray(numpy.bitwise_and(data, 0x03), dtype="int8")

    real_pol0[real_pol0<=1]=real_pol0[real_pol0<=1]-2
    real_pol0[real_pol0>=2]=real_pol0[real_pol0>=2]-1

    imag_pol0[imag_pol0<=1]=imag_pol0[imag_pol0<=1]-2
    imag_pol0[imag_pol0>=2]=imag_pol0[imag_pol0>=2]-1

    real_pol1[real_pol1<=1]=real_pol1[real_pol1<=1]-2
    real_pol1[real_pol1>=2]=real_pol1[real_pol1>=2]-1

    imag_pol1[imag_pol1<=1]=imag_pol1[imag_pol1<=1]-2
    imag_pol1[imag_pol1>=2]=imag_pol1[imag_pol1>=2]-1
    
    pol0=real_pol0+1J*imag_pol0
    pol1=real_pol1+1J*imag_pol1
    del real_pol0
    del imag_pol0
    del real_pol1
    del imag_pol1
    pol0=pol0.reshape(-1, num_channels)
    pol1=pol1.reshape(-1, num_channels)
    return pol0, pol1
    
def unpack_4_bit(data, num_channels):
    pol0_bytes=data[:, 0::2]
    pol1_bytes=data[:, 1::2]
    real_pol0=numpy.right_shift(numpy.bitwise_and(pol0_bytes, 0xf0), 4)
    imag_pol0=numpy.bitwise_and(pol0_bytes, 0x0f)
    real_pol1=numpy.right_shift(numpy.bitwise_and(pol1_bytes, 0xf0), 4)
    imag_pol1=numpy.bitwise_and(pol1_bytes, 0x0f)
    
    real_pol0[real_pol0>7]=real_pol0[real_pol0>7]-16
    imag_pol0[imag_pol0>7]=imag_pol0[imag_pol0>7]-16

    real_pol1[real_pol1>7]=real_pol1[real_pol1>7]-16
    imag_pol1[imag_pol1>7]=imag_pol1[imag_pol1>7]-16

    pol0=real_pol0+1J*imag_pol0
    pol1=real_pol1+1J*imag_pol1

    del real_pol0
    del imag_pol0
    del real_pol1
    del imag_pol1

    pol0=pol0.reshape(-1, num_channels)
    pol1=pol1.reshape(-1, num_channels)
    return pol0, pol1
    
def get_data(file_name):
    file_data=open(file_name, "r")
    data=numpy.fromfile(file_data, dtype=[("spec_num", ">I"), ("spectra", "1230B")])
    file_data.close()
    spectra=data["spectra"].reshape(-1, 246)
    return data["spec_num"], spectra
