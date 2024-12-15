import requests

url=input("Url daxil et:")



security_headers = {
    "Strict-Transport-Security": "",
    "Content-Security-Policy": "",
    "X-Content-Type-Options": "",
    "X-Frame-Options": "",
    "X-XSS-Protection": "",
    "Referrer-Policy": "",
    "Permissions-Policy": "",
    "Cache-Control": "",
    "Access-Control-Allow-Origin": "",
    "Expect-CT": "",
    "Feature-Policy": "",
    "Set-Cookie": "",
    "Cross-Origin-Resource-Policy": "",
    "Cross-Origin-Opener-Policy": "",
    "Cross-Origin-Embedder-Policy": "",
    "Server": "",
    "X-Permitted-Cross-Domain-Policies": ""
}
# security_headers["Access-Control-Allow-Origin"]=url
response=requests.get(url)
print(response.headers)
for header in security_headers:
    if header in response.headers:
        print(f"{header}: {response.headers[header]}")
    else:
        print(f"{header}: Not found")
