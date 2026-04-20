from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.itinerary import itinerary
from app.models import Itinerary, ItineraryDay
from app.itinerary.forms import ItineraryForm, DayForm


@itinerary.route('/')
@login_required
def index():
    itineraries = Itinerary.query.order_by(Itinerary.created_at.desc()).all()
    return render_template('itinerary/index.html', itineraries=itineraries)


@itinerary.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ItineraryForm()
    if form.validate_on_submit():
        itin = Itinerary(
            title=form.title.data,
            destination=form.destination.data,
            duration_days=form.duration_days.data,
            user_id=current_user.id
        )
        db.session.add(itin)
        db.session.commit()

        for day_num in range(1, form.duration_days.data + 1):
            day = ItineraryDay(
                day_number=day_num,
                title=f'Day {day_num}',
            )
            db.session.add(day)
        db.session.commit()

        flash('Itinerary created!', 'success')
        return redirect(url_for('itinerary.detail', id=itin.id))
    return render_template('itinerary/form.html', form=form)


@itinerary.route('/<int:id>')
@login_required
def detail(id):
    itin = Itinerary.query.get_or_404(id)
    days = ItineraryDay.query.filter_by(itinerary_id=id).order_by(ItineraryDay.day_number).all()
    return render_template('itinerary/detail.html', itinerary=itin, days=days)


@itinerary.route('/<int:id>/day/<int:day_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_day(id, day_id):
    itin = Itinerary.query.get_or_404(id)
    day = ItineraryDay.query.get_or_404(day_id)
    form = DayForm(obj=day)

    if form.validate_on_submit():
        day.title = form.title.data
        day.description = form.description.data
        day.accommodation = form.accommodation.data
        db.session.commit()
        flash(f'Day {day.day_number} updated!', 'success')
        return redirect(url_for('itinerary.detail', id=id))

    return render_template('itinerary/edit_day.html', form=form, itinerary=itin, day=day)


@itinerary.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    itin = Itinerary.query.get_or_404(id)
    db.session.delete(itin)
    db.session.commit()
    flash('Itinerary deleted.', 'success')
    return redirect(url_for('itinerary.index'))


@itinerary.route('/api/destinations')
def destinations_api():
    return jsonify([])
