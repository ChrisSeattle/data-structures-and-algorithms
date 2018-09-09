from .graph import Graph
from .conftest import graph_empty, graph_filled, graph_filled_for_traversal, z_vert, y_vert, x_vert



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
    assert len(graph_empty()) == 0
    assert len(graph_filled()) == 6


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


def test_method_add_edge_exists():
    """ Can we see the Graph method add_edge
    """
    assert Graph.add_edge


def test_method_get_neighbors_exists():
    """ Can we see the Graph method get_neighbors
    """
    assert Graph.get_neighbors
