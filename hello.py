from cgi import parse_qs                                                        
                                                                                
def app(environ, start_response):                                               
        status = '200 OK'                                                       
        headers = [                                                             
                ('Content-Type', 'text/plain')                                  
        ]                                                                       
        start_response(status, headers )                                        
        qs = parse_qs(environ['QUERY_STRING'])                                  
        #return ['%s=%s<br>' % (k, qs[k][0]) for k in qs ]                      
        resp = environ['QUERY_STRING'].split("&")                               
        resp = [item+"\r\n" for item in resp]                                   
        return resp
