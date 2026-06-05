from topology import adjacency


def test_adjacency_exists():
    graph = adjacency()

    assert "Keter" in graph
    assert "Malkhut" in graph


def test_keter_connected():
    graph = adjacency()

    assert len(graph["Keter"]) > 0from aleph_olam.topology import SEPHIROT

def test_sephirot_count():
    assert len(SEPHIROT) == 10
