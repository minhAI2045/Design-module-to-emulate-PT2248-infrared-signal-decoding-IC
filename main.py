import os
from tkinter import PROJECTING
import ffmpeg

filename = "Trim video\\cut segment time.txt"
alphabet = "Trim video\\alphabet.txt"
DDMMYY = "20052023"             # day month year of measurement
TT = "2"                 # order of measurers
N = "5"                  # camera order
typeOfVid = ".mp4"               # save data type    for example "mp4" would be ".mp4"
suffix = "_" + N + "_" + DDMMYY + "_" + TT + typeOfVid
nameVid =""           # Name of video after cutting :  nameVid = prefix + suffix
fileVid = "Vid_Son_May5.mp4"            # Video needs to be cut

def trim(in_file, out_file, start, end):
    if os.path.exists(out_file):
        os.remove(out_file)

    in_file_probe_result = ffmpeg.probe(in_file)
    in_file_duration = in_file_probe_result.get(
        "format", {}).get("duration", None)
    print(in_file_duration)

    input_stream = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    video = input_stream.trim(start=start, end=end).setpts(pts)
    audio = (input_stream
             .filter_("atrim", start=start, end=end)
             .filter_("asetpts", pts))
    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    output = ffmpeg.output(video_and_audio, out_file, format="mp4")
    output.run()

    out_file_probe_result = ffmpeg.probe(out_file)
    out_file_duration = out_file_probe_result.get(
        "format", {}).get("duration", None)
    print(out_file_duration)
    

with open(filename, "r") as file, open(alphabet, "r") as alphabet:
    lines = file.readlines()
    pairs = zip(lines[::2], lines[1::2])  # match pairs of values
    alphas = alphabet.readlines()
    
    for pair, alpha in zip(pairs, alphas):
        start = pair[0].strip()
        end = pair[1].strip()
        prefix = alpha.strip()
        nameVid= prefix + suffix
        print("Start: ", start)
        print("End: ", end)
        print("Namevid", nameVid)
        trim(fileVid, nameVid, start, end)

