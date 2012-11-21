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

Under the directory test, you wil find some Python script to send query on Maarch

Change under test/common.py the URL and login/password for the user, with your information.

After launch python test/connection.py, you must see something similar

.. code-block:: 

    Number of repositories: 1
    
    =======[ REPOSITORIES INFORMATIONS ]=============
    Repository Name: Maarch main Repository
    Reporistory ID: e1125a70-33c0-11e2-81c1-0800200c9a66
    ----
    =======[ END REPOSITORIES INFORMATIONS ]=========
    
    =======[ DEFAULT REPOSITORY ]====================
    Repository fingerprint: e1125a70-33c0-11e2-81c1-0800200c9a66
    Repository name: Maarch main Repository
    
        [INFORMATION]
        cmisVersionSupported: 1.0
        repositoryDescription: Maarch main Repository
        productVersion: 1.4.0
        rootFolderId: workspace://
        repositoryId: e1125a70-33c0-11e2-81c1-0800200c9a66
        repositoryName: Maarch main Repository
        vendorName: Maarch
        productName: Maarch Entreprise
        -------------
