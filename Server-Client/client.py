##############################################################################
# author: kumark2                                                            #
# email: kiran.kumar@aalto.fi                                                #
##############################################################################
# The function 'client()' present in this is called from the phy_interace.py #
# It interacts with the server.py file inorder to do the periodic            #
# measurements (upload, download and ping) and sends these data to server    #
############################################################################## 

#!/usr/bin/python

import socket,os,sys, subprocess, datetime, time
host = '10.42.0.1' # Should always know the IP address of the local_RRM
#host = '10.100.6.250'

def m_client():
    # Make a new socket 
    m= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start=datetime.datetime.now()
    startedAt= str(start.strftime("%m_%d_%H_%M_%S"))
    try:
        m.bind(('10.42.0.77', 6005))
        #m.bind(('10.100.13.175', 6005))
    except:
        print "Bind failed1"

    try:
            #Receive MeasurementResponse from the enodeB
            data2, addr = m.recvfrom(1024)
            recv_data=eval(data2)
            data=recv_data[0]
            print "Received", data, "from", addr
            list1=recv_data[1]
            new_addr =addr

            # Check for the received parameters
            if data=="MeasurementResponse":
                lis=["Ready", 1]
                time.sleep(1)
                m.sendto(repr(lis), new_addr)

                #=======================Receiving 10 sec data==========================
                fp = open("myfile.pdf",'w')
                print "Receiving upload data for 10 sec"
                while 1:
                    fname, addr = m.recvfrom(1024)
                    fp.write(fname)
                    if (fname=="done"):
                        print fname
                        break 
                fp.close()

            #Find out the size of the file received from the server
            statinfo = os.stat("myfile.pdf")
            download_size = (statinfo.st_size)/10
            print "Download data is of size", download_size

            #=======================Sending 10 sec data==========================
            time.sleep(1)
            start_time = time.time()
            end_time = start_time + 10
            print "Sending upload data for 10 sec"
            f = open("Finnish.pdf", 'r')
            while time.time() < end_time:                
                data = f.read(1024)
                #print data
                m.sendto(data, new_addr)
                pass
            m.sendto("done",new_addr)
            f.close()
            print "DATA SENT"
            
            #Receive the upload file size from the server
            data2, addr = m.recvfrom(1024)
            recv_data=eval(data2)
            data=recv_data[0]
            list1=recv_data[1]
            print "Upload data is of size", list1
            upload_size = list1/10
            
            #=======================Ping test==========================
            totalTime = 0
            totalPings = 0

            while totalPings< 10:
                totalPings = totalPings + 1
                start = time.time()
                m.sendto(repr(totalPings),new_addr)
                try:
                    ping_data, addr = m.recvfrom(1024)
                    elapsed = ((time.time() - start)) * 1000
                    totalTime = totalTime + elapsed
                except:
                    print "Connection timed out for Packet #", totalPings

            ping_average = totalTime/10
            print "Average round trip", ping_average

            #Sending the final Measurement Message containing Client ID,Start Time, End Time, Ping Average,
            #Download throughput, upload throughput
            end=datetime.datetime.now()
            endedAt= str(end.strftime("%m_%d_%H_%M_%S"))
            list1 = [1, startedAt, endedAt, ping_average, download_size, upload_size]
            mylist= ["Measurement_message",list1]
            time.sleep(1)
            m.sendto(repr(mylist),new_addr)
    except:
          print "error in m_client"

if __name__=='__main__':
    m_client()
