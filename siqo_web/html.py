#==============================================================================
#                                             (c) SIQO 11, 12, 13, 24
# Kniznica pre pracu s HTML dokumentom
#
#------------------------------------------------------------------------------
import os

#==============================================================================
# package's constants
#------------------------------------------------------------------------------
_VER      = '1.00'

if 'siqo-test' in os.environ: _IS_TEST = True if os.environ['siqo-test']=='1' else False 
else                        : _IS_TEST = False

#==============================================================================
# package's variables
#------------------------------------------------------------------------------

#==============================================================================
# HTML library
#------------------------------------------------------------------------------
def renderItem(item, lang):
    "Returns HTML for json-encoded item"
    
    if 'type' in item.keys(): typ = item['type']
    else                    : typ = 'P'
    
    toRet = ''

    #--------------------------------------------------------------------------
    # Rozlisi Backward, Forward alebo nieco ine
    #--------------------------------------------------------------------------
    if False: return toRet

    #--------------------------------------------------------------------------
    # Skusim vsetky zname typy
    #--------------------------------------------------------------------------
    elif typ == 'LINK'         : toRet = inputButton(item, lang)
    elif typ == 'CHECKBOX'     : toRet = inputCheckBox(item, lang)
    elif typ == 'RADIO'        : toRet = inputRadio(item, lang)
    elif typ == 'TEXT'         : toRet = inputText(item, lang)

    elif typ == 'LABEL'        : toRet = label(item, lang)
    elif typ == 'P'            : toRet = p(item, lang)
    elif typ == 'P-START'      : toRet = pStart(item, lang)
    elif typ == 'P-CONT'       : toRet = pCont(item, lang)
    elif typ == 'P-STOP'       : toRet = pStop(item, lang)
    elif typ == 'IMAGE'        : toRet = image(item, lang)

    elif typ == 'HEADTITLE'    : toRet = headTtile(item, lang)
    elif typ == 'HEADSUBTIT'   : toRet = headSubTitle(item, lang)
    elif typ == 'HEADCOMMENT'  : toRet = headComment(item, lang)

    elif typ == 'BARMENUITEM'  : toRet = barMenuItem(item, lang)

    elif typ == 'STAGESELECTOR': toRet = stageSelector(item, lang)

    elif typ == 'NEWLINE'      : toRet = newLine()
    elif typ == 'BREAK'        : toRet = breakLine()
    elif typ == 'SPLIT'        : toRet = split()
    
    elif typ == 'FUNC'         : toRet = fcia(item)
    elif typ == 'HTML'         : toRet = html(item)
    elif typ == 'DIVSTART'     : toRet = divStart(item)
    elif typ == 'DIVSTOP'      : toRet = divStop(item)
    
    return toRet
    
#------------------------------------------------------------------------------
def itemDrop(item, key):
    
    if key in item.keys(): 
        
        val = item[key]
        item[key] = ''
        
    else: val = '_none_'
    
    return (item, val)
    
#==============================================================================
# Jednoriadkove HTML vyrazy
#------------------------------------------------------------------------------
def newLine():

    return "\n"

#------------------------------------------------------------------------------
def breakLine():

    return '<br>'

#------------------------------------------------------------------------------
# Headers
#------------------------------------------------------------------------------
def h1(item, lang):
    
    (item, txt) = itemDrop(item, lang)

    return f'<h1 {html_atts(item)}>{txt}</h1> \n'

#------------------------------------------------------------------------------
def h2(item, lang):

    (item, txt) = itemDrop(item, lang)

    return f'<h2 {html_atts(item)}>{txt}</h2> \n'

#------------------------------------------------------------------------------
def h3(item, lang):

    (item, txt) = itemDrop(item, lang)

    return f'<h3 {html_atts(item)}>{txt}</h3> \n'

#------------------------------------------------------------------------------
def h4(item, lang):

    (item, txt) = itemDrop(item, lang)

    return f'<h4 {html_atts(item)}>{txt}</h4> \n'

