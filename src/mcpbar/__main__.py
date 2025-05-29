from mcpbar.log import logger
import typer


app = typer.Typer(name="mcpbar")

@app.command()
def run_test():
    logger.info("Run test OK")

@app.command()
def run_server():
    logger.info("Run server")


def main():
    app()
