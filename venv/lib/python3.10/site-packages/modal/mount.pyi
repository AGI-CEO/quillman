import __main__
import modal._blob_utils
import modal._resolver
import modal.object
import pathlib
import typing
import typing_extensions

def client_mount_name():
    ...


class _MountEntry:
    remote_path: pathlib.PurePosixPath

    def description(self) -> str:
        ...

    def get_files_to_upload(self) -> typing.Iterator[typing.Tuple[pathlib.Path, str]]:
        ...

    def watch_entry(self) -> typing.Tuple[pathlib.Path, pathlib.Path]:
        ...


class _MountFile(_MountEntry):
    local_file: pathlib.Path
    remote_path: pathlib.PurePosixPath

    def description(self) -> str:
        ...

    def get_files_to_upload(self):
        ...

    def watch_entry(self):
        ...

    def __init__(self, local_file: pathlib.Path, remote_path: pathlib.PurePosixPath) -> None:
        ...

    def __repr__(self):
        ...

    def __eq__(self, other):
        ...


class _MountDir(_MountEntry):
    local_dir: pathlib.Path
    remote_path: pathlib.PurePosixPath
    condition: typing.Callable[[str], bool]
    recursive: bool

    def description(self):
        ...

    def get_files_to_upload(self):
        ...

    def watch_entry(self):
        ...

    def __init__(self, local_dir: pathlib.Path, remote_path: pathlib.PurePosixPath, condition: typing.Callable[[str], bool], recursive: bool) -> None:
        ...

    def __repr__(self):
        ...

    def __eq__(self, other):
        ...


class _MountHandle(modal.object._Handle):
    ...

class MountHandle(modal.object.Handle):
    def __init__(self):
        ...


class AioMountHandle(modal.object.AioHandle):
    def __init__(self):
        ...


class _Mount(modal.object._Provider[_MountHandle]):
    _entries: typing.List[_MountEntry]

    def __init__(self, *args, **kwargs):
        ...

    @staticmethod
    def _from_entries(*entries: _MountEntry) -> _Mount:
        ...

    @property
    def entries(self):
        ...

    def is_local(self) -> bool:
        ...

    def add_local_dir(self, local_path: typing.Union[str, pathlib.Path], *, remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None, condition: typing.Union[typing.Callable[[str], bool], None] = None, recursive: bool = True) -> _Mount:
        ...

    @staticmethod
    def from_local_dir(local_path: typing.Union[str, pathlib.Path], *, remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None, condition: typing.Union[typing.Callable[[str], bool], None] = None, recursive: bool = True):
        ...

    def add_local_file(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None) -> _Mount:
        ...

    @staticmethod
    def from_local_file(local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None) -> _Mount:
        ...

    @staticmethod
    def _description(entries: typing.List[_MountEntry]) -> str:
        ...

    @staticmethod
    def _get_files(entries: typing.List[_MountEntry]) -> typing.AsyncGenerator[modal._blob_utils.FileUploadSpec, None]:
        ...

    @staticmethod
    async def _load_mount(entries: typing.List[_MountEntry], resolver: modal._resolver.Resolver, existing_object_id: typing.Union[str, None]):
        ...


class Mount(modal.object.Provider[MountHandle]):
    _entries: typing.List[_MountEntry]

    def __init__(self, *args, **kwargs):
        ...

    @staticmethod
    def _from_entries(*entries: _MountEntry) -> Mount:
        ...

    @property
    def entries(self):
        ...

    def is_local(self) -> bool:
        ...

    def add_local_dir(self, local_path: typing.Union[str, pathlib.Path], *, remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None, condition: typing.Union[typing.Callable[[str], bool], None] = None, recursive: bool = True) -> Mount:
        ...

    @staticmethod
    def from_local_dir(local_path: typing.Union[str, pathlib.Path], *, remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None, condition: typing.Union[typing.Callable[[str], bool], None] = None, recursive: bool = True):
        ...

    def add_local_file(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None) -> Mount:
        ...

    @staticmethod
    def from_local_file(local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None) -> Mount:
        ...

    @staticmethod
    def _description(entries: typing.List[_MountEntry]) -> str:
        ...

    class ___get_files_spec(typing_extensions.Protocol):
        def __call__(self, entries: typing.List[_MountEntry]) -> typing.Generator[modal._blob_utils.FileUploadSpec, None, None]:
            ...

        def aio(self, entries: typing.List[_MountEntry]) -> typing.AsyncGenerator[modal._blob_utils.FileUploadSpec, None]:
            ...

    _get_files: ___get_files_spec

    class ___load_mount_spec(typing_extensions.Protocol):
        def __call__(self, entries: typing.List[_MountEntry], resolver: modal._resolver.Resolver, existing_object_id: typing.Union[str, None]):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _load_mount: ___load_mount_spec


class AioMount(modal.object.AioProvider[AioMountHandle]):
    _entries: typing.List[_MountEntry]

    def __init__(self, *args, **kwargs):
        ...

    @staticmethod
    def _from_entries(*entries: _MountEntry) -> AioMount:
        ...

    @property
    def entries(self):
        ...

    def is_local(self) -> bool:
        ...

    def add_local_dir(self, local_path: typing.Union[str, pathlib.Path], *, remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None, condition: typing.Union[typing.Callable[[str], bool], None] = None, recursive: bool = True) -> AioMount:
        ...

    @staticmethod
    def from_local_dir(local_path: typing.Union[str, pathlib.Path], *, remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None, condition: typing.Union[typing.Callable[[str], bool], None] = None, recursive: bool = True):
        ...

    def add_local_file(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None) -> AioMount:
        ...

    @staticmethod
    def from_local_file(local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.PurePosixPath, None] = None) -> AioMount:
        ...

    @staticmethod
    def _description(entries: typing.List[_MountEntry]) -> str:
        ...

    @staticmethod
    def _get_files(entries: typing.List[_MountEntry]) -> typing.AsyncGenerator[modal._blob_utils.FileUploadSpec, None]:
        ...

    @staticmethod
    async def _load_mount(*args, **kwargs):
        ...


def _create_client_mount():
    ...


def create_client_mount():
    ...


def aio_create_client_mount():
    ...


def _get_client_mount():
    ...


def _create_package_mounts(module_names: typing.Sequence[str]) -> typing.List[_Mount]:
    ...


def create_package_mounts(module_names: typing.Sequence[str]) -> typing.List[Mount]:
    ...


def aio_create_package_mounts(module_names: typing.Sequence[str]) -> typing.List[AioMount]:
    ...
