import json
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypedDict, TypeIs, cast

from utils import cyan_print, sep_print

################################################################################
#
# TypeIs - Outro exemplo mais complexo
#
################################################################################

# Modela os dados que esperamos receber de fora


class ProductDict(TypedDict, total=False):
    name: str
    price: float
    stock: int
    url: str


################################################################################

# Objetos finais que queremos


@dataclass
class PhysicalProduct:
    name: str
    price: float
    stock: int


@dataclass
class DigitalProduct:
    name: str
    price: float
    url: str


type Product = PhysicalProduct | DigitalProduct

################################################################################

# Carrega os dados... Simula dados vindos de fora


def load_json_data() -> object:
    database = Path("exemplo40.json").resolve()

    with database.open("r", encoding="utf8") as file:
        return json.load(file)


################################################################################

# Type Predicate Functions (Aqui que entra o TypeIs)


def is_valid_dict(item: object) -> TypeIs[dict[str, Any]]:
    return isinstance(item, dict)


def is_physical_product(item: object) -> TypeIs[ProductDict]:
    if not is_valid_dict(item):
        return False

    has_str_name = isinstance(
        item.get("name"),
        str,
    )
    has_numeric_price = isinstance(
        item.get("price"),
        int | float,
    )
    has_int_stock = isinstance(
        item.get("stock"),
        int,
    )
    has_no_url = not item.get("url")

    return has_str_name and has_int_stock and has_numeric_price and has_no_url


def is_digital_product(item: object) -> TypeIs[ProductDict]:
    if not is_valid_dict(item):
        return False

    has_str_name = isinstance(
        item.get("name"),
        str,
    )
    has_numeric_price = isinstance(
        item.get("price"),
        int | float,
    )
    has_str_url = isinstance(
        item.get("url"),
        str,
    )
    has_no_stock = not item.get("stock")

    return has_str_name and has_str_url and has_numeric_price and has_no_stock


################################################################################

# Vamos tentar processar os dados


def parse_api_products(api_data: object) -> list[Product]:
    # Só quero garantir que temos um iterável aqui
    assert isinstance(api_data, Iterable), "Something went wrong with the API data"

    # Esse cast foi para o Pyright parar de amolar com coisas `Unknown`,
    # eu VOU checar.
    api_data = cast("Iterable[dict[str, Any]]", api_data)
    parsed_products: list[Product] = []

    for item in api_data:
        if is_physical_product(item):
            product = PhysicalProduct(
                name=item["name"],
                price=item["price"],
                stock=item["stock"],
            )
            parsed_products.append(product)
            continue  # Guard clause: continua para o próximo loop

        # COMPORTAMENTO DO PYRIGHT:
        # O Pyright mostra intersection como mostro abaixo.
        # Intersection (& ou E) significa tudo que tem em um tipo & no outro
        # Lembrando que isso não é possível em Python, então PhysicalProduct
        # Pyright: <subclass of dict[str, Any] and PhysicalProduct>
        if is_digital_product(item):
            product = DigitalProduct(
                name=item["name"],
                price=item["price"],
                url=item["url"],
            )
            parsed_products.append(product)
            continue  # Guard clause: continua para o próximo loop

        # Só pra gente ver o que não entrou na lista
        cyan_print("Not a valid product")
        cyan_print(item)

    return parsed_products


################################################################################

# Podemos testar

if __name__ == "__main__":
    sep_print()

    data = load_json_data()  # object
    parsed_products = parse_api_products(data)  # list[Product]

    sep_print()

    for product in parsed_products:
        # Ainda quer garantia?
        if isinstance(product, PhysicalProduct):
            cyan_print("Físico:", product.name, product.price, product.stock)

        if isinstance(product, DigitalProduct):
            cyan_print("Digital:", product.name, product.price, product.url)

    sep_print()

################################################################################
