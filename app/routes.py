from locale import currency
from app import *
from app import server
from app.models import *
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from .models import *
from .forms import *


login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(id)



@server.route('/login', methods=["GET","POST"])
def login():
	form = LoginForm()
	if current_user.is_authenticated is True:
		return redirect(url_for('dashboard'))
	elif form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			print(form.password.data)
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=True)
				session['username'] = request.form['username']
				return redirect(url_for('dashboard'))
			else:
				flash('Invalid username or password')
				return render_template('login.html', form=form)
		else:
			return redirect(url_for('dashboard'))
	return render_template('login.html', form=form)


@server.route('/register', methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		new_user = User(form.firstname.data, form.lastname.data, form.usertype.data, form.username.data, form.password.data)
		dbase.session.add(new_user)
		dbase.session.commit()
		
		return redirect(url_for('login'))
	return render_template('register.html', title="Register Admin", form=form)

@server.route('/admin/dashboard', methods=["GET","POST"])
@login_required
def dashboard():
	#user = User.query.filter_by(id=current_user.id).first()
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	dryseason = DrySeason.query.all()
	erosion = Erosion.query.filter_by(erosion_id=1).first()
	forestprotection = ForestProtection.query.all()
	rainforestation = Rainforestation.query.all()
	datagathering = Datagathering.query.all()
	investmentlc = InvestmentLC.query.all()
	investmentcost = InvestmentCost.query.filter_by(investmentcost_id=1).first()
	lcclass = LCClassification.query.all()
	floodtemporal = FloodTemporal.query.all()
	erosiontemporal = ErosionTemporal.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	form5 = DrySeasonForm() 
	form6 = ErosionForm()
	form7 = LCClassificationForm()
	form8 = FloodTemporalForm()
	form9 = ErosionTemporalForm()
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	forminvlc  = InvestmentLCForm()
	formic = InvestmentCostForm()

	#rf_sum = Rainforestation.query.all()
	#print(sum(rf_sum))

	return render_template('index.html', investmentcost=investmentcost,formic=formic, forminvlc=forminvlc,investmentlc=investmentlc, form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9, formfp=formfp, formrf=formrf, formdg=formdg, reforestation=reforestation, hectares=hectares, investment=investment, dryseason=dryseason, erosion=erosion, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, floodtemporal = floodtemporal, erosiontemporal= erosiontemporal, lcclass=lcclass, user=user )


@server.route('/admin/settings', methods=["GET","POST"])
@login_required
def settings():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	dryseason = DrySeason.query.all()
	erosion = Erosion.query.filter_by(erosion_id=1).first()
	forestprotection = ForestProtection.query.all()
	rainforestation = Rainforestation.query.all()
	datagathering = Datagathering.query.all()
	investmentlc = InvestmentLC.query.all()
	investmentcost = InvestmentCost.query.filter_by(investmentcost_id=1).first()
	lcclass = LCClassification.query.all()
	floodtemporal = FloodTemporal.query.all()
	erosiontemporal = ErosionTemporal.query.all()
	investors = Investors.query.all()
	investorform = InvestorForm()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	form5 = DrySeasonForm() 
	form6 = ErosionForm()
	form7 = LCClassificationForm()
	form8 = FloodTemporalForm() 	
	form9 = ErosionTemporalForm()
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	forminvlc  = InvestmentLCForm()
	formic = InvestmentCostForm()

	#rf_sum = Rainforestation.query.all()
	#print(sum(rf_sum))

	return render_template('settings.html', investors=investors, investorform=investorform, investmentcost=investmentcost,formic=formic, forminvlc=forminvlc,investmentlc=investmentlc, form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6,form7=form7, form8=form8, form9=form9, formfp=formfp, formrf=formrf, formdg=formdg, reforestation=reforestation, hectares=hectares, investment=investment, dryseason=dryseason, erosion=erosion, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, lcclass=lcclass,floodtemporal=floodtemporal, erosiontemporal=erosiontemporal, user=user )


@server.route('/admin/rainforestation_cost', methods=["GET","POST"])
@login_required
def rainforestation_cost():
	user = User.query.filter_by(id=current_user.id).first()
	forestprotection = ForestProtection.query.all()
	rainforestation = Rainforestation.query.all()
	datagathering = Datagathering.query.all()
	investmentcost =  InvestmentCost.query.filter_by(investmentcost_id=1).first()
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	formic = InvestmentCostForm()

	return render_template('costbreakdown.html', investmentcost=investmentcost, formic=formic, formfp=formfp, formrf=formrf, formdg=formdg, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, user=user )

@server.route('/admin/investment',methods=["GET","POST"])
@login_required
def investment():
    form = InvestmentForm()
    #investment=Investment.query.filter_by(investment_id=1).first()
    if form.validate_on_submit():
        add_investment = Investment(form.investment_amount.data)
        dbase.session.add(add_investment)
        dbase.session.commit()
        return redirect(url_for('settings',form=form, investment=investment))
    return redirect(url_for('settings',form=form, investment=investment))

@server.route('/admin/investmentcost', methods=['GET','POST'])
def investmentcost():
	investmentcost = InvestmentCost.query.filter_by(investmentcost_id=1).first()
	formic = InvestmentCostForm()
	if formic.validate_on_submit():
		investmentcost.investmentcost_cost = formic.investmentcost_cost.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', investmentcost=investmentcost))
	elif request.method == 'GET':
		formic.investmentcost_cost.data = investmentcost.investmentcost_cost
	return render_template('settings.html',formic=formic, investmentcost=investmentcost)

@server.route('/admin/add_investmentlc', methods=['GET','POST'])
def add_investmentlc():
	forminvlc = InvestmentLCForm()
	if forminvlc.validate_on_submit():
		add_investmentlc = InvestmentLC(forminvlc.investmentlc_name.data, forminvlc.investmentlc_hectares.data, forminvlc.investmentlc_reduced.data)
		dbase.session.add(add_investmentlc)
		dbase.session.commit()	
		return redirect(url_for('settings',forminvlc=forminvlc))
	return render_template('settings.html', forminvlc=forminvlc)

@server.route('/admin/update/<int:investmentlc_id>/investmentlc', methods=['GET','POST'])
def update_investmentlc(investmentlc_id):
	forminvlc = InvestmentLCForm()
	investmentlc = InvestmentLC.query.get_or_404(investmentlc_id)
	if forminvlc.validate_on_submit():
		investmentlc.investmentlc_name = forminvlc.investmentlc_name.data
		investmentlc.investmentlc_hectares = forminvlc.investmentlc_hectares.data
		investmentlc.investmentlc_reduced = forminvlc.investmentlc_reduced.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', investmentlc=investmentlc))
	elif request.method == 'GET':
		forminvlc.investmentlc_name.data = investmentlc.investmentlc_name
		forminvlc.investmentlc_hectares.data = investmentlc.investmentlc_hectares
		forminvlc.investmentlc_reduced.data = investmentlc.investmentlc_reduced
	return redirect(url_for('settings.html', forminvlc=forminvlc, investmentlc=investmentlc))


@server.route("/admin/delete/<int:investmentlc_id>/investmentlc", methods=['POST'])
def deleteinvlc(investmentlc_id):
    deleteinvlc = InvestmentLC.query.get_or_404(investmentlc_id)
    dbase.session.delete(deleteinvlc)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))

