from flask import Flask, render_template, url_for, Response
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from numpy import ndarray
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

from morse_code import morse_code_translator, morse_code_audio_gen

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class TranslatorForm(FlaskForm):
    function = SelectField("Select Function", choices=[
                           'Text -> Morse', 'Morse -> Text'])
    input = TextAreaField("Input", validators=[DataRequired()])
    submit = SubmitField("Done")


class TextToMorseAudioForm(FlaskForm):
    input = TextAreaField("Text to audio", validators=[DataRequired()])
    submit = SubmitField("Done")


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/morse_translator", methods=["GET", "POST"])
def morse_translator():
    form = TranslatorForm()
    if form.validate_on_submit():
        if form.function.data == "Text -> Morse":
            output = morse_code_translator.text_to_morse(form.input.data)
            if output == 0:
                output = "ERROR: Invalid Character Found."
        else:
            output = morse_code_translator.morse_to_text(form.input.data)
            if output == 0:
                output = "ERROR: Invalid Character Found."
        return render_template("morse-translator.html", form=form, output=output)
    return render_template("morse-translator.html", form=form, output="")

@app.route("/audio_generator", methods=["GET", "POST"])
def audio_generator():
    form = TextToMorseAudioForm()
    if form.validate_on_submit():
        output = morse_code_translator.text_to_morse(form.input.data)
        if output == 0:
            output = "ERROR: Invalid Character Found."
        morse_audio = morse_code_audio_gen.morse_to_audio(output)
        if isinstance(morse_audio, ndarray):
            morse_code_audio_gen.save_audio(morse_audio, "audio/morse_audio")
        return render_template("generate-audio.html", form=form, output=1)
    return render_template("generate-audio.html", form=form, output=0)

@app.route("/play_audio")
def play_audio():
    wav_file_path = "audio/morse_audio.wav"

    def generate_audio():
        with open(wav_file_path, "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate_audio(), mimetype="audio/wav", headers={"Content-Disposition": "attachment; filename=morse_audio.wav"})


if __name__ == "__main__":
    app.run(debug = True)
