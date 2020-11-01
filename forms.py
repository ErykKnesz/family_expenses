from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    date = StringField('date', validators=[DataRequired()])
    item = StringField('item', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])
    expense = FloatField('expense', validators=[DataRequired()])