@server.route('/admin/add_forestprotection', methods=['GET','POST'])
def add_forestprotection():
	formfp = ForestProtectionForm()
	if formfp.validate_on_submit():
		new_forestprotection = ForestProtection(formfp.fp_category.data, formfp.fp_item.data, formfp.fp_description.data, formfp.fp_qty.data, formfp.fp_total.data, formfp.fp_personnel.data, formfp.fp_remarks.data)
		dbase.session.add(new_forestprotection)
		dbase.session.commit()	
		return redirect(url_for('forestprotection',formfp=formfp))
	return render_template('index.html', formfp=formfp)


@server.route('/admin/update/<int:investment_id>/investment', methods=['GET','POST'])
def update_investment(investment_id):
	form = InvestmentForm()
	investment = Investment.query.get_or_404(investment_id)
	if form.validate_on_submit():
		investment.investment_amount = form.investment_amount.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', investment=investment))
	elif request.method == 'GET':
		form.investment_amount.data = investment.investment_amount
		#return numberFormat("Php {:,.2f}".format(investment.investment_amount))
	return redirect(url_for('settings.html', form=form, investment=investment))


@server.route('/admin/update/<int:hectares_id>/hectares', methods=['GET','POST'])
def update_hectares(hectares_id):
	form2 = HectaresForm()
	hectares = Hectares.query.get_or_404(hectares_id)
	if form2.validate_on_submit():
		hectares.hectares_total = form2.hectares_total.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', hectares=hectares))
	elif request.method == 'GET':
		form2.hectares_total.data = hectares.hectares_total
	return redirect(url_for('settings.html', form2=form2, hectares=hectares))

