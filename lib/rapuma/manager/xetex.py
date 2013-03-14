#!/usr/bin/python
# -*- coding: utf_8 -*-
# version: 20111207
# By Dennis Drescher (dennis_drescher at sil.org)

###############################################################################
######################### Description/Documentation ###########################
###############################################################################

# This manager class will handle component rendering with XeTeX.



###############################################################################
################################# Project Class ###############################
###############################################################################
# Firstly, import all the standard Python modules we need for
# this process

import os, shutil, re
import subprocess

# Load the local classes
from rapuma.core.tools import *
from rapuma.project.manager import Manager
from rapuma.group.usfm import PT_Tools
from rapuma.core.proj_config import ConfigTools


###############################################################################
################################## Begin Class ################################
###############################################################################

class Xetex (Manager) :

    # Shared values
    xmlConfFile     = 'xetex.xml'

    def __init__(self, project, cfg, cType) :
        '''Do the primary initialization for this manager.'''

        super(Xetex, self).__init__(project, cfg)

        # Create all the values we can right now for this manager.
        # Others will be created at run time when we know the cid.
        self.project                = project
        self.local                  = project.local
        self.cfg                    = cfg
        self.gid                    = project.gid
        self.cType                  = cType
        self.Ctype                  = cType.capitalize()
        self.renderer               = 'xetex'
        self.manager                = self.cType + '_' + self.renderer.capitalize()
        self.managers               = project.managers
        self.pt_tools               = PT_Tools(project)
        self.configTools            = ConfigTools(project)
        # Bring in some manager objects we will need
        if self.cType + '_Hyphenation' not in self.manager :
            self.project.createManager(self.cType, 'hyphenation')
        self.hyphenation = self.managers[self.cType + '_Hyphenation']
        if self.cType + '_Layout' not in self.managers :
            self.project.createManager(self.cType, 'layout')
        self.layout = self.managers[self.cType + '_Layout']
        if self.cType + '_Font' not in self.managers :
            self.project.createManager(self.cType, 'font')
        self.font = self.managers[self.cType + '_Font']
        # Get config objs
        self.projConfig             = project.projConfig
        self.layoutConfig           = self.layout.layoutConfig
        self.fontConfig             = self.font.fontConfig
        self.userConfig             = self.project.userConfig
        # Some config settings
        self.pdfViewer              = self.projConfig['Managers'][self.manager]['pdfViewerCommand']
        self.pdfUtilityCommand      = self.projConfig['Managers'][self.manager]['pdfUtilityCommand']
        self.sourceEditor           = self.projConfig['CompTypes'][self.Ctype]['sourceEditor']
        self.macroPackage           = self.projConfig['Managers'][self.manager]['macroPackage']

        # Get settings for this component
        self.managerSettings = self.projConfig['Managers'][self.manager]
        for k, v in self.managerSettings.iteritems() :
            if v == 'True' or v == 'False' :
                setattr(self, k, str2bool(v))
            else :
                setattr(self, k, v)

        # Set some Booleans (this comes after persistant values are set)
        self.usePdfViewer           = str2bool(self.projConfig['Managers'][self.manager]['usePdfViewer'])
        self.useHyphenation         = str2bool(self.projConfig['Managers'][self.cType + '_Hyphenation']['useHyphenation'])
        self.useMarginalVerses      = str2bool(self.layoutConfig['ChapterVerse']['useMarginalVerses'])
        self.useIllustrations       = self.layoutConfig['Illustrations']['useIllustrations']

        # File names
        # Some of these file names will only be used once but for consitency
        # we will create them all in one place.
        self.ptxMargVerseFileName   = 'ptxplus-marginalverses.tex'
        self.macLinkFileName        = self.cType + '_macLink.tex'
        self.setTexFileName         = self.cType + '_set.tex'
        self.extTexFileName         = self.cType + '_set-ext.tex'
        self.grpExtTexFileName      = self.gid + '_' + self.cType + '-ext.tex'
        self.styFileName            = self.cType + '.sty'
        self.extStyFileName         = self.cType + '-ext.sty'
        self.grpExtStyFileName      = self.gid + '_' + self.cType + '-ext.sty'
        self.lccodeFileName         = self.hyphenation.compLccodeFileName
        self.compHyphFileName       = self.hyphenation.compHyphenFileName
        self.hyphExcepTexFileName   = self.cType + '_hyphenation.tex'
        # Folder paths
        self.rapumaMacrosFolder     = self.local.rapumaMacrosFolder
        self.rapumaMacPackFolder    = os.path.join(self.rapumaMacrosFolder, self.macroPackage)
        self.rapumaConfigFolder     = self.local.rapumaConfigFolder
        self.projConfFolder         = self.local.projConfFolder
        self.projComponentsFolder   = self.local.projComponentsFolder
        self.gidFolder              = os.path.join(self.projComponentsFolder, self.gid)
        self.projHyphenationFolder  = self.local.projHyphenationFolder
        self.projFontsFolder        = self.local.projFontsFolder
        self.projStylesFolder       = self.local.projStylesFolder
        self.projMacrosFolder       = self.local.projMacrosFolder
        self.projMacPackFolder      = os.path.join(self.local.projMacrosFolder, self.macroPackage)
        # Set file names with full path 
        self.ptxMargVerseFile       = os.path.join(self.projMacPackFolder, self.ptxMargVerseFileName)
        self.layoutXmlFile          = os.path.join(self.rapumaConfigFolder, self.project.projectMediaIDCode + '_layout.xml')
        self.layoutConfFile         = os.path.join(self.projConfFolder, self.project.projectMediaIDCode + '_layout.conf')
        self.fontConfFile           = os.path.join(self.projConfFolder, 'font.conf')
        self.illustrationConfFile   = os.path.join(self.projConfFolder, 'illustration.conf')
        self.projConfFile           = os.path.join(self.projConfFolder, 'project.conf')
        self.macLinkFile            = os.path.join(self.projMacrosFolder, self.macLinkFileName)
        self.setTexFile             = os.path.join(self.projMacrosFolder, self.setTexFileName)
        self.extTexFile             = os.path.join(self.projMacrosFolder, self.extTexFileName)
        self.grpExtTexFile          = os.path.join(self.projMacrosFolder, self.grpExtTexFileName)
        self.usrGrpExtTexFile       = os.path.join(self.project.userConfig['Resources']['macros'], self.grpExtTexFile)
        self.styFile                = os.path.join(self.projStylesFolder, self.styFileName)
        self.extStyFile             = os.path.join(self.projStylesFolder, self.extStyFileName)
        self.grpExtStyFile          = os.path.join(self.projStylesFolder, self.grpExtStyFileName)
        self.rpmExtTexFile          = os.path.join(self.rapumaMacrosFolder, self.extTexFileName)
        self.usrExtTexFile          = os.path.join(self.project.userConfig['Resources']['macros'], self.extTexFileName)
        self.lccodeFile             = os.path.join(self.projHyphenationFolder, self.lccodeFileName)
        self.compHyphFile           = os.path.join(self.projHyphenationFolder, self.compHyphFileName)
        self.hyphExcepTexFile       = os.path.join(self.projHyphenationFolder, self.hyphExcepTexFileName)

        # Make any dependent folders if needed
        if not os.path.isdir(self.gidFolder) :
            os.mkdir(self.gidFolder)

        # Check to see if the PDF viewer is ready to go
        if not self.pdfViewer :
            defaultViewer = self.project.userConfig['System']['pdfDefaultViewerCommand']
            self.pdfViewer = defaultViewer
            self.projConfig['Managers'][self.manager]['pdfViewerCommand'] = defaultViewer
            writeConfFile(self.projConfig)

        # Record some error codes
        # FIXME: much more needs to be done with this
        self.xetexErrorCodes =  {
            0   : 'Rendering succeful.',
            256 : 'Something really awful happened.'
                                }


