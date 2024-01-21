#==============================================================================
#  SIQO Homepage: Configuration
#------------------------------------------------------------------------------
import os

#==============================================================================
# package's constants
#------------------------------------------------------------------------------
_VER      = 1.00
_IS_TEST  = True if os.environ['wsiqo-test-mode']=='1' else False

#==============================================================================
# package's variables
#------------------------------------------------------------------------------

#==============================================================================
# Config class
#------------------------------------------------------------------------------
class Config:
    
    SECRET_KEY = os.environ.get('wsiqo-secret-key') or "ekjwn47wtyqgpUHP43UGH3"



#==============================================================================
print(f"config {_VER}")

#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------