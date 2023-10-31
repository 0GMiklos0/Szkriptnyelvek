from utils_mod import duplaz, is_palindrom

def test_duplaz():
    assert duplaz(100) == 200
    assert duplaz(5) == 10
    assert duplaz(2.233) == 4.466
    
def test_is_palindrom():
    assert is_palindrom("amma")
    assert is_palindrom("hahahah")
    assert is_palindrom("kalamajka")
    assert is_palindrom(" ")