@server.route('/admin/update/<int:reforestation_id>/reforestation', methods=['GET','POST'])
def update_reforestation(reforestation_id):
	form3 = ReforestationForm()
	reforestation = Reforestation.query.get_or_404(reforestation_id)
	if form3.validate_on_submit():
		reforestation.reforestation_total = form3.reforestation_total.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('rainforestation_cost', reforestation=reforestation))
	elif request.method == 'GET':
		form3.reforest_total.data = reforestation.reforestation_total
	return redirect(url_for('costbreakdown.html', form3=form3, reforestation=reforestation))

@server.route('/admin/forestprotection', methods=['GET','POST'])
@login_required
def forestprotection():
	formfp = ForestProtectionForm()
	forestprotection = ForestProtection.query.all()
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	formrf = RainforestationForm()
	return render_template('settings.html', forestprotection=forestprotection, formfp=formfp, user=user, investment=investment, hectares=hectares, form=form, form2=form2, formrf=formrf)


@server.route("/admin/item/<int:fp_id>/forestprotection/delete", methods=['POST'])
def deletefp(fp_id):
    deletefp = ForestProtection.query.get_or_404(fp_id)
    dbase.session.delete(deletefp)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))

@server.route('/admin/update/<int:fp_id>/forestprotection', methods=['GET','POST'])
def updatefp(fp_id):
	formfp = ForestProtection()
	forestprotection = ForestProtection.query.get_or_404(fp_id)
	if formfp.validate_on_submit():
		forestprotection.fp_category = formfp.fp_category.data
		forestprotection.fp_item = formfp.fp_item.data
		forestprotection.fp_description = formfp.fp_description.data
		forestprotection.fp_qty = formfp.fp_qty.data
		forestprotection.fp_total = formfp.fp_total.data
		forestprotection.fp_personnel = formfp.fp_personnel.data
		forestprotection.fp_remarks = formfp.fp_remarks.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', forestprotection=forestprotection))
	elif request.method == 'GET':
		formfp.fp_category.data = forestprotection.fp_category
		formfp.fp_item.data = forestprotection.fp_item
		formfp.fp_description.data = forestprotection.fp_description
		formfp.fp_qty.data = forestprotection.fp_qty
		formfp.fp_total.data = forestprotection.fp_total
		formfp.fp_personnel.data = forestprotection.fp_personnel
		formfp.fp_remarks.data = forestprotection.fp_remarks
	return redirect(url_for('settings.html', formfp=formfp, forestprotection=forestprotection))

@server.route('/admin/rainforestation', methods=['GET','POST'])
@login_required
def rainforestation():
	user = User.query.filter_by(id=current_user.id).first()
	formrf = RainforestationForm()
	rainforestation = Rainforestation.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	return render_template('settings.html', user = user, formrf=formrf, rainforestation=rainforestation, investment=investment, hectares=hectares, form=form,form2=form2)

@server.route('/admin/add_rainforestation', methods=['GET','POST'])
def add_rainforestation():
	formrf = RainforestationForm()
	user = User.query.filter_by(id=current_user.id).first()
	if formrf.validate_on_submit():
		new_rainforestation = Rainforestation(formrf.rf_category.data, formrf.rf_item.data, formrf.rf_description.data, formrf.rf_qty.data, formrf.rf_total.data, formrf.rf_personnel.data, formrf.rf_remarks.data)
		dbase.session.add(new_rainforestation)
		dbase.session.commit()	
		return redirect(url_for('rainforestation_cost',formrf=formrf, user=user))
	return render_template('costbreakdown.html', formrf=formrf, user=user)


@server.route("/admin/item/<int:rf_id>/rainforestation/delete", methods=['POST'])
def deleterf(rf_id):
    deleterf = Rainforestation.query.get_or_404(rf_id)
    dbase.session.delete(deleterf)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))


@server.route('/admin/update/<int:rf_id>/rainforestation', methods=['GET','POST'])
def updaterf(rf_id):
	formrf = RainforestationForm()
	rainforestation = Rainforestation.query.get_or_404(rf_id)
	if formrf.validate_on_submit():
		rainforestation.rf_category = formrf.rf_category.data
		rainforestation.rf_item = formrf.rf_item.data
		rainforestation.rf_description = formrf.rf_description.data
		rainforestation.rf_qty = formrf.rf_qty.data
		rainforestation.rf_total = formrf.rf_total.data
		rainforestation.rf_personnel = formrf.rf_personnel.data
		rainforestation.rf_remarks = formrf.rf_remarks.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', rainforestation=rainforestation))
	elif request.method == 'GET':
		formrf.rf_category.data = rainforestation.rf_category
		formrf.rf_item.data = rainforestation.rf_item
		formrf.rf_description.data = rainforestation.rf_description
		formrf.rf_qty.data = rainforestation.rf_qty
		formrf.rf_total.data = rainforestation.rf_total
		formrf.rf_personnel.data = rainforestation.rf_personnel
		formrf.rf_remarks.data = rainforestation.rf_remarks
	return redirect(url_for('settings.html', formrf=formrf, rainforestation=rainforestation))

