from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    review = TextAreaField('Article Review',validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class ArticleForm(FlaskForm):
    title = StringField("Article Title", validators = [Required()])
    content = TextAreaField('Write your article here')
    submit = SubmitField('Submit')