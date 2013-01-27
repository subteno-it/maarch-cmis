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

import os

CMISURL = os.environ.get('CMIS_HOST', 'http://www.maarch-cmis.local/ws_server.php/?CMIS')
CMISUSER = os.environ.get('CMIS_USER','superadmin')
CMISPASS = os.environ.get('CMIS_PASS', 'admin')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
