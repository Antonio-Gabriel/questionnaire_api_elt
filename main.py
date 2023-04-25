import uvicorn, typer, asyncio
from src.main import main_pipeline
from src.main.server import app

typer_cli = typer.Typer()

@typer_cli.command("server")
def http_server():
    """start appication server"""
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")


@typer_cli.command("pipeline")
def run_pipeline():
    """start pipeline process"""
    asyncio.run(main_pipeline.run_pipeline())


if __name__ == "__main__":
    typer_cli()
