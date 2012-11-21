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

client = CmisClient(CMISURL, CMISUSER, CMISPASS)

# Number of repositories
print "Number of repositories: %d" % len(client.repositories)

# List of all repositories
print '=======[ REPOSITORIES INFORMATIONS ]============='
for r in client.repositories:
    print 'Repository Name: %s' % r['repositoryName']
    print 'Reporistory ID: %s' % r['repositoryId']
    print '----'

print '=======[ END REPOSITORIES INFORMATIONS ]=========\n'

repo = client.defaultRepository

print '=======[ DEFAULT REPOSITORY ]===================='
print 'Repository fingerprint: ' + repo.id
print 'Repository name: ' + repo.name

info = repo.info
print '    [INFORMATION]'
for k, v in info.items():
    print '    %s: %s' % (k, v)
print '    -------------'




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