@server.route('/admin/datagathering', methods=['GET','POST'])
@login_required
def datagathering():
	formdg = DataGatheringForm()
	datagathering = Datagathering.query.all()
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	formrf = RainforestationForm()
	return render_template('settings.html', datagathering=datagathering, formdg=formdg, user=user, investment=investment, hectares=hectares, form=form, form2=form2, formrf=formrf)


@server.route('/admin/add_datagathering', methods=['GET','POST'])
def add_datagathering():
	formdg = DataGatheringForm()
	if formdg.validate_on_submit():
		new_datagathering = Datagathering(formdg.dg_category.data, formdg.dg_item.data, formdg.dg_description.data, formdg.dg_qty.data, formdg.dg_total.data, formdg.dg_personnel.data, formdg.dg_remarks.data)
		dbase.session.add(new_datagathering)
		dbase.session.commit()	
		return redirect(url_for('settings',formdg=formdg))
	return render_template('settings.html', formdg=formdg)


@server.route('/admin/item/<int:dg_id>/datagathering/delete', methods=['POST'])
def deletedg(dg_id):
    deletedg = Datagathering.query.get_or_404(dg_id)
    dbase.session.delete(deletedg)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))


@server.route('/admin/update/<int:dg_id>/datagathering', methods=['GET','POST'])
def updatedg(dg_id):
	formdg = DataGatheringForm()
	datagathering = Datagathering.query.get_or_404(dg_id)
	if formdg.validate_on_submit():
		datagathering.dg_category = formdg.dg_category.data
		datagathering.dg_item = formdg.dg_item.data
		datagathering.dg_description = formdg.dg_description.data
		datagathering.dg_qty = formdg.dg_qty.data
		datagathering.dg_total = formdg.dg_total.data
		datagathering.dg_personnel = formdg.dg_personnel.data
		datagathering.dg_remarks = formdg.dg_remarks.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', datagathering=datagathering))
	elif request.method == 'GET':
		formdg.dg_category.data = datagathering.dg_category
		formdg.dg_item.data = datagathering.dg_item
		formdg.dg_description.data = datagathering.dg_description
		formdg.dg_qty.data = datagathering.dg_qty
		formdg.dg_total.data = datagathering.dg_total
		formdg.dg_personnel.data = datagathering.dg_personnel
		formdg.dg_remarks.data = datagathering.dg_remarks
	return redirect(url_for('settings.html', formdg=formdg, datagathering=datagathering))


@server.route('/admin/landcover', methods=['GET','POST'])
@login_required
def landcover():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	floodtemporal = FloodTemporal.query.all()
	investmentcost = InvestmentCost.query.filter_by(investmentcost_id=1).first()
	datagathering = Datagathering.query.all()
	rainforestation = Rainforestation.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form8 = FloodTemporalForm()
	return render_template('landcover.html', form=form, form2=form2, form3=form3,form8=form8, datagathering = datagathering, rainforestation=rainforestation, investmentcost=investmentcost, floodtemporal=floodtemporal, reforestation=reforestation, hectares=hectares, investment=investment, user=user )
	

@server.route('/admin/rainscenario', methods=['GET','POST'])
@login_required
def rainscenario():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	return render_template('rainfall.html', form=form, form2=form2, form3=form3, reforestation=reforestation, hectares=hectares, investment=investment, user=user )


@server.route('/admin/erosion', methods=['GET','POST'])
@login_required
def erosion():
	user = User.query.filter_by(id=current_user.id).first()
	erosion = Erosion.query.filter_by(erosion_id=1).first()
	erosiontemporal = ErosionTemporal.query.all()
	investmentcost = InvestmentCost.query.filter_by(investmentcost_id=1).first()
	form6 = ErosionForm()
	return render_template('erosion.html', form6=form6, erosiontemporal=erosiontemporal, investmentcost=investmentcost,erosion=erosion, user=user )


