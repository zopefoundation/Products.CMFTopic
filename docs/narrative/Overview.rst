PortalTopic Overview
====================

*Note: this help file is old and being updated (ney, replaced) as
:doc:`Topics`

PortalTopics present collections of portal items according to catalog
searches formulated by the PortalTopic creator/configurer.

Visitors to a portal topic see a brief description of the topic, its
criteria, available subtopics, and the batch-browsable results.
(Eventually the visitor will be able to sort and filter the results to
their liking.  Initially, we will be providing rudimentary batched
browsing.)  Visitors will also see links to subtopics which refine the

PortalTopic configurers (the creator and anyone generally enabled to
configure a portal topic, according to site policy) can toggle the
browsing view to adjust the topic query criteria, adding, deleting,
and modifying textual, numeric, and list criteria against the site's
standard content metadata fields.

PortalTopic configurers will also be able to add new topic objects to
the topic that will act as subtopics, with their queries refining the
results of the containing topic query.  Subtopic nesting, and the
cumulative refinement, is unlimited.

Use Cases
---------

**Topic Visitor** browses topic on PortalTopic page --
  PortalTopics visitors see a (possibly empty) description of the
  topic, its (possibly) empty collectino of subtopics, and
  batch-browsable links to the topic contents.

  Visitor visits topic --
    ... sees topic description, subtopics, and first batch of topic
    contents links.

    Visitor browses topic collection --
      The visitor can follow a result link to the target contents,
      advance bakwards and forward in the results batch (if it's
      more than a single screenful),

    *(Not in v1.0.) Visitor twiddles filtering and sorting parameters* --
      *to adjust their view of the results.*

    Visitor navigates to subtopic --
      ... by following subtopic link.

    Visitor gets help about PortalTopics purpose and navigation --
    ... by hitting help button.  *(Just this design doc, in v1.0.)*

    * (Not in v1.0.)  Eventually, when returning to a topic, the
    visitor's view resumes with batch, sort, and filter state as
    they last left it.  For now, they return to start.*

**Topic configurer** configures topic
  Configurers can toggle the view of the topic to reveal controls
  for adjusting the topic description, subtopics, and topic query
  criteria.

  Topic configurer adjusts topic criteria --
    Configurer hits a button that opens the configuration form,
    showing a view of the same topic, with:

    * A text area for the filling in the topic description

    * An add/delete/rename list of subtopics, for managing
      their containment.

    * A section for changing the topic criteria.

      The top of the section is a table with columns for string,
      integer, and list criteria entries.  The bottom is a row of
      buttons: "Submit Changes", "Delete Checked", and "Reset"

      Table entries for already set criteria will consist of a
      checkbox, the criterion field name, and an input box for the
      value.  The checkbox indicates entries to be deleted.

      The bottom of each column will have a "blank" entry, for
      adding a new criterion.  It will be like the existing
      entries but it will not have the checkbox, and its initial
      value will be empty.

    - *(Not in v1.0.) A control for designating whether or not to
      apply the topic query.  (The topic may only be for
      collecting and specifying the common aspects of a query for
      it's subtopics).*

  The qeury results will display as they would for a regular visitor.

  Topic configurer gets help about configuring PortalTopics --
    ... by hitting help button.  *(Just this design doc, in v1.0.)*
