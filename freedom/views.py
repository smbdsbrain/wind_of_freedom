import os
import uuid

from aioga import GA

GA_TRACKING_ID = os.getenv('GA_TRACKING_ID')


async def wind(request, wind):
    cid = uuid.uuid4()
    async with GA(GA_TRACKING_ID) as ga:
        ga.event(str(cid), ec='post', ea='post', ev=request.content_length)
    return wind