###############################################################################
############################ Manager Level Functions ##########################
###############################################################################

    def rtnBoolDepend (self, bdep) :
        '''Return the boolean value of a boolDepend target. This assumes that
        the format is config:section:key, or config:section:section:key, if
        it ever becomes different, this breaks. The config is expected to be 
        the common internal reference so consitency is absolutly necessary for 
        this to work.'''

        parts = bdep.split(':')
        ptn = len(parts)
        cfg = getattr(self, parts[0])
        if ptn == 3 :
            sec = parts[1]
            key = parts[2]
            if self.configTools.hasPlaceHolder(sec) :
                (holderType, holderKey) = self.configTools.getPlaceHolder(sec)
                # system (self) delclaired value
                if holderType == 'self' :
                    sec = self.configTools.insertValue(sec, getattr(self, holderKey))
            return cfg[sec][key]
        if ptn == 4 :
            secA = parts[1]
            secB = parts[2]
            key = parts[3]
            if self.configTools.hasPlaceHolder(secB) :
                (holderType, holderKey) = self.configTools.getPlaceHolder(secB)
                # system (self) delclaired value
                if holderType == 'self' :
                    secB = self.configTools.insertValue(secB, getattr(self, holderKey))
            return cfg[secA][secB][key]


    def texFileHeader (self, fName) :
        '''Create a generic file header for a non-editable .tex file.'''

        return '% ' + fName + ' created: ' + tStamp() + '\n' \
            + '% This file is auto-generated, do not bother editing it\n\n'


    def copyInMargVerse (self) :
        '''Copy in the marginalverse macro package.'''

        macrosTarget    = os.path.join(self.local.projMacrosFolder, self.macroPackage)
        macrosSource    = os.path.join(self.local.rapumaMacrosFolder, self.macroPackage)

        # Copy in to the process folder the macro package for this component
        if not os.path.isdir(macrosTarget) :
            os.makedirs(macrosTarget)

        if not os.path.isfile(self.ptxMargVerseFile) :
            shutil.copy(os.path.join(macrosSource, fName(self.ptxMargVerseFile)), self.ptxMargVerseFile)
            self.project.log.writeToLog('XTEX-070', [fName(self.ptxMargVerseFile)])
            return True


    def removeMargVerse (self) :
        '''Remove the marginal verse macro package from the project.'''

        if os.path.isfile(self.ptxMargVerseFile) :
            os.remove(self.ptxMargVerseFile)
            return True


    def makeTexSettingsDict (self, xmlFile) :
        '''Create a dictionary object from a layout xml file. This will track two kinds of
        bool settings for both True and False so setting output can be determined depending
        on what kind of bool it is. boolDependFalse is a very rare case though. Nonetheless
        those are tracked for each setting regardless of their use.'''

        if  os.path.exists(xmlFile) :
            # Read in our XML file
            doc = ElementTree.parse(xmlFile)
            # Create an empty dictionary
            data = {}
            # Extract the section/key/value data
            thisSection = ''; thisTex = ''; thisBoolDepTrue = ''; thisBoolDepFalse = ''
            for event, elem in ElementTree.iterparse(xmlFile):
                if elem.tag == 'setting' :
                    if thisTex or thisBoolDepTrue or thisBoolDepFalse:
                        data[thisSection] = {self.macroPackage : thisTex, 'boolDependTrue' : thisBoolDepTrue, 'boolDependFalse' : thisBoolDepFalse}
                    thisSection = ''
                    thisTex = ''
                    thisBoolDepTrue = ''
                    thisBoolDepFalse = ''
                if elem.tag == 'key' :
                    thisSection = elem.text
                elif elem.tag == self.macroPackage :
                    thisTex = elem.text
                elif elem.tag == 'boolDependTrue' :
                    thisBoolDepTrue = elem.text
                elif elem.tag == 'boolDependFalse' :
                    thisBoolDepFalse = elem.text
            # Ship it!
            return data
        else :
            raise IOError, "Can't open " + xmlFile


    def copyInMacros (self) :
        '''Copy in the right macro set for this component and renderer combination.'''

        if self.cType.lower() == 'usfm' :

            # Copy in to the process folder the macro package for this component
            if not os.path.isdir(self.projMacPackFolder) :
                os.makedirs(self.projMacPackFolder)

            mCopy = False
            for root, dirs, files in os.walk(self.rapumaMacPackFolder) :
                for f in files :
                    fTarget = os.path.join(self.projMacPackFolder, f)
                    if not os.path.isfile(fTarget) :
                        shutil.copy(os.path.join(self.rapumaMacPackFolder, f), fTarget)
                        mCopy = True
                        self.project.log.writeToLog('XTEX-070', [fName(fTarget)])

            return mCopy
        else :
            self.project.log.writeToLog('XTEX-075', [self.cType])


    def displayPdfOutput (self, pdfFile) :
        '''Display a PDF XeTeX output file if that is turned on.'''

