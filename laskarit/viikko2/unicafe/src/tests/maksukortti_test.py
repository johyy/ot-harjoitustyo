import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 2.1")
    
    def test_saldo_vahenee_nostaessa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_palauttaa_true_jos_rahat_riittavat(self):
        self.assertTrue(self.maksukortti.ota_rahaa(8))

    def test_palauttaa_false_jos_rahat_eivat_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(20))