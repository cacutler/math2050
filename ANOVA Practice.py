import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from bioinfokit.analys import stat
data = pd.read_csv("Diet_R.csv")
df = pd.DataFrame(data)
df["dif"] = df["pre.weight"] - df["weight6weeks"]
model = ols("df.dif ~ C(df.Diet)", data = df).fit()
anova_table = sm.stats.anova_lm(model, typ = 2)
print(anova_table)
res = stat()
res.tukey_hsd(df, res_var = "dif", xfac_var = "Diet", anova_model = "dif ~ C(Diet)")
res.tukey_summary