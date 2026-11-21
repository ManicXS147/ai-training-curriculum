"""Generate the synthetic tool-down case kit for AI for Troubleshooting.

Seeded, so the numbers on the slides and in INSTRUCTOR-KEY.txt stay stable.
Run:  python3 gen_kit.py <kit folder> [chart-data.json]
Writes alarm_history.csv, fdc_summary.csv and fdc_limits.csv into the kit folder
and prints the numbers the deck quotes. The text files (brief, notes, logs,
manual excerpt, lessons, prompts) are written by hand and live in the kit.
Everything is invented: no real tool, vendor, lot, product or person.
"""
import csv, random, sys, json
from datetime import datetime as DT, timedelta as TD

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
CHART = sys.argv[2] if len(sys.argv) > 2 else None
R = random.Random(20261106)
CH = ['ETCH-04 A', 'ETCH-04 B', 'ETCH-05 A', 'ETCH-05 B']
def t(s): return DT.strptime(s, '%Y-%m-%d %H:%M')
def fmt(d): return d.strftime('%Y-%m-%d %H:%M')

# ---------------- the story ----------------
PM_DOWN, PM_UP = t('2026-11-05 20:00'), t('2026-11-06 07:10')        # 04B chuck PM + new He MFC, signed off Fri 07:05
MFC05A_DOWN, MFC05A_UP = t('2026-11-05 09:00'), t('2026-11-05 10:40')  # 05A He MFC swap, no chuck work
PATCH_04A = (t('2026-11-06 05:00'), t('2026-11-06 05:50'))              # tool software patch, loaded on 04A side
DIP = (t('2026-11-07 22:35'), t('2026-11-07 23:20'))                    # facility He header pressure dip
DOWNS = [  # 04B after the PM: (alarm time, code, back up)
    (t('2026-11-07 02:10'), 'HE-101', t('2026-11-07 03:30')),
    (t('2026-11-07 14:20'), 'HE-101', t('2026-11-07 16:00')),
    (t('2026-11-08 00:55'), 'ESC-220', t('2026-11-08 02:30')),
    (t('2026-11-08 09:00'), 'HE-101', t('2026-11-09 00:40')),  # held for engineering most of Sunday
    (t('2026-11-09 05:30'), 'HE-101', None),                   # still down at Monday 07:00
]
END = t('2026-11-09 07:00')
FDC_START = t('2026-10-26 00:00')
PRODUCTS = ['P-110', 'P-220', 'P-330', 'P-440']
RECIPE = {'P-110': 'OX-ETCH-12', 'P-220': 'OX-ETCH-12', 'P-330': 'VIA-ETCH-07', 'P-440': 'VIA-ETCH-07'}
WETCLEAN = {'ETCH-04 A': '2026-10-27 08:00', 'ETCH-05 B': '2026-10-29 08:00', 'ETCH-05 A': '2026-10-31 08:00', 'ETCH-04 B': '2026-10-28 20:00'}

def down_windows(ch):
    w = []
    if ch == 'ETCH-04 B':
        w.append((PM_DOWN, PM_UP))
        for a, _, up in DOWNS: w.append((a, up or END + TD(hours=1)))
    if ch == 'ETCH-05 A': w.append((MFC05A_DOWN, MFC05A_UP))
    if ch == 'ETCH-04 A': w.append(PATCH_04A)
    s = t(WETCLEAN[ch]); w.append((s, s + TD(hours=5)))
    return sorted(w)

def hit(ch, a, b):
    for s, e in down_windows(ch):
        if not (b <= s or a >= e): return e
    return None

# ---------------- FDC: one row per lot run ----------------
runs = []
for ch in CH:
    x = FDC_START + TD(minutes=R.randint(0, 60))
    while x < END:
        dur = TD(minutes=R.randint(70, 95))
        e = hit(ch, x, x + dur)
        if e: x = e + TD(minutes=R.randint(15, 40)); continue
        if x + dur > END: break
        if R.random() < 0.10: x += TD(minutes=R.randint(30, 120)); continue
        runs.append(dict(ch=ch, start=x, end=x + dur, prod=R.choice(PRODUCTS)))
        x = x + dur + TD(minutes=R.randint(8, 25))
runs.sort(key=lambda r: r['start'])

