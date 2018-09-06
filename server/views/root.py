from flask import Blueprint, render_template

root = Blueprint('root', __name__)


@root.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('hello.html')

@root.route('/grid', methods=['GET', 'POST'])
def grid():
    return render_template('grid.html')

@root.route('/tree', methods=['GET', 'POST'])
def tree():
    return render_template('tree.html')