#        import pdb; pdb.set_trace()
        if self.usePdfViewer :
            # Build the viewer command
            self.pdfViewer.append(pdfFile)
            # Run the XeTeX and collect the return code for analysis
            try :
                subprocess.Popen(self.pdfViewer)
                # FIXME: We need to pop() the last item (pdfFile)
                # to avoid it somehow being writen out to the proj.conf
                self.pdfViewer.pop()
                return True
            except Exception as e :
                # If we don't succeed, we should probably quite here
                self.project.log.writeToLog('XTEX-105', [str(e)])


    def makeHyphenExceptionFile (self) :
        '''Create a TeX hyphenation file. There must be a texWordList for this
        to work properly.'''

        # Create the output file here
        with codecs.open(self.hyphenTex, "w", encoding='utf_8') as hyphenTexObject :
            hyphenTexObject.write('% ' + fName(self.hyphenTex) + '\n')
            hyphenTexObject.write('% This is an auto-generated hyphenation rules file for this project.\n')
            hyphenTexObject.write('% Please refer to the documentation for details on how to make changes.\n\n')
            hyphenTexObject.write('\hyphenation{\n')
            # Look for the intermediate component hyphenation file, remake if needed
            # Go get the file if it is to be had
            if not os.path.isfile(self.compHyphen) :
                # Call the Hyphenation manager to create a sorted file of hyphenated words
                self.hy_tools.updateHyphenation(self.cType)
            with codecs.open(self.compHyphen, "r", encoding='utf_8') as hyphenWords :
                for word in hyphenWords :
                    # Strip out commented lines/words
                    if word[:1] != '#' and word != '' :
                        # Swap the generic hyphen markers out if they are there
                        hyphenTexObject.write(re.sub(u'<->', u'-', word))

            hyphenTexObject.write('}\n')

        return True


    def makeLccodeFile (self) :
        '''Make a simple starter lccode file to be used with TeX hyphenation.'''

        # Create the file and put default settings in it
        with codecs.open(self.lccodeTex, "w", encoding='utf_8') as lccodeObject :
            lccodeObject.write('% ' + fName(self.lccodeTex) + '\n')
            lccodeObject.write('% This is an auto-generated lccode rules file for this project.\n')
            lccodeObject.write('% Please refer to the documentation for details on how to make changes.\n\n')
            lccodeObject.write('\lccode "2011 = "2011	% Allow TeX hyphenation to ignore a Non-break hyphen\n')
            # Add in all our non-word-forming characters as found in our PT project
            for c in self.pt_tools.getNWFChars() :
                uv = rtnUnicodeValue(c)
                # We handel these chars special in this context
                if not uv in ['2011', '002D'] :
                    lccodeObject.write('\lccode "' + uv + ' = "' + uv + '\n')

            # Add special exceptions
            lccodeObject.write('\catcode "2011 = 11	% Changing the catcode here allows the \lccode above to work\n')

        return True



