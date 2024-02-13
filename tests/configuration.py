import json
import pathlib


def get_configuration():
    """Read env_configuration.json and make it a dictionary"""
    current_path = pathlib.Path(__file__)

    with open(current_path.parent.parent / "env_configuration.json") as c:
        config = c.read()
        configuration = json.loads(config)

    return configuration
