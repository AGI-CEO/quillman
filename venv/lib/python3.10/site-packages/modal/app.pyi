import modal._resolver
import modal.client
import modal.object
import typing
import typing_extensions

Tree = typing.TypeVar("Tree")

class _App:
    _tag_to_object: typing.Dict[str, modal.object._Handle]
    _tag_to_existing_id: typing.Dict[str, str]
    _client: modal.client._Client
    _app_id: str
    _app_page_url: str
    _resolver: typing.Union[modal._resolver.Resolver, None]
    _function_invocations: int

    def __init__(self, client: modal.client._Client, app_id: str, app_page_url: str, tag_to_object: typing.Union[typing.Dict[str, modal.object._Handle], None] = None, tag_to_existing_id: typing.Union[typing.Dict[str, str], None] = None, stub_name: typing.Union[str, None] = None):
        ...

    @property
    def client(self) -> modal.client._Client:
        ...

    @property
    def app_id(self) -> str:
        ...

    async def _create_all_objects(self, blueprint: typing.Dict[str, modal.object._Provider], output_mgr, new_app_state: int):
        ...

    async def disconnect(self):
        ...

    async def stop(self):
        ...

    def log_url(self):
        ...

    def __getitem__(self, tag: str) -> modal.object._Handle:
        ...

    def __getattr__(self, tag: str) -> modal.object._Handle:
        ...

    def track_function_invocation(self):
        ...

    @property
    def function_invocations(self):
        ...

    async def _init_container(self, client: modal.client._Client, app_id: str, stub_name: str):
        ...

    @staticmethod
    async def init_container(client: modal.client._Client, app_id: str, stub_name: str = '') -> _App:
        ...

    @staticmethod
    async def _init_existing(client: modal.client._Client, existing_app_id: str) -> _App:
        ...

    @staticmethod
    async def _init_new(client: modal.client._Client, description: typing.Union[str, None] = None, detach: bool = False, deploying: bool = False) -> _App:
        ...

    @staticmethod
    async def _init_from_name(client: modal.client._Client, name: str, namespace):
        ...

    async def create_one_object(self, provider: modal.object._Provider) -> modal.object._Handle:
        ...

    async def deploy(self, name: str, namespace, object_entity: str) -> str:
        ...

    @staticmethod
    def _reset_container():
        ...


class App:
    _tag_to_object: typing.Dict[str, modal.object.Handle]
    _tag_to_existing_id: typing.Dict[str, str]
    _client: modal.client.Client
    _app_id: str
    _app_page_url: str
    _resolver: typing.Union[modal._resolver.Resolver, None]
    _function_invocations: int

    def __init__(self, client: modal.client.Client, app_id: str, app_page_url: str, tag_to_object: typing.Union[typing.Dict[str, modal.object.Handle], None] = None, tag_to_existing_id: typing.Union[typing.Dict[str, str], None] = None, stub_name: typing.Union[str, None] = None):
        ...

    @property
    def client(self) -> modal.client.Client:
        ...

    @property
    def app_id(self) -> str:
        ...

    class ___create_all_objects_spec(typing_extensions.Protocol):
        def __call__(self, blueprint: typing.Dict[str, modal.object.Provider], output_mgr, new_app_state: int):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _create_all_objects: ___create_all_objects_spec

    class __disconnect_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    disconnect: __disconnect_spec

    class __stop_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    stop: __stop_spec

    def log_url(self):
        ...

    def __getitem__(self, tag: str) -> modal.object.Handle:
        ...

    def __getattr__(self, tag: str) -> modal.object.Handle:
        ...

    def track_function_invocation(self):
        ...

    @property
    def function_invocations(self):
        ...

    class ___init_container_spec(typing_extensions.Protocol):
        def __call__(self, client: modal.client.Client, app_id: str, stub_name: str):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _init_container: ___init_container_spec

    class __init_container_spec(typing_extensions.Protocol):
        def __call__(self, client: modal.client.Client, app_id: str, stub_name: str = '') -> App:
            ...

        async def aio(self, *args, **kwargs) -> App:
            ...

    init_container: __init_container_spec

    class ___init_existing_spec(typing_extensions.Protocol):
        def __call__(self, client: modal.client.Client, existing_app_id: str) -> App:
            ...

        async def aio(self, *args, **kwargs) -> App:
            ...

    _init_existing: ___init_existing_spec

    class ___init_new_spec(typing_extensions.Protocol):
        def __call__(self, client: modal.client.Client, description: typing.Union[str, None] = None, detach: bool = False, deploying: bool = False) -> App:
            ...

        async def aio(self, *args, **kwargs) -> App:
            ...

    _init_new: ___init_new_spec

    class ___init_from_name_spec(typing_extensions.Protocol):
        def __call__(self, client: modal.client.Client, name: str, namespace):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _init_from_name: ___init_from_name_spec

    class __create_one_object_spec(typing_extensions.Protocol):
        def __call__(self, provider: modal.object.Provider) -> modal.object.Handle:
            ...

        async def aio(self, *args, **kwargs) -> modal.object.Handle:
            ...

    create_one_object: __create_one_object_spec

    class __deploy_spec(typing_extensions.Protocol):
        def __call__(self, name: str, namespace, object_entity: str) -> str:
            ...

        async def aio(self, *args, **kwargs) -> str:
            ...

    deploy: __deploy_spec

    @staticmethod
    def _reset_container():
        ...


class AioApp:
    _tag_to_object: typing.Dict[str, modal.object.AioHandle]
    _tag_to_existing_id: typing.Dict[str, str]
    _client: modal.client.AioClient
    _app_id: str
    _app_page_url: str
    _resolver: typing.Union[modal._resolver.Resolver, None]
    _function_invocations: int

    def __init__(self, client: modal.client.AioClient, app_id: str, app_page_url: str, tag_to_object: typing.Union[typing.Dict[str, modal.object.AioHandle], None] = None, tag_to_existing_id: typing.Union[typing.Dict[str, str], None] = None, stub_name: typing.Union[str, None] = None):
        ...

    @property
    def client(self) -> modal.client.AioClient:
        ...

    @property
    def app_id(self) -> str:
        ...

    async def _create_all_objects(self, *args, **kwargs):
        ...

    async def disconnect(self, *args, **kwargs):
        ...

    async def stop(self, *args, **kwargs):
        ...

    def log_url(self):
        ...

    def __getitem__(self, tag: str) -> modal.object.AioHandle:
        ...

    def __getattr__(self, tag: str) -> modal.object.AioHandle:
        ...

    def track_function_invocation(self):
        ...

    @property
    def function_invocations(self):
        ...

    async def _init_container(self, *args, **kwargs):
        ...

    @staticmethod
    async def init_container(*args, **kwargs) -> AioApp:
        ...

    @staticmethod
    async def _init_existing(*args, **kwargs) -> AioApp:
        ...

    @staticmethod
    async def _init_new(*args, **kwargs) -> AioApp:
        ...

    @staticmethod
    async def _init_from_name(*args, **kwargs):
        ...

    async def create_one_object(self, *args, **kwargs) -> modal.object.AioHandle:
        ...

    async def deploy(self, *args, **kwargs) -> str:
        ...

    @staticmethod
    def _reset_container():
        ...


_container_app: _App

container_app: App

aio_container_app: AioApp

def is_local() -> bool:
    ...
