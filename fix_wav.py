import struct

# Read the raw data
with open('exports/lyria_20260202_130007.wav', 'rb') as f:
    raw_data = f.read()

# Audio parameters
sample_rate = 44100
num_channels = 2
bits_per_sample = 16
bytes_per_sample = bits_per_sample // 8

# Create WAV header
with open('exports/fixed_audio.wav', 'wb') as f:
    # RIFF header
    f.write(b'RIFF')
    file_size = 36 + len(raw_data)
    f.write(struct.pack('<I', file_size))
    f.write(b'WAVE')
    
    # fmt chunk
    f.write(b'fmt ')
    f.write(struct.pack('<I', 16))  # PCM chunk size
    f.write(struct.pack('<H', 1))   # PCM format
    f.write(struct.pack('<H', num_channels))
    f.write(struct.pack('<I', sample_rate))
    byte_rate = sample_rate * num_channels * bytes_per_sample
    f.write(struct.pack('<I', byte_rate))
    block_align = num_channels * bytes_per_sample
    f.write(struct.pack('<H', block_align))
    f.write(struct.pack('<H', bits_per_sample))
    
    # data chunk
    f.write(b'data')
    f.write(struct.pack('<I', len(raw_data)))
    f.write(raw_data)

num_samples = len(raw_data) // (bytes_per_sample * num_channels)
print(f"Created fixed_audio.wav with {num_samples} samples")
