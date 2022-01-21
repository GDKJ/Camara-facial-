# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:38:48 2022

@author: juni_
"""
import unittest

#import login
from login2 import Ui_MainWindow



class TestBasica(unittest.TestCase):
    
    #TEST DE SETEADO USUARIO 
    def test_1setusuario(self):
                
        program=Ui_MainWindow()
        program.Setear_usuario("OJO AL GATO")
        self.assertEqual(program.NOMBRE,"OJO AL GATO")
   
    def test_2setusuario(self):
                
        program=Ui_MainWindow()
        program.Setear_usuario("KARLA")
        self.assertEqual(program.NOMBRE,"KARLA")
        
    
    
    def test_3setusuario(self):
                
        program=Ui_MainWindow()
        program.Setear_usuario("GENESIS")
        self.assertNotEqual(program.NOMBRE,"KARLA")
        
    #TEST DE SETEADO CONTRASENA 

    def test_1setclave(self):
                
        program=Ui_MainWindow()
        program.Setear_clave("12345")
        self.assertEqual(program.CLAVE,"12345")
        
        
    def test_2setclave(self):
                
        program=Ui_MainWindow()
        program.Setear_clave("12345")
        self.assertNotEqual(program.CLAVE,"123456")
    
           
    #TEST DE OBTENCION USUARIO
    
    def test_1ObtUsuario(self):
        program=Ui_MainWindow()
        program.Setear_usuario("PRUEBA")       
        self.assertEqual(program.NOMBRE,"PRUEBA")
        usuario=program.Obtener_usuario()
        self.assertEqual(usuario,"PRUEBA")
        
    def test_2ObtUsuario(self):
        program=Ui_MainWindow()
        program.Setear_usuario("PRUEBA")       
        self.assertEqual(program.NOMBRE,"PRUEBA")
        usuario=program.Obtener_usuario()
        self.assertNotEqual(usuario,"PRUEBAS")
    
    #TEST DE OBTENCION CONTRASENA
    
    def test_ObtClave(self):
        program=Ui_MainWindow()
        program.Setear_clave("12345")       
        self.assertEqual(program.CLAVE,"12345")
        clave=program.Obtener_clave()
        self.assertEqual(clave,"12345")

    def test_2ObtClave(self):
        program=Ui_MainWindow()
        program.Setear_clave("12345")       
        self.assertEqual(program.CLAVE,"12345")
        clave=program.Obtener_clave()
        self.assertNotEqual(clave,"123456")    
    
    
    #TEST DE CONDICIONES USUARIO
    
    def test_len_usuario_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_usuario("GENESIS")
        usuario=program.Obtener_usuario()
        B=len(usuario)
        self.assertTrue(program.usuario_correct(B)==1)
    def test_len_usuario_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_usuario("DAYANA")
        usuario=program.Obtener_usuario()
        B=len(usuario)
        self.assertTrue(program.usuario_correct(B)==1)    
        
    def test_len_usuario_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_usuario("GENESIS ANCHUNDIA")
        usuario=program.Obtener_usuario()
        B=len(usuario)
        self.assertFalse(program.usuario_correct(B)==1)
    
    #TEST DE CONDICIONES CONTRASENA
        
    def test_len_clave_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_clave("12345")
        clave=program.Obtener_clave()
        B=len(clave)
        self.assertTrue(program.clave_correct(B)==1)
        
        
    def test_len_clave_correct(self):
        
        program=Ui_MainWindow()
        program.Setear_clave("12")
        clave=program.Obtener_clave()
        B=len(clave)
        self.assertFalse(program.clave_correct(B)==1)
        
    
    
if __name__=="__main__":
    unittest.main()