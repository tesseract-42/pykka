import threading
from typing import (
    Any,
    Generic,
    Optional,
    Type,
    Union,
    overload,
)

from typing_extensions import Literal

from pykka import ActorProxy, Future
from pykka._actor import ActorInbox, _A

class ActorRef(Generic[_A]):
    actor_class: Type[_A]
    actor_urn: str
    actor_inbox: ActorInbox
    actor_stopped: threading.Event
    def __init__(self, actor: _A) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def is_alive(self) -> bool: ...
    def tell(self, message: Any) -> None: ...
    @overload
    def ask(
        self,
        message: Any,
        block: Literal[False],
        timeout: Optional[float] = ...,
    ) -> Future[Any]: ...
    @overload  # noqa: Allow redefinition
    def ask(
        self,
        message: Any,
        block: Literal[True],
        timeout: Optional[float] = ...,
    ) -> Any: ...
    @overload  # noqa: Allow redefinition
    def ask(
        self, message: Any, block: bool = ..., timeout: Optional[float] = ...
    ) -> Union[Future[Any], Any]: ...
    @overload
    def stop(self, block: Literal[True], timeout: Optional[float]) -> bool: ...
    @overload  # noqa: Allow redefinition
    def stop(
        self, block: Literal[False], timeout: Optional[float] = ...
    ) -> Future[bool]: ...
    @overload  # noqa: Allow redefinition
    def stop(
        self, block: bool, timeout: Optional[float] = ...
    ) -> Union[Future[bool], bool]: ...
    def proxy(self) -> ActorProxy: ...
