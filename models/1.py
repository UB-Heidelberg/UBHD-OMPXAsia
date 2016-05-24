# -*- coding: utf-8 -*-
'''
Copyright (c) 2015 Heidelberg University Library
Distributed under the GNU GPL v3. For full terms see the file
LICENSE.md
'''

import re
from gluon.custom_import import track_changes

if re.compile('\w{2}(\-\w{2})?').match(request.vars.lang or ''):
    session.forced_language = request.vars.lang
if session.forced_language:
    T.force(session.forced_language)
else:
    session.forced_language = 'de'
    T.force(session.forced_language)

track_changes(True)
