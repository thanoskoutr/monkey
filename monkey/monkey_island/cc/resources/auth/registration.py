import logging

import flask_restful
from flask import make_response, request
from flask_apispec import doc
from flask_apispec.views import MethodResource

from common.utils.exceptions import AlreadyRegisteredError, InvalidRegistrationCredentialsError
from monkey_island.cc.resources.auth.credential_utils import get_username_password_from_request
from monkey_island.cc.services import AuthenticationService

logger = logging.getLogger(__name__)


class Registration(MethodResource, flask_restful.Resource):
    @doc(description="Monkey registration GET method.", tags=["registration"])
    def get(self):
        return {"needs_registration": AuthenticationService.needs_registration()}

    @doc(description="Monkey registration POST method.", tags=["registration"])
    def post(self):
        username, password = get_username_password_from_request(request)

        try:
            AuthenticationService.register_new_user(username, password)
            return make_response({"error": ""}, 200)
        except (InvalidRegistrationCredentialsError, AlreadyRegisteredError) as e:
            return make_response({"error": str(e)}, 400)
