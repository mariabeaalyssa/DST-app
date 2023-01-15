from app import dbase, generate_password_hash, UserMixin

class User(UserMixin, dbase.Model):
	
	__tablename__ = 'user'
    
	id = dbase.Column(dbase.Integer, primary_key=True)
	firstname = dbase.Column(dbase.String(50), nullable=False)
	lastname = dbase.Column(dbase.String(50), nullable=False)
	usertype = dbase.Column(dbase.String(50), nullable=False)
	username = dbase.Column(dbase.String(50), nullable=False)
	password = dbase.Column(dbase.String(200), nullable=False)
	
	
	def __init__(self, firstname='',lastname='', usertype='', username='', password=''):
		self.firstname = firstname
		self.lastname = lastname
		self.usertype = usertype
		self.username = username
		self.password = generate_password_hash(password, method='sha256')
		
class Item(dbase.Model):
    __tablename__ = "items"

    item_id = dbase.Column(dbase.Integer, primary_key=True)
    item_name = dbase.Column(dbase.String(50))
    category = dbase.Column(dbase.String(50))
    quantity = dbase.Column(dbase.Integer)
    total = dbase.Column(dbase.Integer)


    def __init__(self, item_name='',category='', quantity='', total=''):
        self.item_name = item_name
        self.category = category
        self.quantity = quantity
        self.total = total

class Investment(dbase.Model):
	__tablename__="investments"

	investment_id = dbase.Column(dbase.Integer, primary_key=True)
	investment_amount = dbase.Column(dbase.Float)

	def __init__(self, investment_amount=''):
		self.investment_amount = investment_amount

class Hectares(dbase.Model):
	__tablename__="hectares"

	hectares_id = dbase.Column(dbase.Integer, primary_key=True)
	hectares_total = dbase.Column(dbase.Integer)

	def __init__(self, hectares_total=''):
		self.hectares_total = hectares_total

class Reforestation(dbase.Model):
	__tablename__="reforestation"

	reforestation_id = dbase.Column(dbase.Integer, primary_key=True)
	reforestation_total = dbase.Column(dbase.Integer)

	def __init__(self, reforestation_total=''):
		self.reforestation_total = reforestation_total

class ForestProtection(dbase.Model):
	__tablename__="forestprotection"

	fp_id = dbase.Column(dbase.Integer, primary_key=True)
	fp_category = dbase.Column(dbase.String(200))
	fp_item = dbase.Column(dbase.String(200))
	fp_description = dbase.Column(dbase.String(200))
	fp_qty = dbase.Column(dbase.Integer)
	fp_total = dbase.Column(dbase.Integer)
	fp_personnel = dbase.Column(dbase.String(200))
	fp_remarks = dbase.Column(dbase.String(200))

	def __init__(self, fp_category='' , fp_item ='', fp_description='', fp_qty='', fp_total='', fp_personnel='', fp_remarks=''):
		self.fp_category = fp_category
		self.fp_item = fp_item
		self.fp_description = fp_description
		self.fp_qty = fp_qty
		self.fp_total = fp_total
		self.fp_personnel = fp_personnel
		self.fp_remarks = fp_remarks


class Rainforestation(dbase.Model):
	__tablename__="rainforestation"

	rf_id = dbase.Column(dbase.Integer, primary_key=True)
	rf_category = dbase.Column(dbase.String(200))
	rf_item = dbase.Column(dbase.String(200))
	rf_description = dbase.Column(dbase.String(200))
	rf_qty = dbase.Column(dbase.Integer)
	rf_total = dbase.Column(dbase.Integer)
	rf_personnel = dbase.Column(dbase.String(200))
	rf_remarks = dbase.Column(dbase.String(200))

	def __init__(self, rf_category='' , rf_item ='', rf_description='', rf_qty='', rf_total='', rf_personnel='', rf_remarks=''):
		self.rf_category = rf_category
		self.rf_item = rf_item
		self.rf_description = rf_description
		self.rf_qty = rf_qty
		self.rf_total = rf_total
		self.rf_personnel = rf_personnel
		self.rf_remarks = rf_remarks

class Datagathering(dbase.Model):
	__tablename__="datagathering"

	dg_id = dbase.Column(dbase.Integer, primary_key=True)
	dg_category = dbase.Column(dbase.String(200))
	dg_item = dbase.Column(dbase.String(200))
	dg_description = dbase.Column(dbase.String(200))
	dg_qty = dbase.Column(dbase.Integer)
	dg_total = dbase.Column(dbase.Integer)
	dg_personnel = dbase.Column(dbase.String(200))
	dg_remarks = dbase.Column(dbase.String(200))

	def __init__(self, dg_category='' , dg_item ='', dg_description='', dg_qty='', dg_total='', dg_personnel='', dg_remarks=''):
		self.dg_category = dg_category
		self.dg_item = dg_item
		self.dg_description = dg_description
		self.dg_qty = dg_qty
		self.dg_total = dg_total
		self.dg_personnel = dg_personnel
		self.dg_remarks = dg_remarks

