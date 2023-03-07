from flask_security import auth_token_required, roles_required

from common import UserRoles
from monkey_island.cc.flask_utils import AbstractResource
from monkey_island.cc.services.reporting.report import ReportService


class SecurityReport(AbstractResource):
    urls = ["/api/report/security"]

    @auth_token_required
    @roles_required(UserRoles.ISLAND.name)
    def get(self):
        ReportService.update_report()
        return ReportService.get_report()
