"""Buduje index.html i sw.js w katalogu głównym repo z plików w src/.
Użycie: python src/build.py
"""
import sys, re, base64, json, os, shutil
here=os.path.dirname(os.path.abspath(__file__))
src_dir, out = here, os.path.dirname(here)
app=open(src_dir+'/app.html',encoding='utf8').read()
data='\n'.join(open(src_dir+'/'+f,encoding='utf8').read() for f in ['data1.js','data2.js','data3.js','data4.js','data5.js'])
assert '/*__DATA__*/' in app and '/*__STANDALONE__*/false' in app
import datetime
BUILD=datetime.datetime.now(__import__('zoneinfo').ZoneInfo('Europe/Warsaw')).strftime('%d.%m.%Y, %H:%M')
body=app.replace('/*__DATA__*/',data).replace('/*__STANDALONE__*/false','true').replace('__BUILD__',BUILD)
# strip head-ish lines that belong in <head> or reference Google Fonts
lines=[l for l in body.split('\n') if not re.match(r'\s*<(title|meta name="claude:|link rel="(preconnect|stylesheet)")',l)]
body='\n'.join(lines)
LAT='U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
EXT='U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF'
faces=[]
for fam,pkg,slug,weights in [('Barlow','barlow','barlow',[400,500,600,700]),('Barlow Condensed','cond','barlow-condensed',[600,700])]:
  for w in weights:
    for sub,rng in [('latin-ext',EXT),('latin',LAT)]:
      p=f'{src_dir}/fonts/{slug}-{sub}-{w}-normal.woff2'
      b=base64.b64encode(open(p,'rb').read()).decode()
      faces.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{b}) format('woff2');unicode-range:{rng}}}")
head=('<!doctype html><html lang="pl"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
 '<title>Wortschatz A2</title>'
 '<meta name="description" content="Fiszki do niemieckiego A2: 28 lekcji, 1461 słów, fiszki, powtórki i sprawdziany.">'
 '<meta name="theme-color" content="#EDF0F2" media="(prefers-color-scheme: light)">'
 '<meta name="theme-color" content="#0F1418" media="(prefers-color-scheme: dark)">'
 '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">'
 '<meta name="apple-mobile-web-app-status-bar-style" content="default"><meta name="apple-mobile-web-app-title" content="Wortschatz">'
 '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="icon" type="image/png" href="icon-192.png">'
 '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0;font:14px system-ui,-apple-system,sans-serif;-webkit-text-size-adjust:100%}img{max-width:100%}[hidden]{display:none!important}'
 +''.join(faces)+'</style></head><body>')
open(out+'/index.html','w',encoding='utf8').write(head+body+'</body></html>')
ver=str(len(open(out+'/index.html','rb').read()))
sw="""const CACHE='wortschatz-%s';
const ASSETS=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./icon-maskable-512.png','./apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const req=e.request;if(req.method!=='GET')return;
  const url=new URL(req.url);if(url.origin!==self.location.origin)return;
  if(req.mode==='navigate'){
    e.respondWith(fetch(new Request(req.url,{cache:'no-cache',credentials:'same-origin'})).then(r=>{if(r.ok){const cp=r.clone();caches.open(CACHE).then(c=>c.put('./index.html',cp));}return r;}).catch(()=>caches.match('./index.html')));
    return;
  }
  e.respondWith(caches.match(req).then(r=>r||fetch(req).then(res=>{if(res.ok){const cp=res.clone();caches.open(CACHE).then(c=>c.put(req,cp));}return res;})));
});
""" % ver
open(out+'/sw.js','w',encoding='utf8').write(sw)
print('Zbudowano index.html i sw.js')
