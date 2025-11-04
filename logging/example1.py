import logging
import sys

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

print(logger)


# Create a handler for standard output (console)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Create a handler for the file
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(logging.INFO)

# Define a formatter (optional, but good practice)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Now, use the logger to write messages
logger.info("This message goes to both console and file.")
logger.warning("A warning message.")