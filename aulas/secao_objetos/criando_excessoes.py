class NameIsGustavoError(Exception): ...


name = "Gustavo"

if name == "Gustavo":
    raise NameIsGustavoError("O nome digitado foi Gustavo")
