"""

Tests for the module.py file in the subpackage folder.

"""

from pythonPackage.subpackage.module import subpackage_module_add_function


def test_subpackage_module_add_function():
    """
    Test the subpackage_module_add_function function.
    :return: None
    """
    assert subpackage_module_add_function(1, 2) == 3
