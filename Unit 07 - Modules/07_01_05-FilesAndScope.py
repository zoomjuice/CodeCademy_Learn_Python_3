"""
Scope also applies to classes and to the files you are working within.

Files are actually modules, so you can give a file access to another file's content using an import statement.
"""

# Import library below:
decimod = __import__('07_01_04-DecimalModule')

# Call your function below:
print(decimod.test_function_please_ignore())
