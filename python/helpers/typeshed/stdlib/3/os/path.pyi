# Stubs for os.path
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.2/library/os.path.html
# adapted for 2.7 by Michal Pokorny
import sys
from typing import (
    overload, List, Any, AnyStr, Sequence, Tuple, BinaryIO, TextIO,
    TypeVar, Union, Text, Callable
)

_T = TypeVar('_T')

if sys.version_info >= (3, 6):
    from builtins import _PathLike
    _PathType = Union[bytes, Text, _PathLike]
else:
    _PathType = Union[bytes, Text]

# ----- os.path variables -----
supports_unicode_filenames = False
# aliases (also in os)
curdir = ...  # type: str
pardir = ...  # type: str
sep = ...  # type: str
altsep = ...  # type: str
extsep = ...  # type: str
pathsep = ...  # type: str
defpath = ...  # type: str
devnull = ...  # type: str

# ----- os.path function stubs -----
def abspath(path: AnyStr) -> AnyStr: ...
def basename(path: AnyStr) -> AnyStr: ...

if sys.version_info >= (3, 5):
    def commonpath(paths: Sequence[AnyStr]) -> AnyStr: ...

# NOTE: Empty lists results in '' (str) regardless of contained type.
# Also, in Python 2 mixed sequences of Text and bytes results in either Text or bytes
# So, fall back to Any
def commonprefix(list: Sequence[AnyStr]) -> Any: ...

def dirname(path: AnyStr) -> AnyStr: ...
def exists(path: _PathType) -> bool: ...
def lexists(path: _PathType) -> bool: ...
def expanduser(path: AnyStr) -> AnyStr: ...
def expandvars(path: AnyStr) -> AnyStr: ...

# These return float if os.stat_float_times() == True,
# but int is a subclass of float.
def getatime(path: _PathType) -> float: ...
def getmtime(path: _PathType) -> float: ...
def getctime(path: _PathType) -> float: ...

def getsize(path: _PathType) -> int: ...
def isabs(path: _PathType) -> bool: ...
def isfile(path: _PathType) -> bool: ...
def isdir(path: _PathType) -> bool: ...
def islink(path: _PathType) -> bool: ...
def ismount(path: _PathType) -> bool: ...

if sys.version_info < (3, 0):
    # Make sure signatures are disjunct, and allow combinations of bytes and unicode.
    # (Since Python 2 allows that, too)
    # Note that e.g. os.path.join("a", "b", "c", "d", u"e") will still result in
    # a type error.
    @overload
    def join(__p1: bytes, *p: bytes) -> bytes: ...
    @overload
    def join(__p1: Text, *p: _PathType) -> Text: ...
    @overload
    def join(__p1: bytes, __p2: Text, *p: _PathType) -> Text: ...
    @overload
    def join(__p1: bytes, __p2: bytes, __p3: Text, *p: _PathType) -> Text: ...
    @overload
    def join(__p1: bytes, __p2: bytes, __p3: bytes, __p4: Text, *p: _PathType) -> Text: ...
else:
    def join(path: AnyStr, *paths: AnyStr) -> AnyStr: ...

def normcase(path: AnyStr) -> AnyStr: ...
def normpath(path: AnyStr) -> AnyStr: ...
if sys.platform == 'win32':
    def realpath(path: AnyStr) -> AnyStr: ...
else:
    def realpath(filename: AnyStr) -> AnyStr: ...
def relpath(path: AnyStr, start: _PathType = ...) -> AnyStr: ...

def samefile(path1: _PathType, path2: _PathType) -> bool: ...
def sameopenfile(fp1: int, fp2: int) -> bool: ...
# TODO
# def samestat(stat1: stat_result,
#             stat2: stat_result) -> bool: ...  # Unix only

if sys.version_info >= (3, 6):
    def split(path: Union[AnyStr, _PathLike[AnyStr]]) -> Tuple[AnyStr, AnyStr]: ...
else:
    def split(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
def splitdrive(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
def splitext(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...

def splitunc(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...  # Windows only, deprecated

if sys.version_info < (3,):
    def walk(path: AnyStr, visit: Callable[[_T, AnyStr, List[AnyStr]], Any], arg: _T) -> None: ...
