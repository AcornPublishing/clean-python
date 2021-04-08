# Import logging module
import logging

logger = logging.getLogger(__name__)          # Create a custom logger
handler = logging.StreamHandler()             # Using stream handler

# Set logging levels
logger.setLevel(logging.WARNING)
logger.setLevel(logging.ERROR)

format_c = logging.Formatter("%(name) - %(levelname) - %(message)")
handler.setFormatter(format_c)               # Add formater to handler
logger.addHandler(handler)

def division(divident, divisor):
    try:
        return divident/divisor
    except ZeroDivisionError:
        logger.error("Zero Division Error")

num = division(4, 0)
