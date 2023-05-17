import numpy as np
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("train.csv")
df = pd.DataFrame(data)
sale_price = df.SalePrice
gr_liv_area = df.GrLivArea
total_bsmt_sf = df.TotalBsmtSF
range1 = max(sale_price) - min(sale_price)
print("SP Mean is", str(np.mean(sale_price)))
print("SP Median is", str(np.median(sale_price)))
print("SP Standard deviation is", str(np.std(sale_price)))
print("SP Range is", str(range1))
print("SP Mode is", str(statistics.mode(sale_price)))
#plt.hist(sale_price)
#sns.distplot(sale_price)
sp_q1 = np.percentile(sale_price, 25)
sp_q2 = np.percentile(sale_price, 50)
sp_q3 = np.percentile(sale_price, 75)
sp_iqr = sp_q3 - sp_q1
sp_upper_bound = sp_q3 + 1.5 * sp_iqr
sp_lower_bound = sp_q1 - 1.5 * sp_iqr
new_sale_price = sale_price[(sale_price > sp_lower_bound) & (sale_price < sp_upper_bound)]
#plt.hist(np.log(new_sale_price))
#sns.distplot(np.log(new_sale_price))
range2 = max(gr_liv_area) - min(gr_liv_area)
print("GLA Mean is", str(np.mean(gr_liv_area)))
print("GLA Median is", str(np.median(gr_liv_area)))
print("GLA Standard deviation is", str(np.std(gr_liv_area)))
print("GLA Range is", str(range2))
print("GLA Mode is", str(statistics.mode(gr_liv_area)))
#plt.hist(gr_liv_area)
#sns.distplot(gr_liv_area)
gla_q1 = np.percentile(gr_liv_area, 25)
gla_q2 = np.percentile(gr_liv_area, 50)
gla_q3 = np.percentile(gr_liv_area, 75)
gla_iqr = gla_q3 - gla_q1
gla_upper_bound = gla_q3 + 1.5 * gla_iqr
gla_lower_bound = gla_q1 - 1.5 * gla_iqr
new_gr_liv_area = gr_liv_area[(gr_liv_area > gla_lower_bound) & (gr_liv_area < gla_upper_bound)]
#plt.hist(new_gr_liv_area)
#sns.distplot(new_gr_liv_area)
range3 = max(total_bsmt_sf) - min(total_bsmt_sf)
print("TBSF Mean is", str(np.mean(total_bsmt_sf)))
print("TBSF Median is", str(np.median(total_bsmt_sf)))
print("TBSF Standard deviation is", str(np.std(total_bsmt_sf)))
print("TBSF Range is", str(range3))
print("TBSF Mode is", str(statistics.mode(total_bsmt_sf)))
#plt.hist(total_bsmt_sf)
#sns.distplot(total_bsmt_sf)
tbsf_q1 = np.percentile(total_bsmt_sf, 25)
tbsf_q2 = np.percentile(total_bsmt_sf, 50)
tbsf_q3 = np.percentile(total_bsmt_sf, 75)
tbsf_iqr = tbsf_q3 - tbsf_q1
tbsf_upper_bound = tbsf_q3 + 1.5 * tbsf_iqr
tbsf_lower_bound = tbsf_q1 - 1.5 * tbsf_iqr
new_total_bsmt_sf = total_bsmt_sf[(total_bsmt_sf > tbsf_lower_bound) & (total_bsmt_sf < tbsf_upper_bound)]
#plt.hist(new_total_bsmt_sf)
sns.distplot(new_total_bsmt_sf)