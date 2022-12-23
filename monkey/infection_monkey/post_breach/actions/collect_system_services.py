import logging

import psutil

from common.common_consts.post_breach_consts import POST_BREACH_SYSTEM_SERVICES_COLLECTION
from infection_monkey.i_puppet.i_puppet import PostBreachData
from infection_monkey.post_breach.pba import PBA
from infection_monkey.telemetry.messengers.i_telemetry_messenger import ITelemetryMessenger

# from typing import Dict


logger = logging.getLogger(__name__)

# Linux doesn't have WindowsError
applicable_exceptions = psutil.AccessDenied
try:
    applicable_exceptions = (psutil.AccessDenied, WindowsError)
except NameError:
    pass

# TODO: Add Windows & Linux Commands
# TODO: Fix Zero Trust Report
# TODO: Format results correctly
# TODO: Check agent memory leaks
# TODO: Check agent's network discovery


class SystemServicesCollection(PBA):
    def __init__(self, telemetry_messenger: ITelemetryMessenger):
        # linux_cmds, windows_cmds = get_commands_to_list_system_services()
        super().__init__(
            telemetry_messenger,
            name=POST_BREACH_SYSTEM_SERVICES_COLLECTION,
            # linux_cmd=linux_cmds,
            # windows_cmd=windows_cmds,
            # linux_cmd="echo 'Discovered the following system services:'; systemctl --type=service -all --no-legend --no-pager --plain",
            linux_cmd="echo 'Discovered the following system services:'; systemctl --type=service --all --no-legend --no-pager --plain | awk '{print $1}'",
            windows_cmd="powershell Write-Output 'Discovered the following system services:'; Get-Service",
        )

    # def run(self, options: Dict):
    #     # TODO: Add description
    #     """
    #     Collects system services from the host.
    #     Currently ...
    #     """
    #     logger.debug("Reading system services")

    #     services = {}
    #     success_state = False

    #     for service in psutil.win_service_iter():
    #         try:
    #             services[service.name()] = {
    #                 "name": service.name(),
    #                 "pid": service.pid(),
    #                 "display_name": service.diplay_name(),
    #                 "status": service.status(),
    #                 "username": service.username(),
    #                 "full_service_path": service.binpath(),
    #             }
    #             success_state = True
    #         except applicable_exceptions:
    #             # TODO: Check which are unavailable as non-admin user
    #             # We may be running as non root and some processes are impossible to acquire in
    #             # Windows/Linux. In this case, we'll just add what we know.
    #             services[service.name()] = {
    #                 "name": service.name(), # "null"
    #                 "pid": service.pid(),
    #                 "display_name": service.diplay_name(),
    #                 "status": service.status(),
    #                 "username": service.username(),
    #                 "full_service_path": service.binpath() # "null"
    #             }
    #             continue
    #     # TODO: Return JSON correctly (like in ProcessCollector)
    #     self.pba_data.append(PostBreachData(self.name, self.command, (services, success_state)))
    #     return self.pba_data
