import pytest

from netsuite import Config


@pytest.fixture
def dummy_config():
    return Config(
        account="123456_SB1",
        auth={
            "consumer_key": "abcdefghijklmnopqrstuvwxyz0123456789",
            "consumer_secret": "abcdefghijklmnopqrstuvwxyz0123456789",
            "token_id": "abcdefghijklmnopqrstuvwxyz0123456789",
            "token_secret": "abcdefghijklmnopqrstuvwxyz0123456789",
        },
    )
