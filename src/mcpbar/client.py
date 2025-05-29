from mcpbar.base import BaseServer, LocalRunnableJsServer, LocalRunnablePyServer
from mcpbar.schema import ServerSchema, ServerType
from typing import Optional


class McpBarClient:
    def __init__(self):
        self.server: Optional[BaseServer] = None

    def load_server(self, server_schema: ServerSchema):
        match server_schema.server_type:
            case ServerType.LOCAL_RUNNABLE_JS.name:
                self.server = LocalRunnableJsServer(server_schema)
            case ServerType.LOCAL_RUNNABLE_PY.name:
                self.server = LocalRunnablePyServer(server_schema)
            case _:
                raise ValueError(f"Unknown server type: {server_schema.server_type}")

        print(f"Loaded server: {self.server}")
        self.server.get_runnable().run()