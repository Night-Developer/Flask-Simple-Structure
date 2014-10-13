from flask import Blueprint

blueprint = Blueprint('blueprint',__name__,template_folder='templates')

@blueprint.route('/')
def show():
    return 'Hola blue print'