###############################################################################
############################# DEPENDENCY FUNCTIONS ############################
###############################################################################

    def makeMacLinkFile (self) :
        '''Check for the exsistance of or the age of the macLink dependent file.
        Create or refresh if needed. If there are any problems, report and die.'''

        # Set some file names
        if self.macroPackage == 'usfmTex' :
            mainMacroFile = os.path.join(self.projMacPackFolder, 'paratext2.tex')
        elif self.macroPackage == 'usfmTex-auto' :
            mainMacroFile = os.path.join(self.projMacPackFolder, 'paratext2.tex')
        else :
            self.project.log.writeToLog('XTEX-115', [self.macroPackage])

        # Check to see if our macros are there
        if not os.path.isdir(self.projMacPackFolder) :
            self.copyInMacros()

        # Check for existance and age. List any files in this next list that
        # could require the rebuilding of the link file
        makeLinkFile = False
        dep = [mainMacroFile, self.fontConfFile, self.layoutConfFile, self.projConfFile]
        if not os.path.isfile(self.macLinkFile) :
            makeLinkFile = True
            self.project.log.writeToLog('XTEX-065', [fName(self.macLinkFile)])
        else :
            for f in dep :
                if isOlder(self.macLinkFile, f) :
                    makeLinkFile = True
                    self.project.log.writeToLog('XTEX-060', [fName(f),fName(self.macLinkFile)])

        if makeLinkFile :
            with codecs.open(self.macLinkFile, "w", encoding='utf_8') as writeObject :
                writeObject.write(self.texFileHeader(fName(self.macLinkFile)))
                writeObject.write('\\input ' + quotePath(mainMacroFile) + '\n')
                # If we are using marginal verses then we will need this
                if self.useMarginalVerses :
                    self.copyInMargVerse()
                    writeObject.write('\\input ' + quotePath(self.ptxMargVerseFile) + '\n')
                else :
                    self.removeMargVerse()

        return True


    def makeSetTexFile (self) :
        '''Create the main settings file that XeTeX will use in gidTex to render 
        gidPdf. This is a required file so it will run every time. However, it
        may not need to be remade. We will look for its exsistance and then compare 
        it to its primary dependents to see if we actually need to do anything.'''

        # Set vals
        dep = [self.layoutConfFile, self.fontConfFile, self.projConfFile]
        makeIt = False

        # Check for existance and age
