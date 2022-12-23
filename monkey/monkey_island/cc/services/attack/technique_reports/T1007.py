from common.common_consts.post_breach_consts import POST_BREACH_SYSTEM_SERVICES_COLLECTION
from monkey_island.cc.services.attack.technique_reports.pba_technique import PostBreachTechnique


class T1007(PostBreachTechnique):
    tech_id = "T1007"
    relevant_systems = ["Linux", "Windows"]
    unscanned_msg = "Monkey didn't try to get a listing of system services."
    scanned_msg = "Monkey tried to get a listing of system services but failed to do so."
    used_msg = "Monkey got a listing of system services successfully."
    pba_names = [POST_BREACH_SYSTEM_SERVICES_COLLECTION]
