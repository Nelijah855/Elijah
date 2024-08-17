with open('x.mp3', 'rb') as file:
    mp3_data = file.read()

# `mp3_data` now contains the binary representation of the entire MP3 file, including the main encoded audio data
    print(f"First 100 bytes of the MP3 data: {mp3_data[:]}")