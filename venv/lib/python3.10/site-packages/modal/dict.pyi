import __main__
import modal.object
import typing
import typing_extensions

def _serialize_dict(data):
    ...


class _DictHandle(modal.object._Handle):
    async def get(self, key: typing.Any) -> typing.Any:
        ...

    async def contains(self, key: typing.Any) -> bool:
        ...

    async def len(self) -> int:
        ...

    async def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    async def update(self, **kwargs) -> None:
        ...

    async def put(self, key: typing.Any, value: typing.Any) -> None:
        ...

    async def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    async def pop(self, key: typing.Any) -> typing.Any:
        ...

    async def __delitem__(self, key: typing.Any) -> typing.Any:
        ...

    async def __contains__(self, key: typing.Any) -> bool:
        ...


class DictHandle(modal.object.Handle):
    def __init__(self):
        ...

    class __get_spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any) -> typing.Any:
            ...

        async def aio(self, *args, **kwargs) -> typing.Any:
            ...

    get: __get_spec

    class __contains_spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any) -> bool:
            ...

        async def aio(self, *args, **kwargs) -> bool:
            ...

    contains: __contains_spec

    class __len_spec(typing_extensions.Protocol):
        def __call__(self) -> int:
            ...

        async def aio(self, *args, **kwargs) -> int:
            ...

    len: __len_spec

    class ____getitem___spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any) -> typing.Any:
            ...

        async def aio(self, *args, **kwargs) -> typing.Any:
            ...

    __getitem__: ____getitem___spec

    class __update_spec(typing_extensions.Protocol):
        def __call__(self, **kwargs) -> None:
            ...

        async def aio(self, *args, **kwargs) -> None:
            ...

    update: __update_spec

    class __put_spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any, value: typing.Any) -> None:
            ...

        async def aio(self, *args, **kwargs) -> None:
            ...

    put: __put_spec

    class ____setitem___spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any, value: typing.Any) -> None:
            ...

        async def aio(self, *args, **kwargs) -> None:
            ...

    __setitem__: ____setitem___spec

    class __pop_spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any) -> typing.Any:
            ...

        async def aio(self, *args, **kwargs) -> typing.Any:
            ...

    pop: __pop_spec

    class ____delitem___spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any) -> typing.Any:
            ...

        async def aio(self, *args, **kwargs) -> typing.Any:
            ...

    __delitem__: ____delitem___spec

    class ____contains___spec(typing_extensions.Protocol):
        def __call__(self, key: typing.Any) -> bool:
            ...

        async def aio(self, *args, **kwargs) -> bool:
            ...

    __contains__: ____contains___spec


class AioDictHandle(modal.object.AioHandle):
    def __init__(self):
        ...

    async def get(self, *args, **kwargs) -> typing.Any:
        ...

    async def contains(self, *args, **kwargs) -> bool:
        ...

    async def len(self, *args, **kwargs) -> int:
        ...

    async def __getitem__(self, *args, **kwargs) -> typing.Any:
        ...

    async def update(self, *args, **kwargs) -> None:
        ...

    async def put(self, *args, **kwargs) -> None:
        ...

    async def __setitem__(self, *args, **kwargs) -> None:
        ...

    async def pop(self, *args, **kwargs) -> typing.Any:
        ...

    async def __delitem__(self, *args, **kwargs) -> typing.Any:
        ...

    async def __contains__(self, *args, **kwargs) -> bool:
        ...


class _Dict(modal.object._Provider[_DictHandle]):
    def __init__(self, data={}):
        ...


class Dict(modal.object.Provider[DictHandle]):
    def __init__(self, data={}):
        ...


class AioDict(modal.object.AioProvider[AioDictHandle]):
    def __init__(self, data={}):
        ...