@server.route('/admin/update/<int:erosion_id>/erosion', methods=['GET','POST'])
def updatees(erosion_id):
	form6 = ErosionForm()
	erosion = Erosion.query.get_or_404(erosion_id)
	if form6.validate_on_submit():
		erosion.erosion_soil = form6.erosion_soil.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', erosion=erosion))
	elif request.method == 'GET':
		form6.erosion_soil.data = erosion.erosion_soil
	return redirect(url_for('settings.html', form6=form6, erosion=erosion))

@server.route('/admin/dryseason', methods=['GET','POST'])
@login_required
def dry_season():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	dryseason = DrySeason.query.all()
	erosion = Erosion.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form5 = DrySeasonForm()
	return render_template('dryseason.html', form=form, form2=form2, form3=form3,form5=form5, erosion=erosion, reforestation=reforestation, hectares=hectares, investment=investment, user=user, dryseason=dryseason )


@server.route('/admin/update/<int:dryseason_id>/dryseason', methods=['GET','POST'])
def updatedsf(dryseason_id):
	form5 = DrySeasonForm()
	dryseason = DrySeason.query.get_or_404(dryseason_id)
	if form5.validate_on_submit():
		dryseason.dryseason_forestage = form5.dryseason_forestage.data
		dryseason.dryseason_hectares = form5.dryseason_hectares.data
		dryseason.dryseason_discharge = form5.dryseason_discharge.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', dryseason=dryseason))
	elif request.method == 'GET':
		form5.dryseason_forestage.data = dryseason.dryseason_forestage
		form5.dryseason_hectares.data = dryseason.dryseason_hectares
		form5.dryseason_discharge.data = dryseason.dryseason_discharge
	return redirect(url_for('settings.html', form5=form5, dryseason=dryseason))

@server.route('/admin/add_dryseason', methods=['GET','POST'])
def add_dryseason():
	form5 = DrySeasonForm()
	if form5.validate_on_submit():
		new_dryseason = DrySeason(form5.dryseason_forestage.data, form5.dryseason_hectares.data, form5.dryseason_discharge.data)
		dbase.session.add(new_dryseason)
		dbase.session.commit()	
		return redirect(url_for('settings',form5=form5))
	return render_template('settings.html', form5=form5)

@server.route('/admin/<int:dryseason_id>/dryseason/delete', methods=['POST'])
def delete_dryseason(dryseason_id):
    deletedryseason = DrySeason.query.get_or_404(dryseason_id)
    dbase.session.delete(deletedryseason)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))

@server.route('/admin/landcover_classification', methods=['GET','POST'])
@login_required
def lcclass():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	lcclass = LCClassification.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form7 = LCClassificationForm()
	return render_template('dryseason.html', form=form, form2=form2, form7=form7, reforestation=reforestation, hectares=hectares, investment=investment, user=user, lcclass=lcclass )


@server.route('/admin/update/<int:lcc_id>/landcover_classification', methods=['GET','POST'])
def updatelcc(lcc_id):
	form7 = LCClassificationForm()
	lccclass = LCClassification.query.get_or_404(lcc_id)
	if form7.validate_on_submit():
		lccclass.lcc_classification = form7.lcc_classification.data
		lccclass.lcc_initial = form7.lcc_initial.data
		lccclass.lcc_publicdomain = form7.lcc_publicdomain.data
		lccclass.lcc_desired= form7.lcc_desired.data
		lccclass.lcc_maximum = form7.lcc_maximum.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', lccclass=lccclass))
	elif request.method == 'GET':
		form7.lcc_classification.data = lccclass.lcc_classification
		form7.lcc_initial.data = lccclass.lcc_initial
		form7.lcc_publicdomain.data = lccclass.lcc_publicdomain
		form7.lcc_desired.data = lccclass.lcc_desired
		form7.lcc_maximum.data = lccclass.lcc_maximum
	return redirect(url_for('settings.html', form7=form7, lccclass=lccclass))

@server.route('/admin/add_landcover_classification', methods=['GET','POST'])
def add_lcclassification():
	form7 = LCClassificationForm()
	if form7.validate_on_submit():
		new_lcclassification = LCClassification(form7.lcc_classification.data, form7.lcc_initial.data, form7.lcc_publicdomain.data,form7.lcc_desired.data, form7.lcc_maximum.data)
		dbase.session.add(new_lcclassification)
		dbase.session.commit()	
		return redirect(url_for('settings',form7=form7))
	return render_template('settings.html', form7=form7)

