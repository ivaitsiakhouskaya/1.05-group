import requests
import unittest

class TestStringMethods(unittest.TestCase):

  def test_onliner(self):
    r = requests.get('https://onliner.by')
    assert r.status_code == 200, 'Onliner not work corret'
    




  def test_mail_ru(self):
    r = requests.get('https://mail.ru')
    assert r.status_code == 200, 'mail.ru not work corret'


   
  def test_vk_com(self):
    r = requests.get('https://vk.com')
    assert r.status_code == 200, 'vk.com not work corret' 
    
if __name__ == '__main__':
    unittest.main()
  






