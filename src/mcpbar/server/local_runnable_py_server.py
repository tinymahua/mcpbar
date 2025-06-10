from mcpbar.base import BaseServer, BaseRunnable
from mcpbar.schema.server_schema import ServerType
from mcpbar.log import logger

"""
Local Runnable Py and Server
"""

class LocalRunnablePy(BaseRunnable):
    def __init__(self, interpreter: str, path: str):
        self.interpreter = interpreter
        self.path = path

    def run(self):
        logger.debug(f'Use python interpreter: {self.interpreter}')
        logger.debug(f"Run {self.path}")


class LocalRunnablePyServer(BaseServer):
    server_type = ServerType.LOCAL_RUNNABLE_PY.name

    def get_runnable(self) -> LocalRunnablePy:
        return LocalRunnablePy(
            interpreter=self.server_params.interpreter,
            path=self.server_params.path)