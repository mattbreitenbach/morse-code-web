# Morse Code Translator Website

## Overview
This project is a web application built with Flask that translates text into Morse code and generates audio files representing the Morse code. Users can enter text into a form, and the application will convert it into Morse code and generate an audio file that can be played directly on the website or downloaded.
Created purely for the joy of coding, this project serves as a showcase of my skills in my personal portfolio. The inspiration comes from the course "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu. While the web design was influenced by one of the course classes, the project represents my personal interpretation and application of the concepts learned, with most of the work being original.

## Features
- Convert text to Morse code.
- Convert Morse code to text.
- Generate Morse code audio in WAV format.
- Play the generated audio directly from the web interface.

## Project Structure
- app.py: Main Flask application file.
- /static/: Contains static files such as images, CSS and JavaScript.
- /templates/: Contains HTML templates for rendering the web pages.
- /audio/: Temporary storage for generated audio files.
- /morse_code/: Contains modules for Morse code translation and audio generation.

## Dependencies
- Flask
- Flask-WTF
- WTForms
- numpy
- scipy
- blinker
- Bootstrap-Flask
- click
- colorama
- itsdangerous
- Jinja2
- MarkupSafe
- Werkzeug
