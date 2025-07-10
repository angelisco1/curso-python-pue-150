from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, HTTPException

errors_bp = Blueprint("error_handlers", __name__)

# @errors_bp.app_errorhandler(404)
# def not_found_error(error):
#     print("ERROR", error)
#     return jsonify({"message": error.description}), error.code


# @errors_bp.app_errorhandler(BadRequest)
# def bad_request_error(error):
#     return jsonify({"message": error.description}), error.code

@errors_bp.app_errorhandler(HTTPException)
def http_errors(error):
    return jsonify({"message": error.description}), error.code