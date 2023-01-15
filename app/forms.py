from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RegistrationForm(FlaskForm):
    firstname = StringField('firstname') 
    lastname = StringField('lastname')
    user_choice = [('admin','admin') , ('technical team','technical team')]
    username = StringField('username', validators=[DataRequired(), Length(min=4,max=20)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6,max=50)])
    usertype = SelectField('User Type', choices = user_choice)
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    
class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	rfid = PasswordField('rfid')

class InvestmentForm(FlaskForm): 
    investment_amount = StringField('Investment Amount')
    submit = SubmitField('Submit')

class HectaresForm(FlaskForm): 
    hectares_total = StringField('Hectares')
    submit = SubmitField('Submit')

class ReforestationForm(FlaskForm): 
    reforestation_total = StringField('Hectares')
    submit = SubmitField('Submit')

class FireControlForm(FlaskForm): 
    firecontrol_item= StringField('Item Name')
    firecontrol_description = StringField('Description')
    firecontrol_qty= StringField('Quantity')
    firecontrol_total= StringField('Total')
    firecontrol_personnel= StringField('Assigned Personnel')
    firecontrol_remarks= StringField('Remarks')
    submit = SubmitField('Submit')

class ForestProtectionForm(FlaskForm):
    category = [('Fire Control','Fire Control'),
                    ('Patrol','Patrol')]
    fp_item = StringField('Item')
    fp_description = StringField('Description')
    fp_qty = StringField('Quantity')
    fp_total = StringField('Total')
    fp_personnel = StringField('Personnel')
    fp_remarks = StringField('Remarks')
    fp_category = SelectField('Category', choices = category)
    submit = SubmitField('Submit')

class RainforestationForm(FlaskForm):
    category = [('Training & Technicaal Assistance','Training & Technicaal Assistance'),
                    ('Remote Sensing & Monitoring','Remote Sensing & Monitoring'),
                    ('Seedlings & Equipment','Seedlings & Equipment'),
                    ('Payments to Farmers', 'Payments to Farmers')
                    ]
    rf_item = StringField('Item')
    rf_description = StringField('Description')
    rf_qty = StringField('Quantity')
    rf_total = StringField('Total')
    rf_personnel = StringField('Personnel')
    rf_remarks = StringField('Remarks')
    rf_category = SelectField('Category', choices = category)
    submit = SubmitField('Submit')

class DataGatheringForm(FlaskForm):
    category = [('Infiltration Readings','Infiltartion Readings'),
                    ('Light Measurements','Light Measurements'),
                    ('Hydrological Sensor Maintenance','Hydrological Sensor Maintenance'),
                    ('Tree Height and DBH', 'Tree Height and DBH'),
                    ('Cloud Storage','Cloud Storage')]
    dg_item = StringField('Item')
    dg_description = StringField('Description')
    dg_qty = StringField('Quantity')
    dg_total = StringField('Total')
    dg_personnel = StringField('Personnel')
    dg_remarks = StringField('Remarks')
    dg_category = SelectField('Category', choices = category)
    submit = SubmitField('Submit')

class DrySeasonForm(FlaskForm): 
    dryseason_forestage = StringField('Forest Age')
    dryseason_hectares = StringField('Hectares Reforested')
    dryseason_discharge = StringField('Amount of Dry Season Flow Discharge')
    submit = SubmitField('Submit')

class ErosionForm(FlaskForm): 
    erosion_soil = StringField('Soil Eroded')
    submit = SubmitField('Submit')

class InvestmentLCForm(FlaskForm): 
    investmentlc_name = StringField('LC No.')
    investmentlc_hectares = StringField('Hectares')
    investmentlc_reduced = StringField('Flood Reduced')
    submit = SubmitField('Submit')


class InvestmentCostForm(FlaskForm): 
    investmentcost_cost= StringField('Investment Cost')
    submit = SubmitField('Submit')

class LCClassificationForm(FlaskForm): 
    lcc_classification = StringField('Classification')
    lcc_initial = StringField('Initial Land Cover')
    lcc_publicdomain = StringField('Public Domain Land Cover')
    lcc_desired = StringField('Desired Land Cover')
    lcc_maximum = StringField('Maximum Land Cover')
    submit = SubmitField('Submit')

class FloodTemporalForm(FlaskForm):
    category = [('Close Forest','Close Forest'),('Open Forest','Open Forest'),('Shrubs','Shrubs')]
    ft_lcc = SelectField('Classification', choices = category)
    ft_hectares = StringField('Hectares')
    ft_reduced = StringField('Flood Reduced')
    submit = SubmitField('Submit')

class ErosionTemporalForm(FlaskForm): 
    category = [('Close Forest','Close Forest'),('Open Forest','Open Forest'),('Shrubs','Shrubs')]
    et_lcc = SelectField('Classification', choices = category)
    et_hectares = StringField('Hectares')
    et_reduced = StringField('Erosion Reduced')
    submit = SubmitField('Submit')

class InvestorForm(FlaskForm): 
    investors_name = StringField('Investor Name')
    investors_office = StringField('Office')
    investors_address = StringField('Address')
    investors_amount = StringField('Amount')
    investors_hectares = StringField('Hectares')
    investors_area = StringField('Reforestation Area')
    submit = SubmitField('Submit')