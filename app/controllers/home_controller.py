import json
import http.client
from flask import current_app, render_template, request, Response
from app.helpers.home_helpers import HomeHelpers


def index():
    """ set secret for goolgeapis"""
    secret = current_app.config.get("GOOGLE_API_KEY")

    return render_template('index.html', secret=secret, title="Home")


def get_distance():
    try:
        """ Creating params dictionary """
        params = dict()
        params["destination"] = request.form.get('destination')

        """ use HomeHelper to check the distance """
        status, result = HomeHelpers(**params).check_distance()

        """ If the status is True the return OK """
        if status:
            return Response(
                json.dumps(result),
                status=http.client.OK,
                mimetype='application/json'
            )

        """ If the status is False the return BAD REQUEST """
        return Response(
            json.dumps(result),
            status=http.client.BAD_REQUEST,
            mimetype='application/json'
        )

    except Exception as e:
        """ raise an exception incase there is something wrong"""
        return Response(
            json.dumps(str(e)),
            status=http.client.INTERNAL_SERVER_ERROR,
            mimetype='application/json'
        )