BASE = {'ETCH-04 A': 0.55, 'ETCH-04 B': 0.60, 'ETCH-05 A': 0.52, 'ETCH-05 B': 0.63}
climb_starts = [PM_UP] + [up for _, _, up in DOWNS if up]
climb_ends = [a for a, _, _ in DOWNS]
start_leak = [1.10, 1.20, 1.24, 1.30, 1.36]
lot = 4100
rows = []
def row(ch, s, e, prod, leak, press, supply, temp, refl, result, lmax=None):
    global lot
    lot += 1
    return dict(run_start=fmt(s), run_end=fmt(e), tool=ch[:7], chamber=ch[-1], lot_id='L26-%04d' % lot,
                product=prod, recipe=RECIPE[prod], wafers=25, he_leak_sccm=round(leak, 2),
                he_leak_max_sccm=round(lmax if lmax is not None else leak + abs(R.gauss(0.08, 0.03)), 2),
                he_pressure_torr=round(press, 2), chuck_temp_c=round(temp, 1), he_supply_psi=round(supply, 1),
                rf_reflected_w=round(refl, 1), result=result)
for r in runs:
    ch, s = r['ch'], r['start']
    leak = BASE[ch] + R.gauss(0, 0.035)
    press = 10.0 + R.gauss(0, 0.04)
    supply = 30.0 + R.gauss(0, 0.3)
    if DIP[0] - TD(minutes=90) < s < DIP[1] and r['end'] > DIP[0]: supply = 21.5 + R.gauss(0, 0.4)
    if ch == 'ETCH-04 B' and s >= PM_UP:
        i = max(j for j, c in enumerate(climb_starts) if c <= s)
        f = (s - climb_starts[i]).total_seconds() / (climb_ends[i] - climb_starts[i]).total_seconds()
        leak = start_leak[i] + (3.95 - start_leak[i]) * min(f, 1) ** 1.25 + (R.gauss(0, 0.03) if f > 0.05 else 0)
        if leak > 3.0: press = 10.0 - (leak - 3.0) * 0.35 + R.gauss(0, 0.03)
    rows.append(row(ch, s, r['end'], r['prod'], leak, press, supply, 60.0 + R.gauss(0, 0.15), 6.0 + abs(R.gauss(0, 1.2)), 'COMPLETE'))
# the run in progress when each 04B alarm fired: aborted at the interlock
for a, code, _ in DOWNS:
    st = a - TD(minutes=R.randint(25, 50))
    prev_end = max((r['end'] for r in runs if r['ch'] == 'ETCH-04 B' and r['end'] <= a), default=st)
    st = max(st, prev_end + TD(minutes=2))  # the aborted run starts after the previous 04B run ends
    rows.append(row('ETCH-04 B', st, a, R.choice(PRODUCTS), 3.9 + R.random() * 0.06, 9.35 + R.random() * 0.1,
                    30 + R.gauss(0, .3), 60 + R.gauss(0, .15), 6 + abs(R.gauss(0, 1)), 'ABORTED',
                    lmax=4.03 if code == 'HE-101' else 3.97))