#        import pdb; pdb.set_trace()
        if os.path.isfile(self.setTexFile) :
            for f in dep :
                if isOlder(self.setTexFile, f) :
                    # Something changed in a conf file this is dependent on
                    makeIt = True
                    break
        else :
            makeIt = True

        # Bail out here if necessary, return True because everything seems okay
        if not makeIt :
            return True
        else :
            # Otherwise make/remake the file
            macTexVals = dict(self.makeTexSettingsDict(self.layoutXmlFile))

            writeObject = codecs.open(self.setTexFile, "w", encoding='utf_8')
            writeObject.write(self.texFileHeader(fName(self.setTexFile)))

            # Bring in the settings from the layoutConfig
            for section in self.layoutConfig.keys() :
                writeObject.write('\n% ' + section + '\n')
                vals = {}

                # Do a precheck here for input order that could affect the section.
                # Be on the look out for an input ordering field. If there is one
                # it should have two or more items in the list this becomes the
                # base for our inputsOrder list used for output
                try :
                    # This setting must have a boolDepend, check what it is here
                    if str2bool(self.rtnBoolDepend(macTexVals['inputsOrder']['boolDependTrue'])) :
                        inputsOrder = self.layoutConfig[section]['inputsOrder']
                    else :
                        inputsOrder = []
                except :
                    inputsOrder = []

                # Start gathering up all the items in this section now
                for k, v in self.layoutConfig[section].iteritems() :
                    # This will prevent output on empty fields, never output when
                    # there is no value
                    if not v :
                        continue
                    # Gather each macro package line we need to output
                    if testForSetting(macTexVals, k, self.macroPackage) :
                        macVal = (macTexVals[k][self.macroPackage])
                        # Test for boolDepend True and False. If there is a boolDepend
                        # then we don't need to output just yet. These next two if/elif
                        # statements insure that output happens in the proper condition.
                        # In some cases we want output only if a certain bool is set to
                        # true, but in a few rare cases we want output when a certain
                        # bool is set to false. These will screen for both cases.
                        if testForSetting(macTexVals, k, 'boolDependTrue') and not str2bool(self.rtnBoolDepend(macTexVals[k]['boolDependTrue'])) :
                            continue
                        elif testForSetting(macTexVals, k, 'boolDependFalse') and not str2bool(self.rtnBoolDepend(macTexVals[k]['boolDependFalse'])) == False :
                            continue
                        # After having made it past the previous two tests, we can ouput now.
                        else :
                            # Here we will build a dictionary for this section made up
                            # of all the k, v, and macVals needed. We also build a
                            # list of keys to be used for ordered output
                            vals[k] = [v, macVal]
                            if not k in inputsOrder :
                                # In case there was an inputsOrder list in the config,
                                # this will prepend the value to that list. The idea is
                                # that the ordered output goes last (or at the bottom)
                                inputsOrder.insert(0, k)

                # Write the lines out according to the inputsOrder
                for key in inputsOrder :
                    writeObject.write(self.configTools.processLinePlaceholders(vals[key][1], vals[key][0]) + '\n')

            # Move on to Fonts, add all the font def commands
            def addParams (writeObject, pList, line) :
                for k,v in pList.iteritems() :
                    if v :
                        line = line.replace(k, v)
                    else :
                        line = line.replace(k, '')
                # Clean out unused placeholders
                line = re.sub(u"\^\^[a-z]+\^\^", "", line)
                # Remove unneeded colon from the end of the string
                line = re.sub(u":\"", "\"", line)
                # Write it out
                writeObject.write(line + '\n')

            writeObject.write('\n% Font Definitions\n')
            for f in self.projConfig['Managers'][self.cType + '_Font']['installedFonts'] :
                fInfo = self.fontConfig['Fonts'][f]
                fontPath            = os.path.join(self.projFontsFolder, f)
                useMapping          = self.projConfig['Managers'][self.cType + '_Font']['useMapping']
                if useMapping :
                    useMapping      = os.path.join(fontPath, useMapping)
                useRenderingSystem  = self.projConfig['Managers'][self.cType + '_Font']['useRenderingSystem']

                useLanguage         = self.projConfig['Managers'][self.cType + '_Font']['useLanguage']
                params              = {}
                if useMapping :
                    params['^^mapping^^'] = ':mapping=' + useMapping
                if useRenderingSystem :
                    params['^^renderer^^'] = '/' + useRenderingSystem
                if useLanguage :
                    params['^^language^^'] = ':language=' + useLanguage
                if fontPath :
                    params['^^path^^'] = fontPath

    #            import pdb; pdb.set_trace()
                # Create the fonts settings that will be used with TeX
                if self.projConfig['Managers'][self.cType + '_Font']['primaryFont'] == f :
                    # Primary
                    writeObject.write('\n% These are normal use fonts for this type of component.\n')
                    for k, v in fInfo['UsfmTeX']['PrimaryFont'].iteritems() :
                        addParams(writeObject, params, v)

                    # Secondary
                    writeObject.write('\n% These are font settings for other custom uses.\n')
                    for k, v in fInfo['UsfmTeX']['SecondaryFont'].iteritems() :
                        addParams(writeObject, params, v)

                # There maybe additional fonts for this component. Their secondary settings need to be captured
                # At this point it would be difficult to handle a full set of parms with a secondary
                # font. For this reason, we take them all out. Only the primary font will support
                # all font features.
                params              = {'^^mapping^^' : '', '^^renderer^^' : '', '^^language^^' : '', '^^path^^' : fontPath}
                if self.project.projConfig['Managers'][self.cType + '_Font']['primaryFont'] != f :
                    # Secondary (only)
                    writeObject.write('\n% These are non-primary extra font settings for other custom uses.\n')
                    for k, v in fInfo['UsfmTeX']['SecondaryFont'].iteritems() :
                        addParams(writeObject, params, v)

            # Add special custom commands (may want to parameterize and move 
            # these to the config XML at some point)
            writeObject.write('\n% Special commands\n')

            # This will insert a code that allows the use of numbers in the source text
            writeObject.write(u'\\catcode`@=11\n')
            writeObject.write(u'\\def\\makedigitsother{\\m@kedigitsother}\n')
            writeObject.write(u'\\def\\makedigitsletters{\\m@kedigitsletters}\n')
            writeObject.write(u'\\catcode `@=12\n')

            # Special space characters
            writeObject.write(u'\\def\\nbsp{\u00a0}\n')
            writeObject.write(u'\\def\\zwsp{\u200b}\n')

            ## Baselineskip Adjustment Hook
            # This hook provides a means to adjust the baselineskip on a
            # specific style. It provides a place to put the initial 
            # setting so the hook can make the change and then go back
            # to the initial setting when done.
            # Usage Example:
            #   \sethook{start}{s1}{\remblskip=\baselineskip \baselineskip=10pt}
            #   \sethook{after}{s1}{\baselineskip=\remblskip}
            writeObject.write(u'\\newdimen\\remblskip \\remblskip=\\baselineskip\n')

            # WORKING TEXT LINE SPACING
            # Take out a little space between lines in working text
            writeObject.write(u'\\def\\suckupline{\\vskip -\\baselineskip}\n')
            writeObject.write(u'\\def\\suckuphalfline{\\vskip -0.5\\baselineskip}\n')
            writeObject.write(u'\\def\\suckupqline{\\vskip -0.25\\baselineskip}\n')

            # Skip some space in the working text
            writeObject.write(u'\\def\\skipline{\\vskip\\baselineskip}\n')
            writeObject.write(u'\\def\\skiphalfline{\\vskip 0.5\\baselineskip}\n')
            writeObject.write(u'\\def\\skipqline{\\vskip 0.25\\baselineskip}\n')

            # End here
            writeObject.close()
            self.project.log.writeToLog('XTEX-040', [fName(self.setTexFile)])
            return True


    def makeGrpExtTexFile (self) :
        '''Create/copy a group TeX extentions file to the project for specified group.'''

        # First look for a user file, if not, then make a blank one
        if not os.path.isfile(self.grpExtTexFile) :
            if os.path.isfile(self.usrGrpExtTexFile) :
                shutil.copy(self.usrGrpExtTexFile, self.grpExtTexFile)
            else :
                # Create a blank file
                with codecs.open(self.grpExtTexFile, "w", encoding='utf_8') as writeObject :
                    writeObject.write(self.texFileHeader(self.grpExtTexFile))
                self.project.log.writeToLog('XTEX-040', [fName(self.grpExtTexFile)])

        # Need to return true here even if nothing was done
        return True


    def makeExtTexFile (self) :
        '''Create/copy a TeX extentions file that has custom code for this project group.
        This will go in before the group extentions file.'''

        # First look for a user file, if not, then one 
        # from Rapuma, worse case, make a blank one
        if not os.path.isfile(self.extTexFile) :
            if os.path.isfile(self.usrExtTexFile) :
                shutil.copy(self.usrExtTexFile, self.extTexFile)
            elif os.path.isfile(self.rpmExtTexFile) :
                shutil.copy(self.rpmExtTexFile, self.extTexFile)
            else :
                # Create a blank file
                with codecs.open(self.extTexFile, "w", encoding='utf_8') as writeObject :
                    writeObject.write(self.texFileHeader(self.extTexFileName))
                self.project.log.writeToLog('XTEX-040', [fName(self.extTexFile)])

        # Need to return true here even if nothing was done
        return True


    def makeCidTexFile (self, cid) :
        '''Create the TeX control file for a subcomponent. The component control
        file will call this to process the working text.'''

        print 'makeCidTexFile', cid

        # Build necessary file names
        cidFolder   = os.path.join(self.projComponentsFolder, cid)
        cidTex      = os.path.join(cidFolder, cid + '.tex')
        cidUsfm     = os.path.join(cidFolder, cid + '.usfm')
        cidTexExt   = os.path.join(cidFolder, cid + '-ext.tex')
        cidSty      = os.path.join(cidFolder, cid + '.sty')


        # Write out the cidTex file
        with codecs.open(cidTex, "w", encoding='utf_8') as cidTexObject :
            cidTexObject.write(self.texFileHeader(fName(cidTex)))
            # User sty and macro extentions are optional at the cid level
            if os.path.isfile(os.path.join(cidTexExt)) :
                cidTexObject.write('\\input \"' + cidTexExt + '\"\n')
            if os.path.isfile(os.path.join(cidSty)) :
                cidTexObject.write('\\stylesheet{' + cidSty + '}\n')
            # The cid is not optional!
            if self.checkDepCidUsfm(cidUsfm) :
                cidTexObject.write('\\ptxfile{' + cidUsfm + '}\n')
            else :
                self.project.log.writeToLog('XTEX-050', [fName(cidUsfm)])
                dieNow()

        return True


    def makeGidTexFile (self, gid, cidList, gidTex) :
        '''Create the main gid TeX control file.'''

        # Since a render run could contain any number of components
        # in any order, we will remake this file on every run. No need
        # for dependency checking
        if os.path.exists(gidTex) :
            os.remove(gidTex)

        # Start writing out the gid.tex file. Check/make dependencies as we go.
        # If we fail to make a dependency it will die and report during that process.
        with codecs.open(gidTex, "w", encoding='utf_8') as gidTexObject :
            gidTexObject.write(self.texFileHeader(fName(gidTex)))
            if self.makeMacLinkFile() :
                gidTexObject.write('\\input \"' + self.macLinkFile + '\"\n')
            if self.makeSetTexFile() :
                gidTexObject.write('\\input \"' + self.setTexFile + '\"\n')
            if self.makeExtTexFile() :
                gidTexObject.write('\\input \"' + self.extTexFile + '\"\n')
            if self.makeGrpExtTexFile() :
                gidTexObject.write('\\input \"' + self.grpExtTexFile + '\"\n')
            if self.checkDepGlobStyFile() :
                gidTexObject.write('\\stylesheet{' + self.styFile + '}\n')
            # Custom sty file at the global level is optional as is hyphenation
            if self.useGroupStyles(gid) :
                groupStyles = self.getGroupStyleFile(gid)
                if groupStyles :
                    gidTexObject.write('\\stylesheet{' + groupStyles + '}\n')
            for cid in cidList :
                cidTex = os.path.join(self.projComponentsFolder, cid, cid + '.tex')
                if self.checkDepCidTex(cid) :
                    gidTexObject.write('\\input \"' + cidTex + '\"\n')
            # This can only hapen once in the whole process, this marks the end
            gidTexObject.write('\\bye\n')

        return True


    def getGroupStyleFile (self, gid) :
        '''Check to see if a group style file (as named in the config)
        exists. if it does, return that file handle.'''

        sty = self.projConfig['Groups'][gid]['styleFile']
        if os.path.exists(os.path.join(self.local.projStylesFolder, sty)) :
            return os.path.join(self.local.projStylesFolder, sty)


    def useGroupStyles (self, gid) :
        '''Check to see if styles have been turned on for this group.'''

        return self.projConfig['Groups'][gid]['useStyles']


    def checkDepGlobStyFile (self) :
        '''Check for the exsistance of the Global Sty file. We need to die if 
        it is not found. This should have been installed when the components
        were brought in. To late to recover now if it is not there.'''

        if not os.path.isfile(self.styFile) :
            self.project.log.writeToLog('XTEX-120', [fName(self.styFile)])
            dieNow()
        else :
            return True


    def checkDepHyphenFile (self) :
        '''If hyphenation is used, check for the exsistance of the TeX Hyphenation 
        files. If one of them is not found, kindly ask the appropreate function to
        make it.'''

        if self.useHyphenation :
            if not os.path.isfile(self.hyphExcepTexFile) or isOlder(self.hyphExcepTexFile, self.compHyphFile) :
                if self.makeHyphenExceptionFile() :
                    self.project.log.writeToLog('XTEX-130', [fName(self.hyphExcepTexFile)])
                else :
                    # If we can't make it, we return False
                    self.project.log.writeToLog('XTEX-170', [fName(self.hyphExcepTexFile)])
                    return False






