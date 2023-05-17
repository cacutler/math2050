import pandas as pd
from scipy import stats
import numpy as np
data = pd.read_excel("FEV.DAT.xls", "FEV")
data1 = pd.read_excel("HORMONE.DAT.xls", "hormone")
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
male = df[df.Sex == 1]
female = df[df.Sex == 0]
smoke = df[df.Smoke == 1]
nonsmoke = df[df.Smoke == 0]
males_5_9 = df[df.Sex == 1][df.Age >= 5][df.Age <= 9]
males_10_14 = df[df.Sex == 1][df.Age >= 10][df.Age <= 14]
males_15_19 = df[df.Sex == 1][df.Age >= 15][df.Age <= 19]
females_5_9 = df[df.Sex == 0][df.Age >= 5][df.Age <= 9]
females_10_14 = df[df.Sex == 0][df.Age >= 10][df.Age <= 14]
females_15_19 = df[df.Sex == 0][df.Age >= 15][df.Age <= 19]
boys_smoke_10_14 = df[df.Sex == 1][df.Smoke == 1][df.Age >= 10][df.Age <= 14]
girls_smoke_10_14 = df[df.Sex == 0][df.Smoke == 1][df.Age >= 10][df.Age <= 14]
boys_smoke_15_19 = df[df.Sex == 1][df.Smoke == 1][df.Age >= 15][df.Age <= 19]
girls_smoke_15_19 = df[df.Sex == 0][df.Smoke == 1][df.Age >= 15][df.Age <= 19]
boys_nonsmoke_10_14 = df[df.Sex == 1][df.Smoke == 0][df.Age >= 10][df.Age <= 14]
girls_nonsmoke_10_14 = df[df.Sex == 0][df.Smoke == 0][df.Age >= 10][df.Age <= 14]
boys_nonsmoke_15_19 = df[df.Sex == 1][df.Smoke == 0][df.Age >= 15][df.Age <= 19]
girls_nonsmoke_15_19 = df[df.Sex == 0][df.Smoke == 0][df.Age >= 15][df.Age <= 19]

