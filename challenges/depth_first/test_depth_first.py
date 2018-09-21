# from .breadth_first import Node, Queue
from .depth_first import Graph
# from .conftest import airline, graph_filled, graph_filled_for_traversal, z_vert, y_vert, x_vert
import pytest
import copy

# --------------
# Start of fixtures
# --------------


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
def airline():
    a = Graph()
    a.add_vert({'Pandora': {'Arendelle': 150, 'Metroville': 82}})
    a.add_vert({'Arendelle': {'Pandora': 150, 'New Monstropolis': 42, 'Metroville': 99}})
    a.add_vert({'Metroville': {'Pandora': 82, 'Arendelle': 99, 'New Monstropolis': 105, 'Narnia': 37, 'Naboo': 26}})
    a.add_vert({'New Monstropolis': {'Arendelle': 42, 'Metroville': 105, 'Naboo': 73}})
    a.add_vert({'Narnia': {'Metroville': 37, 'Naboo': 250, }})
    a.add_vert({'Naboo': {'New Monstropolis': 73, 'Narnia': 250, 'Metroville': 26}})
    return a

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

# --------------
# End of fixtures
# --------------


def test_alive():
    """ Does our test file even run
    """
    pass


def test_graph_exists():
    """ can we basically see the object
    """
    assert Graph


def test_fixture_exists():
    """ Do we see fixtures in conftest file
    """
    assert graph_empty
    assert graph_filled
    assert graph_filled_for_traversal


def test_length_works_on_fixtures():
    """ Checking the len() reports expected results on our test graphs
    """
    assert len(graph_filled_for_traversal()) == 7
    assert len(graph_filled()) == 6
    assert len(graph_empty()) == 0


def test_graph_repr():
    """ Do we get the exprected repr response
    """
    expected = "<Graph | Vertices: ['A', 'B', 'C', 'D', 'E', 'F'] | Length: 6>"
    actual = repr(graph_filled())
    assert expected == actual


def test_graph_str():
    """ Do we see expected str response
    """
    expected = "['A', 'B', 'C', 'D', 'E', 'F', 'G']"
    actual = str(graph_filled_for_traversal())
    assert expected == actual


def test_fixture_vert_exists():
    """ Do we see the dictionaries setup as 'verticies'
    """
    assert z_vert
    assert y_vert
    assert x_vert


def test_method_has_vert_exists():
    """ Can we see the Graph method has_vert
    """
    assert Graph.has_vert


def test_has_vert_returns_true():
    """ If passed a valid vertice name, reports true
    """
    assert graph_filled().has_vert('A')


def test_has_vert_returns_false():
    """ If passed an invalid vertice name, reports false
    """
    assert not graph_filled().has_vert('P')


def test_method_add_vert_exists():
    """ Can we see the Graph method add_vert
    """
    assert Graph.add_vert


def test_method_add_vert_simple_vert_name():
    """ Does method add_vert work for a single vert name passed
    """
    e = graph_empty()
    assert not e.has_vert('P')
    e.add_vert('P')
    assert e.has_vert('P')


def test_add_vert_vert_name_list():
    """ Does method add_vert work when passed a list of names
    """
    e = graph_empty()
    assert not e.has_vert('P')
    assert not e.has_vert('Q')
    e.add_vert(['P', 'Q'])
    assert e.has_vert('P')
    assert e.has_vert('Q')


def test_method_add_vert_dict():
    """ Does method add_vert work when passed a single dict
        We would not expect it to work on a list of vertices
    """
    e = graph_empty()
    assert not e.has_vert('Z')
    e.add_vert(z_vert())
    assert e.has_vert('Z')


def test_method_add_edge_exists():
    """ Can we see the Graph method add_edge
    """
    assert Graph.add_edge


def test_method_add_edge_on_new_verts():
    """ Can we add edges on new empty verts
    """
    e = graph_empty()
    e.add_vert('P')
    e.add_vert('Q')
    e.add_edge('P', 'Q', 5)
    expected = {'P': {'Q': 5}, 'Q': {}}
    actual = e.graph
    assert expected == actual


def test_add_edge_on_verts_with_no_edges():
    """ Can we add edges on verts that exist with no edges
    """
    g = graph_filled()
    g.add_edge('C', 'E', 6)
    actual = g.graph['C']
    expected = {'E': 6}
    assert expected == actual


def test_add_edge_on_existing_verts_with_edges():
    """ Can we add edges on verts that already have edges
    """
    g = graph_filled()
    assert g.graph['A'] == {'B': 10}
    g.add_edge('A', 'E', 7)
    assert g.graph['A'] == {'B': 10, 'E': 7}


def test_add_edge_error_for_not_valid_first_vert():
    """ Can we add edges on new empty verts
    """
    g = graph_filled()
    with pytest.raises(ValueError):
        g.add_edge('P', 'B', 6)


