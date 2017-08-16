import turtle as OO00O00OOOO00O000 #line:3
tina =OO00O00OOOO00O000 .Turtle ()#line:4
def drawGrid (O000000O00O0OO0OO ,O0O00OO0OOOO00OO0 ):#line:5
  O0O000O00OOOOO00O =220 #line:6
  tina .hideturtle ()#line:7
  tina .tracer (0 ,0 )#line:8
  tina .speed (10 )#line:9
  tina .penup ()#line:10
  for OOOOOOOO0OO0000O0 in range (0 ,O000000O00O0OO0OO +1 ):#line:11
      tina .setpos (0 -O0O000O00OOOOO00O ,OOOOOOOO0OO0000O0 *50 -O0O000O00OOOOO00O )#line:12
      tina .pensize (1 )#line:13
      if OOOOOOOO0OO0000O0 %3 ==0 :#line:14
        tina .pensize (O0O00OO0OOOO00OO0 )#line:15
      tina .pendown ()#line:16
      tina .forward (O000000O00O0OO0OO *50 )#line:17
      tina .penup ()#line:18
  tina .left (90 )#line:19
  for OOOOOOOO0OO0000O0 in range (0 ,O000000O00O0OO0OO +1 ):#line:20
      tina .setpos (OOOOOOOO0OO0000O0 *50 -O0O000O00OOOOO00O ,0 -O0O000O00OOOOO00O )#line:21
      tina .pensize (1 )#line:22
      if OOOOOOOO0OO0000O0 %3 ==0 :#line:23
        tina .pensize (5 )#line:24
      tina .pendown ()#line:25
      tina .forward (O000000O00O0OO0OO *50 )#line:26
      tina .penup ()#line:27
  tina .update ()#line:28
class Box :#line:30
    def __init__ (O00O00O000000OO0O ):#line:32
        O00O00O000000OO0O .turtle =OO00O00OOOO00O000 .Turtle ()#line:34
        O00O00O000000OO0O .turtle .hideturtle ()#line:35
        O00O00O000000OO0O .turtle .speed (10 )#line:36
        O00O00O000000OO0O .value =0 #line:37
        O00O00O000000OO0O .highlighted =False #line:38
    def draw (O0O000OO0O00O0OO0 ,O0O0000000O000OOO ,OOO0O0OO0OO0O0O00 ,OO0OO0O00O00OOOOO ,O0OO0OO00000000O0 ):#line:40
        screen .onclick (None )#line:41
        if OO0OO0O00O00OOOOO :#line:42
            O0O000OO0O00O0OO0 .turtle .begin_fill ()#line:43
            O0O000OO0O00O0OO0 .turtle .fillcolor (OO0OO0O00O00OOOOO )#line:44
        O0O000OO0O00O0OO0 .turtle .penup ()#line:45
        O0O000OO0O00O0OO0 .turtle .setpos (O0O0000000O000OOO *50 -219 ,OOO0O0OO0OO0O0O00 *50 -219 )#line:46
        O0O000OO0O00O0OO0 .turtle .pencolor (O0OO0OO00000000O0 )#line:47
        O0O000OO0O00O0OO0 .turtle .forward (48 )#line:48
        O0O000OO0O00O0OO0 .turtle .left (90 )#line:49
        O0O000OO0O00O0OO0 .turtle .forward (48 )#line:50
        O0O000OO0O00O0OO0 .turtle .left (90 )#line:51
        O0O000OO0O00O0OO0 .turtle .forward (48 )#line:52
        O0O000OO0O00O0OO0 .turtle .left (90 )#line:53
        O0O000OO0O00O0OO0 .turtle .forward (48 )#line:54
        O0O000OO0O00O0OO0 .turtle .left (90 )#line:55
        if OO0OO0O00O00OOOOO :#line:56
          O0O000OO0O00O0OO0 .turtle .end_fill ()#line:57
        O0O000OO0O00O0OO0 .turtle .update ()#line:58
        screen .onclick (click )#line:59
        return True #line:60
    def write (OO00000O00OOOO000 ,OOO0O0OO0OO0O0OO0 ,O00000O0000OOO00O ,OOOO0O0OO0O0O0OOO ):#line:62
        OO00000O00OOOO000 .turtle .color ("black")#line:63
        OO00000O00OOOO000 .turtle .setpos (O00000O0000OOO00O *50 +15 -220 ,(OOO0O0OO0OO0O0OO0 *50 )+15 -220 )#line:64
        OO00000O00OOOO000 .turtle .write (str (OOOO0O0OO0O0O0OOO ),font =("Arial",20 ,"normal"))#line:65
        game .grid [OOO0O0OO0OO0O0OO0 ][O00000O0000OOO00O ].value =OOOO0O0OO0O0O0OOO #line:66
        OO00000O00OOOO000 .turtle .update ()#line:67
    def highlight (OOO0000O00OOOO0O0 ,OOO0OO0OO00O00OO0 ,O00O000OO0000OO0O ):#line:69
        if OOO0000O00OOOO0O0 .highlighted :#line:70
            OOO0000O00OOOO0O0 .draw (OOO0OO0OO00O00OO0 ,O00O000OO0000OO0O ,"lightblue","black")#line:71
            OOO0000O00OOOO0O0 .highlighted =False #line:72
            if not game .grid [O00O000OO0000OO0O ][OOO0OO0OO00O00OO0 ].value ==0 :#line:73
              OOO0000O00OOOO0O0 .write (O00O000OO0000OO0O ,OOO0OO0OO00O00OO0 ,game .grid [O00O000OO0000OO0O ][OOO0OO0OO00O00OO0 ].value )#line:74
        elif game .highlighted ==False :#line:75
            OOO0000O00OOOO0O0 .draw (OOO0OO0OO00O00OO0 ,O00O000OO0000OO0O ,"pink","black")#line:76
            OOO0000O00OOOO0O0 .highlighted =True #line:77
            if not game .grid [O00O000OO0000OO0O ][OOO0OO0OO00O00OO0 ].value ==0 :#line:78
                OOO0000O00OOOO0O0 .write (O00O000OO0000OO0O ,OOO0OO0OO00O00OO0 ,game .grid [O00O000OO0000OO0O ][OOO0OO0OO00O00OO0 ].value )#line:79
            return True #line:80
