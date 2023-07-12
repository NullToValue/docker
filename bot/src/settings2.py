import logging
import os
from dotenv import load_dotenv

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.WARNING)
load_dotenv()

print(os.environ)