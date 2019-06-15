import numpy
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import albatrostools
import argparse

def plot_4_bit_hist(pol0, pol1, channel):
    print("plotting channel "+str(channel))
    fig=pyplot.figure(figsize=(12, 10))
    axs1=fig.add_subplot(221)
    axs1.hist(numpy.real(pol0), bins=numpy.arange(-7, 8, 1), edgecolor='black', linewidth=1.2, align="left")
    axs1.title.set_text("Real Pol0")
    #axs1.grid()
    axs2=fig.add_subplot(222)
    axs2.hist(numpy.imag(pol0), bins=numpy.arange(-7, 8, 1), edgecolor='black', linewidth=1.2, align="left")
    axs2.title.set_text("Imag Pol0")
    #axs2.grid()
    axs3=fig.add_subplot(223)
    axs3.hist(numpy.real(pol1), bins=numpy.arange(-7, 8, 1), edgecolor='black', linewidth=1.2, align="left")
    axs3.title.set_text("Real Pol1")
    #axs3.grid()
    axs4=fig.add_subplot(224)
    axs4.hist(numpy.imag(pol1), bins=numpy.arange(-7, 8, 1), edgecolor='black', linewidth=1.2, align="left")
    axs4.title.set_text("Imag Pol1")
    #axs4.grid()
    pyplot.savefig("chan_"+str(channel)+"_4_bit_hist.png")
    pyplot.clf()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("datafile", type=str, help="data file for histrogram")
    args=parser.parse_args()
    
    channels=20

    spec_num, data=albatrostools.get_data(args.datafile)
    print(data.shape)
    pol0, pol1=albatrostools.unpack_4_bit(data, channels)
    
    for i in range(channels):
        plot_4_bit_hist(pol0[:, i], pol1[:, 1], i)

        
