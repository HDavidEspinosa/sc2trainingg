# AUTOGENERATED! DO NOT EDIT! File to edit: 01_load_config.ipynb (unless otherwise specified).

__all__ = ['Config_settings', 'load_configurations']

# Cell
import os
import json
import jsonschema
import errno

from typing import Dict, Any
from dataclasses import dataclass
from jsonschema import validate
from pathlib import Path

# Cell
# Configuration of a frozen dataclass for the json file content
# to assure inmutability.
@dataclass(frozen=True)
class Config_settings:
    """

    ---

    Frozen `dataclass` that describes the configuration attributes of SC2 Training Grounds

    ---

    **Attributes:**
        *`port_adress (str)`:* address for the server running the MongoDB service
        *`port_number (int)`:* port number that indicates the proper service for the MongoDB service in the server.
        *`db_name (str)`:* name of the database that needs to be accessed
        *`replay_path (str)`:* path to the folder containing the SC2 replays to process. Use absolute path to prevent problems.
    """
    port_address: str
    port_number: int
    db_name: str
    replay_path: str

# Internal Cell
Config_schema = {
    "type": "object",
    "properties":{
        "DB_NAME": {"type":"string"},
        "STEP_MULT": {"type":"number"},
        "MATCH_UPS":  {"type":"array"},
        "SC2_PATH":  {"type":"string"},
        "PORT_ADDRESS":  {"type":"string"},
        "PORT_NUMBER": {"type":"number"},
        "REPLAY_PATH": {"type":"string"}
    }
}

def validate_config_file(file: Path, schema: Dict[str, Any]) -> bool:
    """Review if a given `file` Path fits a predefined `jsonschema`

    Args:
        file (Path): the path to the file that while ve validated.
        schema (Dict[str, Any]): the schema that the information needs to comply with.

    Returns:
        bool: `True` if the file complies with the schema, `False` otherwise.

    Raises:
        jsonschema.exceptions.SchemaError: The configuration schema is invalid.
    """

    try:
        validate(file, schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    except jsonschema.exceptions.SchemaError as err:
        print(err)
        print("The Config_schema is invalid")
        raise err

    return True

# Internal Cell
def open_config_file(config_path: Path) -> Dict[str, Any]:
    """Opens a json if it exists and matches a specific configuration schema.

    Args:
        config_path (Path): path to the session's `config.json`

    Returns:
        Dict[str, Any]: dictionary extracted from `config.json`.

    Raises:
        FileNotFoundError: in case `config_path` doesn't point to an existing file.
    """
    if (
        config_path.exists() and
        validate_config_file(json.load(config_path.open()), Config_schema)
    ):
        with config_path.open('r') as cf:
            return json.load(cf)
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)

# Cell
def load_configurations(config_path: Path) -> Config_settings:
    """
    ---

    Look for the project's `config.json` file in `config_path`, verifies that it contains the proper data and then returns a `Config_settings` object that contains the data.

    ----

    **Args:**
        *`config_path (Path)`:* path to the session's `config.json`

    **Returns:**
        *`Config_settings`:* frozen `dataclass` containing the data extracted from `config.json`.
    """
    config_dict = open_config_file(config_path)
    return Config_settings(
        config_dict['PORT_ADDRESS'],
        config_dict['PORT_NUMBER'],
        config_dict['DB_NAME'],
        config_dict['REPLAY_PATH']
    )