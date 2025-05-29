import sys
import pathlib


sys.path.insert(0, pathlib.Path(__file__).parent.parent.joinpath('src').__str__())


from mcpbar.__main__ import main

if __name__ == '__main__':
    main()