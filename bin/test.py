import sys
import pathlib


sys.path.insert(0, pathlib.Path(__file__).parent.parent.joinpath('src').__str__())


from mcpbar.schema import ServerSchema
from mcpbar.schema import ServerType

s = ServerSchema()