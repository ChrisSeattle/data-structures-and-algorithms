from .graph import Graph
from .conftest import graph_empty, graph_filled, graph_filled_for_traversal, z_vert, y_vert, x_vert
import pytest


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
    pass


def test_breadth_first_on_invalid_vert():
    """ Do we get expected error when called on not present vertice
    """
    pass


def test_breadth_first_on_traversal_input():
    """ Do we get expected output on valid graph to traverse.
    """
    pass

