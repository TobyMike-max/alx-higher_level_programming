#!/usr/bin/python3
# test_base.py
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.Testcase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(22, Base(22).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(23)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 20
        self.assertEqual(20, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instances)

    def test_str_id(self):
        self.assertEqual("Good-day", Base("Good-day").id)

    def test_float(self):
        self.assertEqual(4.5, Base(4.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(8), Base(complex(8)).id)

    def test_dict_id(self):
        self.assertEqual({'one': 1, 'two': 2}, Base({'one': 1, 'two': 2}).id)

    def test_true_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([20, 5, 7], Base([20, 5, 7]).id)

    def test_tuple_id(self):
        self.assertEqual((9, 20), Base((9, 20)).id)

    def test_set_id(self):
        self.assertEqual({2, 4, 6}, Base({2, 4, 6}).id)

    def test_range_id(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Hello', Base(b'Hello').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'jesus'), Base(bytearray(b'jesus')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
