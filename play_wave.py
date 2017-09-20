# -*- coding: utf-8 -*-
import sysimport waveimport pyaudio
write = sys.stdout.write
class play_wave: def __init__(self, wave_fname):  self.wave_fname = wave_fname  self.wf = wave.open(self.wave_fname, 'r')  self.channels = self.wf.getnchannels()  self.sample_width = self.wf.getsampwidth()  self.framerate = self.wf.getframerate()  self.frames = self.wf.getnframes()  self.length_sec = self.frames / self.framerate
  self.chunk = 1024   def output_wave_info(self):  write('#Channels: '+str(self.channels)+'\n')  write('Sample Width: '+str(self.sample_width)+'\n')  write('Frame Rate: '+str(self.framerate)+'\n')  write('#Frames: '+str(self.frames)+'\n')  write('Length in Sec: '+str(self.length_sec)+'\n')  def play(self):  self.pa = pyaudio.PyAudio()  self.stream = self.pa.open(format=self.pa.get_format_from_width(self.sample_width),      channels=self.channels, rate=self.framerate, output=True)
  data = self.wf.readframes(self.chunk)  while len(data) > 0:   self.stream.write(data)   data = self.wf.readframes(self.chunk)  self.stream.close()  self.pa.terminate() def main(): if len(sys.argv) < 2:  sys.stderr.write('Usage: python $0 wave_fname\n')  sys.exit(1)  wave_fname = sys.argv[1]  hd = play_wave(wave_fname) hd.output_wave_info() hd.play()
 if __name__ == '__main__': main()
  
