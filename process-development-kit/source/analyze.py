import csv, numpy as np, itertools, statistics as st, json
D=list(csv.DictReader(open('out/doe_results.csv')))
def X(rows):
    A=np.array([(float(r['power_W'])-525)/75 for r in rows]);B=np.array([(float(r['pressure_Torr'])-4)/.5 for r in rows])
    C=np.array([(float(r['sih4_sccm'])-220)/40 for r in rows]);Dd=np.array([(float(r['spacing_mil'])-400)/50 for r in rows])
    f={'A':A,'B':B,'C':C,'D':Dd}
    cols=['1','A','B','C','D']+[a+b for a,b in itertools.combinations('ABCD',2)]
    M=np.column_stack([np.ones(len(rows))]+[f[c] if len(c)==1 else f[c[0]]*f[c[1]] for c in cols[1:]])
    return cols,M
for resp in ['dep_rate_A_per_min','nu_pct_1sigma','stress_MPa','ri_633nm','hf_wer_A_per_min']:
  for lab,rows in [('all',D),('drop',[r for r in D if not r['notes']])]:
    cols,M=X(rows); y=np.array([float(r[resp]) for r in rows])
    b,res,_,_=np.linalg.lstsq(M,y,rcond=None)
    yh=M@b; dof=len(y)-len(b); s2=((y-yh)**2).sum()/dof
    se=np.sqrt(np.diag(s2*np.linalg.inv(M.T@M))); t=b/se
    r2=1-((y-yh)**2).sum()/((y-y.mean())**2).sum()
    sig=[(c,round(2*v,3),round(tt,1)) for c,v,tt in zip(cols,b,t) if c!='1' and abs(tt)>2.2]
    print(resp,lab,'n',len(y),'R2',round(r2,3),'s',round(np.sqrt(s2),3),sig)

def fit(rows,resp):
    cols,M=X(rows); y=np.array([float(r[resp]) for r in rows]); b=np.linalg.lstsq(M,y,rcond=None)[0]; return cols,b
def pred(cols,b,p,pr,c,d):
    f={'A':(p-525)/75,'B':(pr-4)/.5,'C':(c-220)/40,'D':(d-400)/50}
    v=b[0]
    for cc,bb in zip(cols[1:],b[1:]): v+=bb*(f[cc] if len(cc)==1 else f[cc[0]]*f[cc[1]])
    return v
R=['dep_rate_A_per_min','nu_pct_1sigma','stress_MPa','ri_633nm','hf_wer_A_per_min']
B=list(csv.DictReader(open('out/spc_baseline.csv')))
porwer=st.mean(float(r['hf_wer_A_per_min']) for r in B if r['chamber']=='A')
print('POR WER A',porwer)
for lab,rows,usewer in [('clean',[r for r in D if not r['notes']],True),('with outlier',D,True),('no wer spec',[r for r in D if not r['notes']],False)]:
    fits={r:fit(rows,r) for r in R}; best=None
    for p in range(450,601,10):
      for b_ in np.arange(3.5,4.51,0.1):
        for c in range(180,261,5):
          for d in range(350,451,10):
            v=[pred(*fits[r],p,b_,c,d) for r in R]
            if v[0]<3700: continue
            m=[(2.0-v[1])/0.5,min(v[2]+250,-50-v[2])/50,min(v[3]-1.98,2.02-v[3])/0.01]
            if usewer: m.append(min(v[4]-porwer*.9,porwer*1.1-v[4])/1.0)
            sc=min(m) if usewer else v[0]/1000+ (0 if min(m)>=0 else -9)
            if best is None or sc>best[0]: best=(sc,p,round(b_,1),c,d,[round(x,3) for x in v])
    print(lab,best)
def cpk(x,lsl=None,usl=None):
    m=st.mean(x);s=st.stdev(x);c=[]
    if lsl is not None:c.append((m-lsl)/(3*s))
    if usl is not None:c.append((usl-m)/(3*s))
    return round(m,3),round(s,3),round(min(c),2)
for name,rows in [('baseline',B),('confirm',list(csv.DictReader(open('out/confirm_runs.csv'))))]:
  for ch in ['A','B','all']:
    rr=[r for r in rows if ch=='all' or r['chamber']==ch]
    print(name,ch,len(rr),'NU',cpk([float(r['nu_pct_1sigma']) for r in rr],usl=2.0),'stress',cpk([float(r['stress_MPa']) for r in rr],-250,-50),
      'RI',cpk([float(r['ri_633nm']) for r in rr],1.98,2.02),'rate',round(st.mean(float(r['dep_rate_A_per_min']) for r in rr)),'wer',round(st.mean(float(r['hf_wer_A_per_min']) for r in rr),2))
