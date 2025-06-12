from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Dict, Any, Union, List
from mcpbar.schema import extern_schema


class ServerTransportType(Enum):
    STDIO = "stdio"
    SSE = 'sse'


class ServerType(Enum):
    LOCAL_RUNNABLE_PY = "LocalRunnablePy"
    LOCAL_RUNNABLE_JS = "LocalRunnableJs"


@dataclass()
class LocalRunnablePyParams:
    command: str
    args: List[str]
    env: Dict[str, str] = field(default_factory=dict)


@dataclass()
class LocalRunnableJsParams:
    command: str
    args: List[str]
    env: Dict[str, str] = field(default_factory=dict)


@dataclass()
class SseServerParams:
    url: str


ServerParams = Union[LocalRunnablePyParams, LocalRunnableJsParams, SseServerParams]

def get_server_type_and_params_from_cline_server(server: extern_schema.ClineStdioServerSchema) -> (ServerType, ServerParams):
    args = server.args
    if len(args) == 0:
        raise ValueError("Invalid cline stdio server schema: miss cmd args")
    server_path = args[-1]
    if server_path.endswith(".py"):
        return ServerType.LOCAL_RUNNABLE_PY, LocalRunnablePyParams(command=server.command, args=server.args, env=server.env)
    elif server_path.endswith(".js"):
        return ServerType.LOCAL_RUNNABLE_JS, LocalRunnableJsParams(command=server.command, args=server.args, env=server.env)
    else:
        raise ValueError(f"Not support cline stdio server script type: `{server_path.split('.')[-1]}`")


@dataclass()
class ServerSchema:
    server_transport_type: str
    server_type: str
    server_params_dict: Dict

    def __post_init__(self):
        if not getattr(ServerType, self.server_type, None):
            raise ValueError(f"Invalid server type: {self.server_type}")
        if not getattr(ServerTransportType, self.server_transport_type, None):
            raise ValueError(f"Invalid server transport type: {self.server_transport_type}")

    @classmethod
    def from_cline_server_schema(cls, server_config: Dict):
        if server_config.get('command', None) is not None:
            cline_schema = extern_schema.ClineStdioServerSchema(
                command=server_config['command'],
                args=server_config.get('args', []),
                env=server_config.get('env', {})
            )
            server_transport_type = ServerTransportType.STDIO.name
        else:
            cline_schema = extern_schema.ClineSseServerSchema(
                url=server_config['url']
            )
            server_transport_type = ServerTransportType.SSE.name

        server_type, server_params = get_server_type_and_params_from_cline_server(cline_schema)
        return cls(
            server_transport_type=server_transport_type,
            server_type=server_type.name,
            server_params_dict=asdict(server_params),
        )
