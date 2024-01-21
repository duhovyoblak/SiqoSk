#==============================================================================
#  SIQO Homepage: DMS API
#------------------------------------------------------------------------------
import os

import siqo_lib.general   as gen

#==============================================================================
# package's constants
#------------------------------------------------------------------------------
_VER      = 1.00
_IS_TEST  = True if os.environ['wsiqo-test-mode']=='1' else False
_PATH     = '../DMS/'

#==============================================================================
# package's variables
#------------------------------------------------------------------------------
journal = None

#==============================================================================
# package's tools
#------------------------------------------------------------------------------

#==============================================================================
# 
#------------------------------------------------------------------------------
def loadJson(fName):
    
    journal.I(f"loadJson: {fName}")
    
    toRet = gen.loadJson(journal, fileName = f"{_PATH}{fName}")
    
    journal.O()
    return toRet

#==============================================================================
# Test cases
#------------------------------------------------------------------------------

#==============================================================================
print(f"dms {_VER}")

#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------