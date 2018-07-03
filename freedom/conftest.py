from pathlib import Path

import aioworkers_aiohttp
import pytest
from aioworkers.core.config import Config
from aioworkers.core.context import Context


@pytest.fixture
def config():
    plugin_config = Path(aioworkers_aiohttp.__file__).with_name('plugin.ini')
    app_config = Path(__file__).parent.with_name('config.yaml')
    config = Config().load(plugin_config, app_config)
    return config


@pytest.fixture
def context(loop, config):
    with Context(config, loop=loop) as ctx:
        yield ctx


@pytest.fixture
def app(context):
    return context.app


@pytest.fixture
def test_server(app):
    from aiohttp.test_utils import TestServer
    return TestServer(app)


@pytest.fixture
def anonym_client(app, test_client, test_server):
    client = app.loop.run_until_complete(test_client(test_server))
    return client
