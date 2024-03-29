#==============================================================================
#  SIQO Homepage: homepage
#------------------------------------------------------------------------------
import os

from   flask              import url_for, render_template, make_response
from   flask              import request, session, abort, redirect
from   markupsafe         import escape

import jinja2 as j2
from   jinja2             import Environment, FileSystemLoader, PackageLoader, select_autoescape

import siqo_lib.general   as gen

from   siqo_web.p_structure      import Structure
from   siqo_web.p_login          import Login
from   siqo_web.p_page           import Page
from   siqo_web.p_forum          import Forum

#==============================================================================
# package's constants
#------------------------------------------------------------------------------
_VER      = '1.00'

if 'siqo-test' in os.environ: _IS_TEST = True if os.environ['siqo-test']=='1' else False 
else                        : _IS_TEST = False

#==============================================================================
# package's variables
#------------------------------------------------------------------------------
journal = None

env = Environment(
    
     autoescape = select_autoescape()
    ,loader     = PackageLoader(package_name="siqo_web", package_path="templates")
)

#==============================================================================
# package's tools
#------------------------------------------------------------------------------


#==============================================================================
# 
#------------------------------------------------------------------------------
def index():
    
    journal.I('views.index()')
    
    template = env.get_template("index.html")
    
    resp = make_response(template.render(is_test=_IS_TEST), 200)
    resp.headers['X-Something'] = 'A value'

    journal.O()
    return resp

#------------------------------------------------------------------------------
def structure():
    
    journal.I('views.structure()')

    page = Structure(journal, env, 'Login', height=670)
    resp = page.resp()

    journal.O()
    return resp

#------------------------------------------------------------------------------
def login():
    
    journal.I('views.login()')

    page = Login(journal, env, 'Login', height=670, template="3 login.html")
    resp = page.resp()

    journal.O()
    return resp

#------------------------------------------------------------------------------
def homepage():
    
    journal.I('views.homepage()')

    page = Page(journal, env, 'Homepage', height=670, template="3 page.html")
    resp = page.resp()

    journal.O()
    return resp

#------------------------------------------------------------------------------
def oralhistory(idx):
    
    journal.I(f'views.oralhistory({idx})')

    page = Forum(journal, env, 'OHISTORY', idx=idx, height=670)
    resp = page.resp()

    journal.O()
    return resp

#==============================================================================
# Test cases
#------------------------------------------------------------------------------

#==============================================================================
print(f"pages {_VER}")

#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------
