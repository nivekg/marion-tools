import albatrostools
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import numpy
import argparse
import os

if __name__=="__main__":
    numpy.set_printoptions(threshold=numpy.inf)
    parser=argparse.ArgumentParser()
    parser.add_argument("datafile", type=str, help="data file for histrogram")
    parser.add_argument("-o", "--outdir", type=str, help="directory to save plots")
    args=parser.parse_args()

    if not os.path.isdir(args.outdir):
        print("making directory: "+args.outdir)
        os.mkdir(args.outdir)

    header, data=albatrostools.get_data(args.datafile, 300000)
    print(header)
    print("finished reading file")
  
    print(data["spectrum_number"])
    
    pyplot.plot(data["spectrum_number"])
    pyplot.savefig(args.outdir+"/spectrum_number.png")
    pyplot.clf()
  
    pols=albatrostools.correlate(data["pol0"], data["pol1"])
    print("just after correlate")
    pol00=numpy.absolute(pols["pol00"])**2
    pol11=numpy.absolute(pols["pol11"])**2
    pol01=pols["pol01"]
    del pols
    
    print("plotting pol00")
    pyplot.imshow(pol00, aspect="auto")
    pyplot.colorbar()
    pyplot.savefig(args.outdir+"/"+"pol00.png")
    pyplot.clf()
    print("plotting pol00 mean")
    mean_pol00=numpy.mean(pol00, axis=0)
    pyplot.plot(mean_pol00)
    pyplot.savefig(args.outdir+"/"+"pol00_mean.png")
    pyplot.clf()
    del mean_pol00
    del pol00
    
    print("plotting pol11")
    pyplot.imshow(pol11, aspect="auto")
    pyplot.colorbar()
    pyplot.savefig(args.outdir+"/"+"pol11.png")
    pyplot.clf()
    print("plotting pol11 mean")
    mean_pol11=numpy.mean(pol11, axis=0)
    pyplot.plot(mean_pol11)
    pyplot.savefig(args.outdir+"/"+"pol11_mean.png")
    pyplot.clf()
    del mean_pol11
    del pol11

    print("plotting pol01 phase")
    phase=numpy.arctan2(numpy.imag(pol01), numpy.real(pol01))
    phase[phase<0]=phase[phase<0]+2*numpy.pi
    pyplot.imshow(phase, aspect="auto")
    pyplot.colorbar()
    pyplot.savefig(args.outdir+"/"+"pol01_phase.png")
    pyplot.clf()
    print("plotting pol01 phase mean")
    mean_phase=numpy.mean(phase, axis=0)
    pyplot.plot(mean_phase)
    pyplot.savefig(args.outdir+"/"+"phase_mean.png")
    pyplot.clf()
    del mean_phase

    print("plotting pol01 amplitude")
    amp=numpy.absolute(pol01)**2
    pyplot.imshow(amp, aspect="auto")
    pyplot.colorbar()
    pyplot.savefig(args.outdir+"/"+"pol01_amp.png")
    pyplot.clf()
    print("plotting pol01 amplitude mean")
    mean_amp=numpy.mean(amp, axis=0)
    pyplot.plot(mean_amp)
    pyplot.savefig(args.outdir+"/"+"amp_mean.png")
    pyplot.clf()
    del mean_amp

