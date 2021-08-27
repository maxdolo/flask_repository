from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    titolo = StringField('Titolo', validators=[
                                    DataRequired("Campo Obbligatorio!"), 
                                    Length(min=3, max=120, 
                                        message="Inserire tra i 3 e i 120 caratteri")])
    descrizione = TextAreaField('Descrizione', validators=[
                                    Length(max=240, message="Inserire non più di 140 caratteri")])
    body = TextAreaField('Body', validators=[DataRequired("Campo Obbligatorio")])
    submit = SubmitField('Pubblica Post')