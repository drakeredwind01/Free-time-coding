import numpy as np
import sounddevice as sd

# Define the number of voices, pitch shifts, and delays
n_voices = 3
pitch_shifts = [1.0, 1.2, 0.8]  # Example pitch shifts
delays = [0.0, 0.02, 0.04]  # Delays in seconds
sampling_rate = 44100  # Example sampling rate

# Function to simulate pitch shifting (can replace with actual pitch shift function)
def pitch_shift(audio, pitch_shift_factor, fs):
    return np.interp(np.arange(0, len(audio), pitch_shift_factor), np.arange(0, len(audio)), audio)

# Callback function for the audio stream
def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)

    # Reshape the input data to a 1D array
    audio = indata[:, 0].copy()

    # Create a list for the processed voices
    processed_voices = []

    # Generate the chorus effect by duplicating and processing each voice
    for i in range(n_voices):
        shifted_audio = pitch_shift(audio, pitch_shifts[i], sampling_rate)
        # Delay the voice by adding zeros (latency)
        delay_samples = int(delays[i] * sampling_rate)
        delayed_audio = np.pad(shifted_audio, (delay_samples, 0), mode='constant')[:len(audio)]
        processed_voices.append(delayed_audio)

    # Sum all the voices together
    output_audio = np.sum(np.array(processed_voices), axis=0)

    # Normalize the output audio to avoid clipping
    output_audio /= np.max(np.abs(output_audio) + 1e-6)  # Avoid division by zero

    # Output the processed audio
    outdata[:, 0] = output_audio[:frames]

# Start the audio stream
with sd.Stream(callback=audio_callback, channels=1, samplerate=sampling_rate, blocksize=1024):
    print("Processing audio. Press Ctrl+C to stop.")
    try:
        while True:
            sd.sleep(1000)  # Keep the program alive
    except KeyboardInterrupt:
        print("Audio processing stopped.")
