from flask import jsonify, make_response


def handle_bad_request(e):
    return make_response(jsonify({"message": "Bad request"}), 400)


def handle_unauthorized(e):
    return make_response(jsonify({"message": "Unauthorized"}), 401)


def handle_forbidden(e):
    return make_response(jsonify({"message": "Forbidden"}), 403)


def handle_not_found(e):
    return make_response(jsonify({"message": "Not found"}), 404)


def handle_method_not_allowed(e):
    return make_response(jsonify({"message": "Method not allowed"}), 405)


def handle_not_processable_error(e):
    return make_response(jsonify({"message": "Not Processable"}), 422)


def handle_internal_server_error(e):
    return make_response(jsonify({"message": "Internal server error"}), 500)