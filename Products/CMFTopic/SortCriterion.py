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
""" Allow topic to specify sorting.

$Id$
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import InitializeClass
from zope.interface import implements

from Products.CMFTopic.AbstractCriterion import AbstractCriterion
from Products.CMFTopic.interfaces import ICriterion
from Products.CMFTopic.permissions import ChangeTopics
from Products.CMFTopic.permissions import View
from Products.CMFTopic.Topic import Topic


class SortCriterion( AbstractCriterion ):

    """
        Represent a mock criterion, to allow spelling the sort order
        and reversal items in a catalog query.
    """

    implements(ICriterion)

    meta_type = 'Sort Criterion'

    security = ClassSecurityInfo()

    field = None # Don't prevent use of field in other criteria

    _editableAttributes = ( 'reversed', )

    def __init__( self, id, index ):
        self.id = id
        self.index = index
        self.reversed = 0

    # inherit permissions
    def Field( self ):
        """
            Map the stock Criterion interface.
        """
        return self.index

    security.declareProtected( ChangeTopics, 'getEditForm' )
    def getEditForm( self ):
        """
            Return the name of skin method which renders the form
            used to edit this kind of criterion.
        """
        return 'sort_edit'

    security.declareProtected( ChangeTopics, 'edit' )
    def edit( self, reversed ):
        """
            Update the value we are to match up against.
        """
        self.reversed = bool(reversed)

    security.declareProtected(View, 'getCriteriaItems')
    def getCriteriaItems( self ):
        """
            Return a tuple of query elements to be passed to the catalog
            (used by 'Topic.buildQuery()').
        """
        result = [ ( 'sort_on', self.index ) ]

        if self.reversed:
            result.append( ( 'sort_order', 'reverse' ) )

        return tuple( result )

InitializeClass( SortCriterion )

# Register as a criteria type with the Topic class
Topic._criteriaTypes.append( SortCriterion )
