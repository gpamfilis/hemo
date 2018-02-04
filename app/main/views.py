from flask import render_template, session, redirect, url_for
from . import main
from .forms import Weight, BMI, BathRoom


@main.route('/')
def home():
    form1 = Weight()
    """Render website's home page."""
    return "hello motherfucker"

@main.route('weight', methods=['GET','POST'])
def weight():
    form1 = Weight()
    """Render website's home page."""

    if form1.validate_on_submit():
        return str(form1.weight.data)
    else:
        return render_template('main/weight.html', form1=form1)

@main.route('bmi', methods=['GET','POST'])
def bmi():
    bmi_form = BMI()
    """Render website's home page."""

    if bmi_form.validate_on_submit():

        bmi = (bmi_form.weight.data)/((bmi_form.height.data)**2)

        return str(bmi)
    else:
        return render_template('main/basic_form.html', form=bmi_form)

@main.route('bathroom', methods=['GET','POST'])
def bathroom():
    form = BathRoom()
    """Render website's home page."""

    if form.validate_on_submit():
        return str(form.output.data)
    else:
        return render_template('main/basic_form.html', form=form)
