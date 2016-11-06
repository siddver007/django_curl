from django.shortcuts import render
from django.http import HttpResponse
from subprocess import Popen, PIPE, STDOUT

def returnFirstWord(s):
	i = 0
	temp = ''
	while i < len(s) and s[i] != ' ':
		temp += s[i]
		i += 1
	return temp	

def getResult(req, template = 'main.html'):
	if req.method == 'POST':
		if req.is_ajax():
			curl_data = req.POST['curl_text'].strip()			
			if curl_data == '' or curl_data is None:
				a = "Empty curl field <err1xef2>"
				return HttpResponse(a)
			elif returnFirstWord(curl_data) != 'curl':
				a = "Not a curl command or curl is spelled out wrong <err1xef2>"
				return HttpResponse(a)
			else:	
				_p = Popen(curl_data + ' -s', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
				output = _p.stdout.read()
				a = output
				return HttpResponse(a)
	return render(req, template)
