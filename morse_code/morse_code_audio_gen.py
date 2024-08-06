import numpy as np
from scipy.io.wavfile import write


def create_tone(frequency: int, duration: int) -> np.ndarray:
    """
    Generates a sine wave tone of a specified frequency and duration.

    Args:
        frequency (int): The frequency of the tone in Hertz (Hz).
        duration_ms (int): The duration of the tone in milliseconds (ms).

    Returns:
        np.ndarray: A NumPy array containing the generated sine wave tone.
    """
    sample_rate = 44100
    t = np.linspace(0, duration / 1000.0, int(sample_rate *
                    duration / 1000.0), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone


def morse_to_audio(morse: str, frequency: int = 1050, speed=1) -> np.ndarray:
    """
    Converts a Morse code string into an audio signal (sine wave) representation.

    Args:
        morse (str): The Morse code string to be converted into an audio signal. Dots 
                     (.) and dashes (-) represent the Morse code characters, while spaces 
                     separate characters and slashes ( / ) are used to separatewords.
        frequency (int, optional): The frequency of the audio tone in Hertz (Hz). 
                                   Defaults to 1050 Hz.
        speed (int, optional): The speed factor for the Morse code timing. A higher value 
                               increases the speed, while a lower value decreases it. 
                               Defaults to 1.

    Returns:
        np.ndarray: A NumPy array containing the audio waveform that corresponds to the 
                    input Morse code string. If an invalid character is encountered, the
                    function returns False.
    """
    speed = np.exp(speed)
    standard_duration = 400/speed

    dot_sound = create_tone(frequency, standard_duration*1)
    dash_sound = create_tone(frequency, standard_duration*3)
    intra_char_sound = create_tone(0, standard_duration*1)
    inter_char_sound = create_tone(0, standard_duration*3)
    blank_space_sound = create_tone(0, standard_duration*7)

    final_audio = blank_space_sound
    for i_char in range(len(morse)):
        if morse[i_char] == ".":
            tone = dot_sound
        elif morse[i_char] == "-":
            tone = dash_sound
        elif morse[i_char] == " " or morse[i_char] == "/":
            continue
        else:
            return 0

        if i_char < len(morse)-1:
            if morse[i_char + 1] == "." or morse[i_char + 1] == "-":
                tone = np.concatenate((tone, intra_char_sound))
            if i_char < len(morse)-2:
                if morse[i_char + 1] == " ":
                    if morse[i_char + 2] == "." or morse[i_char + 2] == "-":
                        tone = np.concatenate((tone, inter_char_sound))
                    if i_char < len(morse)-3:
                        if morse[i_char + 2] == "/" and morse[i_char + 3] == " ":
                            tone = np.concatenate((tone, blank_space_sound))

        final_audio = np.concatenate((final_audio, tone))

    final_audio = np.concatenate((final_audio, blank_space_sound))
    return final_audio


def save_audio(audio: np.ndarray, file_name: str) -> bool:
    """
    Save a NumPy array as an audio file in WAV format.

    Parameters:
    audio (np.ndarray): The audio data as a NumPy array. This should be a 1D array of audio samples.
    file_name (str): The name of the file to save, without the extension.

    Returns:
    bool: 1 if the audio was saved successfully, 0 otherwise.
    """
    try:
        write(f"{file_name}.wav", 44100, audio.astype(np.float32))
        return 1
    except:
        return 0
