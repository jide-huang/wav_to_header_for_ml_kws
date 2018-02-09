import wave
import binascii
import struct
inputWaveFile='yes.wav'
outputHeaderFile='wav_data.h'

wr=wave.open(inputWaveFile,'rb');
fw=open(outputHeaderFile, 'w');

fw.write('#define WAVE_DATA {');

print(wr)
print(wr.getsampwidth())
print(wr.getframerate())

lenght=wr.getnframes();

for i in range(16000):
    if(i>=lenght):
        fw.write('0,');
    else:
        data=wr.readframes(1)
        ba=bytearray(data)
        sh=struct.unpack('h', ba)[0]
        fw.write(str(sh));
        fw.write(',')
        print(sh)
        

wr.close();


fw.write('}');
fw.close();

