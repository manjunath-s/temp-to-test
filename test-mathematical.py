import requests
import json

gqry = "gremlin=g.V().has('vertex_label','Version').has('pname',within('io.vertx:vertx-core')).in('has_dependency').values('sid')"
payload = {'gremlin':gqry}
url = 'http://bayesian-gremlin-http-saket-graph.dev.rdu2c.fabric8.io/'

r = requests.post(url,data=json.dumps(payload))

sids = r.json()['result']['data']

sidslen = len(sids)

strsids = '\',\''.join(map(str, sids))
strsids = strsids.replace('\n',"")
gqry1 = "g.V().has('vertex_label','Stack').has('sid',within('"+strsids+"')).out('has_dependency').values('pname').count().map(union(identity(),constant("+str(sidslen)+")).fold(1){a,b -> b/a})"


payload = {'gremlin':gqry1}
url = 'http://bayesian-gremlin-http-saket-graph.dev.rdu2c.fabric8.io/'

r = requests.post(url,data=json.dumps(payload))
print(r.text)


