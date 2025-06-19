from mcpbar.base import BaseServer, BaseRunnable
from mcpbar.schema.server_schema import ServerType, ServerSchema
from mcpbar.log import logger
from mcp import ClientSession, StdioServerParameters
from mcpbar.schema.server_schema import LocalRunnablePyParams
from mcpbar.server.server_transports import StdioTransportServerMixin
from typing import List
import pathlib
from subprocess import getstatusoutput
import os



"""
Local Runnable Py and Server
"""

class LocalRunnablePy(BaseRunnable):
    def __init__(self, command: str, args: List[str]):
        super().__init__()
        self.command = command
        self.args = args

    def run(self):
        logger.debug(f'Use python command: {self.command}')
        logger.debug(f"Run {self.args}")


class LocalRunnablePyServer(BaseServer, StdioTransportServerMixin):
    server_type = ServerType.LOCAL_RUNNABLE_PY.name

    def __init__(self, server_schema: ServerSchema, server_params_schema:  type[LocalRunnablePyParams]):
        super().__init__(server_schema, server_params_schema)

    def get_runnable(self) -> LocalRunnablePy:
        return LocalRunnablePy(
            command=self.server_params.command,
            args=self.server_params.args)

    def make_mcp_server_parameters(self) -> StdioServerParameters:
        command = self.init_runtime_env()

        mcp_server_parameters = StdioServerParameters(
            command=command,
            args=self.server_params.args,
            env=self.server_params.env,
        )
        print(f'server_params2: {mcp_server_parameters}')
        return mcp_server_parameters

    def init_runtime_env(self) -> str:
        correct_project_root = None
        server_script = self.server_params.args[-1]
        server_project_root = pathlib.Path(server_script).parent
        while True:
            if server_project_root.joinpath('pyproject.toml').exists():
                correct_project_root = server_project_root
                break
            server_project_root = server_project_root.parent

        if correct_project_root is None:
            raise Exception(f'Can not find pyproject.toml for {server_script}')

        uv_sync_cmd = f'uv sync --project {correct_project_root}'
        logger.debug(f'Run {uv_sync_cmd}')
        status, output = getstatusoutput(uv_sync_cmd)
        if status != 0:
            raise Exception(f'Can not sync project {correct_project_root}: {output}')
        logger.debug(f'Sync project {correct_project_root} done')
        if os.name == 'nt':
            return correct_project_root.joinpath(*['.venv', 'Scripts', 'mcp.exe']).__str__()
        else:
            return correct_project_root.joinpath(*['.venv', 'bin', 'mcp']).__str__()

    async def prepare_session(self) -> ClientSession:
        stdio_transport = await self.make_transport(self.exit_stack, self.make_mcp_server_parameters)
        transport_read, transport_write = stdio_transport
        self.client_session = await self.exit_stack.enter_async_context(ClientSession(transport_read, transport_write))
        print(00)
        await self.client_session.initialize()
        return self.client_session