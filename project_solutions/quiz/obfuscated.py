import random
import urllib . request
import re
oo000 = [ "All" ,
 "General Knowledge" ,
 "Entertainment: Books" ,
 "Entertainment: Film" ,
 "Entertainment: Music" ,
 "Entertainment: Musicals & Theatres" ,
 "Entertainment: Television" ,
 "Entertainment: Video Games" ,
 "Entertainment: Board Games" ,
 "Science & Nature" ,
 "Science: Computers" ,
 "Science: Mathematics" ,
 "Mythology" ,
 "Sports" ,
 "Geography" ,
 "History" ,
 "Politics" ,
 "Art" ,
 "Celebrities" ,
 "Animals" ,
 "Vehicles" ,
 "Entertainment: Comics" ,
 "Science: Gadgets" ,
 "Entertainment: Japanese Anime & Manga" ,
 "Entertainment: Cartoon & Animations"
 ]
ii = [ "easy" , "medium" , "hard" , "random" ]
def oOOo ( s ) :
 s = s . replace ( '&#039;' , "'" )
 s = s . replace ( '&quot;' , '"' )
 return s
 if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
def IIi1IiiiI1Ii ( q ) :
 if 39 - 39: O0 - ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
 Ii1I = re . search ( r'question":"(.*?)"' , str ( q ) ) . group ( 0 ) [ 11 : - 1 ] if re . search ( r'question":"(.*)"' , str ( q ) ) else ""
 print ( oOOo ( Ii1I ) )
 IiiIII111iI = oOOo ( re . search ( r'correct_answer":"(.*?)"' , str ( q ) ) . group ( 0 ) [ 17 : - 1 ] ) if re . search ( r'correct_answer":"(.*)"' , str ( q ) ) else ""
 if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
 Oo = eval ( oOOo ( re . search ( r'incorrect_answers":\[(.*?)\]' , str ( q ) ) . group ( 0 ) [ 19 : ] ) ) if re . search ( r'incorrect_answers":\[(.*?)\]' , str ( q ) ) else ""
 if 27 - 27: o00 * O0IiiiIiI1iIiI1 - ii1Ii * iii1I1I % Oo0Ooo + OO0OO0O0O0
 Oo . append ( IiiIII111iI )
 if 89 - 89: II - iiiIIii1IIi - ooOO00oOo . I1i1iI1i * o00 * I1IiiI
 random . shuffle ( Oo )
 if 25 - 25: I1i1iI1i
 print ( "Your possible answers are:" )
 if 89 - 89: iII111iiiii11 - o00 * ii1Ii
 for O0I11i1i11i1I in range ( len ( Oo ) ) :
  print ( "  " + str ( O0I11i1i11i1I + 1 ) + ". " + Oo [ O0I11i1i11i1I ] )
  if 31 - 31: Oo0Ooo / ooOO00oOo / ii1Ii * O00oOoOoO0o0O / oOo0O0Ooo
 Oo0o0ooO0oOOO = Oo [ int ( input ( "Input the correct answer number, or 0 for a new set of questions. " ) ) - 1 ]
 if 58 - 58: Oo0Ooo % O0IiiiIiI1iIiI1
 if Oo0o0ooO0oOOO == IiiIII111iI :
  print ( "You got it right! Congratulations!" )
  return True
 elif Oo0o0ooO0oOOO == 0 :
  return "restart"
 else :
  print ( "Oh no! The correct answer was " + IiiIII111iI + "\n" )
  return False
  if 54 - 54: O0oo0OO0 % OO0OO0O0O0 + ooOO00oOo - II / Oo0ooO0oo0oO
def Ii1I ( category , difficulty , data ) :
 iIiiI1 = 0
 OoOooOOOO = IIi1IiiiI1Ii ( data )
 if not OoOooOOOO :
  print ( "Your score was " + str ( iIiiI1 ) + " in " + category + " with an " + difficulty + " difficulty." )
  return
 elif OoOooOOOO == "restart" :
  return
 else :
  iIiiI1 += 1
  if 45 - 45: O0IiiiIiI1iIiI1 + I1i1iI1i
while True :
 if 17 - 17: iiiiIi11i
 if 64 - 64: I1i1iI1i % I1IiiI % iII111iiiii11
 print ( "Your categories options are:" )
 for O0I11i1i11i1I in range ( len ( oo000 ) ) :
  print ( "  " + str ( O0I11i1i11i1I + 1 ) + ". " + oo000 [ O0I11i1i11i1I ] )
  if 3 - 3: II + OO0OO0O0O0
  if 42 - 42: O0oo0OO0 / I1IiiI + Oo0Ooo - I1i1iI1i
 while True :
  oo0Ooo0 = int ( input ( "Which category number do you want?" ) ) - 1
  if oo0Ooo0 > len ( oo000 ) :
   print ( "Uh oh, please pick one of the valid options!" )
  else :
   oo0Ooo0 = oo000 [ oo0Ooo0 ]
   break
   if 46 - 46: ii1Ii % ii1Ii - O00oOoOoO0o0O * iiiiIi11i % II
   if 55 - 55: oOoO0oo0OOOo % I1IiiI / I1i1iI1i - O00oOoOoO0o0O - OO0OO0O0O0 / O0
   if 28 - 28: iiiIIii1IIi - I1IiiI
 while True :
  OO = input ( "Do you want easy, medium or hard problems? Input \"random\" for a random difficulty." ) . lower ( )
  if OO not in ii :
   print ( "Uh oh, please pick one of the valid options!" )
  else :
   break
   if 55 - 55: Ooo00oOo00o / iii1I1I * O0oo0OO0
   if 86 - 86: Oo0Ooo + I1i1iI1i + ii1Ii * Oo0ooO0oo0oO + iiiiIi11i
 if oo0Ooo0 == 0 and OO == "random" :
  oOoO = 'https://opentdb.com/api.php?amount=1'
 elif oo0Ooo0 == 0 :
  oOoO = 'https://opentdb.com/api.php?amount=1&difficulty=' + OO
 elif OO == "random" :
  oOoO = 'https://opentdb.com/api.php?amount=1&category=' + str ( oo000 . index ( oo0Ooo0 ) + 8 )
 else :
  oOoO = 'https://opentdb.com/api.php?amount=1&category=' + str ( oo000 . index ( oo0Ooo0 ) + 8 ) + '&difficulty=' + OO
 Ii1I ( oo0Ooo0 , OO , urllib . request . urlopen ( oOoO ) . read ( ) )
 print ( "Restarting!" )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3