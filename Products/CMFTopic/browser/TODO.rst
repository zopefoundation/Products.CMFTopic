Converting skins to views:
==========================

[x] ITopic @@view:
------------------
- [x] topic_view.py
- [x] topic_view_template.pt

[x] IMutableMinimalDublinCore @@properties (without acquireCriteria):
---------------------------------------------------------------------
- [x] topic_edit_control.py -> use @@properties from CMFDefault
- [x] topic_edit_form.py -> use @@properties from CMFDefault
- [x] topic_edit_template.pt -> use @@properties from CMFDefault

[x] IMutableTopic @@criteria (with acquireCriteria):
----------------------------------------------------
- [x] topic_addCriterion.py -> CriteriaView (ADD)
- [x] topic_deleteCriteria.py -> CriteriaView (DELETE)
- [x] topic_editCriteria.py -> CriteriaView (EDIT)
- [x] topic_criteria_form.pt -> topic_criteria.pt
- [x] acquireCriteria: topic_edit_control.py -> CriteriaView (EDIT)
- [x] acquireCriteria: topic_edit_form.py -> CriteriaView (EDIT)
- [x] acquireCriteria: topic_edit_template.pt -> topic_criteria.pt

[x] FriendlyDateCriterion @@edit:
---------------------------------
- [x] friendlydatec_editform.pt -> friendlydatec_editform.pt

[x] ListCriterion @@edit:
-------------------------
- [x] listc_edit.pt -> listc_edit.pt

[x] SimpleIntCriterion @@edit:
------------------------------
- [x] sic_edit.pt -> sic_edit.pt

[x] SimpleStringCriterion @@edit:
---------------------------------
- [x] ssc_edit.pt -> ssc_edit.pt

[x] SortCriterion @@edit:
-------------------------
- [x] sort_edit.pt -> sort_edit.pt

[x] ++resource++topic_icon.gif:
-------------------------------
- [x] topic_icon.gif
