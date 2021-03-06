# -*- coding: utf-8 -*-
#
## This file is part of ZENODO.
## Copyright (C) 2012, 2013 CERN.
##
## ZENODO is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## ZENODO is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with ZENODO. If not, see <http://www.gnu.org/licenses/>.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

from invenio.legacy.dbquery import run_sql

depends_on = ['openaire_2013_05_02_pidstore']


def info():
    return "Insert hbpro output format"


def do_upgrade():
    """ Implement your upgrades here  """
    res = run_sql("SELECT id FROM format WHERE code='hbpro'")
    if res:
        run_sql("""UPDATE format SET code='hbpro', content_type="text/html", name="HTML brief provisional", visibility=0, description="HTML brief provisional output format." WHERE code='hbpro'""")
    else:
        run_sql("""INSERT INTO format (content_type, name, visibility, description, code) VALUES ("text/html", "HTML brief provisional", 0, "HTML brief provisional output format.", 'hbpro')""")

    res = run_sql("SELECT id FROM format WHERE code='hdcur'")
    if res:
        run_sql("""UPDATE format SET code='hdcur', content_type="text/html", name="HTML detailed curation", visibility=0, description="HTML detailed curation output format." WHERE code='hdcur'""")
    else:
        run_sql("""INSERT INTO format (content_type, name, visibility, description, code) VALUES ("text/html", "HTML detailed curation", 0, "HTML detailed curation output format.", 'hdcur')""")