#------------------------------------------------------------------------------
# Link <a href="url"?args>txt</a>
#------------------------------------------------------------------------------
def a(item, lang):

    (item, url) = itemDrop(item, 'url')
    (item, arg) = itemDrop(item, 'arg')
    (item, txt) = itemDrop(item, lang )

    link = url
    if arg != '_none_': link += f'?{arg}'
    
    item["href"] = link

    return f'<a {html_atts(item)}>{txt}</a>'

#------------------------------------------------------------------------------
def p(item, lang):

    (item, hid) = itemDrop(item, 'hidden')
    (item, txt) = itemDrop(item, lang )

    #--------------------------------------------------------------------------
    # If paragraph is not hidden
    #--------------------------------------------------------------------------
    if hid == '_none_' or not hid: return f'<p {html_atts(item)}>{txt}</p>\n'
    else                         : return f'<p hidden {html_atts(item)}>{txt}</p>\n'

#------------------------------------------------------------------------------
def pStart(item, lang):

    return f'<p {html_atts(item)}>'

#------------------------------------------------------------------------------
def pCont(item, lang):

    (item, txt) = itemDrop(item, lang )
    return txt

#------------------------------------------------------------------------------
def pStop():

    return '</p>\n'

#------------------------------------------------------------------------------
def split():

    atts = {"SK":"––«•»––", "class":"center"}
    return p(atts, 'SK')

#------------------------------------------------------------------------------
def html(item, lang):

    (item, code) = itemDrop(item, 'html')
    return f'{code}\n'

#------------------------------------------------------------------------------
def pre(item, lang):

    (item, txt) = itemDrop(item, lang)
    return f'<pre {html_atts(item)}>{txt}</pre>\n'

#------------------------------------------------------------------------------
def label(item, lang):

    (item, txt) = itemDrop(item, lang)
    return f'<label {html_atts(item)}>{txt}</label>\n'

#==============================================================================
# Viacriadkove HTML vyrazy
#------------------------------------------------------------------------------
def divStart(item):
    
    """
    atts = { "class"  : classx
            ,"name"   : name
            ,"id"     : idx
            ,"onClick": onClick
            ,"style"  : f'height:{h} width:{w} top:{t} left:{l} float:{flt}'
           }
    """
    return f'<div {html_atts(item)}>\n'

#------------------------------------------------------------------------------
def divStop():

    return '</div> \n'

#------------------------------------------------------------------------------
def divBreak(item, lang):

    atts = { "class"  : "Break"
#            ,"style"  : f'height:{h} width:{w}'
           }

    return f'<div {html_atts(atts)}></div> \n'

#------------------------------------------------------------------------------
def textThumb(item, lang):
 
#    toRet = divStart("ObjectText", idx, idx, h, w, '', '', '', flt)
    toRet = divStart(item)

#    toRet += a(url, p('lorem ipsum'), atts={"target":"_blank"})
       
#    if title != '':
#        toRet += p(title, atts={"class":"txt file"})
   
    toRet += divStop()
    
    return toRet

#------------------------------------------------------------------------------
def image(item, lang):
 
#    toRet = divStart("ObjectImage", idx, idx, h, w, '', '', '', flt)
    toRet = divStart(item)

#    atts = {"src":url, "style":"width:100% max-height:90%", "alt":alt}
#    txt = f'<img {html_atts(atts)}>'

    toRet += a(item, lang)

#    if title != '':
#        toRet += p(title, atts={"class":"foto"})
   
    toRet += divStop()
    
    return toRet

#------------------------------------------------------------------------------
# Input items
#------------------------------------------------------------------------------
def inputRadio(item, lang):

    item["type"] = "radio"
    
    #--------------------------------------------------------------------------
    # Radio button
    #--------------------------------------------------------------------------
    if 'checked' in item.keys():
        
        if item['checked']: checkType = 'checked'
        else              : checkType = ''
        
        item['checked'] = ''
        
    else: checkType = ''
    
    #--------------------------------------------------------------------------
    # Label
    #--------------------------------------------------------------------------
    txt = item[lang]
    item[lang] = ''
    
    atts = {"for": item['id']}
    
    #--------------------------------------------------------------------------
    # html
    #--------------------------------------------------------------------------
    toRet  = f'<input {html_atts(item)} {checkType}/>\n'
    toRet += f'<label {html_atts(atts)}>{txt}</label><br>'

    return toRet

