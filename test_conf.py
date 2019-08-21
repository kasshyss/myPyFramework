#!/usr/bin/env python
#-*- coding: utf-8 -*-

import lib.m_conf as conf
import lib.m_logger as log

import unittest
import os

logger = log.get_logger('test', log.get_logger_level('debug'))

logger.debug('Init')

current_path = os.path.dirname(os.path.realpath(__file__))
conf_path = os.path.join(current_path, 'testconf')

class TestConf(unittest.TestCase):

    def test_get_section_params_exceptions(self):
        # fct get_section
        with self.assertRaises(IOError):
                conf.get_section('','','')
        with self.assertRaises(TypeError):
                conf.get_section(1,'','')
        with self.assertRaises(TypeError):
                conf.get_section('',1,'')
        with self.assertRaises(TypeError):
                conf.get_section('','',1)
        # empty file
        with self.assertRaises(IOError):
            conf.get_section('test_empty.ini', conf_path, 'testo') 

    def test_get_section_normal_run(self):
        self.assertEqual(conf.get_section('normal_run.ini', conf_path,'TEST')['field1'],'toto')

    def test_get_conf_paramas_exceptions(self):
    # fct get_section
        with self.assertRaises(IOError):
                conf.get_conf('','')
        with self.assertRaises(TypeError):
                conf.get_conf(1,'')
        with self.assertRaises(TypeError):
                conf.get_conf('',1)



if __name__ == '__main__':
    unittest.main()
