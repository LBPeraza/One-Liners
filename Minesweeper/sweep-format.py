
(lambda r,c,n:# rows, cols, number of mines
  (lambda r,c:
    (lambda n:
    (lambda M,S,K,W,Z:# margin, cell size, box size, Z combinator
      (lambda a:
        (lambda t,T,s,B,g:# tkinter,time,getCellBounds(row,col),getCell(x,y)
            (lambda R,u:# root,upperTriangle
                (lambda C:# canvas
                    C.pack()or
                    (lambda m,z,x,v,k,o,i:# generateMines(r,c), create_rect/poly/oval/line/text/arc
                        (lambda b,q:# board,replaceCell(board,row,col,newVal)
                            (lambda p:# makeMove(row,col,board),replaceCell(board,row,col,newVal)
                                (lambda P,O,Y,d,y:# data, drawRaised/Sunken Rect
                                    (lambda e,Q:# drawCell, timerFired
                                        (lambda F,w:# redrawAll
                                            # R.bind('<Key>',lambda e:print(d[8]))and
                                            s.setrecursionlimit(15000)or
                                            R.bind('<Button-1>',lambda e:(
                                              d.update({3:e.x,4:e.y})or
                                              (lambda P:(
                                                d.update({1:P,9:T.time()}if not d[6]and(d[7]or not d[8])else{})
                                                )if P else None
                                              )(g(e.x,e.y))
                                              )or w())and
                                            R.bind('<B1-Motion>',lambda e:d.update({1:g(e.x,e.y),3:e.x,4:e.y}
                                              if(d[7]or not d[8])and not d[6]else{})or w())and
                                            (lambda t:
                                              R.bind('<Button-2>',t)and
                                              R.bind('<Button-3>',t)
                                            )(lambda e:
                                              ((d.update({0:F(d[0],*g(e.x,e.y))})
                                               or d.update({
                                                  7:n-sum(map(lambda r:r.count(-1),d[0])),
                                                  8:all(map(lambda r:None not in r,d[0]))
                                                }))if g(e.x,e.y)else None)or w()
                                              )and
                                            R.bind('<B1-ButtonRelease>',lambda e:
                                              ((d.update({
                                                2:T.time(),
                                                5:m(*g(e.x,e.y))
                                              })if(d[5]==None and g(e.x,e.y))else(
                                                d.update({
                                                  0:[[None]*c for _ in[0]*r],
                                                  1:0,2:None,3:0,4:0,5:None,6:False,7:n,8:False
                                                })if P<=e.x<=P+Y and O<=e.y<=O+Y else None
                                              ))or
                                              (lambda x:#print(x)or
                                                ((d.update({
                                                  0:x[0],
                                                  6:x[1]
                                                  })
                                                or d.update({8:all(map(lambda r:None not in r,d[0]))}))if x!=None else None)
                                              )(p(*g(e.x,e.y),d[0],d[5])if g(e.x,e.y)and not d[6]and d[5]!=None else None)
                                              )or
                                              d.update({1:None,3:0,4:0})or w())and
                                            Q(w)and
                                            w()
                                        )(lambda B,R,C:
                                            q(B,R,C,-1)if B[R][C]==None else(
                                              q(B,R,C,None)if B[R][C]==-1 else B),
                                          lambda:# def redrawAll()
                                            (lambda H:
                                              C.delete(t.ALL)or
                                              y(K,K,2*M+c*S-K,a+r*S-K+M,1)and# grey background
                                              y(M,M,M+c*S,a-M,0)and# top box
                                              z(2*M-K,2*M-K,2*M-K+50,a-2*M+K,fill='black',width=0)and# left text bg
                                              o(2*M-K+25,a/2,fill='red',text='%03d'%# left text
                                                d[7],font='courier 20'
                                                )and
                                              H()and# smiley face
                                              z(c*S+K-50,2*M-K,c*S+K,a-2*M+K,fill='black',width=0)and# right text bg
                                              o(c*S+K-25,a/2,fill='red',font='courier 20',text=('000'if d[2]==None else# right text
                                                '%03d'%min(999,int(d[9]-d[2]))))and
                                              z(M,a,M+c*S,a+r*S,fill='#666',width=0)and# dark grey bg
                                              [e(i,j)for i in range(r)for j in range(c)]and# draw all cells
                                              y(M,a,M+c*S,a+r*S,0,0)and# sink the cells
                                              1
                                            )(lambda:#print(d[6])or
                                            #P: left
                                            #O: top
                                            #K: margin
                                            #Y: width/height
                                                (lambda K,D,T,E,F,G,H:
                                                  y(P,O,P+Y,O+Y,0 if (P<=d[3]<=P+Y and O<=d[4]<=O+Y)else 1,0)and
                                                  v(P+K,O+K,P+Y-K,O+Y-K,fill='yellow')and
                                                  ((i(P+2*K,O+0.55*Y,P+Y-2*K,O+Y+2*K,start=30,extent=120,style=t.ARC)and
                                                    k(P+E*Y,O+E*Y,P+E*Y+D,O+E*Y+D)and
                                                    k(P+E*Y,O+E*Y+D,P+E*Y+D,O+E*Y)and
                                                    k(P+(1-E)*Y,O+E*Y,P+(1-E)*Y-D,O+E*Y+D)and
                                                    k(P+(1-E)*Y,O+E*Y+D,P+(1-E)*Y-D,O+E*Y)
                                                    )if d[6]else
                                                      (v(P+E*Y,O+E*Y,P+E*Y+D,O+E*Y+D,fill='black',width=0)and
                                                       v(P+(1-E)*Y,O+E*Y,P+(1-E)*Y-D,O+E*Y+D,fill='black',width=0)and
                                                       v(P+Y/2-D,O+Y/2,P+Y/2+D,O+3*Y/4))
                                                    if d[1]else
                                                      (v(P+T*Y,O+Y/2-D,P+T*Y+D,O+Y/2,fill='black',width=0)and
                                                       v(P+2*Y/3-D,O+Y/2-D,P+2*Y/3,O+Y/2,fill='black',width=0)and
                                                       i(P+Y/4,O+Y/4,P+3*Y/4,O+3*Y/4,start=215,extent=110,style=t.ARC))
                                                    if d[7]or not d[8]else(
                                                      i(P+Y/4,O+Y/4,P+3*Y/4,O+3*Y/4,start=205,extent=130,style=t.ARC)and
                                                      v(P+Y*F,O+Y*G,P+Y*F+H,O+Y*G+H,fill='black',width=0)and
                                                      v(P+(1-F)*Y,O+Y*G,P+(1-F)*Y-H,O+Y*G+H,fill='black',width=0)and
                                                      # z(P+F*Y,O+Y*G,P+Y*F+H+1,O+Y*G+H/2,fill='black',width=0)and
                                                      # z(P+(1-F)*Y+1,O+Y*G,P+(1-F)*Y-H,O+Y*G+H/2,fill='black',width=0)and
                                                      k(P+Y*F,O+Y*G+H/4,P+K,O+Y/2)and
                                                      k(P+(1-F)*Y,O+Y*G+H/4,P+Y-K,O+Y/2)and
                                                      k(P+Y*F,O+Y*G+H/4,P+(1-F)*Y,O+Y*G+H/4)
                                                    )
                                                  )
                                              )(4,4,0.3,0.3,0.25,0.35,8)
                                            )
                                          )
                                    )((lambda r,c:# def drawCell(row, col)
                                        (lambda f,g:
                                            (((#z(B(r,c),width=0,fill='black')and
                                             # x(u(r,c),fill='white')and
                                              (((lambda a,b:
                                                x(b[0],(b[1][0],b[0][1]),(b[0][0],b[1][1]),fill='white')and# white upper triangle
                                                z(a,fill='grey',width=0)#actual grey part
                                                )(B(r,c,K),B(r,c)))and
                                                # y(a[0][0],a[0][1],a[1][0],a[1][1],1))(B(r,c,K))and
                                                ((f()
                                                  if d[0][r][c]==-1
                                                  # if (r,c)in d.get(5,set())
                                                  else 1))
                                                if((r,c)!=d[1]or d[0][r][c]==-1)and(not d[6]or (r,c)not in d[5])else z(B(r,c),fill='grey',outline='#666666')
                                              )
                                                if d[0][r][c]in[None,-1]
                                                # z(B(r,c,1),width=0,fill='white')and
                                             # (z(B(r,c,K),fill='grey',width=0)))if d[0][r][c]==None
                                             else z(B(r,c),fill='grey',outline='#666666'))and
                                            ((lambda i:
                                                o((i[0][0]+i[1][0])/2,
                                                  (i[0][1]+i[1][1])/2,
                                                  fill=['blue','#008800','red','#440088','maroon','turquoise','black','#444444'][(d[0][r][c]-1)%8],
                                                  text=str(d[0][r][c]),
                                                  font='arial 14 bold'
                                             ))(B(r,c))if d[0][r][c]not in[None,-1,0] else 0))
                                            if(g==0)or d[6]!=(r,c)else
                                              (z(B(r,c),fill='red',outline='#666666')and 0 if d[6]==(r,c)else None)
                                            )or
                                            (None if(g>=0)or(r,c)not in d[5]else(
                                                (lambda A:
                                                  (lambda a,b,C,R,m:#(print(a,b,C,R)if(r,c)==(1,1)else None)or
                                                    [v(x-R,y-R,x+R,y+R,fill='black',width=0) for(x,y)in
                                                      [(a+C*m.cos(m.radians(l)),b-C*m.sin(m.radians(l)))for l in range(0,360,45)]])(*A)
                                                )((lambda b:(
                                                    (b[0][0]+b[1][0])/2,
                                                    (b[0][1]+b[1][1])/2+0.5,
                                                    (b[1][0]-b[0][0])/2+0.5,
                                                    1,__import__('math')))(B(r,c,5)))and
                                                 v(B(r,c,5),fill='black',width=0)and
                                                 v(B(r-0.05,c-0.05,9.5),fill='white',width=0)
                                                ))
                                        )(lambda:(lambda p:
                                            # (print(r,c,p,p[0][0],p[1][0]))or
                                            k(p[0][0]+(p[1][0]-p[0][0])/4,
                                              p[0][1]+(p[1][1]-p[0][1])/7,
                                              p[0][0]+(p[1][0]-p[0][0])/4,
                                              p[1][1]-(p[1][1]-p[0][1])/7)and
                                            x(p[0][0]+(p[1][0]-p[0][0])/4,
                                              p[0][1]+(p[1][1]-p[0][1])/7,
                                              p[0][0]+(p[1][0]-p[0][0])/4,
                                              p[0][1]+(p[1][1]-p[0][1])/2,
                                              p[1][0]-(p[1][0]-p[0][0])/3,
                                              p[0][1]+(p[1][1]-p[0][1])/3,
                                              fill='red',width=1,outline='black')
                                            )(B(r,c,K)),
                                            (0 if not d[6] else -1)if d[7]or not d[8] else 1 #  0: playing
                                                                                             #  1: won
                                                                                             # -1: lost
                                          )
                                        ),
                                          Z(lambda f:lambda w:(d.update({9:T.time()}if not d[6]and(d[7]or not d[8])else{})or w()and None)or(C.after(1000,f,w)))
                                     )
                                )((2*M+c*S)/2-W*S/2+M,a/2-W*S/2+M,W*S-2*M,
                                  {0:b,1:0,2:None,3:0,4:0,5:None,6:False,7:n,8:False,9:None},
                                  lambda a,b,c,d,e,f=1:
                                        (lambda C:
                                            z(a-K,b-K,a,d,fill=C[e],width=0)and
                                            z(a-K,b-K,c,b,fill=C[e],width=0)and
                                            z(a-K,d,c+K,d+K,fill=C[e^1],width=0)and
                                            z(c,b-K,c+K,d+K,fill=C[e^1],width=0)and
                                            x(a-K,d+K,a,d,a-K,d,fill=C[e])and
                                            x(c,b-K,c+K,b-K,c,b,fill=C[e])and
                                            (z(a,b,c,d,fill='grey',width=0)if f else 1)
                                        )(['#666666','white'])
                                            # x(a-K,b-K,c+K,b-K,a-K,d+K,fill='#666666')and
                                            # x(a-K,d+K,c+K,b-K,c+K,d+K,fill='white')and
                                        )
                            )(Z(lambda f:(lambda R,C,B,M:# makeMove(row, col, board,mines)
                                    ((B,(False))if R<0 or R>=r or C<0 or C>=c or B[R][C]!=None
                                     else ((B,(R,C))
                                        if(R,C)in M
                                        else(
                                          ((lambda v:(
                                              (lambda N:
                                                N if v>0 else
                                                f(R+1,C+1,
                                                  f(R+1,C,
                                                    f(R+1,C-1,
                                                      f(R,C+1,
                                                        f(R,C-1,
                                                          f(R-1,C+1,
                                                            f(R-1,C,
                                                              f(R-1,C-1,N,M)[0],M
                                                            )[0],M
                                                          )[0],M
                                                        )[0],M
                                                      )[0],M
                                                    )[0],M
                                                  )[0],M
                                                )[0]
                                              )(q(B,R,C,v))
                                            )
                                          )(
                                              len(set({(R-1,C-1),(R-1,C),(R-1,C+1),
                                                   (R,C-1),          (R,C+1),
                                                   (R+1,C-1),(R+1,C),(R+1,C+1)})&M)
                                            ),False)
                                        )
                                        ))))
                                )
                    )(
                        # (lambda R:[[R.choice([None]+list(range(-1,9)))for j in range(c)] for i in range(r)])(__import__('random'))
                     [[None]*c for _ in [0]*r]
                     ,
                      lambda b,r,c,n:# q: replaceValue(board,row,col,newVal)
                          [[(b[i][j]if(i,j)!=(r,c)else n)for j in range(len(b[0]))]for i in range(len(b))]))(
                      (lambda R,C:
                        (lambda M:
                          set(
                            M.sample(
                              {(i,j) for j in range(c) for i in range(r)}-{(R-1,C-1),(R-1,C),(R-1,C+1),
                                                                           (R,C-1),  (R,C),  (R,C+1),
                                                                           (R+1,C-1),(R+1,C),(R+1,C+1)}
                            ,n))
                        )(__import__('random'))),
                       C.create_rectangle,C.create_polygon,C.create_oval,C.create_line,C.create_text,C.create_arc)
            )(t.Canvas(R,width=2*M+c*S,height=a+M+r*S,bd=0,highlightthickness=0))
            )(t.Tk(),
             lambda r,c:#def get upper triangle
                (B(r,c)[0],(B(r,c)[0][0],B(r,c)[1][1]),(B(r,c)[1][0],B(r,c)[0][1]))
             )
        )(__import__('tkinter'),
          __import__('time'),
          __import__('sys'),
         lambda r,c,m=0:(# def getCellBounds(r,c): ((x0,y0),(x1,y1))
            (M+c*S+m,a+r*S+m),
            (M+(c+1)*S-m,a+(r+1)*S-m)),
         lambda x,y:# def getCell(x,y): (r,c) or (None,None)
            (lambda R,C:(R,C)if(0<=R<r and 0<=C<c)else None
                )(int((y-3-a)//S),int((x-3-M)//S)))
        )(2*M+W*S)
    )(10,21,2,2.5,lambda f:(lambda x:f(lambda *args:x(x)(*args)))(lambda x:f(lambda *args:x(x)(*args))))
)(min([n,r*c-9,(r-1)*(c-1)])))(max(r,9),max(c,9)))(16,30,99)

