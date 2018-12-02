import socket
import time
import sys

TCP_IP = '0.0.0.0'
TCP_PORT = 5008

BUFFER_SIZE = 20 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connection address:', addr)

def send_data(val):
    while  True:
        data = conn.recv(BUFFER_SIZE).decode()
        if not data: break
        time.sleep(1)
        print (data)
        if data=='quit':
            s.close()
            sys.exit(0)
        
        if data !='ok':
            print('sleep 5 sec')
            time.sleep(1)
        
        line=[]
        file=open('log.txt','r')
        for l in file:
            line.append(l)
        print(line[-1])
        if line[-1].replace('\n','') ==data.replace('\n','') and line[-1].replace('\n','')!='ok':
            print('deviating')
            print('move rotate right and go 10cm and rotate left')
            
            conn.send('l01r00.'.encode())
            var= conn.recv(BUFFER_SIZE).decode()
            print('>',var)
            conn.send('l01r01.'.encode())
            var= conn.recv(BUFFER_SIZE).decode()
            print('>',var)
            conn.send('l00r01.'.encode())

            try:
                v=data.split(',')
                x0,y0,xf,yf= int(v[0])+10 ,int(v[1]),int(v[2]),int(v[3])
                string=str(x0)+','+str(y0)+','+str(xf)+','+str(yf)
                ob=open('d.txt','w')
                ob.write(string)
                ob.close()
            except:
                print('pass')
        file.close()

        fileob=open('log.txt','a+')
        fileob.write(data+'\n')
        fileob.close()    

        if data == 'ok':
            conn.send(val.encode()) 
        if not data == 'ok':
            conn.send('l00r00.'.encode())
        break
