from textual.binding import Binding
from textual.containers import Container
from textual.reactive import var


class ListContainer(Container):

    BINDINGS = [
        Binding(key="ctrl+l", action="toggle_chat_list", description="Toggle Chat List"),
    ]

    show_chat_list = var(True)

    def watch_show_chat_list(self, show_chat_list: bool) -> None:
        """Called when show_chat_list is modified."""
        self.set_class(show_chat_list, "-show-chat-list")

    def action_toggle_chat_list(self) -> None:
        """Called in response to key binding."""
        self.show_chat_list = not self.show_chat_list

