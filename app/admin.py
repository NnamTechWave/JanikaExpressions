from flask import Blueprint, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_required
from flask_admin import AdminIndexView, expose

from . import db
from .models import User

admin = Blueprint('admin', __name__)

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('users.login'))
        return super(MyAdminIndexView, self).index()

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(index_view=MyAdminIndexView(), template_mode='bootstrap3')
admin.add_view(SecureModelView(User, db.session))
