import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.riittamaton = Maksukortti(200)

    def test_kassassa_oikea_maara_rahaa_aluksi(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisia_lounaita_myyty_aluksi(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaita_lounaita_myyty_aluksi(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_edullisissa_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateisosto_toimii_edullisissa_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_toimii_edullisissa_vaihtoraha(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(270)), '30')
    
    def test_kateisosto_toimii_edullisissa_riittamaton_maksu_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisosto_toimii_edullisissa_riittamaton_maksu_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_toimii_edullisissa_riittamaton_maksu_vaihtoraha(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(200)), '200')
    
    def test_kateisosto_toimii_maukkaissa_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kateisosto_toimii_maukkaissa_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_toimii_maukkaissa_vaihtoraha(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(450)), '50')
    
    def test_kateisosto_toimii_maukkaissa_riittamaton_maksu_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisosto_toimii_maukkaissa_riittamaton_maksu_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_toimii_maukkaissa_riittamaton_maksu_vaihtoraha(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(350)), '350')
    
    def test_korttiosto_toimii_edullisissa_kortti_veloitus(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
    
    def test_korttiosto_toimii_edullisissa_kortti_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_korttiosto_toimii_edullisissa_kortti_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_toimii_edullisissa_kortti_riittamaton_maksu_veloitus(self):
        self.kassapaate.syo_edullisesti_kortilla(self.riittamaton)
        self.assertEqual(str(self.riittamaton), "saldo: 2.0")

    def test_korttiosto_toimii_edullisissa_kortti_riittamaton_maksu_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.riittamaton)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_toimii_edullisissa_kortti_riittamaton_maksu_false(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.riittamaton))

    def test_korttiosto_toimii_edullisissa_kassa_sailyy(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttiosto_toimii_maukkaissa_kortti_veloitus(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
    
    def test_korttiosto_toimii_maukkaissa_kortti_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    
    def test_korttiosto_toimii_maukkaissa_kortti_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_toimii_maukkaissa_kortti_riittamaton_maksu_veloitus(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.riittamaton)
        self.assertEqual(str(self.riittamaton), "saldo: 2.0")

    def test_korttiosto_toimii_maukkaissa_kortti_riittamaton_maksu_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.riittamaton)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_toimii_maukkaissa_kortti_riittamaton_maksu_false(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.riittamaton))

    def test_korttiosto_toimii_maukkaissa_kassa_sailyy(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_ladatessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")
    
    def test_kortille_ladatessa_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_kortille_lataaminen_ei_onnistu_negatiivisella_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_lataaminen_ei_onnistu_negatiivisella_kortti(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")