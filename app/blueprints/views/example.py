from flask import jsonify

def example_view():
    return jsonify({
        'message': 'Hello, World!'
    })