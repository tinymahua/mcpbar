from mcpbar.schema import ServerSchema, ServerType
from mcpbar.log import logger

"""
Base Runnable class and Base server class
"""

class BaseRunnable:
    def run(self):
        pass

class BaseServer:
    server_type: str
    def __init__(self, server_schema: ServerSchema):
        self.server_schema = server_schema
        if self.server_schema.server_type != self.server_type:
            raise ValueError(f"Server type {self.server_schema.server_type} not match {self.server_type}")

    def get_runnable(self) -> BaseRunnable:
        raise NotImplemented

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
            interpreter=self.server_schema.server_params.interpreter,
            path=self.server_schema.server_params.path)

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
        return LocalRunnableJs(path=self.server_schema.server_params.path)
