from pathlib import Path

from loguru import logger

LOG_PATH: Path = Path("logs/main.py")

if __name__ == "__main__":
    """."""
    logger.add(
        LOG_PATH,
        format="{time:YYYY-MM-DD - HH:mm!UTC} {level} {message}",
        colorize=True,
        level="INFO",
    )
    logger.info("-" * 80)

    # TODO: write a class for this or something
    logger.info("step_1")  # TODO: add colors to module rows
    # step_1()
    ...
