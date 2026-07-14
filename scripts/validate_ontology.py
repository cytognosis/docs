#!/usr/bin/env python3
"""Validate ontology.yaml: DAG (no cycles), no orphans, asset classes reach a surface. Exit 0 = pass."""
import sys, re, pathlib

def load(path):
    nodes, overlays, cur = {}, [], None
    for raw in pathlib.Path(path).read_text().splitlines():
        line = raw.strip()
        if line.startswith('- {id:'):
            m = re.match(r"- \{id: ([\w-]+), type: ([\w-]+), parents: \[([^\]]*)\]", line)
            if m:
                nid, ntype, parents = m.group(1), m.group(2), [p.strip() for p in m.group(3).split(',') if p.strip()]
                nodes[nid] = {'type': ntype, 'parents': parents}
        elif line.startswith('- {from:'):
            m = re.match(r"- \{from: ([\w-]+), to: ([\w-]+), type: ([\w-]+)", line)
            if m: overlays.append((m.group(1), m.group(2), m.group(3)))
    return nodes, overlays

def main(path='ontology.yaml'):
    nodes, overlays = load(path)
    errs = []
    # 1. parents exist; non-root has >=1 parent
    for nid, n in nodes.items():
        if n['type'] != 'root' and not n['parents']:
            errs.append(f'orphan: {nid}')
        for p in n['parents']:
            if p not in nodes: errs.append(f'{nid}: unknown parent {p}')
    # 2. acyclic over hierarchy + overlays
    edges = {nid: set(n['parents']) for nid, n in nodes.items()}
    for f, t, _ in overlays: edges.setdefault(f, set()).add(t)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {k: WHITE for k in edges} | {k: WHITE for k in nodes}
    def dfs(u, stack):
        color[u] = GRAY
        for v in edges.get(u, ()):  # parent direction
            if color.get(v, WHITE) == GRAY: errs.append('cycle: ' + ' -> '.join(stack + [u, v]))
            elif color.get(v, WHITE) == WHITE: dfs(v, stack + [u])
        color[u] = BLACK
    for k in list(nodes):
        if color[k] == WHITE: dfs(k, [])
    # 3. every asset-class reaches a surface via ancestry
    def reaches_surface(nid, seen=None):
        seen = seen or set()
        if nid in seen: return False
        seen.add(nid)
        n = nodes[nid]
        if n['type'] == 'surface': return True
        return any(reaches_surface(p, seen) for p in n['parents'] if p in nodes)
    for nid, n in nodes.items():
        if n['type'] == 'asset-class' and not reaches_surface(nid):
            errs.append(f'homeless asset-class: {nid}')
    if errs:
        print('FAIL'); [print(' -', e) for e in errs]; return 1
    counts = {}
    for n in nodes.values(): counts[n['type']] = counts.get(n['type'], 0) + 1
    print(f"PASS: {len(nodes)} nodes ({counts}), {len(overlays)} overlay edges, acyclic, no orphans, all asset classes homed")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'ontology.yaml'))