# FIXME: Need a dependency filter here
            if isOlder(self.lccodeFile, self.hyphExcepTexFile) :
                if self.makeLccodeFile() :
                    self.project.log.writeToLog('XTEX-130', [fName(self.lccodeFile)])
                else :
                    # If we can't make it, we return False
                    self.project.log.writeToLog('XTEX-170', [fName(self.lccodeFile)])
                    return False
            return True
        else :
            # If Hyphenation is turned off, we return True and don't need to worry about it.
            return True


    def checkDepCidTex (self, cid) :
        '''Check for the exsistance of the cidTex dependent file. Request one to
        be made if it is not there and Return True.'''

        # Build necessary file names
        cidFolder   = os.path.join(self.projComponentsFolder, cid)
        cidTex      = os.path.join(cidFolder, cid + '.tex')
        cidUsfm     = os.path.join(cidFolder, cid + '.usfm')
        cidTexExt   = os.path.join(cidFolder, cid + '-ext.tex')
        cidSty      = os.path.join(cidFolder, cid + '.sty')

        print 'checkDepCidTex', cid

        # Must be a cidUsfm file to continue
        if not os.path.isfile(cidUsfm) :
            self.project.log.writeToLog('XTEX-050', [fName(cidUsfm)])
            dieNow()

        # Just make it if it is not there
        if not os.path.isfile(cidTex) :
            if self.makeCidTexFile(cid) :
                self.project.log.writeToLog('XTEX-065', [fName(cidTex)])
                return True
        else :
            # Do not (re)make it unless a dependent has changed
            dep = [cidTexExt, cidSty, cidUsfm]
            for f in dep :
                # Weed out unused files
                if not os.path.isfile(f) :
                    continue

                if isOlder(cidTex, f) :
                    if self.makeCidTexFile(cid) :
                        self.project.log.writeToLog('XTEX-065', [fName(cidTex)])
            # Not sure if returning True here is good or not
            return True


    def checkDepCidUsfm (self, cidUsfm) :
        '''Check for the exsistance of the cidUsfm dependent file. Return

        True if it is there or report and die if it is not.'''

        if not os.path.isfile(cidUsfm) :
            self.project.log.writeToLog('XTEX-050', [fName(cidUsfm)])
            dieNow()
        else :
            return True


