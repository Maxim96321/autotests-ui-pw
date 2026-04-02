from elements.base_elememt import BaseElement


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "link"
