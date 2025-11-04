import logging
import pprint

# --- Logger for formatted log files ---
file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.DEBUG)

# File handler for structured logs
file_handler = logging.FileHandler('application.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)

# --- Logger for pretty-printed console output ---
console_logger = logging.getLogger('console_logger')
console_logger.setLevel(logging.INFO)

# Console handler for pretty-printed output
console_handler = logging.StreamHandler()

# Custom formatter for pretty printing (e.g., using pprint for data structures)
class PrettyPrintFormatter(logging.Formatter):
    def format(self, record):
        # Format the basic log message
        formatted_message = super().format(record)
        # If the message contains a dictionary or list, pretty-print it
        if isinstance(record.msg, (dict, list)):
            return f"{record.levelname}: {pprint.pformat(record.msg)}"
        return formatted_message

console_formatter = PrettyPrintFormatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)
console_logger.addHandler(console_handler)

# --- Usage ---
file_logger.info("This is an informational message for the log file.")
file_logger.debug("Debug information for the log file: %s", {"data": "some_value", "id": 123})

console_logger.info("Starting application...")
console_logger.debug("This debug message won't appear in the console output (due to level).")
console_logger.info({"user": "john.doe", "action": "login", "status": "success"})
console_logger.warning("A warning message for the console.")