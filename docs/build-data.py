# Erzeugt docs/data/workflows.js aus den bereinigten Exporten in workflows/.
# Aufruf aus dem Repo-Wurzelverzeichnis: python3 docs/build-data.py
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = [
  ('chain',  '01', 'Recherche und Titelwahl', '01-recherche-und-titelwahl.json'),
  ('chain',  '02', 'Manuskript',              '02-manuskript-produktion.json'),
  ('chain',  '03', 'Cover und Versand',       '03-cover-metadaten-versand.json'),
  ('chain',  '04', 'Redaktionelle Freigabe',  '04-redaktionelle-freigabe.json'),
  ('chain',  '09', 'Etsy-Produkte',           '09-etsy-produkte-und-listings.json'),
  ('manual', '14', 'Print-Cover',             '14-print-cover.json'),
  ('manual', '15', 'Titelei reparieren',      '15-titelei-platzhalter.json'),
  ('system', '',   'Fehler-Alarm',            'system/fehler-alarm.json'),
  ('system', '',   'Execution fortsetzen',    'system/execution-fortsetzen.json'),
  ('system', '',   'Testlauf-Starter',        'system/testlauf-starter.json'),
  ('system', '',   'Websuche (Sub)',          'system/tavily-suche-sub.json'),
]
out = []
for gruppe, nr, titel, datei in LISTE:
    w = json.load(open(os.path.join(ROOT, 'workflows', datei), encoding='utf-8'))
    out.append({'key': datei.split('/')[-1].replace('.json', ''), 'group': gruppe, 'nr': nr,
                'title': titel, 'file': 'workflows/' + datei,
                'nodes': w['nodes'], 'connections': w['connections']})
with open(os.path.join(ROOT, 'docs', 'data', 'workflows.js'), 'w', encoding='utf-8') as f:
    f.write('window.WORKFLOWS = ' + json.dumps(out, ensure_ascii=False) + ';\n')
print(len(out), 'Workflows geschrieben')
