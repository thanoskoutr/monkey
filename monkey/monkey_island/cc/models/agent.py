from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field
from typing_extensions import TypeAlias

from common.base_models import MutableInfectionMonkeyBaseModel

from . import MachineID

AgentID: TypeAlias = UUID


class Agent(MutableInfectionMonkeyBaseModel):
    """Represents an agent that has run on a victim machine"""

    id: AgentID = Field(..., allow_mutation=False)
    """Uniquely identifies an instance of an agent"""

    machine_id: MachineID = Field(..., allow_mutation=False)
    """The machine that the agent ran on"""

    start_time: datetime = Field(..., allow_mutation=False)
    """The time the agent process started"""

    stop_time: Optional[datetime]
    """The time the agent process exited"""

    parent_id: Optional[AgentID] = Field(allow_mutation=False)
    """The ID of the parent agent that spawned this agent"""

    cc_server: str = Field(default="")
    """The address that the agent used to communicate with the island"""

    log_contents: str = Field(default="")
    """The contents of the agent's log (empty until the agent shuts down)"""