###############################################################################
################################# Main Function ###############################
###############################################################################

    def run (self, renderParams) :
        '''This will check all the dependencies for a group and then
        use XeTeX to render it.'''

        gid = renderParams['gid']
        force = renderParams['force']
        cidList = renderParams['cidList']
        gidFolder = os.path.join(self.local.projComponentsFolder, gid)
        # This is the file we will make. If force is set, delete the old one.
        gidPdf = os.path.join(gidFolder, gid + '.pdf')
        if force :
            if os.path.isfile(gidPdf) :
                os.remove(gidPdf)

        # Create, if necessary, the gid.tex file
        gidTex = os.path.join(gidFolder, gid + '.tex')
        # First, go through and make/update any dependency files
        self.makeMacLinkFile()
        self.makeSetTexFile()



        self.makeExtTexFile()




        self.checkDepHyphenFile()
        # Now make the gid main setting file
        self.makeGidTexFile(gid, cidList, gidTex)

        # Dynamically create a dependency list for the render process
        dep = [gidTex, self.extTexFile]
        for cid in cidList :
            cType = self.projConfig['Groups'][gid]['cType']
#            cidUsfm = self.managers[cType + '_Text'].getCompWorkingTextPath(cid)
            cidUsfm = self.project.groups[gid].getCidPath(cid)
            cidAdj = self.project.groups[gid].getCidAdjPath(cid)
            cidIlls = self.project.groups[gid].getCidPiclistPath(cid)
            dep.append(cidUsfm)
            if os.path.isfile(cidAdj) :
                dep.append(cidAdj)
            if os.path.isfile(cidIlls) :
                dep.append(cidIlls)

        # Render if gidPdf is older or is missing
        render = False
        if not os.path.isfile(gidPdf) :
            render = True
        else :
            for d in dep :
                if isOlder(gidPdf, d) :
                    render = True
                    break

        # Call the renderer
        if render :
            # Create the environment that XeTeX will use. This will be temporarily set
            # by subprocess.call() just before XeTeX is run.
            texInputsLine = self.project.local.projHome + ':' \
                            + self.projMacPackFolder + ':' \
                            + self.projMacrosFolder + ':' \
                            + os.path.join(self.projComponentsFolder, gid) + ':.'

            # Create the environment dictionary that will be fed into subprocess.call()
            envDict = dict(os.environ)
            envDict['TEXINPUTS'] = texInputsLine

            # Create the XeTeX command argument list that subprocess.call()
            # will run with
            cmds = ['xetex', '-output-directory=' + gidFolder, gidTex]

            # Run the XeTeX and collect the return code for analysis
