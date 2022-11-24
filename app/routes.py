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
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	form5 = DrySeasonForm() 
	form6 = ErosionForm()  	
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	forminvlc  = InvestmentLCForm()
	formic = InvestmentCostForm()

	#rf_sum = Rainforestation.query.all()
	#print(sum(rf_sum))

	return render_template('index.html', investmentcost=investmentcost,formic=formic, forminvlc=forminvlc,investmentlc=investmentlc, form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, formfp=formfp, formrf=formrf, formdg=formdg, reforestation=reforestation, hectares=hectares, investment=investment, dryseason=dryseason, erosion=erosion, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, user=user )


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
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	form5 = DrySeasonForm() 
	form6 = ErosionForm()  	
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	forminvlc  = InvestmentLCForm()
	formic = InvestmentCostForm()

	#rf_sum = Rainforestation.query.all()
	#print(sum(rf_sum))

	return render_template('settings.html', investmentcost=investmentcost,formic=formic, forminvlc=forminvlc,investmentlc=investmentlc, form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, formfp=formfp, formrf=formrf, formdg=formdg, reforestation=reforestation, hectares=hectares, investment=investment, dryseason=dryseason, erosion=erosion, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, user=user )


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
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	return render_template('landcover.html', form=form, form2=form2, form3=form3, reforestation=reforestation, hectares=hectares, investment=investment, user=user )
	

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
	form6 = ErosionForm()
	return render_template('erosion.html', form6=form6, erosion=erosion, user=user )


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

@server.route('/about', methods=['GET','POST'])
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
	return render_template('currency.html', form=form, form2=form2, form3=form3,form5=form5, erosion=erosion, reforestation=reforestation, hectares=hectares, investment=investment, user=user, dryseason=dryseason )


@server.route('/logout')
@login_required
def logout():
	session.clear()
	logout_user()
	return redirect(url_for('login'))
	


##-------------------- public view
##-------------------- public view
##-------------------- public view

@server.route('/', methods=["GET","POST"])
def p_dashboard():
	user = user = User.query.filter_by(id=1).first()
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
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	form5 = DrySeasonForm() 
	form6 = ErosionForm()  	
	formfp = ForestProtectionForm()
	formrf = RainforestationForm()
	formdg = DataGatheringForm()
	forminvlc  = InvestmentLCForm()
	formic = InvestmentCostForm()

	return render_template('p_index.html', investmentcost=investmentcost,formic=formic, forminvlc=forminvlc,investmentlc=investmentlc, form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, formfp=formfp, formrf=formrf, formdg=formdg, reforestation=reforestation, hectares=hectares, investment=investment, dryseason=dryseason, erosion=erosion, forestprotection=forestprotection, rainforestation=rainforestation, datagathering=datagathering, user=user )


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
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	return render_template('p_landcover.html', form=form, form2=form2, form3=form3, reforestation=reforestation, hectares=hectares, investment=investment, user=user )
	

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

 