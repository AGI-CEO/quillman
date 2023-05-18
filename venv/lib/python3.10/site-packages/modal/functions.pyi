import __main__
import google.protobuf.message
import inspect
import modal._function_utils
import modal._output
import modal._resolver
import modal.call_graph
import modal.client
import modal.gpu
import modal.image
import modal.mount
import modal.object
import modal.proxy
import modal.retries
import modal.schedule
import modal.secret
import modal.shared_volume
import modal.stub
import modal_proto.api_pb2
import os
import typing
import typing_extensions

def exc_with_hints(exc: BaseException):
    ...


async def _process_result(result, stub, client=None):
    ...


async def _create_input(args, kwargs, client, idx=None) -> modal_proto.api_pb2.FunctionPutInputsItem:
    ...


class _OutputValue:
    value: typing.Any

    def __init__(self, value: typing.Any) -> None:
        ...

    def __repr__(self):
        ...

    def __eq__(self, other):
        ...


class _Invocation:
    def __init__(self, stub, function_call_id, client=None):
        ...

    @staticmethod
    async def create(function_id, args, kwargs, client):
        ...

    def pop_function_call_outputs(self, timeout: typing.Union[float, None], clear_on_success: bool):
        ...

    async def run_function(self):
        ...

    async def poll_function(self, timeout: typing.Union[float, None] = None):
        ...

    def run_generator(self):
        ...


def _map_invocation(function_id: str, input_stream: typing.AsyncIterable[typing.Any], kwargs: typing.Dict[str, typing.Any], client: modal.client._Client, is_generator: bool, order_outputs: bool, return_exceptions: bool, count_update_callback: typing.Union[typing.Callable[[int, int], None], None]):
    ...


class FunctionStats:
    backlog: int
    num_active_runners: int
    num_total_runners: int

    def __init__(self, backlog: int, num_active_runners: int, num_total_runners: int) -> None:
        ...

    def __repr__(self):
        ...

    def __eq__(self, other):
        ...


class _FunctionHandle(modal.object._Handle):
    _web_url: typing.Union[str, None]
    _info: typing.Union[modal._function_utils.FunctionInfo, None]
    _stub: typing.Union[modal.stub._Stub, None]
    _is_remote_cls_method: bool
    _function_name: typing.Union[str, None]

    def _initialize_from_empty(self):
        ...

    def _initialize_from_local(self, stub, info: modal._function_utils.FunctionInfo):
        ...

    def _hydrate_metadata(self, handle_metadata: google.protobuf.message.Message):
        ...

    async def make_bound_function_handle(self, params: inspect.BoundArguments) -> _FunctionHandle:
        ...

    def _get_handle_metadata(self):
        ...

    def _set_mute_cancellation(self, value: bool = True):
        ...

    def _set_output_mgr(self, output_mgr: modal._output.OutputManager):
        ...

    def _get_function(self) -> _Function:
        ...

    @property
    def web_url(self) -> str:
        ...

    @property
    def is_generator(self) -> bool:
        ...

    def _track_function_invocation(self):
        ...

    def _map(self, input_stream: typing.AsyncIterable[typing.Any], order_outputs: bool, return_exceptions: bool, kwargs={}):
        ...

    def map(self, *input_iterators, kwargs={}, order_outputs=None, return_exceptions=False) -> typing.AsyncGenerator[typing.Any, None]:
        ...

    async def for_each(self, *input_iterators, kwargs={}, ignore_exceptions=False):
        ...

    def starmap(self, input_iterator, kwargs={}, order_outputs=None, return_exceptions=False):
        ...

    async def _call_function(self, args, kwargs):
        ...

    async def _call_function_nowait(self, args, kwargs):
        ...

    def _call_generator(self, args, kwargs):
        ...

    async def _call_generator_nowait(self, args, kwargs):
        ...

    def call(self, *args, **kwargs) -> typing.Awaitable[typing.Any]:
        ...

    def __call__(self, *args, **kwargs) -> typing.Any:
        ...

    async def spawn(self, *args, **kwargs) -> typing.Union[_FunctionCall, None]:
        ...

    def get_raw_f(self) -> typing.Callable[..., typing.Any]:
        ...

    async def get_current_stats(self) -> FunctionStats:
        ...

    def bind_obj(self, obj, objtype) -> _FunctionHandle:
        ...

    def __get__(self, obj, objtype=None) -> _FunctionHandle:
        ...


