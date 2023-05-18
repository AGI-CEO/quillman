import google.protobuf.message
import modal._resolver
import modal.client
import typing
import typing_extensions

H = typing.TypeVar("H", bound="_Handle")

_BLOCKING_H = typing.TypeVar("_BLOCKING_H", bound="Handle")

_ASYNC_H = typing.TypeVar("_ASYNC_H", bound="AioHandle")

class _Handle:
    _type_prefix: str

    def __init__(self):
        ...

    def _init(self):
        ...

    @classmethod
    def _new(cls: typing.Type[H]) -> H:
        ...

    def _initialize_from_empty(self):
        ...

    def _hydrate(self, client: modal.client._Client, object_id: str, handle_metadata: typing.Union[google.protobuf.message.Message, None]):
        ...

    def is_hydrated(self) -> bool:
        ...

    def _hydrate_metadata(self, handle_metadata: google.protobuf.message.Message):
        ...

    def _get_handle_metadata(self) -> typing.Union[google.protobuf.message.Message, None]:
        ...

    @classmethod
    def _from_id(cls: typing.Type[H], object_id: str, client: modal.client._Client, handle_metadata: typing.Union[google.protobuf.message.Message, None]) -> H:
        ...

    @classmethod
    async def from_id(cls: typing.Type[H], object_id: str, client: typing.Union[modal.client._Client, None] = None) -> H:
        ...

    @property
    def object_id(self) -> str:
        ...

    @classmethod
    async def from_app(cls: typing.Type[H], app_name: str, tag: typing.Union[str, None] = None, namespace=1, client: typing.Union[modal.client._Client, None] = None) -> H:
        ...


class Handle:
    _type_prefix: str

    def __init__(self):
        ...

    def _init(self):
        ...

    @classmethod
    def _new(cls: typing.Type[_BLOCKING_H]) -> _BLOCKING_H:
        ...

    def _initialize_from_empty(self):
        ...

    def _hydrate(self, client: modal.client.Client, object_id: str, handle_metadata: typing.Union[google.protobuf.message.Message, None]):
        ...

    def is_hydrated(self) -> bool:
        ...

    def _hydrate_metadata(self, handle_metadata: google.protobuf.message.Message):
        ...

    def _get_handle_metadata(self) -> typing.Union[google.protobuf.message.Message, None]:
        ...

    @classmethod
    def _from_id(cls: typing.Type[_BLOCKING_H], object_id: str, client: modal.client.Client, handle_metadata: typing.Union[google.protobuf.message.Message, None]) -> _BLOCKING_H:
        ...

    @classmethod
    def from_id(cls: typing.Type[_BLOCKING_H], object_id: str, client: typing.Union[modal.client.Client, None] = None) -> _BLOCKING_H:
        ...

    @property
    def object_id(self) -> str:
        ...

    @classmethod
    def from_app(cls: typing.Type[_BLOCKING_H], app_name: str, tag: typing.Union[str, None] = None, namespace=1, client: typing.Union[modal.client.Client, None] = None) -> _BLOCKING_H:
        ...


class AioHandle:
    _type_prefix: str

    def __init__(self):
        ...

    def _init(self):
        ...

    @classmethod
    def _new(cls: typing.Type[_ASYNC_H]) -> _ASYNC_H:
        ...

    def _initialize_from_empty(self):
        ...

    def _hydrate(self, client: modal.client.AioClient, object_id: str, handle_metadata: typing.Union[google.protobuf.message.Message, None]):
        ...

    def is_hydrated(self) -> bool:
        ...

    def _hydrate_metadata(self, handle_metadata: google.protobuf.message.Message):
        ...

    def _get_handle_metadata(self) -> typing.Union[google.protobuf.message.Message, None]:
        ...

    @classmethod
    def _from_id(cls: typing.Type[_ASYNC_H], object_id: str, client: modal.client.AioClient, handle_metadata: typing.Union[google.protobuf.message.Message, None]) -> _ASYNC_H:
        ...

    @classmethod
    async def from_id(*args, **kwargs) -> _ASYNC_H:
        ...

    @property
    def object_id(self) -> str:
        ...

    @classmethod
    async def from_app(*args, **kwargs) -> _ASYNC_H:
        ...


P = typing.TypeVar("P", bound="_Provider")

