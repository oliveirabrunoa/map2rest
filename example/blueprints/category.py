from flask import Blueprint, jsonify, request
import datetime

# @app.route('/course_type', methods=['GET'])
# def course_type_teste():
#     print("teste")
#     return True
#     # course_types = models.Post.query.all()
#     # return jsonify(result=[dict(id=ct.id_course_type, description=ct.description_course_type) for ct in course_types])
category = Blueprint("category", __name__)

@category.route('/category')
def hello():
    return "Hello World!"
