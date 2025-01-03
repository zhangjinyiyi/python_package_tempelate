#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File    :   setup.py
@Time    :   2024/06/08 12:51:46
@Author  :   Jinyi Zhang 
@Version :   1.0
@Contact :   zhangjinyi.cn@hotmail.com
@License :   (C)Copyright 2023-2024, Jinyi Zhang
@Desc    :   None
"""

import re
from setuptools import setup
import os
from datetime import datetime


def get_property(prop):
    """get project properties

    Args:
        prop (str): property
        project (str): project name

    Returns:
        str: property value
    """
    init_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "__init__.py")
    try:
        result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(init_file).read())
        return result.group(1)
    except:
        if prop == "__version__":
            return "0.0.0"
        else:
            return ""
    

author = get_property('__author__')
author_email = get_property('__author_email__')
description = get_property('__description__')
version = get_property('__version__')

package_dir = os.path.dirname(os.path.abspath(__file__))
project_name = os.path.basename(package_dir)
packages = [project_name]
packages += [project_name + "." + name for name in os.listdir(package_dir) if os.path.isdir(os.path.join(package_dir, name))]

setup(
    name=project_name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    packages=packages,
    package_dir={project_name: package_dir}
)
            






