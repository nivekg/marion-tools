import numpy
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import albatrostools
import argparse
import os

def plot_2_bit_hist(pol0, pol1, channel, outdir):
    print("plotting channel "+str(channel))
    fig=pyplot.figure(figsize=(12, 10))
    axs1=fig.add_subplot(221)
    axs1.hist(numpy.real(pol0), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs1.title.set_text("Real Pol0")
    axs1.set_xticks(numpy.arange(-2.25, 3, 1.25))
    axs1.set_xticklabels(range(-2, 3, 1))
    axs2=fig.add_subplot(222)
    axs2.hist(numpy.imag(pol0), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs2.title.set_text("Imag Pol0")
    axs2.set_xticks(numpy.arange(-2.25, 3, 1.25))
    axs2.set_xticklabels(range(-2, 3, 1))
    axs3=fig.add_subplot(223)
    axs3.hist(numpy.real(pol1), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs3.title.set_text("Real Pol1")
    axs3.set_xticks(numpy.arange(-2.25, 3, 1.25))
    axs3.set_xticklabels(range(-2, 3, 1))
    axs4=fig.add_subplot(224)
    axs4.hist(numpy.imag(pol1), bins=numpy.arange(-2.25, 3, 1.25), edgecolor='black', linewidth=1.2)
    axs4.title.set_text("Imag Pol1")
    axs4.set_xticks(numpy.arange(-2.25, 3, 1.25))
    axs4.set_xticklabels(range(-2, 3, 1))
    pyplot.savefig(outdir+"/"+"chan_"+str(channel)+"_2_bit_hist.png")
    pyplot.clf()

def plot_4_bit_hist(pol0, pol1, channel, outdir):
    print("plotting channel "+str(channel))
    fig=pyplot.figure(figsize=(12, 10))
    axs1=fig.add_subplot(221)
    axs1.hist(numpy.real(pol0), bins=numpy.arange(-7, 9, 1), edgecolor='black', linewidth=1.2, align="left")
    axs1.title.set_text("Real Pol0")
    axs1.set_xticks(range(-8, 9, 1))
    axs1.set_xticklabels(range(-8, 9, 1))
    axs2=fig.add_subplot(222)
    axs2.hist(numpy.imag(pol0), bins=numpy.arange(-7, 9, 1), edgecolor='black', linewidth=1.2, align="left")
    axs2.title.set_text("Imag Pol0")
    axs2.set_xticks(range(-8, 9, 1))
    axs2.set_xticklabels(range(-8, 9, 1))
    axs3=fig.add_subplot(223)
    axs3.hist(numpy.real(pol1), bins=numpy.arange(-7, 9, 1), edgecolor='black', linewidth=1.2, align="left")
    axs3.title.set_text("Real Pol1")
    axs3.set_xticks(range(-8, 9, 1))
    axs3.set_xticklabels(range(-8, 9, 1))
    axs4=fig.add_subplot(224)
    axs4.hist(numpy.imag(pol1), bins=numpy.arange(-7, 9, 1), edgecolor='black', linewidth=1.2, align="left")
    axs4.title.set_text("Imag Pol1")
    axs4.set_xticks(range(-8, 9, 1))
    axs4.set_xticklabels(range(-8, 9, 1))
    pyplot.savefig(outdir+"/"+"chan_"+str(channel)+"_4_bit_hist.png")
    pyplot.clf()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("datafile", type=str, help="data file for histrogram")
    parser.add_argument("-o", "--outdir", type=str, help="directory to save plots")
    args=parser.parse_args()

    header, data=albatrostools.get_data(args.datafile, -1)

    print(header)

    if not os.path.isdir(args.outdir):
        print("making directory: "+args.outdir)
        os.mkdir(args.outdir)

    numpy.set_printoptions(threshold=numpy.inf)
    print(data["spectrum_number"])

    pyplot.plot(data["spectrum_number"])
    pyplot.savefig(args.outdir+"/spectrum_number.png")
    pyplot.clf()
    
    for index, chan in enumerate(header["channels"]):
        if header["bit_mode"]==2:
            plot_2_bit_hist(data["pol0"][:, index], data["pol1"][:, index], chan, args.outdir)
        if header["bit_mode"]==4:
            plot_4_bit_hist(data["pol0"][:, index], data["pol1"][:, index], chan, args.outdir)

        
