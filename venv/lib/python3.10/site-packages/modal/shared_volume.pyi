import __main__
import modal.object
import modal_proto.api_pb2
import pathlib
import typing
import typing_extensions

class _SharedVolumeHandle(modal.object._Handle):
    async def write_file(self, remote_path: str, fp: typing.BinaryIO) -> int:
        ...

    def read_file(self, path: str) -> typing.AsyncIterator[bytes]:
        ...

    def iterdir(self, path: str) -> typing.AsyncIterator[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
        ...

    async def add_local_file(self, local_path: typing.Union[pathlib.Path, str], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None):
        ...

    async def add_local_dir(self, local_path: typing.Union[pathlib.Path, str], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None):
        ...

    async def listdir(self, path: str) -> typing.List[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
        ...

    async def remove_file(self, path: str, recursive=False):
        ...


class SharedVolumeHandle(modal.object.Handle):
    def __init__(self):
        ...

    class __write_file_spec(typing_extensions.Protocol):
        def __call__(self, remote_path: str, fp: typing.BinaryIO) -> int:
            ...

        async def aio(self, *args, **kwargs) -> int:
            ...

    write_file: __write_file_spec

    class __read_file_spec(typing_extensions.Protocol):
        def __call__(self, path: str) -> typing.Iterator[bytes]:
            ...

        def aio(self, path: str) -> typing.AsyncIterator[bytes]:
            ...

    read_file: __read_file_spec

    class __iterdir_spec(typing_extensions.Protocol):
        def __call__(self, path: str) -> typing.Iterator[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
            ...

        def aio(self, path: str) -> typing.AsyncIterator[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
            ...

    iterdir: __iterdir_spec

    class __add_local_file_spec(typing_extensions.Protocol):
        def __call__(self, local_path: typing.Union[pathlib.Path, str], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None):
            ...

        async def aio(self, *args, **kwargs):
            ...

    add_local_file: __add_local_file_spec

    class __add_local_dir_spec(typing_extensions.Protocol):
        def __call__(self, local_path: typing.Union[pathlib.Path, str], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None):
            ...

        async def aio(self, *args, **kwargs):
            ...

    add_local_dir: __add_local_dir_spec

    class __listdir_spec(typing_extensions.Protocol):
        def __call__(self, path: str) -> typing.List[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
            ...

        async def aio(self, *args, **kwargs) -> typing.List[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
            ...

    listdir: __listdir_spec

    class __remove_file_spec(typing_extensions.Protocol):
        def __call__(self, path: str, recursive=False):
            ...

        async def aio(self, *args, **kwargs):
            ...

    remove_file: __remove_file_spec


class AioSharedVolumeHandle(modal.object.AioHandle):
    def __init__(self):
        ...

    async def write_file(self, *args, **kwargs) -> int:
        ...

    def read_file(self, path: str) -> typing.AsyncIterator[bytes]:
        ...

    def iterdir(self, path: str) -> typing.AsyncIterator[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
        ...

    async def add_local_file(self, *args, **kwargs):
        ...

    async def add_local_dir(self, *args, **kwargs):
        ...

    async def listdir(self, *args, **kwargs) -> typing.List[modal_proto.api_pb2.SharedVolumeListFilesEntry]:
        ...

    async def remove_file(self, *args, **kwargs):
        ...


class _SharedVolume(modal.object._Provider[_SharedVolumeHandle]):
    def __init__(self, cloud: typing.Union[str, None] = None) -> None:
        ...


class SharedVolume(modal.object.Provider[SharedVolumeHandle]):
    def __init__(self, cloud: typing.Union[str, None] = None) -> None:
        ...


class AioSharedVolume(modal.object.AioProvider[AioSharedVolumeHandle]):
    def __init__(self, cloud: typing.Union[str, None] = None) -> None:
        ...
