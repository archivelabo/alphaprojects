from flask import Flask , request
from flask import render_template_string
from flask import redirect
if 64 - 64: i11iIiiIii
import os , re
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = Flask ( __name__ )
if 78 - 78: i11i . oOooOoO0Oo0O
if 10 - 10: IIiI1I11i11
class ooOO00oOo :
 def __init__ ( self , content , complete ) :
  self . text = content
  self . done = complete
  if 92 - 92: O0O / oo000 % IiIi11iIIi1Ii / o0OOO - iiiiIi11i . Ii1I
@ o0OO00 . route ( '/' )
def IiiIII111iI ( ) :
 IiII = [ ]
 iI1Ii11111iIi = open ( 'db.csv' , 'r' )
 for i1i1II in iI1Ii11111iIi :
  i1i1II = i1i1II . split ( ',' )
  IiII . append ( ooOO00oOo ( i1i1II [ 0 ] , i1i1II [ 1 ] . rstrip ( ) ) )
 O0oo0OO0 = """<ul>
{% for task in tasks %}
    <li>
        {% if task.done == '1' %} <strike> {% endif %}{{ task.text }} {% if task.done == '1'%} </strike>{% endif %}
        <a href="#" onclick="goto('/done/'+ '{{ task.text }}')">X</a>
        <a href="#" onclick="goto('/delete/' + '{{ task.text }}')">Delete</a>
    </li>
{% endfor %}
</ul>


<form method="post" onsubmit="get_action(this);">
    <p><input type="text" name="content" required></p>
    <input type="submit" value="Add task">
</form>

<script>

    function get_action(form) {
        form.action = window.location.pathname + "/task" + window.location.pathname;
     }
function goto(url){window.location.href=window.location.href.substr(0, window.location.href.lastIndexOf("0") + 1) + '/' + url + '/' + window.location.pathname}

</script>"""
 return render_template_string ( O0oo0OO0 , tasks = IiII )
 if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
 if 12 - 12: o0oOoO00o
@ o0OO00 . route ( '/task/<string:path>' , methods = [ 'POST' ] )
def i1 ( path ) :
 oOOoo00O0O = request . form [ 'content' ]
 if not oOOoo00O0O :
  return 'Error'
 i1111 = ooOO00oOo ( oOOoo00O0O , 0 )
 iI1Ii11111iIi = open ( 'db.csv' , 'a' )
 iI1Ii11111iIi . write ( i1111 . text + "," + str ( i1111 . done ) + "\n" )
 print ( request . url . replace ( "http" , "https" ) [ 31 : ] )
 print ( path )
 return redirect ( request . url . replace ( "http" , "https" ) . replace ( "task/" , "" ) )
 if 22 - 22: OOo000 . i111I
 if 89 - 89: oooO0oo0oOOOO
@ o0OO00 . route ( '/delete/<string:content>/<string:path>' )
def I11i1i11i1I ( content , path ) :
 iI1Ii11111iIi = open ( 'db.csv' , 'r' )
 Iiii = open ( 'db_new.csv' , 'w' )
 for i1i1II in iI1Ii11111iIi :
  if content not in i1i1II :
   Iiii . write ( i1i1II )
   if 87 - 87: iiiiIi11i / OOo000 + o0oOoO00o - OOo000 . OOo000 / i11i
 os . remove ( 'db.csv' )
 os . rename ( 'db_new.csv' , 'db.csv' )
 return redirect ( re . sub ( r"delete/(.+)/" , "" , request . url . replace ( "http" , "https" ) ) )
 if 11 - 11: oOooOoO0Oo0O % IiIi11iIIi1Ii - IIiI1I11i11
 if 58 - 58: i11iIiiIii % o0oOoO00o
@ o0OO00 . route ( '/done/<string:content>/<string:path>' )
def O0OoOoo00o ( content , path ) :
 iI1Ii11111iIi = open ( 'db.csv' , 'r' )
 Iiii = open ( 'db_new.csv' , 'w' )
 for i1i1II in iI1Ii11111iIi :
  if content not in i1i1II :
   Iiii . write ( i1i1II )
  else :
   if int ( i1i1II [ - 2 ] ) :
    Iiii . write ( i1i1II [ : - 2 ] + '0\n' )
   else :
    Iiii . write ( i1i1II [ : - 2 ] + '1\n' )
    if 31 - 31: i11i + O0O . o0oOoO00o
 os . remove ( 'db.csv' )
 os . rename ( 'db_new.csv' , 'db.csv' )
 return redirect ( re . sub ( r"done/(.+)/" , "" , request . url . replace ( "http" , "https" ) ) )
 if 68 - 68: oOooOoO0Oo0O - i11iIiiIii - O0O / Ii1I - O0O + i1IIi
 if 48 - 48: OoooooooOO % IiIi11iIIi1Ii . oOooOoO0Oo0O - ooO0oo0oO0 % i1IIi % OoooooooOO
if __name__ == '__main__' :
 o0OO00 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3