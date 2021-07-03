#!/usr/bin/env python
from metamodel.entities.MindMap import MindMap
from metamodel.entities.Marker import Marker
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Factory module for the MindMap metamodel.
"""

def factory(classname, name=""):
    if classname not in globals():
        return None
    klass = globals()[classname]
    return klass()
