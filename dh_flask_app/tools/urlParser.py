import urllib.parse

def url_converter(url):
    try:
        p = urllib.parse.urlparse(url, 'http')
        netloc = p.netloc or p.path
        path = p.path if p.netloc else ''
        if not netloc.startswith('www.'):
            netloc = 'www.' + netloc
        p = urllib.parse.ParseResult('http', netloc, path, *p[3:])
        return p.geturl()
    except:
        return url