class Game :#line:82
    def __init__ (OOO0O0O0O0O000OOO ):#line:83
        OOO0O0O0O0O000OOO .turtle =OO00O00OOOO00O000 .Turtle ()#line:85
        OOO0O0O0O0O000OOO .turtle .hideturtle ()#line:86
        OOO0O0O0O0O000OOO .turtle .speed (10 )#line:87
        OOO0O0O0O0O000OOO .grid =[[0 ]*9 for _OOO0O0OOO0OOO00O0 in range (9 )]#line:88
        for OOOO00OOOO0OO0O00 in range (9 ):#line:89
          for OO0OOOOO0OOOO0O00 in range (9 ):#line:90
            OOO0O0O0O0O000OOO .grid [OOOO00OOOO0OO0O00 ][OO0OOOOO0OOOO0O00 ]=Box ()#line:91
        drawGrid (9 ,5 )#line:92
        OOO0O0O0O0O000OOO .highlighted =False #line:93
def findNextCellToFill (OO0000O00O0OOO000 ,OO0O0OOO0OO0000OO ,O00O0OO0O0O0OO000 ):#line:96
        for OOOOOOOO000000000 in range (OO0O0OOO0OO0000OO ,9 ):#line:97
                for O0000OOOOO0OO0O00 in range (O00O0OO0O0O0OO000 ,9 ):#line:98
                        if OO0000O00O0OOO000 [OOOOOOOO000000000 ][O0000OOOOO0OO0O00 ]==0 :#line:99
                                return OOOOOOOO000000000 ,O0000OOOOO0OO0O00 #line:100
        for OOOOOOOO000000000 in range (0 ,9 ):#line:101
                for O0000OOOOO0OO0O00 in range (0 ,9 ):#line:102
                        if OO0000O00O0OOO000 [OOOOOOOO000000000 ][O0000OOOOO0OO0O00 ]==0 :#line:103
                                return OOOOOOOO000000000 ,O0000OOOOO0OO0O00 #line:104
        return -1 ,-1 #line:105
def isValid (OOOOO0OO0O00OO000 ,O00OOOO0O00OO0O0O ,OOOOOOOO00O00OO00 ,OOOO0OOOO0O00OOO0 ):#line:107
        O0OOOO000000OO0OO =all ([OOOO0OOOO0O00OOO0 !=OOOOO0OO0O00OO000 [O00OOOO0O00OO0O0O ][OOOOOO00O000OO0O0 ]for OOOOOO00O000OO0O0 in range (9 )])#line:108
        if O0OOOO000000OO0OO :#line:109
                O0O0OO00OO0OOO0OO =all ([OOOO0OOOO0O00OOO0 !=OOOOO0OO0O00OO000 [O00OOOOOOO0OO0O00 ][OOOOOOOO00O00OO00 ]for O00OOOOOOO0OO0O00 in range (9 )])#line:110
                if O0O0OO00OO0OOO0OO :#line:111
                        OOOO0O00O00O0OOO0 ,O00O0O0OO00OO0O00 =3 *(O00OOOO0O00OO0O0O /3 ),3 *(OOOOOOOO00O00OO00 /3 )#line:113
                        for O0OOOOO00O000OOO0 in range (OOOO0O00O00O0OOO0 ,OOOO0O00O00O0OOO0 +3 ):#line:114
                                for OOOOO0O00O00O0000 in range (O00O0O0OO00OO0O00 ,O00O0O0OO00OO0O00 +3 ):#line:115
                                        if OOOOO0OO0O00OO000 [O0OOOOO00O000OOO0 ][OOOOO0O00O00O0000 ]==OOOO0OOOO0O00OOO0 :#line:116
                                                return False #line:117
                        return True #line:118
        return False #line:119