class FunctionHandle(modal.object.Handle):
    _web_url: typing.Union[str, None]
    _info: typing.Union[modal._function_utils.FunctionInfo, None]
    _stub: typing.Union[modal.stub.Stub, None]
    _is_remote_cls_method: bool
    _function_name: typing.Union[str, None]

    def __init__(self):
        ...

    def _initialize_from_empty(self):
        ...

    def _initialize_from_local(self, stub, info: modal._function_utils.FunctionInfo):
        ...

    def _hydrate_metadata(self, handle_metadata: google.protobuf.message.Message):
        ...

    class __make_bound_function_handle_spec(typing_extensions.Protocol):
        def __call__(self, params: inspect.BoundArguments) -> FunctionHandle:
            ...

        async def aio(self, *args, **kwargs) -> FunctionHandle:
            ...

    make_bound_function_handle: __make_bound_function_handle_spec

    def _get_handle_metadata(self):
        ...

    def _set_mute_cancellation(self, value: bool = True):
        ...

    def _set_output_mgr(self, output_mgr: modal._output.OutputManager):
        ...

    def _get_function(self) -> Function:
        ...

    @property
    def web_url(self) -> str:
        ...

    @property
    def is_generator(self) -> bool:
        ...

    def _track_function_invocation(self):
        ...

    class ___map_spec(typing_extensions.Protocol):
        def __call__(self, input_stream: typing.Iterable[typing.Any], order_outputs: bool, return_exceptions: bool, kwargs={}):
            ...

        def aio(self, input_stream: typing.AsyncIterable[typing.Any], order_outputs: bool, return_exceptions: bool, kwargs={}):
            ...

    _map: ___map_spec

    class __map_spec(typing_extensions.Protocol):
        def __call__(self, *input_iterators, kwargs={}, order_outputs=None, return_exceptions=False) -> typing.Generator[typing.Any, None, None]:
            ...

        def aio(self, *input_iterators, kwargs={}, order_outputs=None, return_exceptions=False) -> typing.AsyncGenerator[typing.Any, None]:
            ...

    map: __map_spec

    class __for_each_spec(typing_extensions.Protocol):
        def __call__(self, *input_iterators, kwargs={}, ignore_exceptions=False):
            ...

        async def aio(self, *args, **kwargs):
            ...

    for_each: __for_each_spec

    def starmap(self, input_iterator, kwargs={}, order_outputs=None, return_exceptions=False):
        ...

    class ___call_function_spec(typing_extensions.Protocol):
        def __call__(self, args, kwargs):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _call_function: ___call_function_spec

    class ___call_function_nowait_spec(typing_extensions.Protocol):
        def __call__(self, args, kwargs):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _call_function_nowait: ___call_function_nowait_spec

    def _call_generator(self, args, kwargs):
        ...

    class ___call_generator_nowait_spec(typing_extensions.Protocol):
        def __call__(self, args, kwargs):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _call_generator_nowait: ___call_generator_nowait_spec

    class __call_spec(typing_extensions.Protocol):
        def __call__(self, *args, **kwargs) -> typing.Any:
            ...

        def aio(self, *args, **kwargs) -> typing.Awaitable[typing.Any]:
            ...

    call: __call_spec

    def __call__(self, *args, **kwargs) -> typing.Any:
        ...

    class __spawn_spec(typing_extensions.Protocol):
        def __call__(self, *args, **kwargs) -> typing.Union[FunctionCall, None]:
            ...

        async def aio(self, *args, **kwargs) -> typing.Union[FunctionCall, None]:
            ...

    spawn: __spawn_spec

    def get_raw_f(self) -> typing.Callable[..., typing.Any]:
        ...

    class __get_current_stats_spec(typing_extensions.Protocol):
        def __call__(self) -> FunctionStats:
            ...

        async def aio(self, *args, **kwargs) -> FunctionStats:
            ...

    get_current_stats: __get_current_stats_spec

    def bind_obj(self, obj, objtype) -> FunctionHandle:
        ...

    def __get__(self, obj, objtype=None) -> FunctionHandle:
        ...


