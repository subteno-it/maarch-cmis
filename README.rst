maarch-cmis
===========

Test script for validate implementation for CMIS under Maarch

First step, Install Trunk version for Maarch Entreprise


.. code-block::

    mkdir maarch_entreprise 
    cd maarch_entreprise
    svn checkout http://svn.maarch.org/core/trunk                       .
    svn checkout http://svn.maarch.org/maarch_entreprise/trunk          apps/maarch_entreprise
    svn checkout http://svn.maarch.org/advanced_physical_archive/trunk  modules/advanced_physical_archive
    svn checkout http://svn.maarch.org/attachments/trunk                modules/attachments
    svn checkout http://svn.maarch.org/autofoldering/trunk              modules/autofoldering
    svn checkout http://svn.maarch.org/basket/trunk                     modules/basket
    svn checkout http://svn.maarch.org/cases/trunk                      modules/cases
    svn checkout http://svn.maarch.org/content_management/trunk         modules/content_management
    svn checkout http://svn.maarch.org/entities/trunk                   modules/entities
    svn checkout http://svn.maarch.org/esign/trunk                      modules/esign
    svn checkout http://svn.maarch.org/folder/trunk                     modules/folder
    svn checkout http://svn.maarch.org/full_text/trunk                  modules/full_text
    svn checkout http://svn.maarch.org/ldap/trunk                       modules/ldap
    svn checkout http://svn.maarch.org/life_cycle/trunk                 modules/life_cycle
    svn checkout http://svn.maarch.org/notes/trunk                      modules/notes
    svn checkout http://svn.maarch.org/notifications/trunk              modules/notifications
    svn checkout http://svn.maarch.org/physical_archive/trunk           modules/physical_archive
    svn checkout http://svn.maarch.org/postindexing/trunk               modules/postindexing
    svn checkout http://svn.maarch.org/record_patrol/trunk              modules/record_patrol
    svn checkout http://svn.maarch.org/reports/trunk                    modules/reports
    svn checkout http://svn.maarch.org/tags/trunk                       modules/tags
    svn checkout http://svn.maarch.org/templates/trunk                  modules/templates

Under the directory test, you will find some unittest to find regressions

Change under test/common.py the URL and login/password for the user, with your information.

After launch make test, you must see something similar

.. code-block:: 

    platform linux2 -- Python 2.6.5 -- pytest-2.3.4 -- /home/alncchau/Envs/cmis/bin/python
    collected 5 items 
    
    test/test_connection.py:29: test_connection PASSED
    test/test_connection.py:39: test_repositories PASSED
    test/test_connection.py:50: test_default_repository PASSED
    test/test_connection.py:61: test_default_repository_info PASSED
    test/test_connection.py:80: test_default_repository_capa PASSED