#                dieNow()
            rCode = subprocess.call(cmds, env = envDict)

            # Analyse the return code
            if rCode == int(0) :
                self.project.log.writeToLog('XTEX-025', [fName(gidTex)])
            elif rCode in self.xetexErrorCodes :
                self.project.log.writeToLog('XTEX-030', [fName(gidTex), self.xetexErrorCodes[rCode], str(rCode)])
            else :
                self.project.log.writeToLog('XTEX-035', [str(rCode)])
                dieNow()

        # Add lines background for composition work
        if str2bool(self.layoutConfig['PageLayout']['useLines']) :
            linesFileName       = self.layoutConfig['PageLayout']['linesFile']
            linesFile           = os.path.join(self.local.projIllustrationsFolder, linesFileName)
            cmd = [self.pdfUtilityCommand, gidPdf, 'background', linesFile, 'output', tempName(gidPdf)]
            try :
                subprocess.call(cmd)
                shutil.copy(tempName(gidPdf), gidPdf)
                os.remove(tempName(gidPdf))
                self.project.log.writeToLog('XTEX-165')
            except Exception as e :
                # If we don't succeed, we should probably quite here
                self.project.log.writeToLog('XTEX-160', [str(e)])
                dieNow()

        # Add a watermark if required
        if str2bool(self.layoutConfig['PageLayout']['useWatermark']) :
            watermarkFileName   = self.layoutConfig['PageLayout']['watermarkFile']
            watermarkFile       = os.path.join(self.local.projIllustrationsFolder, watermarkFileName)
            cmd = [self.pdfUtilityCommand, gidPdf, 'background', watermarkFile, 'output', tempName(gidPdf)]
            try :
                subprocess.call(cmd)
                shutil.copy(tempName(gidPdf), gidPdf)
                os.remove(tempName(gidPdf))
                self.project.log.writeToLog('XTEX-145')
            except Exception as e :
                # If we don't succeed, we should probably quite here
                self.project.log.writeToLog('XTEX-140', [str(e)])
                dieNow()

        # Review the results if desired
        if os.path.isfile(gidPdf) :
            if self.displayPdfOutput(gidPdf) :
                self.project.log.writeToLog('XTEX-095', [fName(gidPdf)])
            else :
                self.project.log.writeToLog('XTEX-100', [fName(gidPdf)])