class AioFunctionHandle(modal.object.AioHandle):
    _web_url: typing.Union[str, None]
    _info: typing.Union[modal._function_utils.FunctionInfo, None]
    _stub: typing.Union[modal.stub.AioStub, None]
    _is_remote_cls_method: bool
    _function_name: typing.Union[str, None]

    def __init__(self):
        ...

    def _initialize_from_empty(self):
        ...

    def _initialize_from_local(self, stub, info: modal._function_utils.FunctionInfo):
        ...

    def _hydrate_metadata(self, handle_metadata: google.protobuf.message.Message):
        ...

    async def make_bound_function_handle(self, *args, **kwargs) -> AioFunctionHandle:
        ...

    def _get_handle_metadata(self):
        ...

    def _set_mute_cancellation(self, value: bool = True):
        ...

    def _set_output_mgr(self, output_mgr: modal._output.OutputManager):
        ...

    def _get_function(self) -> AioFunction:
        ...

    @property
    def web_url(self) -> str:
        ...

    @property
    def is_generator(self) -> bool:
        ...

    def _track_function_invocation(self):
        ...

    def _map(self, input_stream: typing.AsyncIterable[typing.Any], order_outputs: bool, return_exceptions: bool, kwargs={}):
        ...

    def map(self, *input_iterators, kwargs={}, order_outputs=None, return_exceptions=False) -> typing.AsyncGenerator[typing.Any, None]:
        ...

    async def for_each(self, *args, **kwargs):
        ...

    def starmap(self, input_iterator, kwargs={}, order_outputs=None, return_exceptions=False):
        ...

    async def _call_function(self, *args, **kwargs):
        ...

    async def _call_function_nowait(self, *args, **kwargs):
        ...

    def _call_generator(self, args, kwargs):
        ...

    async def _call_generator_nowait(self, *args, **kwargs):
        ...

    def call(self, *args, **kwargs) -> typing.Awaitable[typing.Any]:
        ...

    def __call__(self, *args, **kwargs) -> typing.Any:
        ...

    async def spawn(self, *args, **kwargs) -> typing.Union[AioFunctionCall, None]:
        ...

    def get_raw_f(self) -> typing.Callable[..., typing.Any]:
        ...

    async def get_current_stats(self, *args, **kwargs) -> FunctionStats:
        ...

    def bind_obj(self, obj, objtype) -> AioFunctionHandle:
        ...

    def __get__(self, obj, objtype=None) -> AioFunctionHandle:
        ...


