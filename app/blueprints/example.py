from flask import Blueprint
from .views.example import example_view

main = Blueprint('main', __name__)

# example create routes/urls
main.add_url_rule('/', 'example_name', view_func=example_view, methods=['GET'])