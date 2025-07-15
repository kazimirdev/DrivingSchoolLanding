# admin.py
from flask import redirect, url_for, render_template, request
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_user, logout_user
from wtforms import PasswordField
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

from src.db import db
from src.models import Category, Slide, GalleryImage, Instructor
from app import app

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return Instructor.query.get(int(user_id))


class LoginForm(FlaskForm):
    email    = StringField("E-mail",    validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit   = SubmitField("Sign in")


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login", next=request.url))


class PriceOnlyCategoryView(SecureModelView):
    """Hide everything except price & activation switch."""
    column_list  = ("name", "position", "price", "description", "image", "is_active")
    form_edit_rules = ("name", "position", "price", "description", "image", "is_active")
    form_create_rules = ("name", "price", "description", "image", "is_active")
    can_export = False
    can_create = False


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_admin):
            return redirect(url_for("login"))
        return super().index()

class PositionedView(SecureModelView):
    column_default_sort = ("position", True)  # sort by order ascending
    column_editable_list = ("position", "is_active")

admin = Admin(app, name="OSK Admin", index_view=MyAdminIndexView(),
              template_mode="bootstrap4")
admin.add_view(PriceOnlyCategoryView(Category, db.session, name="Cennik"))
admin.add_view(SecureModelView(Slide, db.session, name="Slajdy"))
admin.add_view(SecureModelView(GalleryImage, db.session, name="Galeria"))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Instructor.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
