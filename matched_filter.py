import matplotlib.pyplot
import scipy
import numpy
import matplotlib
import scipy.signal

def find_peak(array):
    peak = scipy.signal.find_peaks(array)
    peak = peak[0]
    return max(array[peak])



def checking_yes(input_signal, filter, peaks):
    convolution = scipy.signal.correlate(input_signal, filter, mode= 'full')
    pks_in_input_signal = find_peak(convolution)
    if pks_in_input_signal > peaks * 0.5:
        print("yes detected")
    else:
        print("no yes")


def template(template_audio):
    template_audio = scipy.io.wavfile.read('yes_template.wav')
    template_audio = template_audio[1]
    template_audio = template_audio / numpy.linalg.norm(template_audio)
    matched_filter = template_audio[::-1]
    ideal_convolution = scipy.signal.correlate(template_audio, matched_filter, mode= 'full')
    return matched_filter, ideal_convolution
#input signal

while True:
    try:
        template_signal = input("Template yes: ")
        template_signal = scipy.io.wavfile.read(template_signal)
        input_signal = input("Input yes: ")
        input_signal = scipy.io.wavfile.read(input_signal)
        break
    except FileNotFoundError:
        print("checking the tail of the files")
    except ValueError:
        print("Try again")

matched_filter, ideal_convolution = template(template_signal)
input_signal = input_signal
input_signal = input_signal[1]
input_signal = input_signal / numpy.linalg.norm(input_signal)
threshold = find_peak(ideal_convolution)
checking_yes(input_signal, matched_filter, threshold)
    


