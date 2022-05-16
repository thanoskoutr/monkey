import flask_restful
from flask_apispec.views import MethodResource

from monkey_island.cc.resources.auth.auth import jwt_required
from monkey_island.cc.services.reporting.report import ReportService


class SecurityReport(MethodResource, flask_restful.Resource):
    @jwt_required
    def get(self):
        return ReportService.get_report()
