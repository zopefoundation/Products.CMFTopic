##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Simple string-matching criterion class
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import InitializeClass
from zope.interface import implements

from Products.CMFTopic.AbstractCriterion import AbstractCriterion
from Products.CMFTopic.interfaces import ICriterion
from Products.CMFTopic.permissions import ChangeTopics
from Products.CMFTopic.permissions import View
from Products.CMFTopic.Topic import Topic


class SimpleStringCriterion( AbstractCriterion ):

    """ Represent a simple field-match for a string value.
    """

    implements(ICriterion)

    meta_type = 'String Criterion'

    security = ClassSecurityInfo()

    _editableAttributes = ( 'value', )

    def __init__(self, id, field):
        self.id = id
        self.field = field
        self.value = ''

    security.declareProtected( ChangeTopics, 'getEditForm' )
    def getEditForm( self ):
        """
            Return the skinned name of the edit form.
        """
        return 'ssc_edit'

    security.declareProtected( ChangeTopics, 'edit' )
    def edit( self, value ):
        """
            Update the value we are to match up against.
        """
        self.value = str( value )

    security.declareProtected(View, 'getCriteriaItems')
    def getCriteriaItems( self ):
        """
            Return a sequence of criteria items, used by Topic.buildQuery.
        """
        result = []

        if self.value is not '':
            result.append( ( self.field, self.value ) )

        return tuple( result )

InitializeClass( SimpleStringCriterion )

# Register as a criteria type with the Topic class
Topic._criteriaTypes.append( SimpleStringCriterion )
