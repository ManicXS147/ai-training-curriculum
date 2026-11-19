"""Generator for the AI for Process Development project kit. Seeded; rerun to rebuild."""
import csv, random, datetime as dt, os, sys, itertools, json
random.seed(11)
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BANNER = "SYNTHETIC TRAINING DATA. Made up for the AI for Process Development course. Not from any real tool, lot, product or person."

# ---- true process model (coded units) ----
def code(p,b,c,d): return ((p-525)/75,(b-4.0)/0.5,(c-220)/40,(d-400)/50)
def rate(A,B,C,D): return 3330+260*A+40*B+280*C-120*D+30*A*C
def nu(A,B,C,D):   return 1.30+0.30*A+0.02*B+0.12*C-0.14*D+0.38*A*B
def stress(A,B,C,D): return -150-55*A+50*B+50*C-10*D
def ri(A,B,C,D): return 2.000+0.004*A-0.002*B+0.016*C
def wer(A,B,C,D): return 20.0-0.4*A+0.4*B-1.2*C+0.2*D
NOISE = dict(rate=22, nu=0.045, stress=7, ri=0.0018, wer=0.22)
def measure(x, nu_off=0.0, nu_sd=None, rate_off=0.0):
    return dict(dep_rate_A_per_min=round(rate(*x)+rate_off+random.gauss(0,NOISE['rate'])),
                nu_pct_1sigma=round(nu(*x)+nu_off+random.gauss(0,nu_sd or NOISE['nu']),2),
                stress_MPa=round(stress(*x)+random.gauss(0,NOISE['stress'])),
                ri_633nm=round(ri(*x)+random.gauss(0,NOISE['ri']),3),
                hf_wer_A_per_min=round(wer(*x)+random.gauss(0,NOISE['wer']),1))

def write_csv(name, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

POR = (500, 4.0, 200, 400)
CH_B = dict(nu_off=0.08, nu_sd=0.095, rate_off=-15)   # chamber B: heater replaced 2025

# ---- spc_baseline.csv: 60 days of POR monitor wafers, both chambers ----
rows=[]; d0=dt.date(2026,8,31)
for day in range(60):
    for ch in "AB":
        kw = CH_B if ch=="B" else {}
        m = measure(code(*POR), **kw)
        thk = round(m['dep_rate_A_per_min']*1.0)  # 60 s step
        rows.append(dict(date=(d0+dt.timedelta(days=day)).isoformat(), tool="PECVD-03", chamber=ch,
            wafer_id=f"MON-{ch}{day+1:03d}", recipe="CAPNIT-POR", thickness_A=thk, **m))
write_csv("spc_baseline.csv", rows)

# ---- doe_results.csv: 2^4 full factorial + 4 centers, chamber A ----
lv = dict(p=(450,600), b=(3.5,4.5), c=(180,260), d=(350,450))
runs=[]
for i,(dd,cc,bb,pp) in enumerate(itertools.product((0,1),repeat=4)):
    runs.append(dict(std_order=i+1, power_W=lv['p'][pp], pressure_Torr=lv['b'][bb], sih4_sccm=lv['c'][cc], spacing_mil=lv['d'][dd]))
for k in range(4): runs.append(dict(std_order=17+k, power_W=525, pressure_Torr=4.0, sih4_sccm=220, spacing_mil=400))
order=list(range(20)); random.shuffle(order)
# make sure a centre point is first and last-ish
out=[]; t=dt.datetime(2026,11,4,7,30)
BAD_STD = None
for ro,idx in enumerate(order):
    r=dict(runs[idx]); x=code(r['power_W'],r['pressure_Torr'],r['sih4_sccm'],r['spacing_mil'])
    m=measure(x); note=""
    if r['power_W']==600 and r['pressure_Torr']==3.5 and r['sih4_sccm']==260 and r['spacing_mil']==350:
        m['nu_pct_1sigma']=3.62; note="Metrology: 49-point map stopped at 31 points (wafer misaligned on stage). Not remeasured."; BAD_STD=r['std_order']
    out.append(dict(run_order=ro+1, std_order=r['std_order'], wafer_id=f"DOE-{ro+1:02d}", tool="PECVD-03", chamber="A",
        run_time=(t+dt.timedelta(minutes=50*ro)).strftime("%Y-%m-%d %H:%M"), **{k:r[k] for k in ('power_W','pressure_Torr','sih4_sccm','spacing_mil')}, **m, notes=note))
    if ro==9: t+=dt.timedelta(hours=14)
write_csv("doe_results.csv", out)

# ---- recommended recipe & confirmation runs ----
REC=(600,3.8,230,350)
xr=code(*REC)
pred={k:f(*xr) for k,f in dict(rate=rate,nu=nu,stress=stress,ri=ri,wer=wer).items()}
rows=[]; t=dt.datetime(2026,11,10,8,0)
for ch in "AB":
    for i in range(15):
        kw = dict(nu_off=0.08, nu_sd=0.095, rate_off=-15) if ch=="B" else dict(nu_sd=0.045)
        m=measure(xr,**kw)
        rows.append(dict(wafer_id=f"CNF-{ch}{i+1:02d}", tool="PECVD-03", chamber=ch, run_time=(t+dt.timedelta(minutes=40*i)).strftime("%Y-%m-%d %H:%M"),
            recipe="CAPNIT-F1", **m))
    t+=dt.timedelta(days=1)
write_csv("confirm_runs.csv", rows)

# ---- tool_limits.csv ----
write_csv("tool_limits.csv",[
 dict(parameter="RF power", unit="W", min=300, max=600, POR=500, note="Hardware limit 600 W on this chamber type"),
 dict(parameter="Chamber pressure", unit="Torr", min=3.5, max=5.0, POR=4.0, note="Below 3.5 Torr the plasma is unstable (TR-2021-014)"),
 dict(parameter="SiH4 flow", unit="sccm", min=100, max=300, POR=200, note=""),
 dict(parameter="NH3 flow", unit="sccm", min=2000, max=2000, POR=2000, note="Fixed for this project. Not in scope."),
 dict(parameter="Electrode spacing", unit="mil", min=300, max=500, POR=400, note=""),
 dict(parameter="Heater temperature", unit="C", min=400, max=400, POR=400, note="Fixed. Changing it needs a new chamber qual."),
 dict(parameter="Deposition time", unit="s", min=20, max=120, POR=60, note="Set to hit 3000 A target thickness"),
])
json.dump(dict(bad_std=BAD_STD, rec=REC, pred=pred), open(os.path.join(OUT,"_meta.json"),"w"))
print("bad std", BAD_STD, "pred", pred)
