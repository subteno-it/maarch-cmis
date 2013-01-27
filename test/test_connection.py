##############################################################################
#
#    CMIS MARCH test module for OpenERP, Validate CMIS under MAarch
#    Copyright (C) 2012 SYLEAM (<http://www.syleam.fr>) Christophe CHAUVET
#
#    This file is a part of CMIS MARCH test
#
#    CMIS MARCH test is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    CMIS MARCH test is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from cmislib import CmisClient
from common import CMISURL, CMISUSER, CMISPASS

import pytest
import cmislib


def setup_module(module):
    try:
        module.TestConnection.client = CmisClient(CMISURL, CMISUSER, CMISPASS)
        module.TestConnection.client.getDefaultRepository()
    except cmislib.exceptions.PermissionDeniedException:
        pytest.fail('Connection error')
    except Exception, e:
        pytest.fail('Error ', str(e))

class TestConnection(object):


    def test_repositories(self):
        """
        Test all repositories (only one with Maarch)
        """
        for r in self.client.repositories:
            if 'repositoryName' not in r:
                pytest.fail('repositoryName is missing from repositories')
            if 'repositoryId' not in r:
                pytest.fail('repositoryId is missing from repositories')

    def test_default_repository(self):
        """
        Test the default repositories
        """
        repo = self.client.defaultRepository
        if not hasattr(repo, 'id'):
            pytest.fail('id is missing from repository object')
        if not hasattr(repo, 'name'):
            pytest.fail('name is missing from repository object')

    def test_default_repository_info(self):
        """
        Test the default repository
        """
        repo = self.client.defaultRepository
        info = repo.info
        assert info.get('cmisVersionSupported')
        assert info.get('repositoryDescription')
        assert info.get('productVersion')
        assert info.get('rootFolderId')
        assert info.get('repositoryId')
        assert info.get('repositoryName')
        assert info.get('vendorName')
        assert info.get('productName')
        # Check value
        assert info.get('vendorName') == 'Maarch'
        assert info.get('cmisVersionSupported') >= 1.0

    def test_default_repository_capa(self):
        """
        Test the default repository capabilities
        """
        repo = self.client.defaultRepository
        capa = repo.capabilities

        assert 'PWCUpdatable' in capa
        assert 'VersionSpecificFiling' in capa
        assert 'Join' in capa
        assert 'ContentStreamUpdatability' in capa
        assert 'AllVersionsSearchable' in capa
        assert 'Renditions' in capa
        assert 'Multifiling' in capa
        assert 'GetFolderTree' in capa
        assert 'GetDescendants' in capa
        assert 'ACL' in capa
        assert 'PWCSearchable' in capa
        assert 'Query' in capa
        assert 'Unfiling' in capa
        assert 'Changes' in capa

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