class _Function(modal.object._Provider[_FunctionHandle]):
    _secrets: typing.Collection[modal.secret._Secret]
    _info: modal._function_utils.FunctionInfo
    _mounts: typing.Collection[modal.mount._Mount]
    _shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.shared_volume._SharedVolume]
    _allow_cross_region_volumes: bool
    _image: typing.Union[modal.image._Image, None]
    _gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig]
    _cloud: typing.Union[str, None]
    _function_handle: _FunctionHandle
    _stub: modal.stub._Stub
    _is_builder_function: bool
    _retry_policy: typing.Union[modal_proto.api_pb2.FunctionRetryPolicy, None]

    @staticmethod
    def from_args(function_handle: _FunctionHandle, info: modal._function_utils.FunctionInfo, stub, image=None, secret: typing.Union[modal.secret._Secret, None] = None, secrets: typing.Collection[modal.secret._Secret] = (), schedule: typing.Union[modal.schedule.Schedule, None] = None, is_generator=False, gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, mounts: typing.Collection[modal.mount._Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.shared_volume._SharedVolume] = {}, allow_cross_region_volumes: bool = False, webhook_config: typing.Union[modal_proto.api_pb2.WebhookConfig, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy._Proxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, timeout: typing.Union[int, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, cpu: typing.Union[float, None] = None, keep_warm: typing.Union[int, None] = None, interactive: bool = False, name: typing.Union[str, None] = None, cloud: typing.Union[str, None] = None, is_builder_function: bool = False, cls: typing.Union[type, None] = None) -> None:
        ...

    def get_panel_items(self) -> typing.List[str]:
        ...

    @property
    def tag(self):
        ...

    def get_build_def(self):
        ...


class Function(modal.object.Provider[FunctionHandle]):
    _secrets: typing.Collection[modal.secret.Secret]
    _info: modal._function_utils.FunctionInfo
    _mounts: typing.Collection[modal.mount.Mount]
    _shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.shared_volume.SharedVolume]
    _allow_cross_region_volumes: bool
    _image: typing.Union[modal.image.Image, None]
    _gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig]
    _cloud: typing.Union[str, None]
    _function_handle: FunctionHandle
    _stub: modal.stub.Stub
    _is_builder_function: bool
    _retry_policy: typing.Union[modal_proto.api_pb2.FunctionRetryPolicy, None]

    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], modal.object._BLOCKING_H], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], modal.object._BLOCKING_H], None] = None):
        ...

    @staticmethod
    def from_args(function_handle: FunctionHandle, info: modal._function_utils.FunctionInfo, stub, image=None, secret: typing.Union[modal.secret.Secret, None] = None, secrets: typing.Collection[modal.secret.Secret] = (), schedule: typing.Union[modal.schedule.Schedule, None] = None, is_generator=False, gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, mounts: typing.Collection[modal.mount.Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.shared_volume.SharedVolume] = {}, allow_cross_region_volumes: bool = False, webhook_config: typing.Union[modal_proto.api_pb2.WebhookConfig, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy.Proxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, timeout: typing.Union[int, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, cpu: typing.Union[float, None] = None, keep_warm: typing.Union[int, None] = None, interactive: bool = False, name: typing.Union[str, None] = None, cloud: typing.Union[str, None] = None, is_builder_function: bool = False, cls: typing.Union[type, None] = None) -> None:
        ...

    def get_panel_items(self) -> typing.List[str]:
        ...

    @property
    def tag(self):
        ...

    def get_build_def(self):
        ...


class AioFunction(modal.object.AioProvider[AioFunctionHandle]):
    _secrets: typing.Collection[modal.secret.AioSecret]
    _info: modal._function_utils.FunctionInfo
    _mounts: typing.Collection[modal.mount.AioMount]
    _shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.shared_volume.AioSharedVolume]
    _allow_cross_region_volumes: bool
    _image: typing.Union[modal.image.AioImage, None]
    _gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig]
    _cloud: typing.Union[str, None]
    _function_handle: AioFunctionHandle
    _stub: modal.stub.AioStub
    _is_builder_function: bool
    _retry_policy: typing.Union[modal_proto.api_pb2.FunctionRetryPolicy, None]

    def __init__(self, load: typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[modal.object._ASYNC_H]], rep: str, is_persisted_ref: bool = False, preload: typing.Union[typing.Callable[[modal._resolver.Resolver, typing.Union[str, None]], typing.Awaitable[modal.object._ASYNC_H]], None] = None):
        ...

    @staticmethod
    def from_args(function_handle: AioFunctionHandle, info: modal._function_utils.FunctionInfo, stub, image=None, secret: typing.Union[modal.secret.AioSecret, None] = None, secrets: typing.Collection[modal.secret.AioSecret] = (), schedule: typing.Union[modal.schedule.Schedule, None] = None, is_generator=False, gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, mounts: typing.Collection[modal.mount.AioMount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.shared_volume.AioSharedVolume] = {}, allow_cross_region_volumes: bool = False, webhook_config: typing.Union[modal_proto.api_pb2.WebhookConfig, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy.AioProxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, timeout: typing.Union[int, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, cpu: typing.Union[float, None] = None, keep_warm: typing.Union[int, None] = None, interactive: bool = False, name: typing.Union[str, None] = None, cloud: typing.Union[str, None] = None, is_builder_function: bool = False, cls: typing.Union[type, None] = None) -> None:
        ...

    def get_panel_items(self) -> typing.List[str]:
        ...

    @property
    def tag(self):
        ...

    def get_build_def(self):
        ...


class _FunctionCall(modal.object._Handle):
    def _invocation(self):
        ...

    async def get(self, timeout: typing.Union[float, None] = None):
        ...

    async def get_call_graph(self) -> typing.List[modal.call_graph.InputInfo]:
        ...

    async def cancel(self):
        ...


class FunctionCall(modal.object.Handle):
    def __init__(self):
        ...

    def _invocation(self):
        ...

    class __get_spec(typing_extensions.Protocol):
        def __call__(self, timeout: typing.Union[float, None] = None):
            ...

        async def aio(self, *args, **kwargs):
            ...

    get: __get_spec

    class __get_call_graph_spec(typing_extensions.Protocol):
        def __call__(self) -> typing.List[modal.call_graph.InputInfo]:
            ...

        async def aio(self, *args, **kwargs) -> typing.List[modal.call_graph.InputInfo]:
            ...

    get_call_graph: __get_call_graph_spec

    class __cancel_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    cancel: __cancel_spec


class AioFunctionCall(modal.object.AioHandle):
    def __init__(self):
        ...

    def _invocation(self):
        ...

    async def get(self, *args, **kwargs):
        ...

    async def get_call_graph(self, *args, **kwargs) -> typing.List[modal.call_graph.InputInfo]:
        ...

    async def cancel(self, *args, **kwargs):
        ...


async def _gather(*function_calls: _FunctionCall):
    ...


class __gather_spec(typing_extensions.Protocol):
    def __call__(self, *function_calls: FunctionCall):
        ...

    async def aio(self, *args, **kwargs):
        ...

gather: __gather_spec


async def aio_gather(*args, **kwargs):
    ...


def current_input_id() -> str:
    ...


def _set_current_input_id(input_id: typing.Union[str, None]):
    ...


class _PartialFunction:
    @staticmethod
    def initialize_cls(user_cls: type, function_handles: typing.Dict[str, _FunctionHandle]):
        ...

    def __init__(self, raw_f: typing.Callable[..., typing.Any], webhook_config: typing.Union[modal_proto.api_pb2.WebhookConfig, None] = None, is_generator: typing.Union[bool, None] = None):
        ...

    def __get__(self, obj, objtype=None) -> _FunctionHandle:
        ...

    def __del__(self):
        ...


class PartialFunction:
    def __init__(self, raw_f: typing.Callable[..., typing.Any], webhook_config: typing.Union[modal_proto.api_pb2.WebhookConfig, None] = None, is_generator: typing.Union[bool, None] = None):
        ...

    @staticmethod
    def initialize_cls(user_cls: type, function_handles: typing.Dict[str, FunctionHandle]):
        ...

    def __get__(self, obj, objtype=None) -> FunctionHandle:
        ...

    def __del__(self):
        ...


class AioPartialFunction:
    def __init__(self, raw_f: typing.Callable[..., typing.Any], webhook_config: typing.Union[modal_proto.api_pb2.WebhookConfig, None] = None, is_generator: typing.Union[bool, None] = None):
        ...

    @staticmethod
    def initialize_cls(user_cls: type, function_handles: typing.Dict[str, AioFunctionHandle]):
        ...

    def __get__(self, obj, objtype=None) -> AioFunctionHandle:
        ...

    def __del__(self):
        ...


def _method(*, is_generator: typing.Union[bool, None] = None) -> typing.Callable[[typing.Callable[..., typing.Any]], _PartialFunction]:
    ...


def _web_endpoint(method: str = 'GET', label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], _PartialFunction]:
    ...


def _asgi_app(label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], _PartialFunction]:
    ...


def _wsgi_app(label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], _PartialFunction]:
    ...


def method(*, is_generator: typing.Union[bool, None] = None) -> typing.Callable[[typing.Callable[..., typing.Any]], PartialFunction]:
    ...


def aio_method(*, is_generator: typing.Union[bool, None] = None) -> typing.Callable[[typing.Callable[..., typing.Any]], AioPartialFunction]:
    ...


def web_endpoint(method: str = 'GET', label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], PartialFunction]:
    ...


def aio_web_endpoint(method: str = 'GET', label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], AioPartialFunction]:
    ...


def asgi_app(label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], PartialFunction]:
    ...


def aio_asgi_app(label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], AioPartialFunction]:
    ...


def wsgi_app(label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], PartialFunction]:
    ...


def aio_wsgi_app(label: typing.Union[str, None] = None, wait_for_response: bool = True) -> typing.Callable[[typing.Callable[..., typing.Any]], AioPartialFunction]:
    ...


_current_input_id: typing.Union[str, None]