import __main__
import modal._resolver
import modal.object
import typing

class _ProxyHandle(modal.object._Handle):
    ...

class _Proxy(modal.object._Provider[_ProxyHandle]):
    ...

class ProxyHandle(modal.object.Handle):
    def __init__(self):
        ...


class AioProxyHandle(modal.object.AioHandle):
    def __init__(self):
        ...


class Proxy(modal.object.Provider[ProxyHandle]):
    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], modal.object._BLOCKING_H], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], modal.object._BLOCKING_H], None] = None):
        ...


class AioProxy(modal.object.AioProvider[AioProxyHandle]):
    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[modal.object._ASYNC_H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[modal.object._ASYNC_H]], None] = None):
        ...
