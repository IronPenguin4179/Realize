import unittest
from text_analysis import Realize, Class_obj
with open('example_files/example.py', 'r') as f:
    FILE = f.readlines()
    file_no_wht = []
    for line in FILE:
        if not line.isspace():
            file_no_wht.append(line)
    FILE_NO_WHT = file_no_wht.copy()

class TestRealizeMethods(unittest.TestCase):
    def setUp(self):
        self.realize = Realize(FILE_NO_WHT)

    #def test_upper(self):
    #    self.assertEqual('foo'.upper(), 'FOO')

    def test_add_class(self):
        self.realize.add_class("Rectangle",5)
        self.assertIsInstance(self.realize.classes_dict["Rectangle"][1],Class_obj)
    
    def test_find_classes(self):
        self.realize.find_classes()
        classes = self.realize.classes_dict

        self.assertEqual(classes["Rectangle"][1].class_name,"Rectangle")
        self.assertEqual(classes["Thing"][1].class_name,"Thing")

class TestClassObjMethods(unittest.TestCase):
    def setUp(self):
        self.cls_obj = Class_obj("Rectangle",5,FILE_NO_WHT)

    def test_find_class_instances(self):
        self.cls_obj.find_class_instances()
        print(self.cls_obj.class_instances)
    def test_find_methods(self):
        self.cls_obj.find_methods()
        print(self.cls_obj.method_calls)

if __name__ == '__main__':
    unittest.main()