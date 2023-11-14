import sajat_halmaz as s
import hamming as h
import hangrend_enum as he
import gombkor as g
import anagramma as a

class Tester:
    def test_hamming():
        assert h.hammingDistance("guns", "mugs") == 2
        assert h.hammingDistance("", "mugs") == -1
        assert h.hammingDistance("mugr", "mugs") == 0
    
    #verem test
    def test_verem(v: s.Verem):
        v.betesz(10)
        assert str(v) == "[10"
        assert str(v) == "[10]"
        assert str(v) == "["
        v.kivesz(10)
        assert str(v) == "[10"
        assert str(v) == "["
        
    def test_hangrend(s: he.Hangnem):
        assert s.check() == "magas"
        assert s.check() == "mély"
        assert s.check() == "vegyes"
        assert s.check() == "semmilye"
    
    def test_gomb(c: g.Ellipse, s: g.Sphere):
        assert c < 3 == False
        assert c < 0 == True
        assert s.radius == 10
    
    def test_anagramma():
        assert a.is_anagramma("kalamajka","majkakaja") == True
        assert a.is_anagramma("kalamajka","majkakaja") == False
        assert a.is_anagramma("","majkakaja") == True