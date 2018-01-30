from django.shortcuts import render
from django.http import HttpResponse
from subprocess import check_output
import shlex

def returnFirstWord(s):
	i = 0
	temp = ''
	while i < len(s) and s[i] != ' ':
		temp += s[i]
		i += 1
	return temp	

def getResult(req, template = 'main.html'):
	if req.method == 'POST':
		try:
			if req.is_ajax():
				curl_data = req.POST['curl_text'].strip()			
				if curl_data == '' or curl_data is None:
					a = "Empty curl field <err1xef2>"
					return HttpResponse(a)
				elif returnFirstWord(curl_data) != 'curl':
					a = "Not a curl command or curl is spelled out wrong <err1xef2>"
					return HttpResponse(a)
				else:	
					curl_data = shlex.split(curl_data)		
					_p = check_output(curl_data, shell=False)
					a = _p
					return HttpResponse(a)
		except:
			a = "Wrong cURL syntax <err1xef2>"	
			return HttpResponse(a)		
	return render(req, template)
