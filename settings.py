# settings.py
import os
from dotenv import load_dotenv
#load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

print( os.getenv('CONNECTION_STRING'))