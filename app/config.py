# !!START
# imports the os module, which provides a portable way to interact with the operating system.
import os
#using environment variables for sensitive configuration values like the secret key, you can keep this information out of your source code and configuration files. 
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # define any other secret environment variables here

# !!END
