import os
import sys
from tempfile import TemporaryDirectory

from pydub import AudioSegment

from music import SongSplitter
from pitch import Mpm
from plot import Plotter
import librosa
import pydub



def main():
        print("음악 파일 경로를 입력하세요 : ", end="")
        path = input()

        print("음악 파일 이름을 입력하세요 : ", end="")
        file_name = input()
        src = file_name + ".mp3"
        dst = file_name + ".wav"
        tmp = dst

        # extract vocal voice
        os.chdir(path)
        spl = 'spleeter separate -p spleeter:2stems -o output ' + file_name + ".mp3"
        os.system(spl)

        # mp3 to wav converting
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")


        # get transcribe
        with TemporaryDirectory() as tempdir:
            try:
                song = SongSplitter(tmp)
                song.set_pitch_detector(Mpm())
                song.set_plotter(Plotter())
                retfile = song.plot_transcription()
                print("Plotted transcription result to '{0}'".format(retfile))
            except IndexError:
                print("Rerun with file path as first arg", file=sys.stderr)


if __name__ == "__main__":
    main()
