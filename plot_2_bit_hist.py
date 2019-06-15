import numpy
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import albatrostools
import argparse

def plot_2_bit_hist(pol0, pol1, channel):
    fig=pyplot.figure(figsize=(12, 10))
    axs1=fig.add_subplot(221)
    axs1.hist(numpy.real(pol0), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs1.title.set_text("Real Pol0")
    axs1.set_xticks(range(-2, 3, 1))
    axs1.set_xticklabels(range(-2, 3, 1))
    axs2=fig.add_subplot(222)
    axs2.hist(numpy.imag(pol0), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs2.title.set_text("Imag Pol0")
    axs2.set_xticks(range(-2, 3, 1))
    axs2.set_xticklabels(range(-2, 3, 1))
    axs3=fig.add_subplot(223)
    axs3.hist(numpy.real(pol1), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs3.title.set_text("Real Pol1")
    axs3.set_xticks(range(-2, 3, 1))
    axs3.set_xticklabels(range(-2, 3, 1))
    axs4=fig.add_subplot(224)
    axs4.hist(numpy.imag(pol1), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs4.title.set_text("Imag Pol1")
    axs4.set_xticks(range(-2, 3, 1))
    axs4.set_xticklabels(range(-2, 3, 1))
    pyplot.savefig("chan_"+str(channel)+"_2_bit_hist.png")
    pyplot.clf()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("datafile", type=str, help="data file for histrogram")
    parser.add_argument("-c", "--channels", type=int, help="Number of channels")
    parser.add_argument("-b", "--bytes_per_packet", type=int, help="NUmber of bytes per packet")
    args=parser.parse_args()

    spec_num, data=albatrostools.get_data(args.datafile, args.channels, args.bytes_per_packet)
    pol0, pol1=albatrostools.unpack_2_bit(data, args.channels)
    
    for i in range(args.channels):
        plot_2_bit_hist(pol0[:, i], pol1[:, 1], i)

        