_BLOCKING_P = typing.TypeVar("_BLOCKING_P", bound="Provider")

_ASYNC_P = typing.TypeVar("_ASYNC_P", bound="AioProvider")

class _Provider(typing.Generic[H]):
    _load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]]
    _preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], None]

    def _init(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], None] = None):
        ...

    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], None] = None):
        ...

    def _init_from_other(self, other: _Provider):
        ...

    @classmethod
    def _from_loader(cls, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[H]], None] = None):
        ...

    @classmethod
    def _get_handle_cls(cls) -> typing.Type[H]:
        ...

    def __repr__(self):
        ...

    @property
    def local_uuid(self):
        ...

    async def _deploy(self, label: str, namespace=1, client: typing.Union[modal.client._Client, None] = None) -> H:
        ...

    def persist(self, label: str, namespace=1):
        ...

    @classmethod
    def from_name(cls: typing.Type[P], app_name: str, tag: typing.Union[str, None] = None, namespace=1) -> P:
        ...

    @classmethod
    async def lookup(cls: typing.Type[P], app_name: str, tag: typing.Union[str, None] = None, namespace=1, client: typing.Union[modal.client._Client, None] = None) -> H:
        ...

    @classmethod
    async def _exists(cls: typing.Type[P], app_name: str, tag: typing.Union[str, None] = None, namespace=1, client: typing.Union[modal.client._Client, None] = None) -> bool:
        ...


class Provider(typing.Generic[_BLOCKING_H]):
    _load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H]
    _preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], None]

    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], None] = None):
        ...

    class ___init_spec(typing_extensions.Protocol):
        def __call__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], None] = None):
            ...

        def aio(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_BLOCKING_H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_BLOCKING_H]], None] = None):
            ...

    _init: ___init_spec

    def _init_from_other(self, other: Provider):
        ...

    @classmethod
    def _from_loader(cls, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], _BLOCKING_H], None] = None):
        ...

    @classmethod
    def _get_handle_cls(cls) -> typing.Type[_BLOCKING_H]:
        ...

    def __repr__(self):
        ...

    @property
    def local_uuid(self):
        ...

    class ___deploy_spec(typing_extensions.Protocol):
        def __call__(self, label: str, namespace=1, client: typing.Union[modal.client.Client, None] = None) -> _BLOCKING_H:
            ...

        async def aio(self, *args, **kwargs) -> _BLOCKING_H:
            ...

    _deploy: ___deploy_spec

    def persist(self, label: str, namespace=1):
        ...

    @classmethod
    def from_name(cls: typing.Type[_BLOCKING_P], app_name: str, tag: typing.Union[str, None] = None, namespace=1) -> _BLOCKING_P:
        ...

    @classmethod
    def lookup(cls: typing.Type[_BLOCKING_P], app_name: str, tag: typing.Union[str, None] = None, namespace=1, client: typing.Union[modal.client.Client, None] = None) -> _BLOCKING_H:
        ...

    @classmethod
    def _exists(cls: typing.Type[_BLOCKING_P], app_name: str, tag: typing.Union[str, None] = None, namespace=1, client: typing.Union[modal.client.Client, None] = None) -> bool:
        ...


class AioProvider(typing.Generic[_ASYNC_H]):
    _load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]]
    _preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], None]

    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], None] = None):
        ...

    def _init(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], None] = None):
        ...

    def _init_from_other(self, other: AioProvider):
        ...

    @classmethod
    def _from_loader(cls, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[_ASYNC_H]], None] = None):
        ...

    @classmethod
    def _get_handle_cls(cls) -> typing.Type[_ASYNC_H]:
        ...

    def __repr__(self):
        ...

    @property
    def local_uuid(self):
        ...

    async def _deploy(self, *args, **kwargs) -> _ASYNC_H:
        ...

    def persist(self, label: str, namespace=1):
        ...

    @classmethod
    def from_name(cls: typing.Type[_ASYNC_P], app_name: str, tag: typing.Union[str, None] = None, namespace=1) -> _ASYNC_P:
        ...

    @classmethod
    async def lookup(*args, **kwargs) -> _ASYNC_H:
        ...

    @classmethod
    async def _exists(*args, **kwargs) -> bool:
        ...
