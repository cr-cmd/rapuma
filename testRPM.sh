#!/bin/sh

rpm project_remove  -i vwxyz
rpm project_create  -t bookTex -n "Simple test project" -i vwxyz -d .

rpm component_add   -c jas                  -t usfm
#rpm component_add   -c apa                  -t adminMSEAG
#rpm component_add   -c m01                  -t vMapper
#rpm component_add   -c simpleNotes          -t projectNotes

#rpm auxiliary_add   -a contentMacros        -t usfmTex
rpm auxiliary_add   -a contentFont          -t fontsTex
#rpm auxiliary_add   -a mapFont              -t fontsTex
#rpm auxiliary_add   -a contentIllustrations -t illustrationsUsfm
#rpm auxiliary_add   -a contentHyphen        -t hyphenTex
#rpm auxiliary_add   -a contentComposition   -t pageCompTex
#rpm auxiliary_add   -a contentStyle         -t stylesUsfm


rpm set_font        -a contentFont          -f CharisSIL            -r primary

#rpm component_render -c apa
#rpm component_render -c m01
#rpm component_render -c simpleNotes

#rpm component_render -c jas



