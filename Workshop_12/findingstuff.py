import urllib.request

opener = urllib.request.FancyURLopener({})
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
f = opener.open(url)
content = f.read().decode('utf-8')

print(content)