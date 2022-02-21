# -*- coding: utf-8 -*-

import unittest

#import login
from login2 import Ui_MainWindow

class TestBasica(unittest.TestCase):
    
    #TEST  USUARIO 
    
    def test_setusuario(self):
                
        program=Ui_MainWindow()
        program.Setear_usuario("GENESIS")
        self.assertEqual(program.NOMBRE,"GENESIS")
        
        
    def test_len_usuario_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_usuario("ANA")
        usuario=program.Obtener_usuario()
        B=len(usuario)
        self.assertTrue(program.usuario_correct(B)=="Usuario debe tener 5-8 digitos") 
        
    def test_len2_usuario_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_usuario("GENESIS ANC")
        usuario=program.Obtener_usuario()
        B=len(usuario)
        self.assertTrue(program.usuario_correct(B)=="Usuario debe tener 5-8 digitos") 
    
    def test_usuario_incorrect(self):
        
        program=Ui_MainWindow()
        program.Setear_usuario("KARLA")
        usuario=program.Obtener_usuario()
        B=len(usuario)
        self.assertTrue(program.usuario_incorrect(B)=="Usuario incorrecto") 
        
        
    #TEST CONTRASENA 

    def test_setclave(self):
                
        program=Ui_MainWindow()
        program.Setear_clave("12345")
        self.assertEqual(program.CLAVE,"12345")
    

    def test_len_clave_correct(self):
       
        program=Ui_MainWindow()
        program.Setear_clave("12")
        clave=program.Obtener_clave()
        B=len(clave)
        self.assertTrue(program.clave_correct(B)=="Contrasena debe tener 4-6 digitos")
        
    def test_len2_clave_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_clave("1234567")
        clave=program.Obtener_clave()
        B=len(clave)
        self.assertTrue(program.clave_correct(B)=="Contrasena debe tener 4-6 digitos")
        
    def test_clave_incorrect(self):
        
        program=Ui_MainWindow()
        program.Setear_clave("genesis123")
        clave=program.Obtener_clave()
        B=len(clave)
        self.assertTrue(program.clave_incorrect(B)=="Contrasena incorrecta")
    
    #TEST OJOS CERRADOS/ABIERTOS

    def test_ojos_cerrados(self):
        program=Ui_MainWindow()
        self.assertEqual(program.ojos_cerrados(0.1),"Ojos cerrados")
        
    def test_ojos_abiertos(self):
        program=Ui_MainWindow()
        self.assertEqual(program.ojos_abiertos(0.3),"Ojos abiertos")
        
    def test_ojos(self):
        program=Ui_MainWindow()
        self.assertEqual(program.ojos(-1)," ")
        
    #TEST ALARMA

    def test_alarma_activada(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo(5),"Alarma activada")
        
    def test_alarma_activada_(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo(6),"Alarma activada")
        
    def test_alarma_sin_activar(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo(-3)," ")
        
    def test_alarma_sin_activar_(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo(0)," ")
        
        
    #TEST CONTEO ALARMA
    
    def test_veces_activacion(self):
        program=Ui_MainWindow()
        self.assertEqual(program.conteo_activacion(0),"La alarma no se activo")
    
    def test_veces_activacion_(self):
        program=Ui_MainWindow()
        self.assertEqual(program.conteo_activacion(1),1)
        
    def test_veces_activacion__(self):
        program=Ui_MainWindow()
        self.assertEqual(program.conteo_activacion(3),3)
        
        
    #TEST BOTON
    def test_boton_emergencia_activo(self):
        program=Ui_MainWindow()
        self.assertEqual(program.boton_act(1),"EMERGENCIA")
    
    def test_boton_emergencia_activo_(self):
        program=Ui_MainWindow()
        self.assertEqual(program.boton_act(0)," ")
        
    #TEST EXCEDE TIEMPO
    
    def test_excede_tiempo(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo_activacion(9),"Time out")
    
    def test_excede_activacion_(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo_activacion(8),"Time out")
        
    def test_excede_activacion__(self):
        program=Ui_MainWindow()
        self.assertEqual(program.tiempo_activacion(7),"")
        
    
    
    
if __name__=="__main__":
    unittest.main()