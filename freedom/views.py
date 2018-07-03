import os
import uuid

from aioga import GA

GA_TRACKING_ID = os.getenv('GA_TRACKING_ID')


async def wind(request, wind):
    cid = uuid.uuid4()
    size = 10
    async with GA(GA_TRACKING_ID) as ga:
        ga.event(str(cid), ec='post', ea='post', ev=size)
