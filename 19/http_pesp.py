'''
Informational responses (100 – 199)
Successful responses (200 – 299)
Redirection messages (300 – 399)
Client error responses (400 – 499)
Server error responses (500 – 599)

'''



{}.get()

def info():return
process_responces = {
    1:info,
    2:lambda: print("Successful response"),
    3:redirect,
    4:cl_error,
    5:serv_error,
}

code = 1
process_responses.get(code)()