print("Male 5-9 fev mean", str(np.mean(males_5_9.FEV)))
print("Male 10-14 fev mean", str(np.mean(males_10_14.FEV)))
print("Male 15-19 fev mean", str(np.mean(males_15_19.FEV)))
print("Female 5-9 fev mean", str(np.mean(females_5_9.FEV)))
print("Female 10-14 fev mean", str(np.mean(females_10_14.FEV)))
print("Female 15-19 fev mean", str(np.mean(females_15_19.FEV)))
print("Smoking boys 10-14 fev mean", str(np.mean(boys_smoke_10_14.FEV)))
print("Smoking girls 10-14 fev mean", str(np.mean(girls_smoke_10_14.FEV)))
print("Smoking boys 15-19 fev mean", str(np.mean(boys_smoke_15_19.FEV)))
print("Smoking girls 15-19 fev mean", str(np.mean(girls_smoke_15_19.FEV)))
print("Nonsmoking boys 10-14 fev mean", str(np.mean(boys_nonsmoke_10_14.FEV)))
print("Nonsmoking girls 10-14 fev mean", str(np.mean(girls_nonsmoke_10_14.FEV)))
print("Nonsmoking boys 15-19 fev mean", str(np.mean(boys_nonsmoke_15_19.FEV)))
print("Nonsmoking girls 15-19 fev mean", str(np.mean(girls_nonsmoke_15_19.FEV)))
print("Ages 5-9 fev with males and females", str(stats.ttest_ind(a = males_5_9.FEV, b = females_5_9.FEV, alternative = "two-sided")))
print("Ages 10-14 fev with males and females", str(stats.ttest_ind(a = males_10_14.FEV, b = females_10_14.FEV, alternative = "two-sided")))
print("Ages 15-19 fev with males and females", str(stats.ttest_ind(a = males_15_19.FEV, b = females_15_19.FEV, alternative = "two-sided")))
print("Ages 10-14 fev with male smokers and nonsmokers", str(stats.ttest_ind(a = boys_smoke_10_14.FEV, b = boys_nonsmoke_10_14.FEV, alternative = "two-sided")))
print("Ages 15-19 fev with male smokers and nonsmokers", str(stats.ttest_ind(a = boys_smoke_15_19.FEV, b = boys_nonsmoke_15_19.FEV, alternative = "two-sided")))
print("Ages 10-14 fev with female smokers and nonsmokers", str(stats.ttest_ind(a = girls_smoke_10_14.FEV, b = girls_nonsmoke_10_14.FEV, alternative = "two-sided")))
print("Ages 15-19 fev with female smokers and nonsmokers", str(stats.ttest_ind(a = girls_smoke_15_19.FEV, b = girls_nonsmoke_15_19.FEV, alternative = "two-sided")))
sal = df1[df1.Hormone == 1]
app = df1[df1.Hormone == 2]
cck = df1[df1.Hormone == 3]
sec = df1[df1.Hormone == 4]
vip = df1[df1.Hormone == 5]
low_dose_app = app[app.Dose <= np.median(app.Dose)]
high_dose_app = app[app.Dose > np.median(app.Dose)]
low_dose_cck = cck[cck.Dose <= np.median(cck.Dose)]
high_dose_cck = cck[cck.Dose > np.median(cck.Dose)]
low_dose_sec = sec[sec.Dose <= np.median(sec.Dose)]
high_dose_sec = sec[sec.Dose > np.median(sec.Dose)]
low_dose_vip = vip[vip.Dose <= np.median(vip.Dose)]
high_dose_vip = vip[vip.Dose > np.median(vip.Dose)]
print("Saline")
print(np.mean(sal.Bilsecpr), np.mean(sal.Bilsecpt), np.mean(sal.Bilphpr), np.mean(sal.Bilphpt), np.mean(sal.Pansecpr), np.mean(sal.Pansecpt), np.mean(sal.Panphpr), np.mean(sal.Panphpt))
print("aPP")
print(np.mean(app.Bilsecpr), np.mean(app.Bilsecpt), np.mean(app.Bilphpr), np.mean(app.Bilphpt), np.mean(app.Pansecpr), np.mean(app.Pansecpt), np.mean(app.Panphpr), np.mean(app.Panphpt))
print("CCK")
print(np.mean(cck.Bilsecpr), np.mean(cck.Bilsecpt), np.mean(cck.Bilphpr), np.mean(cck.Bilphpt), np.mean(cck.Pansecpr), np.mean(cck.Pansecpt), np.mean(cck.Panphpr), np.mean(cck.Panphpt))
print("VIP")
print(np.mean(vip.Bilsecpr), np.mean(vip.Bilsecpt), np.mean(vip.Bilphpr), np.mean(vip.Bilphpt), np.mean(vip.Pansecpr), np.mean(vip.Pansecpt), np.mean(vip.Panphpr), np.mean(vip.Panphpt))
print("Secretin")
print(np.mean(sec.Bilsecpr), np.mean(sec.Bilsecpt), np.mean(sec.Bilphpr), np.mean(sec.Bilphpt), np.mean(sec.Pansecpr), np.mean(sec.Pansecpt), np.mean(sec.Panphpr), np.mean(sec.Panphpt))
print("Biliary Secretion with saline", str(stats.ttest_ind(a = sal.Bilsecpr, b = sal.Bilsecpt, alternative = "two-sided")))
print("Biliary pH with saline", str(stats.ttest_ind(a = sal.Bilphpr, b = sal.Bilphpt, alternative = "two-sided")))
print("Pancreatic Secretion with saline", str(stats.ttest_ind(a = sal.Pansecpr, b = sal.Pansecpt, alternative = "two-sided")))
print("Pancreatic pH with saline", str(stats.ttest_ind(a = sal.Panphpr, b = sal.Panphpt, alternative = "two-sided")))
print("Biliary Secretion with app", str(stats.ttest_ind(a = app.Bilsecpr, b = app.Bilsecpt, alternative = "two-sided")))
print("Biliary pH with app", str(stats.ttest_ind(a = app.Bilphpr, b = app.Bilphpt, alternative = "two-sided")))
print("Pancreatic Secretion with app", str(stats.ttest_ind(a = app.Pansecpr, b = app.Pansecpt, alternative = "two-sided")))
print("Pancreatic pH with app", str(stats.ttest_ind(a = app.Panphpr, b = app.Panphpt, alternative = "two-sided")))
print("Biliary Secretion with cck", str(stats.ttest_ind(a = cck.Bilsecpr, b = cck.Bilsecpt, alternative = "two-sided")))
print("Biliary pH with cck", str(stats.ttest_ind(a = cck.Bilphpr, b = cck.Bilphpt, alternative = "two-sided")))
print("Pancreatic Secretion with cck", str(stats.ttest_ind(a = cck.Pansecpr, b = cck.Pansecpt, alternative = "two-sided")))
print("Pancreatic pH with cck", str(stats.ttest_ind(a = cck.Panphpr, b = cck.Panphpt, alternative = "two-sided")))
print("Biliary Secretion with vip", str(stats.ttest_ind(a = vip.Bilsecpr, b = vip.Bilsecpt, alternative = "two-sided")))
print("Biliary pH with vip", str(stats.ttest_ind(a = vip.Bilphpr, b = vip.Bilphpt, alternative = "two-sided")))
print("Pancreatic Secretion with vip", str(stats.ttest_ind(a = vip.Pansecpr, b = vip.Pansecpt, alternative = "two-sided")))
print("Pancreatic pH with vip", str(stats.ttest_ind(a = vip.Panphpr, b = vip.Panphpt, alternative = "two-sided")))
print("Biliary Secretion with sec", str(stats.ttest_ind(a = sec.Bilsecpr, b = sec.Bilsecpt, alternative = "two-sided")))
print("Biliary pH with sec", str(stats.ttest_ind(a = sec.Bilphpr, b = sec.Bilphpt, alternative = "two-sided")))
print("Pancreatic Secretion with sec", str(stats.ttest_ind(a = sec.Pansecpr, b = sec.Pansecpt, alternative = "two-sided")))
print("Pancreatic pH with sec", str(stats.ttest_ind(a = sec.Panphpr, b = sec.Panphpt, alternative = "two-sided")))
print("Pre-Biliary Secretion with aPP vs. saline", str(stats.ttest_ind(a = app.Bilsecpr, b = sal.Bilsecpr, alternative = "two-sided")))
print("Post-Biliary Secretion with aPP vs. saline", str(stats.ttest_ind(a = app.Bilsecpt, b = sal.Bilsecpt, alternative = "two-sided")))
print("Pre-Pancreatic Secretion with aPP vs. saline", str(stats.ttest_ind(a = app.Pansecpr, b = sal.Pansecpr, alternative = "two-sided")))
print("Post-Pancreatic Secretion with aPP vs. saline", str(stats.ttest_ind(a = app.Pansecpt, b = sal.Pansecpt, alternative = "two-sided")))
print("Pre-Biliary pH with aPP vs. saline", str(stats.ttest_ind(a = app.Bilphpr, b = sal.Bilphpr, alternative = "two-sided")))
print("Post-Biliary pH with aPP vs. saline", str(stats.ttest_ind(a = app.Bilphpt, b = sal.Bilphpt, alternative = "two-sided")))
print("Pre-Pancreatic ph with aPP vs. saline", str(stats.ttest_ind(a = app.Panphpr, b = sal.Panphpr, alternative = "two-sided")))
print("Post-Pancreatic ph with aPP vs. saline", str(stats.ttest_ind(a = app.Panphpt, b = sal.Panphpt, alternative = "two-sided")))
print("Pre-Biliary Secretion with CCK vs. saline", str(stats.ttest_ind(a = cck.Bilsecpr, b = sal.Bilsecpr, alternative = "two-sided")))
print("Post-Biliary Secretion with CCK vs. saline", str(stats.ttest_ind(a = cck.Bilsecpt, b = sal.Bilsecpt, alternative = "two-sided")))
print("Pre-Pancreatic Secretion with CCK vs. saline", str(stats.ttest_ind(a = cck.Pansecpr, b = sal.Pansecpr, alternative = "two-sided")))
print("Post-Pancreatic Secretion with CCK vs. saline", str(stats.ttest_ind(a = cck.Pansecpt, b = sal.Pansecpt, alternative = "two-sided")))
print("Pre-Biliary pH with CCK vs. saline", str(stats.ttest_ind(a = cck.Bilphpr, b = sal.Bilphpr, alternative = "two-sided")))
print("Post-Biliary pH with CCK vs. saline", str(stats.ttest_ind(a = cck.Bilphpt, b = sal.Bilphpt, alternative = "two-sided")))
print("Pre-Pancreatic ph with CCK vs. saline", str(stats.ttest_ind(a = cck.Panphpr, b = sal.Panphpr, alternative = "two-sided")))
print("Post-Pancreatic ph with CCK vs. saline", str(stats.ttest_ind(a = cck.Panphpt, b = sal.Panphpt, alternative = "two-sided")))
print("Pre-Biliary Secretion with VIP vs. saline", str(stats.ttest_ind(a = vip.Bilsecpr, b = sal.Bilsecpr, alternative = "two-sided")))
print("Post-Biliary Secretion with VIP vs. saline", str(stats.ttest_ind(a = vip.Bilsecpt, b = sal.Bilsecpt, alternative = "two-sided")))
print("Pre-Pancreatic Secretion with VIP vs. saline", str(stats.ttest_ind(a = vip.Pansecpr, b = sal.Pansecpr, alternative = "two-sided")))
print("Post-Pancreatic Secretion with VIP vs. saline", str(stats.ttest_ind(a = vip.Pansecpt, b = sal.Pansecpt, alternative = "two-sided")))
print("Pre-Biliary pH with VIP vs. saline", str(stats.ttest_ind(a = vip.Bilphpr, b = sal.Bilphpr, alternative = "two-sided")))
print("Post-Biliary pH with VIP vs. saline", str(stats.ttest_ind(a = vip.Bilphpt, b = sal.Bilphpt, alternative = "two-sided")))
print("Pre-Pancreatic ph with VIP vs. saline", str(stats.ttest_ind(a = vip.Panphpr, b = sal.Panphpr, alternative = "two-sided")))
print("Post-Pancreatic ph with VIP vs. saline", str(stats.ttest_ind(a = vip.Panphpt, b = sal.Panphpt, alternative = "two-sided")))
print("Pre-Biliary Secretion with secretin vs. saline", str(stats.ttest_ind(a = sec.Bilsecpr, b = sal.Bilsecpr, alternative = "two-sided")))
print("Post-Biliary Secretion with secretin vs. saline", str(stats.ttest_ind(a = sec.Bilsecpt, b = sal.Bilsecpt, alternative = "two-sided")))
print("Pre-Pancreatic Secretion with secretin vs. saline", str(stats.ttest_ind(a = sec.Pansecpr, b = sal.Pansecpr, alternative = "two-sided")))
print("Post-Pancreatic Secretion with secretin vs. saline", str(stats.ttest_ind(a = sec.Pansecpt, b = sal.Pansecpt, alternative = "two-sided")))
print("Pre-Biliary pH with secretin vs. saline", str(stats.ttest_ind(a = sec.Bilphpr, b = sal.Bilphpr, alternative = "two-sided")))
print("Post-Biliary pH with secretin vs. saline", str(stats.ttest_ind(a = sec.Bilphpt, b = sal.Bilphpt, alternative = "two-sided")))
print("Pre-Pancreatic ph with secretin vs. saline", str(stats.ttest_ind(a = sec.Panphpr, b = sal.Panphpr, alternative = "two-sided")))
print("Post-Pancreatic ph with secretin vs. saline", str(stats.ttest_ind(a = sec.Panphpt, b = sal.Panphpt, alternative = "two-sided")))
print("Pre-Biliary secretion of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Bilsecpr, b = low_dose_app.Bilsecpr, alternative = "greater")))
print("Post-Biliary secretion of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Bilsecpt, b = low_dose_app.Bilsecpt, alternative = "greater")))
print("Pre-Pancreatic secretion of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Pansecpr, b = low_dose_app.Pansecpr, alternative = "greater")))
print("Post-Pancreatic secretion of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Pansecpt, b = low_dose_app.Pansecpt, alternative = "greater")))
print("Pre-Biliary ph of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Bilphpr, b = low_dose_app.Bilphpr, alternative = "greater")))
print("Post-Biliary ph of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Bilphpt, b = low_dose_app.Bilphpt, alternative = "greater")))
print("Pre-Pancreatic ph of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Panphpr, b = low_dose_app.Panphpr, alternative = "greater")))
print("Post-Pancreatic ph of app high dose vs. low dose", str(stats.ttest_ind(a = high_dose_app.Panphpt, b = low_dose_app.Panphpt, alternative = "greater")))
print("Pre-Biliary secretion of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Bilsecpr, b = low_dose_cck.Bilsecpr, alternative = "greater")))
print("Post-Biliary secretion of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Bilsecpt, b = low_dose_cck.Bilsecpt, alternative = "greater")))
print("Pre-Pancreatic secretion of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Pansecpr, b = low_dose_cck.Pansecpr, alternative = "greater")))
print("Post-Pancreatic secretion of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Pansecpt, b = low_dose_cck.Pansecpt, alternative = "greater")))
print("Pre-Biliary ph of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Bilphpr, b = low_dose_cck.Bilphpr, alternative = "greater")))
print("Post-Biliary ph of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Bilphpt, b = low_dose_cck.Bilphpt, alternative = "greater")))
print("Pre-Pancreatic ph of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Panphpr, b = low_dose_cck.Panphpr, alternative = "greater")))
print("Post-Pancreatic ph of cck high dose vs. low dose", str(stats.ttest_ind(a = high_dose_cck.Panphpt, b = low_dose_cck.Panphpt, alternative = "greater")))
print("Pre-Biliary secretion of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Bilsecpr, b = low_dose_vip.Bilsecpr, alternative = "greater")))
print("Post-Biliary secretion of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Bilsecpt, b = low_dose_vip.Bilsecpt, alternative = "greater")))
print("Pre-Pancreatic secretion of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Pansecpr, b = low_dose_vip.Pansecpr, alternative = "greater")))
print("Post-Pancreatic secretion of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Pansecpt, b = low_dose_vip.Pansecpt, alternative = "greater")))
print("Pre-Biliary ph of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Bilphpr, b = low_dose_vip.Bilphpr, alternative = "greater")))
print("Post-Biliary ph of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Bilphpt, b = low_dose_vip.Bilphpt, alternative = "greater")))
print("Pre-Pancreatic ph of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Panphpr, b = low_dose_vip.Panphpr, alternative = "greater")))
print("Post-Pancreatic ph of vip high dose vs. low dose", str(stats.ttest_ind(a = high_dose_vip.Panphpt, b = low_dose_vip.Panphpt, alternative = "greater")))
print("Pre-Biliary secretion of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Bilsecpr, b = low_dose_sec.Bilsecpr, alternative = "greater")))
print("Post-Biliary secretion of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Bilsecpt, b = low_dose_sec.Bilsecpt, alternative = "greater")))
print("Pre-Pancreatic secretion of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Pansecpr, b = low_dose_sec.Pansecpr, alternative = "greater")))
print("Post-Pancreatic secretion of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Pansecpt, b = low_dose_sec.Pansecpt, alternative = "greater")))
print("Pre-Biliary ph of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Bilphpr, b = low_dose_sec.Bilphpr, alternative = "greater")))
print("Post-Biliary ph of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Bilphpt, b = low_dose_sec.Bilphpt, alternative = "greater")))
print("Pre-Pancreatic ph of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Panphpr, b = low_dose_sec.Panphpr, alternative = "greater")))
print("Post-Pancreatic ph of secretin high dose vs. low dose", str(stats.ttest_ind(a = high_dose_sec.Panphpt, b = low_dose_sec.Panphpt, alternative = "greater")))