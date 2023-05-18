import __main__
import modal.object
import typing
import typing_extensions

class _QueueHandle(modal.object._Handle):
    async def _get_nonblocking(self, n_values: int) -> typing.List[typing.Any]:
        ...

    async def _get_blocking(self, timeout: typing.Union[float, None], n_values: int) -> typing.List[typing.Any]:
        ...

    async def get(self, block: bool = True, timeout: typing.Union[float, None] = None) -> typing.Union[typing.Any, None]:
        ...

    async def get_many(self, n_values: int, block: bool = True, timeout: typing.Union[float, None] = None) -> typing.List[typing.Any]:
        ...

    async def put(self, v: typing.Any) -> None:
        ...

    async def put_many(self, vs: typing.List[typing.Any]) -> None:
        ...


class QueueHandle(modal.object.Handle):
    def __init__(self):
        ...

    class ___get_nonblocking_spec(typing_extensions.Protocol):
        def __call__(self, n_values: int) -> typing.List[typing.Any]:
            ...

        async def aio(self, *args, **kwargs) -> typing.List[typing.Any]:
            ...

    _get_nonblocking: ___get_nonblocking_spec

    class ___get_blocking_spec(typing_extensions.Protocol):
        def __call__(self, timeout: typing.Union[float, None], n_values: int) -> typing.List[typing.Any]:
            ...

        async def aio(self, *args, **kwargs) -> typing.List[typing.Any]:
            ...

    _get_blocking: ___get_blocking_spec

    class __get_spec(typing_extensions.Protocol):
        def __call__(self, block: bool = True, timeout: typing.Union[float, None] = None) -> typing.Union[typing.Any, None]:
            ...

        async def aio(self, *args, **kwargs) -> typing.Union[typing.Any, None]:
            ...

    get: __get_spec

    class __get_many_spec(typing_extensions.Protocol):
        def __call__(self, n_values: int, block: bool = True, timeout: typing.Union[float, None] = None) -> typing.List[typing.Any]:
            ...

        async def aio(self, *args, **kwargs) -> typing.List[typing.Any]:
            ...

    get_many: __get_many_spec

    class __put_spec(typing_extensions.Protocol):
        def __call__(self, v: typing.Any) -> None:
            ...

        async def aio(self, *args, **kwargs) -> None:
            ...

    put: __put_spec

    class __put_many_spec(typing_extensions.Protocol):
        def __call__(self, vs: typing.List[typing.Any]) -> None:
            ...

        async def aio(self, *args, **kwargs) -> None:
            ...

    put_many: __put_many_spec


class AioQueueHandle(modal.object.AioHandle):
    def __init__(self):
        ...

    async def _get_nonblocking(self, *args, **kwargs) -> typing.List[typing.Any]:
        ...

    async def _get_blocking(self, *args, **kwargs) -> typing.List[typing.Any]:
        ...

    async def get(self, *args, **kwargs) -> typing.Union[typing.Any, None]:
        ...

    async def get_many(self, *args, **kwargs) -> typing.List[typing.Any]:
        ...

    async def put(self, *args, **kwargs) -> None:
        ...

    async def put_many(self, *args, **kwargs) -> None:
        ...


class _Queue(modal.object._Provider[_QueueHandle]):
    def __init__(self):
        ...


class Queue(modal.object.Provider[QueueHandle]):
    def __init__(self):
        ...


class AioQueue(modal.object.AioProvider[AioQueueHandle]):
    def __init__(self):
        ...
