import __main__
import modal.object
import typing

class _SecretHandle(modal.object._Handle):
    ...

class SecretHandle(modal.object.Handle):
    def __init__(self):
        ...


class AioSecretHandle(modal.object.AioHandle):
    def __init__(self):
        ...


class _Secret(modal.object._Provider[_SecretHandle]):
    @staticmethod
    def from_dict(env_dict: typing.Dict[str, str] = {}, template_type=''):
        ...

    def __init__(self, env_dict: typing.Dict[str, str]):
        ...

    @staticmethod
    def from_dotenv(path=None):
        ...


class Secret(modal.object.Provider[SecretHandle]):
    def __init__(self, env_dict: typing.Dict[str, str]):
        ...

    @staticmethod
    def from_dict(env_dict: typing.Dict[str, str] = {}, template_type=''):
        ...

    @staticmethod
    def from_dotenv(path=None):
        ...


class AioSecret(modal.object.AioProvider[AioSecretHandle]):
    def __init__(self, env_dict: typing.Dict[str, str]):
        ...

    @staticmethod
    def from_dict(env_dict: typing.Dict[str, str] = {}, template_type=''):
        ...

    @staticmethod
    def from_dotenv(path=None):
        ...
