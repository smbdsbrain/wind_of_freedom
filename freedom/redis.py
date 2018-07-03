import logging
import os

import aioworkers_redis.base


class Connector(aioworkers_redis.base.Connector):
    async def init(self):
        # 💩 Patch config
        redis_host = os.getenv('REDIS_HOST')
        if redis_host:
            logging.info(f"Set redis config: {redis_host}")
            self.config.connection = {
                'host': redis_host,
            }
        return await super().init()
