#####################################################################################
# author: kumark2                                                                   #
# email: kiran.kumar@aalto.fi                                                       #
#####################################################################################
# The function 'server()' present in this is called from the local_rrm.py         #
# It interacts with the client.py file inorder to receive the periodic measurement#
# (upload, download and ping) from the UE                                           #
##################################################################################### 

#!/usr/bin/python

import socket, os, time, subprocess, datetime, sys
#import write_data
import record_data

# Function called from local_RRM to receive measurement data
def server_2():
	m = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client=('10.42.0.77', 6005)
	#client=('10.100.13.175', 6005)
	try:

		    time.sleep(3)
		    ticket=datetime.datetime.now()
		    ticketrequestedAt=str(ticket.strftime("%m_%d_%H_%M_%S"))
		    list2=(00000001,1.0,ticketrequestedAt)
		    my_list=["MeasurementResponse", list2]
		    m.sendto(repr(my_list), client)

		    try:
		    		#Wait to receive the "Ready" message from the client
			    	recv_data, addr= m.recvfrom(1024)
			    	list1=eval(recv_data)
			    	new_addr = addr
			    	data=list1[1]
			    	recv_data = list1[0]
			    	print "Received", recv_data, "from", addr

			    	if (recv_data =="Ready"):
			    		start_time = time.time()
			    		end_time = start_time + 10

		    			#==========================Sending 10 sec data================================
			    		print "Sending download data for 10 sec"
			    		f = open("Finnish.pdf", 'r')
			    		while time.time() < end_time:		    				
		    				data = f.read(1024)
		    				m.sendto(data, client)
		    				pass
		    			m.sendto("done",client)
		    			f.close()
		    			print "DATA SENT"
		    			
		    			#==========================Receiving 10 sec data================================
		    			fp=open("myfile.pdf",'w')
		    			print "Receiving upload data for 10 sec"
		    			while 1:
		    				fname,addr = m.recvfrom(1024)
		    				#print fname
		    				fp.write(fname)
		    				if (fname == "done"):
		    					print fname
		    					break
		    			fp.close()

		    			#Find out the size of the file received from the Client
		    			statinfo = os.stat("myfile.pdf")
		    			upload_size = statinfo.st_size
		    			print upload_size
		    			list3=(upload_size)
		    			my_list=["uploadSize", list3]
		    			m.sendto(repr(my_list), client)

			    		#==========================Ping test===============================
			    		try:
			    			a = 0
			    			while a < 10:
			    				a = a+1
			    				ping_data, ping_addr = m.recvfrom(1024)
			    				#print "Received", ping_data, "from", ping_addr
			    				m.sendto(ping_data,client)
			    		except:
			    			print "Error in PING"

			    		recv_data, addr= m.recvfrom(1024)
			    		list1=eval(recv_data)
			    		data=list1[1]
			    		recv_data = list1[0]
			    		print data
			    		print "Received", recv_data, "from", addr
			    		#write_data.write_data(data)
			    		record_data.record_data(data)

		    except:
			  	print "Error in server_2"
			  	return 0

	except:
		print "Error in server_2 outer"
		return 0


