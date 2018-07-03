import aioworkers_aiohttp.app


class Application(aioworkers_aiohttp.app.Application):
    def __init__(self, config, *, context, **kwargs):
        super(Application, self).__init__(config, debug=config.debug, context=context, **kwargs)
