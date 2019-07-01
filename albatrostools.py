import numpy

def unpack_1_bit(data, num_channels):
    real_pol0_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x80), 7), dtype="int8")
    imag_pol0_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x40), 6), dtype="int8")
    real_pol1_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x20), 5), dtype="int8")
    imag_pol1_chan0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x10), 4), dtype="int8")
    real_pol0_chan1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x08), 3), dtype="int8")
    imag_pol0_chan1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x04), 2), dtype="int8")
    real_pol1_chan1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(data, 0x02), 1), dtype="int8")
    imag_pol1_chan1=numpy.asarray(numpy.bitwise_and(data, 0x01), dtype="int8")
    real_pol0=numpy.ravel(numpy.column_stack((real_pol0_chan0, real_pol0_chan1)))
    imag_pol0=numpy.ravel(numpy.column_stack((imag_pol0_chan0, imag_pol0_chan1)))
    real_pol1=numpy.ravel(numpy.column_stack((real_pol1_chan0, real_pol1_chan1)))
    imag_pol1=numpy.ravel(numpy.column_stack((imag_pol1_chan0, imag_pol1_chan1)))
    real_pol0[real_pol0==0]=-1
    imag_pol0[imag_pol0==0]=-1
    real_pol1[real_pol1==0]=-1
    imag_pol1[imag_pol1==0]=-1
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
    imag_pol1=numpy.asarray(numpy.bitwise_and(data, 0x03), dtype="int8")

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
    print(pol0.shape)
    print(pol1.shape)
    return pol0, pol1
    
def unpack_4_bit(data, num_channels):
    pol0_bytes=data[:, 0::2]
    pol1_bytes=data[:, 1::2]
    real_pol0=numpy.asarray(numpy.right_shift(numpy.bitwise_and(pol0_bytes, 0xf0), 4), dtype="int8")
    imag_pol0=numpy.asarray(numpy.bitwise_and(pol0_bytes, 0x0f), dtype="int8")
    real_pol1=numpy.asarray(numpy.right_shift(numpy.bitwise_and(pol1_bytes, 0xf0), 4), dtype="int8")
    imag_pol1=numpy.asarray(numpy.bitwise_and(pol1_bytes, 0x0f), dtype="int8")
    
    real_pol0[real_pol0>8]=real_pol0[real_pol0>8]-16
    imag_pol0[imag_pol0>8]=imag_pol0[imag_pol0>8]-16

    real_pol1[real_pol1>8]=real_pol1[real_pol1>8]-16
    imag_pol1[imag_pol1>8]=imag_pol1[imag_pol1>8]-16

    pol0=real_pol0+1J*imag_pol0
    pol1=real_pol1+1J*imag_pol1

    del real_pol0
    del imag_pol0
    del real_pol1
    del imag_pol1

    pol0=pol0.reshape(-1, num_channels)
    pol1=pol1.reshape(-1, num_channels)
    return pol0, pol1

def correlate(pol0, pol1):
    pols={}
    data=[pol0, pol1]
    for i in range(2):
        for j in range(i, 2):
            pols["pol%d%d"%(i, j)]=data[i]*numpy.conj(data[j])
    return pols
    
def get_data(file_name, channels, bytes_per_packet, items=-1):
    file_data=open(file_name, "r")
    data=numpy.fromfile(file_data, count=items, dtype=[("spec_num", ">I"), ("spectra", "%dB"%(bytes_per_packet-4))])
    file_data.close()
    #mem_data=numpy.memmap(data, dtype=[("spec_num", ">I"), ("spectra", "%dB"%(bytes_per_packet-4))])
    spectra=data["spectra"].reshape(-1, channels)
    return data["spec_num"], spectra