class Erosion(dbase.Model):
	__tablename__="erosion"

	erosion_id = dbase.Column(dbase.Integer, primary_key=True)
	erosion_soil = dbase.Column(dbase.Integer)

	def __init__(self, erosion_soil=''):
		self.erosion_soil = erosion_soil

class DrySeason(dbase.Model):
	__tablename__="dryseason"

	dryseason_id = dbase.Column(dbase.Integer, primary_key=True)
	dryseason_forestage = dbase.Column(dbase.Integer)
	dryseason_hectares = dbase.Column(dbase.Integer)
	dryseason_discharge = dbase.Column(dbase.Integer)

	def __init__(self, dryseason_forestage='', dryseason_hectares='', dryseason_discharge='' ):
		self.dryseason_forestage = dryseason_forestage
		self.dryseason_hectares = dryseason_hectares
		self.dryseason_discharge = dryseason_discharge


class InvestmentLC(dbase.Model):
	__tablename__="investmentlc"

	investmentlc_id = dbase.Column(dbase.Integer, primary_key=True)
	investmentlc_name = dbase.Column(dbase.String(200))
	investmentlc_hectares = dbase.Column(dbase.Integer)
	investmentlc_reduced = dbase.Column(dbase.Integer)


	def __init__(self, investmentlc_name='', investmentlc_hectares='', investmentlc_reduced='' ):
		self.investmentlc_name = investmentlc_name
		self.investmentlc_hectares = investmentlc_hectares
		self.investmentlc_reduced = investmentlc_reduced

class InvestmentCost(dbase.Model):
	__tablename__="investmentcost"

	investmentcost_id = dbase.Column(dbase.Integer, primary_key=True)
	investmentcost_cost = dbase.Column(dbase.Integer)

	def __init__(self, investmentcost_cost='' ):
		self.investmentcost_cost = investmentcost_cost

class LCClassification(dbase.Model):
	__tablename__="classification"

	lcc_id = dbase.Column(dbase.Integer, primary_key=True)
	lcc_classification = dbase.Column(dbase.String(200))
	lcc_initial = dbase.Column(dbase.Integer)
	lcc_publicdomain = dbase.Column(dbase.Integer)
	lcc_desired = dbase.Column(dbase.Integer)
	lcc_maximum = dbase.Column(dbase.Integer)

	def __init__(self, lcc_classification='', lcc_initial='', lcc_publicdomain='',lcc_desired='', lcc_maximum='' ):
		self.lcc_classification = lcc_classification
		self.lcc_initial = lcc_initial
		self.lcc_publicdomain = lcc_publicdomain
		self.lcc_desired = lcc_desired
		self.lcc_maximum = lcc_maximum

class FloodTemporal(dbase.Model):
	__tablename__="floodtemporal"

	ft_id = dbase.Column(dbase.Integer, primary_key=True)
	ft_lcc = dbase.Column(dbase.String(200))
	ft_hectares = dbase.Column(dbase.Integer)
	ft_reduced = dbase.Column(dbase.Integer)

	def __init__(self, ft_lcc='', ft_hectares='',ft_reduced=''):
		self.ft_lcc = ft_lcc
		self.ft_hectares = ft_hectares
		self.ft_reduced = ft_reduced

class ErosionTemporal(dbase.Model):
	__tablename__="erosiontemporal"

	et_id = dbase.Column(dbase.Integer, primary_key=True)
	et_lcc = dbase.Column(dbase.String(200))
	et_hectares = dbase.Column(dbase.Integer)
	et_reduced = dbase.Column(dbase.Integer)

	def __init__(self, et_lcc='', et_hectares='',et_reduced=''):
		self.et_lcc = et_lcc
		self.et_hectares = et_hectares
		self.et_reduced = et_reduced

class Investors(dbase.Model):
	__tablename__="investors"

	investors_id = dbase.Column(dbase.Integer, primary_key=True)
	investors_name = dbase.Column(dbase.String(200))
	investors_office = dbase.Column(dbase.String(200))
	investors_address = dbase.Column(dbase.String(200))
	investors_amount = dbase.Column(dbase.Integer)
	investors_hectares = dbase.Column(dbase.Integer)
	investors_area = dbase.Column(dbase.String(200))

	def __init__(self, investors_name='', investors_office='',investors_address='', investors_amount ='', investors_hectares = '', investors_area=''):
		self.investors_name = investors_name
		self.investors_office = investors_office
		self.investors_address = investors_address
		self.investors_amount = investors_amount
		self.investors_hectares = investors_hectares
		self.investors_area = investors_area