def test_add_edge_error_for_not_valid_second_vert():
    """ Can we add edges on new empty verts
    """
    g = graph_filled()
    with pytest.raises(ValueError):
        g.add_edge('B', 'Q', 8)


def test_add_edge_overwrite_existing_edge():
    """ If the edge existed, it should update it
    """
    g = graph_filled()
    assert g.graph['B'] == {'A': 5, 'D': 15, 'C': 20}
    g.add_edge('B', 'A', 6)
    assert g.graph['B'] == {'A': 6, 'D': 15, 'C': 20}


def test_method_get_neighbors_exists():
    """ Can we see the Graph method get_neighbors
    """
    assert Graph.get_neighbors


def test_method_get_neighbors_returns_expected():
    """ Do we get the correct response when called valid vertice
    """
    g = graph_filled()  # 'B': {'A': 5, 'D': 15, 'C': 20}
    expected = ['A', 'D', 'C']
    actual = g.get_neighbors('B')
    assert expected == actual


def test_method_get_neighbors_on_invalid_vert():
    """ Do we get expected error when called on not present vertice
    """
    e = graph_empty()
    with pytest.raises(ValueError):
        e.get_neighbors('B')


def test_method_breadth_first_exists():
    """ Can we see the method
    """
    assert Graph.breadth_first


def test_breadth_first_on_empty_graph():
    """ Do we handle when graph has no vertices
    """
    e = graph_empty()
    with pytest.raises(ValueError):
        e.breadth_first('a')


def test_breadth_first_on_invalid_vert():
    """ Do we get expected error when called on not present vertice
    """
    g = graph_filled()
    with pytest.raises(ValueError):
        g.breadth_first('z')


def test_breadth_first_on_traversal_input():
    """ Do we get expected output on valid graph to traverse.
    """
    expected1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # expected2 = ['A', 'C', 'B', 'F', 'G', 'D', 'E']
    # import copy
    temp = graph_filled_for_traversal()
    t = copy.deepcopy(temp)
    actual = t.breadth_first('A')
    assert expected1 == actual

# -----------------
# Added for get_edges
# -----------------


def test_method_get_edges_exists():
    """ Can we see the method
    """
    assert Graph.get_edges


def test_get_edges_on_empty_graph(graph_empty):
    """ Do we handle when graph has no vertices
    """
    assert isinstance(graph_empty, Graph)
    success, cost = graph_empty.get_edges(['a'])
    assert success is False


def test_get_edges_on_invalid_vert(graph_filled):
    """ Do we get expected results when called on not present vertice
    """
    assert isinstance(graph_filled, Graph)
    success, cost = graph_filled.get_edges(['z'])
    assert success is False


def test_fixture_for_airline_exists(airline):
    """ Do we see the airline fiture in conftest file
    """
    assert isinstance(airline, Graph)


def test_airline_routes_2_cities(airline):
    """ Do we get expected results from the airline questions
    """
    input = ['Metroville', 'Pandora']
    expected = (True, 82)
    actual = airline.get_edges(input)
    assert expected == actual


def test_airline_routes_3_cities(airline):
    """ Do we get expected results from the airline questions
    """
    input = ['Arendelle', 'New Monstropolis', 'Naboo']
    expected = (True, 115)
    actual = airline.get_edges(input)
    assert expected == actual


def test_airline_2_cities_exists_not_connected(airline):
    """ Do we get expected results from the airline questions
    """
    input = ['Naboo', 'Pandora']
    expected = (False, 0)
    actual = airline.get_edges(input)
    assert expected == actual


def test_airline_3_cities_exists_not_connected(airline):
    """ Do we get expected results from the airline questions
    """
    input = ['Narnia', 'Arendelle', 'Naboo']
    expected = (False, 0)
    actual = airline.get_edges(input)
    assert expected == actual

# ---------------
# Added for depth_first
# ---------------


def test_method_depth_first_exists():
    """ Can we see the method
    """
    assert Graph.depth_first


def test_depth_first_on_empty(graph_empty):
    """ If there are no vertices, do we handle it
    """
    actual = graph_empty.depth_first()
    expected = None
    assert expected == actual


def test_depth_first_on_example_data():
    """ Using the data from the challenge
    """
    g = Graph()
    g.add_vert({
        'A': {'B': 1, 'D': 1},
        'B': {'A': 1, 'C': 1, 'D': 1},
        'D': {'A': 1, 'B': 1, 'E': 1, 'H': 1, 'F': 1},
        'C': {'B': 1, 'G': 1},
        'G': {'C': 1},
        'E': {'D': 1, 'H': 1},
        'H': {'E': 1, 'F': 1},
        'F': {'D': 1, 'H': 1},
        })
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = g.depth_first()
    assert expected == actual
