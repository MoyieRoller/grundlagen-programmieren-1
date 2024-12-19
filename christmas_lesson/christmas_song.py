import math, wave, struct
import secret_christmas_song_data

pitches = secret_christmas_song_data.pitches
durations = secret_christmas_song_data.durations

def mtof(p_midi_note):
    return 432. * 2 ** ((p_midi_note - 69) / 12)

frequencies = []
for midi_note in pitches:
    frequencies.append(mtof(midi_note))

sr = 44100
len_samples = []
for duration in durations:
    len_samples.append(int(sr * duration))

def make_audio_buffer(p_sr, p_frequency, p_len_smps):
    buffer = []
    for i in range(p_len_smps):
        sample = math.sin(2. * math.pi * i * p_frequency / p_sr)
        buffer.append(sample)
    return buffer

audio_buffer = []
for i in range(len(frequencies)):
    local_audio_buffer = make_audio_buffer(sr, frequencies[i], len_samples[i])
    for j in range(len(local_audio_buffer)):
        local_audio_buffer[j] *= 1. - j / len(local_audio_buffer)
    for k in local_audio_buffer:
        audio_buffer.append(k)

# write buffer
bin_buf = bytearray()
for sample in audio_buffer:
    local_sample = sample * ((2**16 - 1) / (2**16))
    bin_buf = bin_buf + struct.pack('h', round(local_sample * 2 ** 16/2))

wav = wave.open('super_secret_christmas_song.wav', 'w')
wav.setnchannels(1)
wav.setsampwidth(2)
wav.setframerate(sr)
wav.writeframes(bin_buf)
wav.close()