rows.sort(key=lambda x: x['run_start'])
for i, x in enumerate(rows): x['lot_id'] = 'L26-%04d' % (4101 + i)
with open(OUT + '/fdc_summary.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# ---------------- alarm history: three weeks, every code ----------------
AL = []
def al(ts, ch, code, sub, text, sev, cleared, comment):
    AL.append(dict(timestamp=ts, tool=ch[:7], chamber=ch[-1], alarm_code=code, subsystem=sub, alarm_text=text,
                   severity=sev, cleared_at=cleared, operator_comment=comment))
HE101 = 'He backside flow high (interlock 4.0 sccm)'
al('2026-11-07 02:10', 'ETCH-04 B', 'HE-101', 'HE', HE101, 'ALARM', '2026-11-07 03:30', 'reset, rechucked test wafer, ran')
al('2026-11-07 14:20', 'ETCH-04 B', 'HE-101', 'HE', HE101, 'ALARM', '2026-11-07 16:00', 'same as nights. reset')
al('2026-11-08 00:55', 'ETCH-04 B', 'ESC-220', 'ESC', 'ESC clamp fault: backside pressure not reached', 'ALARM', '2026-11-08 02:30', 'clamp fault, prob the He dip earlier. reset')
al('2026-11-08 09:00', 'ETCH-04 B', 'HE-101', 'HE', HE101, 'ALARM', '2026-11-09 00:40', 'held for eng. on-call: reset and run, MFC swap Mon')
al('2026-11-09 05:30', 'ETCH-04 B', 'HE-101', 'HE', HE101, 'ALARM', '', 'down. waiting on day shift eng')
for ch, m, c in zip(CH, [41, 42, 44, 47], [23, 21, 24, 22]):
    al('2026-11-07 22:%02d' % m, ch, 'HE-310', 'HE', 'He supply pressure low (< 25 psi)', 'WARNING', '2026-11-07 23:%02d' % c, 'facilities He event')
for ts, ch, c in [('2026-10-20 11:14', 'ETCH-04 B', 'chipped wafer, removed, no repeat'),
                  ('2026-10-23 03:52', 'ETCH-05 A', 'wafer off center on chuck, robot re-taught'),
                  ('2026-10-28 16:37', 'ETCH-04 A', 'warped wafer from rework lot, removed'),
                  ('2026-10-30 21:05', 'ETCH-05 B', 'wafer chipped at edge, removed'),
                  ('2026-11-01 08:26', 'ETCH-04 B', 'backside particle on wafer, removed, no repeat')]:
    al(ts, ch, 'HE-101', 'HE', HE101, 'ALARM', fmt(t(ts) + TD(minutes=R.randint(20, 50))), c)
for ts, ch, code, txt, c in [('2026-10-21 06:40', 'ETCH-05 A', 'ESC-231', 'ESC dechuck timeout', 'auto retry ok'),
                             ('2026-10-24 19:12', 'ETCH-04 A', 'ESC-205', 'ESC clamp voltage deviation', 'cleared, monitor'),
                             ('2026-10-31 13:03', 'ETCH-05 B', 'ESC-231', 'ESC dechuck timeout', 'auto retry ok'),
                             ('2026-11-03 02:48', 'ETCH-04 B', 'ESC-231', 'ESC dechuck timeout', 'auto retry ok')]:
    al(ts, ch, code, 'ESC', txt, 'WARNING', fmt(t(ts) + TD(minutes=R.randint(1, 6))), c)
ROUT = [('TM-014', 'TRANSFER', 'Wafer not detected at transfer arm', 'WARNING', ['retry ok', 'sensor wiped', 'retry ok, no wafer damage']),
        ('RF-052', 'RF', 'RF reflected power high', 'WARNING', ['cleared on next step', 'auto tune recovered']),
        ('PC-033', 'PRESSURE', 'Throttle valve position out of range', 'WARNING', ['cleared', 'recovered on its own']),
        ('EP-071', 'ENDPOINT', 'Endpoint not detected, timed etch used', 'WARNING', ['lot dispositioned by eng, ok', 'monitor wafer ok']),
        ('CW-008', 'COOLING', 'Chiller flow low', 'ALARM', ['chiller filter changed', 'flow recovered']),
        ('DI-002', 'INTERLOCK', 'Lid interlock open', 'ALARM', ['lid closed after inspection', 'cleared']),
        ('VA-019', 'VACUUM', 'Load lock pump-down slow', 'WARNING', ['cleared', 'cycled ok'])]
start = t('2026-10-19 00:00')
while len(AL) < 46:
    code, sub, txt, sev, cm = R.choice(ROUT)
    ch = R.choice(CH)
    ts = start + TD(minutes=R.randint(0, int((END - start).total_seconds() // 60) - 90))
    if hit(ch, ts, ts + TD(minutes=1)) or (DIP[0] - TD(hours=3) < ts < DIP[1] + TD(hours=3)): continue
    if ch == 'ETCH-04 B' and ts > PM_DOWN: continue  # keep 04B's post-PM history to the case alarms
    al(fmt(ts), ch, code, sub, txt, sev, fmt(ts + TD(minutes=R.randint(2, 40))), R.choice(cm))
AL.sort(key=lambda a: a['timestamp'])
with open(OUT + '/alarm_history.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(AL[0].keys())); w.writeheader(); w.writerows(AL)

# ---------------- FDC limits ----------------
LIM = []
for ch in CH:
    A = ch.endswith('A')
    for p, wl, wh, al_, ah, by in [
        ('he_leak_sccm', '', '2.0' if A else '', '', '4.0', 'chamber qual 2023' if A else 'tool default (interlock only)'),
        ('he_pressure_torr', '9.5', '10.5', '9.0', '11.0', 'chamber qual 2023'),
        ('chuck_temp_c', '58.5', '61.5', '57.0', '63.0', 'chamber qual 2023'),
        ('he_supply_psi', '25', '', '20', '', 'facilities 2022'),
        ('rf_reflected_w', '', '15', '', '30', 'chamber qual 2023'),
        ('chamber_pressure_mtorr', '28', '32', '25', '35', 'chamber qual 2023')]:
        LIM.append(dict(tool=ch[:7], chamber=ch[-1], parameter=p, warning_low=wl, warning_high=wh, alarm_low=al_, alarm_high=ah, source=by))
with open(OUT + '/fdc_limits.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(LIM[0].keys())); w.writeheader(); w.writerows(LIM)

# ---------------- numbers the deck and key quote ----------------
def key(x): return x['tool'] + ' ' + x['chamber']
def n_al(ch, a, b, code='HE-101'): return sum(1 for x in AL if x['alarm_code'] == code and key(x) == ch and a <= x['timestamp'] < b)
def n_run(ch, a, b): return sum(1 for x in rows if key(x) == ch and a <= x['run_start'] < b)
since, e, pm = fmt(MFC05A_UP), fmt(END), fmt(PM_UP)
b = [x for x in rows if key(x) == 'ETCH-04 B']
post = [x for x in b if x['run_start'] >= pm]
pre = [x for x in b if x['run_start'] < fmt(PM_DOWN)]
over2 = [x for x in post if x['he_leak_sccm'] > 2.0]
climbs = []
for i, (s0, e0) in enumerate(zip(climb_starts, climb_ends)):
    rr = [x for x in post if fmt(s0) <= x['run_start'] < fmt(e0)]
    w = next((x['run_start'] for x in rr if x['he_leak_sccm'] > 2.0), None)
    climbs.append(dict(start=fmt(s0), alarm=fmt(e0), hours=round((e0 - s0).total_seconds() / 3600, 1), runs=len(rr), first_over_2=w,
                       warn_hours_early=round((e0 - t(w)).total_seconds() / 3600, 1) if w else None))
stats = dict(
    alarms=len(AL), esc_rows=sum(1 for x in AL if x['subsystem'] == 'ESC'), he101=sum(1 for x in AL if x['alarm_code'] == 'HE-101'),
    fdc_rows=len(rows),
    new_mfc=dict(alarms=n_al('ETCH-04 B', pm, e) + n_al('ETCH-05 A', since, e), runs=n_run('ETCH-04 B', pm, e) + n_run('ETCH-05 A', since, e)),
    old_mfc=dict(alarms=n_al('ETCH-04 A', since, e) + n_al('ETCH-05 B', since, e), runs=n_run('ETCH-04 A', since, e) + n_run('ETCH-05 B', since, e)),
    by_chamber_since_mfc={c: (n_al(c, since, e), n_run(c, since, e)) for c in CH},
    he101_04B_week_before=n_al('ETCH-04 B', '2026-10-30 00:00', fmt(PM_DOWN)),
    pre_pm_04B_mean=round(sum(x['he_leak_sccm'] for x in pre) / len(pre), 2),
    first_run_after_pm=post[0], runs_after_pm=len(post), climbs=climbs,
    runs_over_2=len(over2), products_over_2=sorted(set(x['product'] for x in over2)),
    downtime_h=round(sum(((up or END) - a).total_seconds() for a, _, up in DOWNS) / 3600, 1))
for k in ('new_mfc', 'old_mfc'): stats[k]['per100'] = round(100 * stats[k]['alarms'] / stats[k]['runs'], 1)
print(json.dumps(stats, indent=1, default=str))
if CHART:
    json.dump(dict(stats=stats, b04=[(x['run_start'], x['he_leak_sccm'], x['result']) for x in b],
                   alarms=[(x['timestamp'], key(x), x['alarm_code']) for x in AL],
                   resets=[fmt(up) for _, _, up in DOWNS if up], pm=[fmt(PM_DOWN), pm]), open(CHART, 'w'), default=str)
