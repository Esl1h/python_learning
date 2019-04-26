#!/usr/bin/python

import sys, smtplib, string, time, rfc822, os, re

def error_hanlder(msg):
    error_fp = open("/tmp/smg_error" + os.getpid().__str__(), 'w')
    error_fp.write(msg)
    error_fp.close()

def main():
    emailname_in = 'fjsabai@gmail.com'
    smtpserver_in = 'gsmtp57.google.com'
    if len(sys.argv) > 1:
	print "\nSend Mail to Gmail (SMG) by Fabio Sabai <fjsabai@gmail.com>\n"  
	i = 1
	if re.compile("@([-a-zA-Z0-9_]+\\.)+[a-zA-Z]{2,3}$").match(sys.argv[1]) is not None:
	    emailname_in = sys.argv[1]
	    i = 2
	if re.compile("([a-zA-Z0-9_]+\\.)+(com|gov|org|ufu){1}(\\.br)?$").match(sys.argv[1]) is not None:
	    smtpserver_in = sys.argv[1]
	    i = 2
	count = [0, 0, 0]
	error_fp = open("/tmp/smg_error" + os.getpid().__str__(), 'w');
	while i < len(sys.argv):
	    mail_filename_in = sys.argv[i]
	    fp = open(mail_filename_in)
	    msg = rfc822.Message(fp)
	    try:
		document = msg.fp.read()
		if document is not None:
		    time.sleep(2)
		    try:
			fullmsg = msg.__str__( ) + '\x0a' + document
	    	        server = smtplib.SMTP(smtpserver_in)
			server.sendmail(msg.getaddr('From')[1], emailname_in, fullmsg)
			server.quit()
			count[0] = count[0] + 1
		        print "    %d Forwarded a message from  : %s"  % (count[0], msg.getaddr('From')[1])
		    except:
			error_fp.write(mail_finename_in + ' ')
			count[1] = count[1] + 1
			print "*** %d ERROR SENDING MESSAGE FROM: %s"  % (count[1], msg.getaddr('From')[1])
	    except:
		count[2] = count[2] + 1
		error_fp.write(mail_filename_in + ' ')
		print "*** %d MESSAGE READ FAILED, SKIPPED" % (count[2])
	    i = i + 1
	    fp.close()
	error_fp.write('\n')
	error_fp.close()
        if count[1] == 0 and count[2] == 0:
	    os.unlink('/tmp/smg_error' + os.getpid().__str__())
	print "\nDone. Stats: %d success %d error %d skipped." % (count[0], count[1], count[2])
    else:
	persist = 1
	from_addr = ""
	fullmsg = ""
	while persist:
    	    try:
    	        line = raw_input()
		fullmsg += line + '\n'
		if line.startswith('From:'):
		    from_addr = line.replace('From:', '').strip()
	    except:
    		persist = 0
	if from_addr != "":
	    pid = os.fork();
	    if pid > 0:
		print fullmsg
		sys.exit(0)
	    elif pid < 0:
		error_handler(fullmsg)
		sys.exit(1)
	    else:
	        try:
		    server = smtplib.SMTP(smtpserver_in)
		    server.sendmail(from_addr, emailname_in, fullmsg)
		    server.quit()
	        except:
		    error_handler(fullmsg)
	else:
	    error_handler(fullmsg)

if __name__ == "__main__":
    main()
