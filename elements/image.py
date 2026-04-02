from elements.base_elememt import BaseElement


class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return "image"
