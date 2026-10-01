import argparse,hashlib,json
from pathlib import Path
import numpy as np,pandas as pd

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--csv',required=True);ap.add_argument('--splits',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 d=pd.read_csv(a.csv,parse_dates=['Timestamp']); s=pd.read_csv(a.splits,usecols=['spatial_split','temporal_split']); d=d.join(s)
 cal=d[d.spatial_split=='calibration'].copy(); X=lambda z:np.c_[np.ones(len(z)),z.PA_Tem.to_numpy(),z.PA_Tem.to_numpy()**2]
 b=np.linalg.lstsq(X(cal),cal.HOBO_Tem,rcond=None)[0]; cal['resid']=cal.HOBO_Tem-X(cal)@b; cal['abs_resid']=abs(cal.resid); qcluster=float(np.quantile(cal.groupby('Location ID').abs_resid.quantile(.95).to_numpy(),.95,method='higher'))
 cal=cal.sort_values('Timestamp'); roll=cal.set_index('Timestamp')['abs_resid'].rolling('30D',closed='left').quantile(.975).rename('q').reset_index().drop_duplicates('Timestamp')
 joint=d[(d.spatial_split=='holdout')&(d.temporal_split=='temporal_holdout')].sort_values('Timestamp'); z=pd.merge_asof(joint[['Timestamp','PA_Tem','HOBO_Tem']],roll,on='Timestamp',direction='backward'); z.q=z.q.fillna(float(np.quantile(cal.abs_resid,.975,method='higher'))); pred=X(z)@b; hit=abs(z.HOBO_Tem-pred)<=z.q
 out={'input_hashes':{'csv_sha256':sha(a.csv),'splits_sha256':sha(a.splits)},'model':'M2_quadratic_PA_temperature','model_hash':'canonical_m2_quadratic_v1','conformal':{'cluster_q95_C':qcluster,'rolling_window_days':30,'nominal_target':.975,'joint_observed_coverage':float(hit.mean()),'joint_coverage_count':int(hit.sum()),'joint_rows':len(z),'mean_interval_width_C':float(2*z.q.mean())},'formal_pass':False}
 Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