#------------------------------------------------------------------------------
def inputCheckBox(item, lang):

    """
    atts = { "type"    : "checkbox"
            ,"class"   : classx
            ,"name"    : name
            ,"value"   : value
            ,"ID"      : idx
            ,"onchange": onChange
           }
    
    if not edit: editType = 'readonly'
    else       : editType = ""
    """
    editType = ''
    return f'<input {html_atts(item)} {editType}/>\n'

#------------------------------------------------------------------------------
def inputText(item, lang):

    """
    atts = { "type"     : "text"
            ,"class"    : classx
            ,"name"     : name
            ,"value"    : value
            ,"ID"       : idx
            ,"size"     : size
            ,"maxlength": maxlength
            ,"onchange" : onChange
           }
    
    if not edit: editType = 'readonly'
    else       : editType = ''
    """
    editType = ''
    return f'<input {html_atts(item)} {editType}/>\n'

#------------------------------------------------------------------------------
# Head block
#------------------------------------------------------------------------------
def headTtile(item, lang):
  
    atts = {"class":"HeaderTitle", "name":"HeaderTitle", "id":"HeaderTitle"}
 
    toRet  = divStart(atts)
    toRet += h1(item, lang)
    toRet += divStop()
    
    print('headTitle :', toRet)
    return toRet

#------------------------------------------------------------------------------
def headComment(item, lang):
  
    atts = {"class":"HeaderComment", "name":"HeaderComment", "id":"HeaderComment"}

    toRet  = divStart(atts)
    toRet += h1(item, lang)
    toRet += divStop()

    return toRet

#------------------------------------------------------------------------------
def headSubTitle(item, lang):
  
    return h4(item, lang)

#------------------------------------------------------------------------------
# NavBar block
#------------------------------------------------------------------------------
def barMenuItem(item, lang):
    
    atts = {"class":"BarMenuItem", "name":"BarMenuItem", "id":"BarMenuItem"}
    
    toRet  = divStart(atts)
    toRet += a(item, lang)
    toRet += divStop()
    
    return toRet

#------------------------------------------------------------------------------
# Stage block
#------------------------------------------------------------------------------
def stageSelector(item, lang):
  
    #--------------------------------------------------------------------------
    # Pripravim atributy do itemu
    #--------------------------------------------------------------------------
    pos = item['pos']
    item['pos'] = ''
    
    item['name'   ] = 'SSB'
    item['id'     ] = f"SSB_{pos}"
    item['value'  ] = pos
    item['onclick'] = f"ShowStage('{pos}')"
    
    if pos == '1': item['checked'] = True
    else         : item['checked'] = False

    atts = {"class":"StageSelectorItem", "name":"StageSelectorItem", "id":"StageSelectorItem"}
        
    #--------------------------------------------------------------------------
    # Render itemu
    #--------------------------------------------------------------------------
    toRet  = divStart(atts)
    toRet += inputRadio(item, lang)
    toRet += divStop()

    return toRet

#------------------------------------------------------------------------------
def stagePanel(item, lang):
  
    #--------------------------------------------------------------------------
    # Pripravim atributy do itemu
    #--------------------------------------------------------------------------
    pos = item['pos']
    item['pos'] = ''
    
    item['name'   ] = 'SSB'
    item['id'     ] = f"SSB_{pos}"
    item['value'  ] = pos
    item['onclick'] = f"ShowStage('{pos}')"
    
    if pos == '1': style = "display:block"
    else         : style = "display:none"
    
    atts = {"class":"StagePanel", "name":"SP", "id":f"SP_{pos}", "style":style}

    #--------------------------------------------------------------------------
    # Render itemu
    #--------------------------------------------------------------------------
    toRet  = divStart(atts)
    toRet += renderItem(item, lang)
    toRet += divStop()

    return toRet

