import pytest
from .breadth_first import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


@pytest.fixture()
def alone_vert():
    return {'alone': {}}


@pytest.fixture()
def z_vert():
    return {'Z': {'Y': 20}}


@pytest.fixture()
def y_vert():
    return {'Y': {'X': 20, 'Z': 20}}


@pytest.fixture()
def x_vert():
    return {'X': {'Z': 20, 'Y': 10}}





