
import sys
import os
import subprocess
import time
from server import send_data
import json
import requests

def initialization(x,y,x1,y1):
    x0,y0,xf,yf=x,y,x1,y1
    start(x0,y0,xf,yf)

def start(x0,y0,xf,yf):
    try:
        os.remove('f.txt')
    except:
        pass

    print('x0,y0,xf,yf',x0,y0,xf,yf)
    write_on_file(x0,y0,xf,yf)
    fileobj=open('path.txt','r')
    for line in fileobj:
        if line =='1':
            print('path 1 is selected')
            if x0<xf:
                draw(x0,xf)
            else:
                draw_m2(x0,xf) 
            send_data('l01r01.')

            if x0<xf:
                draw(y0,yf)
            else:
                draw_m2(y0,yf) 

        else:
            print('path 2 is selected')
            #send_data('path2')
            if x0<xf:
                draw(y0,yf)
            else:
                draw_m2(y0,yf) 

            send_data('l00r01.')
            if x0<xf:
                draw(x0,xf)
            else:
                draw_m2(x0,xf)


def draw(v0,vf):
    for v0 in range(v0,vf):
        print('v0,vf',v0,vf)
        if v0%6==0:
            time.sleep(1)
            
            send_data('l01r01.')

            try:
                ob=open('d.txt','r')
                for line in ob:
                    print(line)
                    st=line.split(',')
                a1,a2,b1,b2=int(st[0]),int(st[1]),int(st[2]),int(st[3])
                ob.close()
                try:
                    print("removing d.txt")
                    os.remove('d.txt')
                    print('calling',a1,a2,b1,b2,"v0,vf",v0,vf)
                    start(a1,a2,b1,b2)
                except:
                    pass
            except:
                pass

def draw_m2(v0,vf):
    for v in range(v0, vf, -1):
        print('v0,vf',v0,vf)
        if v%6==0:
            time.sleep(1)
            send_data('l01r01.')
            try:
                ob=open('d.txt','r')
                for line in ob:
                    print(line)
                    st=line.split(',')
                a1,a2,b1,b2=int(st[0]),int(st[1]),int(st[2]),int(st[3])
                ob.close()
                try:
                    print("removind d.txt")
                    os.remove('d.txt')
                    print('calling',a1,a2,b1,b2,"v0,vf",v0,vf)
                    start(a1,a2,b1,b2)
                except:
                    pass
            except:
                pass        


def starter():
    try:
        fob=open('d.txt','r')
    except:
        print('-------------------------------------------------------------------------------------')
        print('\n\nd.txt NOT FOUND CREATE d.txt AND ENTER SOURCE AND DEST, example 0,0,18,36\n\n')
        print('-------------------------------------------------------------------------------------')
    for line in fob:
        st=line.split(',')
    a1,a2,b1,b2=int(st[0]),int(st[1]),int(st[2]),int(st[3])
    try:
        subprocess.call('rm d.txt')
    except:
        pass
    initialization(a1,a2,b1,b2)

def write_on_file(x0,y0,xf,yf):
    obj=open('f.txt','a')
    v=str(x0)+','+str(y0)+','+str(xf)+','+str(yf)
    obj.write(v)

starter()