@server.route('/admin/<int:lcc_id>/landcover_classification/delete', methods=['POST'])
def delete_lcc(lcc_id):
    deletelcc = LCClassification.query.get_or_404(lcc_id)
    dbase.session.delete(deletelcc)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))

@server.route('/admin/flood_temporal', methods=['GET','POST'])
@login_required
def floodtemporal():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	floodtempporal = FloodTemporal.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form8 = FloodTemporalForm()
	return render_template('dryseason.html', form=form, form2=form2, form8=form8, reforestation=reforestation, hectares=hectares, investment=investment, user=user, floodtempporal=floodtempporal )


@server.route('/admin/update/<int:ft_id>/flood_temporal', methods=['GET','POST'])
def updateft(ft_id):
	form8 = FloodTemporalForm()
	floodtemporal = FloodTemporal.query.get_or_404(ft_id)
	if form8.validate_on_submit():
		floodtemporal.ft_lcc = form8.ft_lcc.data
		floodtemporal.ft_hectares = form8.ft_hectares.data
		floodtemporal.ft_reduced = form8.ft_reduced.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', floodtemporal=floodtemporal))
	elif request.method == 'GET':
		form8.ft_lcc.data = floodtemporal.ft_lcc
		form8.ft_hectares.data = floodtemporal.ft_hectares
		form8.ft_reduced.data = floodtemporal.ft_reduced
	return redirect(url_for('settings.html', form8=form8, floodtemporal=floodtemporal))

@server.route('/admin/add_flodd_temporal', methods=['GET','POST'])
def add_floodtemporal():
	form8 = FloodTemporalForm()
	if form8.validate_on_submit():
		new_floodtemporal = FloodTemporal(form8.ft_lcc.data, form8.ft_hectares.data, form8.ft_reduced.data)
		dbase.session.add(new_floodtemporal)
		dbase.session.commit()	
		return redirect(url_for('settings',form8=form8))
	return render_template('settings.html', form8=form8)

@server.route('/admin/<int:ft_id>/flood_temporal/delete', methods=['POST'])
def delete_ft(ft_id):
    deleteft = FloodTemporal.query.get_or_404(ft_id)
    dbase.session.delete(deleteft)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))


@server.route('/admin/erosion_temporal', methods=['GET','POST'])
@login_required
def erosiontemporal():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	erosiontemporal = ErosionTemporal.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form9 = ErosionTemporal()
	return render_template('dryseason.html', form=form, form2=form2, form9=form9, reforestation=reforestation, hectares=hectares, investment=investment, user=user, erosiontemporal=erosiontemporal )


@server.route('/admin/update/<int:et_id>/erosion_temporal', methods=['GET','POST'])
def updateet(et_id):
	form9 = ErosionTemporalForm()
	erosiontemporal = FloodTemporal.query.get_or_404(et_id)
	if form9.validate_on_submit():
		erosiontemporal.et_lcc = form9.et_lcc.data
		erosiontemporal.et_hectares = form9.et_hectares.data
		erosiontemporal.et_reduced = form9.et_reduced.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('settings', erosiontemporal=erosiontemporal))
	elif request.method == 'GET':
		form9.et_lcc.data = erosiontemporal.et_lcc
		form9.et_hectares.data = erosiontemporal.et_hectares
		form9.et_reduced.data = erosiontemporal.et_reduced
	return redirect(url_for('settings.html', form9=form9, erosiontemporal=erosiontemporal))

@server.route('/admin/add_erosion_temporal', methods=['GET','POST'])
def add_erosiontemporal():
	form9 = ErosionTemporalForm()
	if form9.validate_on_submit():
		new_erosiontemporal = ErosionTemporal(form9.et_lcc.data, form9.et_hectares.data, form9.et_reduced.data)
		dbase.session.add(new_erosiontemporal)
		dbase.session.commit()	
		return redirect(url_for('settings',form9=form9))
	return render_template('settings.html', form9=form9)

@server.route('/admin/<int:et_id>/erosion_temporal/delete', methods=['POST'])
def delete_et(et_id):
    deleteet = ErosionTemporal.query.get_or_404(et_id)
    dbase.session.delete(deleteet)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('settings'))


@server.route('/admin/investors', methods=['GET','POST'])
@login_required
def investors():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	erosiontemporal = ErosionTemporal.query.all()
	investors = Investors.query.all()
	investorform = InvestorForm()
	form = InvestmentForm()
	form2 = HectaresForm()
	form9 = ErosionTemporal()
	return render_template('investors.html', investors = investors, investorform=investorform, form=form, form2=form2, form9=form9, reforestation=reforestation, hectares=hectares, investment=investment, user=user, erosiontemporal=erosiontemporal )


