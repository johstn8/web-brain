#!/usr/bin/env python3
"""Link-Check fuer das Web-Brain-Vault.

Prueft jeden Wikilink auf existierende Zieldatei und existierenden Anker.
Meldet ausserdem Pfade mit Leerzeichen oder Grossbuchstaben.
Exit-Code 1, sobald ein toter Link gefunden wird.
"""
import os, re, subprocess, sys, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else '.'
ROOT = subprocess.check_output(['git','rev-parse','--show-toplevel']).decode().strip()
os.chdir(ROOT)

files = subprocess.check_output(['git','ls-files']).decode().splitlines()
mdfiles = [f for f in files if f.endswith('.md')]
existing = set(files)

def slug(h):
    h = re.sub(r'[`*_\[\]]', '', h)
    return h.strip().lower()

headings = {}
for f in mdfiles:
    hs = set()
    for line in open(f, encoding='utf-8'):
        m = re.match(r'#{1,6}\s+(.*?)\s*$', line)
        if m:
            hs.add(slug(re.sub(r'[`*_\[\]]', '', m.group(1))))
    headings[f] = hs

LINK = re.compile(r'\[\[([^\[\]]+)\]\]')
dead = []
for f in mdfiles:
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        for m in LINK.finditer(line):
            inner = m.group(1)
            for sep in ['\\|', '|']:
                j = inner.find(sep)
                if j != -1:
                    inner = inner[:j]; break
            target, _, anchor = inner.partition('#')
            tgt = target if target else f
            if target and tgt not in existing:
                if tgt + '.md' in existing:
                    tgt = tgt + '.md'
                else:
                    dead.append((f, i, m.group(0), 'Datei fehlt'))
                    continue
            if anchor and slug(anchor) not in headings.get(tgt, set()):
                dead.append((f, i, m.group(0), 'Anker fehlt in ' + tgt))

bad_paths = [f for f in files
             if (' ' in f or f != f.lower())
             and not re.fullmatch(r'(AGENTS|CLAUDE|README|SETUP-OFFEN)\.md', os.path.basename(f))
             and not f.startswith('graphify-out/')
             and os.path.basename(f) != 'README.md']

for f, i, l, why in dead:
    print(f'TOT  {f}:{i}  {l}  -> {why}')
for f in bad_paths:
    print(f'PFAD {f}  -> Leerzeichen oder Grossbuchstaben')
print(f'\n{len(mdfiles)} Dateien, {sum(len(LINK.findall(open(f,encoding="utf-8").read())) for f in mdfiles)} Wikilinks, '
      f'{len(dead)} tote Links, {len(bad_paths)} auffaellige Pfade')
sys.exit(1 if dead or bad_paths else 0)