def solveSudoku (OOOO0O0O000OOOO0O ,i =0 ,j =0 ):#line:121
        i ,j =findNextCellToFill (OOOO0O0O000OOOO0O ,i ,j )#line:122
        if i ==-1 :#line:123
                return True #line:124
        for OOO0O0OO000OOOO00 in range (1 ,10 ):#line:125
                if isValid (OOOO0O0O000OOOO0O ,i ,j ,OOO0O0OO000OOOO00 ):#line:126
                        OOOO0O0O000OOOO0O [i ][j ]=OOO0O0OO000OOOO00 #line:127
                        if solveSudoku (OOOO0O0O000OOOO0O ,i ,j ):#line:128
                                return True #line:129
                        OOOO0O0O000OOOO0O [i ][j ]=0 #line:131
        return False #line:132
def space ():#line:134
    OO0O0O0OOO0000OO0 =[[0 for OOOO0000OO000OO0O in range (9 )]for O0OOOOO00OOOOO0OO in range (9 )]#line:135
    for OOO000O0OO0OO0OO0 in range (9 ):#line:136
      for OO0OOOOOOO000O000 in range (9 ):#line:137
          OO0O0O0OOO0000OO0 [OOO000O0OO0OO0OO0 ][OO0OOOOOOO000O000 ]=game .grid [OOO000O0OO0OO0OO0 ][OO0OOOOOOO000O000 ].value #line:138
    if solveSudoku (OO0O0O0OOO0000OO0 ):#line:139
        for OOO000O0OO0OO0OO0 in range (9 ):#line:140
            for OO0OOOOOOO000O000 in range (9 ):#line:141
                game .grid [OOO000O0OO0OO0OO0 ][OO0OOOOOOO000O000 ].turtle .penup ()#line:142
                game .highlighted =[OOO000O0OO0OO0OO0 ,OO0OOOOOOO000O000 ]#line:143
                keypress (OO0O0O0OOO0000OO0 [OOO000O0OO0OO0OO0 ][OO0OOOOOOO000O000 ])#line:144
    else :#line:146
        print ("Can't solve :()")#line:147
def click (OO0O0OOOO0OO00OOO ,OO00OOO0O0O000O0O ):#line:149
  if OO0O0OOOO0OO00OOO >-220 and OO00OOO0O0O000O0O >-220 :#line:150
    OO0OO0O00O00O0O0O =int ((OO00OOO0O0O000O0O +220 )//50 )#line:151
    O0000OO0OOOOO00OO =int ((OO0O0OOOO0OO00OOO +220 )//50 )#line:152
    if game .grid [OO0OO0O00O00O0O0O ][O0000OO0OOOOO00OO ].highlight (O0000OO0OOOOO00OO ,OO0OO0O00O00O0O0O ):#line:153
        game .highlighted =[OO0OO0O00O00O0O0O ,O0000OO0OOOOO00OO ]#line:154
    else :#line:155
        game .highlighted =False #line:156
def keypress (O000O00O0OO0O0O0O ):#line:159
  if game .highlighted :#line:161
    if O000O00O0OO0O0O0O ==0 :#line:162
      game .grid [game .highlighted [0 ]][game .highlighted [1 ]].value =0 #line:163
      game .grid [game .highlighted [0 ]][game .highlighted [1 ]].draw (x ,y ,"lightblue","black")#line:164
      game .grid [game .highlighted [0 ]][game .highlighted [1 ]].highlight (game .highlighted [1 ],game .highlighted [0 ])#line:165
    else :#line:166
      game .grid [game .highlighted [0 ]][game .highlighted [1 ]].write (game .highlighted [0 ],game .highlighted [1 ],O000O00O0OO0O0O0O )#line:167
      game .grid [game .highlighted [0 ]][game .highlighted [1 ]].highlight (game .highlighted [1 ],game .highlighted [0 ])#line:168
screen =OO00O00OOOO00O000 .Screen ()#line:170
screen .bgcolor ("lightblue")#line:171
game =Game ()#line:173
screen .onkey (space ,"space")#line:176
screen .onkey (lambda :keypress (1 ),"1")#line:177
screen .onkey (lambda :keypress (2 ),"2")#line:178
screen .onkey (lambda :keypress (3 ),"3")#line:179
screen .onkey (lambda :keypress (4 ),"4")#line:180
screen .onkey (lambda :keypress (5 ),"5")#line:181
screen .onkey (lambda :keypress (6 ),"6")#line:182
screen .onkey (lambda :keypress (7 ),"7")#line:183
screen .onkey (lambda :keypress (8 ),"8")#line:184
screen .onkey (lambda :keypress (9 ),"9")#line:185
screen .onclick (click )#line:186
screen .listen ()#line:187
screen .mainloop ()