#------------------------------------------------------------------------------
# HTML Tabulka
#------------------------------------------------------------------------------
def tableStart(classx, name='', idx='', h=''):

    atts = { "class"  : classx
            ,"name"   : name
            ,"ID"     : idx
            ,"style"  : f'height:{h}'
           }

    return f'<table {html_atts(atts)}>\n'

#------------------------------------------------------------------------------
def tableStop():

    return '</table>\n'

#------------------------------------------------------------------------------
def tableRowStart(classx, name='', idx=''):

    atts = { "class"  : classx
            ,"name"   : name
            ,"ID"     : idx
           }

    return f'<tr {html_atts(atts)}>\n'

#------------------------------------------------------------------------------
def tableRowStop():

    return '</tr>\n'

#------------------------------------------------------------------------------
def tableDataItem(classx, value, title='', idx='', colspan=''):

    atts = { "class"  : classx
            ,"value"  : value
            ,"title"  : title
            ,"ID"     : idx
            ,"colspan": colspan
           }

    return f'<td {html_atts(atts)}>html_entities(value)</td>\n'

#------------------------------------------------------------------------------
def tableCheckItem(name, value, classx='', edit=True, onChange='', idx=''):

    return f'<td>{inputCheckBox(classx, name, value, idx, edit, onChange)}</td>\n'

#------------------------------------------------------------------------------
def tableInputItem(name, value, classx, size, maxlength=40, edit=True, onChange='', idx=''):
    
    return f'<td>{inputText(classx, name, value, idx, size, maxlength, edit, onChange)}</td>\n'

#------------------------------------------------------------------------------
def tableInputHidden(name, value):

    atts = { "type"     : "hidden"
            ,"name"     : name
            ,"value"    : value
           }

    return f'<input {html_atts(atts)}/>\n'

#------------------------------------------------------------------------------
#==============================================================================
# Pomocne metody
#------------------------------------------------------------------------------
# Presmerovanie dokumentu
#------------------------------------------------------------------------------
def html_location(location):
 
    return location
 
#------------------------------------------------------------------------------
def html_baseurl(): 

#  návrat http:#<thiswebsite>/<thisdirectory>
#    return "https:#" . _SERVER['HTTP_HOST'] . dirname(_SERVER['PHP_SELF'])

#  návrat http:#<thiswebsite>
    return "http:# . _SERVER['HTTP_HOST'] . '/'"

#==============================================================================
# Bezpecnostne fcie
#------------------------------------------------------------------------------
def HTMLSecure(txt):

    withoutBreaks           = txt.replace('\n', 'PAGMAN_RESERVED_BREAK')
    HTMLSecureWithoutBreaks = html_entities(withoutBreaks)
    HTMLSecureString        = HTMLSecureWithoutBreaks.replace('PAGMAN_RESERVED_BREAK', '<br>')
    
    return(HTMLSecureString)
  
#------------------------------------------------------------------------------
def html_entities(txt):

    return txt

#------------------------------------------------------------------------------
def html_specialchars(txt):

    return txt

#------------------------------------------------------------------------------
def html_attribute(name, value):

    if value != '': return f' {name} ="{html_specialchars(value)}"'
    else          : return ''

#------------------------------------------------------------------------------
def html_atts(atts):

    toRet = ''

    for key, val in atts.items():
        if val != '': toRet += html_attribute(key, val)
        
    return toRet

#------------------------------------------------------------------------------
# Osetrenie vstupu v stringu vratane odstranenia magic quotes
#------------------------------------------------------------------------------
"""
def str_input( txt )

  if  get_magic_quotes_gpc() )
     txt = stripslashes(str)
      
    return str

#------------------------------------------------------------------------------
# Osetrenie vstupu v poli vratane odstranenia magic quotes
#------------------------------------------------------------------------------
def array_input( arr )

  if  get_magic_quotes_gpc() )
  
    while(i = each(arr)) 
      arr[i[0]] = stripslashes(i[1])
    
      
    return arr

#------------------------------------------------------------------------------
# Debug output na obrazovku
#------------------------------------------------------------------------------
def Debug( stat ) 

    printf( "<p>%s\n</p>\n", stat )
"""
#==============================================================================
print(f"html {_VER}")

#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------