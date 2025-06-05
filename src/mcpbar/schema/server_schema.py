from dataclasses import dataclass, field, fields
from enum import Enum
from typing import Dict, Any, Union

class ServerType(Enum):
    LOCAL_RUNNABLE_PY = "LocalRunnablePy"
    LOCAL_RUNNABLE_JS = "LocalRunnableJs"

@dataclass()
class LocalRunnablePyParams:
    interpreter: str
    path: str


@dataclass()
class LocalRunnableJsParams:
    path: str


ServerParams = Union[LocalRunnablePyParams, LocalRunnableJsParams]


@dataclass()
class ServerSchema:
    server_type: str
    server_params_dict: Dict
    server_params: ServerParams = field(init=False)

    def __post_init__(self):
        if not getattr(ServerType, self.server_type, None):
            raise ValueError(f"Invalid server type: {self.server_type}")

        match  self.server_type:
            case ServerType.LOCAL_RUNNABLE_PY.name:
                self.server_params = LocalRunnablePyParams(**self.server_params_dict)
            case ServerType.LOCAL_RUNNABLE_JS.name:
                self.server_params = LocalRunnableJsParams(**self.server_params_dict)
