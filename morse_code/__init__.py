# Metadata
__version__ = '1.0.0'
__author__ = 'Matheus dos Santos Breitenbach'

# Import functions 
from .morse_code_translator import text_to_morse, morse_to_text
from .morse_code_audio_gen import create_tone, morse_to_audio, save_audio