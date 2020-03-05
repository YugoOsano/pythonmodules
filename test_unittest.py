# Effective Python Item 56
# Test everything with unittest

def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('Must be str or bytes, '
              'found: %r' % data)

from unittest import TestCase, main

class UtilsTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str, object())
        
if __name__ == '__main__':
    # raise verbosity
    # https://stackoverflow.com/questions/13034207/unittest-increase-modules-verbosity-when-tested
    main(verbosity=2)
    
