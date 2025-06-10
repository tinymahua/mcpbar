from mcpbar.schema.server_schema import ServerType
from mcpbar.base import BaseServer, BaseRunnable
from mcpbar.log import logger
from mcpbar.schema.server_schema import LocalRunnableJsParams

"""
Local Runnable Js and Server
"""

class LocalRunnableJs(BaseRunnable):
    def __init__(self, path: str):
        self.path = path

    def run(self):
        logger.debug(f"Run {self.path}")



class LocalRunnableJsServer(BaseServer):
    server_type = ServerType.LOCAL_RUNNABLE_JS.name

    def get_runnable(self) -> LocalRunnableJs:
        return LocalRunnableJs(path=self.server_params.path)
