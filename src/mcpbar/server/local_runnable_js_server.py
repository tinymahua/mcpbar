from mcpbar.schema.server_schema import ServerType, ServerSchema
from mcpbar.base import BaseServer, BaseRunnable
from mcpbar.log import logger
from mcp import ClientSession, StdioServerParameters
from mcpbar.server.server_transports import StdioTransportServerMixin
from mcpbar.schema.server_schema import LocalRunnableJsParams


"""
Local Runnable Js and Server
"""

class LocalRunnableJs(BaseRunnable):
    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def run(self):
        logger.debug(f"Run {self.path}")



class LocalRunnableJsServer(BaseServer, StdioTransportServerMixin):
    server_type = ServerType.LOCAL_RUNNABLE_JS.name

    def __init__(self, server_schema: ServerSchema, server_params_schema:  type[LocalRunnableJsParams]):
        super().__init__(server_schema, server_params_schema)

    def get_runnable(self) -> LocalRunnableJs:
        return LocalRunnableJs(path=self.server_params.command)

    def make_mcp_server_parameters(self) -> StdioServerParameters:
        mcp_server_parameters = StdioServerParameters(
            command=self.server_params.command,
            args=self.server_params.args,
            env=self.server_params.env,
        )
        return mcp_server_parameters

    async def prepare_session(self) -> None:
        stdio_transport = await self.make_transport(self.exit_stack, self.make_mcp_server_parameters,)
        transport_read, transport_write = stdio_transport
        self.client_session = await self.exit_stack.enter_async_context(ClientSession(transport_read, transport_write))
        await self.client_session.initialize()
        return self.client_session