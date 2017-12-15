# -*- coding: utf-8 -*-
#
# Copyright (c), 2016-2017, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
"""
This module contains the exception classes of the 'xmlschema' package.
"""
from .compat import URLError


class XMLSchemaException(Exception):
    """The base exception that let you catch all the errors generated by the library."""
    pass


class XMLSchemaOSError(XMLSchemaException, OSError):
    pass


class XMLSchemaAttributeError(XMLSchemaException, AttributeError):
    pass


class XMLSchemaTypeError(XMLSchemaException, TypeError):
    pass


class XMLSchemaValueError(XMLSchemaException, ValueError):
    pass


class XMLSchemaSyntaxError(XMLSchemaException, SyntaxError):
    pass


class XMLSchemaKeyError(XMLSchemaException, KeyError):
    pass


class XMLSchemaURLError(XMLSchemaException, URLError):
    pass


class XMLSchemaRegexError(XMLSchemaException, ValueError):
    """Raised when an error is found when parsing an XML Schema regular expression."""
    pass


class XMLSchemaXPathError(XMLSchemaException, ValueError):
    """Raised when an error is found when parsing an XPath expression."""
    pass