@server.route('/investors_settings', methods=['GET','POST'])
@login_required
def investors_settings():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	erosiontemporal = ErosionTemporal.query.all()
	investors = Investors.query.all()
	investorform = InvestorForm()
	form = InvestmentForm()
	form2 = HectaresForm()
	form9 = ErosionTemporal()
	return render_template('investors_settings.html', investors = investors, investorform=investorform, form=form, form2=form2, form9=form9, reforestation=reforestation, hectares=hectares, investment=investment, user=user, erosiontemporal=erosiontemporal )


@server.route('/admin/update/<int:investors_id>/investors', methods=['GET','POST'])
def updateinvestor(investors_id):
	investorform = InvestorForm()
	investors = Investors.query.get_or_404(investors_id)
	user = User.query.filter_by(id=current_user.id).first()
	if investorform.validate_on_submit():
		investors.investors_name = investorform.investors_name.data
		investors.investors_office = investorform.investors_office.data
		investors.investors_address = investorform.investors_address.data
		investors.investors_amount = investorform.investors_amount.data
		investors.investors_hectares = investorform.investors_hectares.data
		investors.investors_area = investorform.investors_area.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('investors_settings', investors=investors))
	elif request.method == 'GET':
		investorform.investors_name.data = investors.investors_name
		investorform.investors_office.data = investors.investors_office
		investorform.investors_address.data = investors.investors_address
		investorform.investors_amount.data = investors.investors_amount
		investorform.investors_hectares.data = investors.investors_hectares
		investorform.investors_area.data = investors.investors_area
	return redirect(url_for('investors_settings.html', investorform=investorform, investors=investors, user=user))

@server.route('/admin/add_investors', methods=['GET','POST'])
def add_investors():
	user = User.query.filter_by(id=current_user.id).first()
	investorform = InvestorForm()
	if investorform.validate_on_submit():
		new_investor = Investors(investorform.investors_name.data, investorform.investors_office.data, investorform.investors_address.data, investorform.investors_amount.data, investorform.investors_hectares.data, investorform.investors_area.data)
		dbase.session.add(new_investor)
		dbase.session.commit()	
		return redirect(url_for('investors_settings',investorform=investorform, user=user))
	return render_template('investors_settings.html', investorform=investorform, user=user)

@server.route('/admin/<int:investors_id>/investors/delete', methods=['POST'])
def delete_investors(investors_id):
    delete_investors = Investors.query.get_or_404(investors_id)
    dbase.session.delete(delete_investors)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('investors_settings'))

@server.route('/admin/about', methods=['GET','POST'])
@login_required
def about():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	dryseason = DrySeason.query.all()
	erosion = Erosion.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form5 = DrySeasonForm()
	return render_template('about.html', form=form, form2=form2, form3=form3,form5=form5, erosion=erosion, reforestation=reforestation, hectares=hectares, investment=investment, user=user, dryseason=dryseason )


@server.route('/', methods=['GET','POST'])
def p_about():

	return render_template('p_about.html' )

@server.route('/admin/waterlevel', methods=['GET','POST'])
def realtime():
	user = User.query.filter_by(id=current_user.id).first()
	return render_template('realtime.html', user=user)

@server.route('/waterlevel', methods=['GET','POST'])
def p_realtime():

	return render_template('p_realtime.html' )


@server.route('/logout')
@login_required
def logout():
	session.clear()
	logout_user()
	return redirect(url_for('login'))
	


##-------------------- public view
##-------------------- public view
##-------------------- public view

@server.route('/dashboard', methods=["GET","POST"])
def p_dashboard():
	user = user = User.query.filter_by(id=1).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	dryseason = DrySeason.query.all()
	erosion = Erosion.query.filter_by(erosion_id=1).first()
	floodtemporal = FloodTemporal.query.all()
	erosiontemporal = ErosionTemporal.query.all()
	forestprotection = ForestProtection.query.all()
	rainforestation = Rainforestation.query.all()
	datagathering = Datagathering.query.all()
	investmentlc = InvestmentLC.query.all()
	investmentcost = InvestmentCost.query.filter_by(investmentcost_id=1).first()
	lcclass = LCClassification.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	form5 = DrySeasonForm() 
	form6 = ErosionForm()
	form7 = LCClassificationForm()
	form8 = FloodTemporalForm()
	form9 = ErosionTemporalForm()
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	forminvlc  = InvestmentLCForm()
	formic = InvestmentCostForm()

	return render_template('p_index.html', investmentcost=investmentcost,formic=formic, forminvlc=forminvlc,investmentlc=investmentlc, form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9, formfp=formfp, formrf=formrf, formdg=formdg, reforestation=reforestation, hectares=hectares, investment=investment, dryseason=dryseason, erosion=erosion, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, lcclass=lcclass, floodtemporal=floodtemporal, erosiontemporal=erosiontemporal,user=user )


