from elements.base_elememt import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"
