import socket
import asyncio
import time
import random
import json
import pydig

from walkoff_app_sdk.app_base import AppBase

class Tools(AppBase):
    """
    An example of a Walkoff App.
    Inherit from the AppBase class to have Redis, logging, and console logging set up behind the scenes.
    """
    __version__ = "1.0.0"
    app_name = "Jack Test"  # this needs to match "name" in api.yaml for WALKOFF to work

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)


    async def ret_str(self, item):
        dns=pydig.query('google.com', 'A')
        return str(dns[0])

if __name__ == "__main__":
    asyncio.run(Tools.run(), debug=True)