@server.route('/rainforestation_cost', methods=["GET","POST"])
def p_rainforestation_cost():
	user = User.query.all()
	forestprotection = ForestProtection.query.all()
	rainforestation = Rainforestation.query.all()
	datagathering = Datagathering.query.all()
	investmentcost =  InvestmentCost.query.filter_by(investmentcost_id=1).first()
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	formic = InvestmentCostForm()

	return render_template('p_costbreakdown.html', investmentcost=investmentcost, formic=formic, formfp=formfp, formrf=formrf, formdg=formdg, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, user=user )

@server.route('/forestprotection', methods=['GET','POST'])
def p_forestprotection():
	formfp = ForestProtectionForm()
	forestprotection = ForestProtection.query.all()
	user = User.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	formrf = RainforestationForm()
	return render_template('p_index.html', forestprotection=forestprotection, formfp=formfp, user=user, investment=investment, hectares=hectares, form=form, form2=form2, formrf=formrf)

@server.route('/rainforestation', methods=['GET','POST'])
def p_rainforestation():
	user = User.query.all()
	formrf = RainforestationForm()
	rainforestation = Rainforestation.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	return render_template('p_index.html', user = user, formrf=formrf, rainforestation=rainforestation, investment=investment, hectares=hectares, form=form,form2=form2)

@server.route('/datagathering', methods=['GET','POST'])
def p_datagathering():
	formdg = DataGatheringForm()
	datagathering = Datagathering.query.all()
	user = User.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	formrf = RainforestationForm()
	return render_template('p_index.html', datagathering=datagathering, formdg=formdg, user=user, investment=investment, hectares=hectares, form=form, form2=form2, formrf=formrf)

@server.route('/landcover', methods=['GET','POST'])
def p_landcover():
	user = User.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	rainforestation = Rainforestation.query.all()
	lcclass = LCClassification.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	return render_template('p_landcover.html', form=form, form2=form2, form3=form3, lcclass = lcclass, rainforestation=rainforestation, reforestation=reforestation, hectares=hectares, investment=investment, user=user )
	

@server.route('/rainscenario', methods=['GET','POST'])
def p_rainscenario():
	user = User.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	return render_template('p_rainfall.html', form=form, form2=form2, form3=form3, reforestation=reforestation, hectares=hectares, investment=investment, user=user )


@server.route('/erosion', methods=['GET','POST'])
def p_erosion():
	user = User.query.all()
	erosion = Erosion.query.filter_by(erosion_id=1).first()
	form6 = ErosionForm()
	return render_template('p_erosion.html', form6=form6, erosion=erosion, user=user )

@server.route('/dryseason', methods=['GET','POST'])
def p_dry_season():
	user = User.query.all()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	dryseason = DrySeason.query.all()
	erosion = Erosion.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form5 = DrySeasonForm()
	return render_template('p_dryseason.html', form=form, form2=form2, form3=form3,form5=form5, erosion=erosion, reforestation=reforestation, hectares=hectares, investment=investment, user=user, dryseason=dryseason )

@server.route('/manage_users', methods=['GET','POST'])
@login_required
def manage_users():
	user = User.query.filter_by(id=current_user.id).first()
	user_list = User.query.all()
	
	return render_template('users.html', user=user, user_list=user_list )

@server.route('/admin/user/<int:id>/delete', methods=['POST'])
def delete_user(id):
    delete_user = User.query.get_or_404(id)
    dbase.session.delete(delete_user)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('manage_users'))

@server.route('/investors', methods=['GET','POST'])
def p_investors():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	erosiontemporal = ErosionTemporal.query.all()
	investors = Investors.query.all()
	investorform = InvestorForm()
	form = InvestmentForm()
	form2 = HectaresForm()
	form9 = ErosionTemporal()
	return render_template('p_investors.html', investors = investors, investorform=investorform, form=form, form2=form2, form9=form9, reforestation=reforestation, hectares=hectares, investment=investment, user=user, erosiontemporal=erosiontemporal )
