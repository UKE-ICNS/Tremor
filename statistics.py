import numpy as np
import os
import pickle
from scipy import stats

os.chdir(r"C:\Users\Mariia Popova\Desktop\PhD\Code\Tremor model\Tremor")

#%% Tremor data

state="Data/trtr2"

with open(f'{state}/trn_psd.pkl', 'rb') as f:
    trn = pickle.load(f)

trn_list = list(trn.items())
trn_pow = np.array(trn_list[0][1])
trn_pow3 = trn_pow[:,2]
trn_pow5 = trn_pow[:,4]
trn_pow8 = trn_pow[:,7]

with open(f'{state}/vla_psd.pkl', 'rb') as f:
    vla = pickle.load(f)

vla_list = list(vla.items())
vla_pow = np.array(vla_list[0][1])
vla_pow3 = vla_pow[:,2]
vla_pow5 = vla_pow[:,4]
vla_pow8 = vla_pow[:,7]

with open(f'{state}/vlp_psd.pkl', 'rb') as f:
    vlp = pickle.load(f)

vlp_list = list(vlp.items())
vlp_pow = np.array(vlp_list[0][1])
vlp_pow3 = vlp_pow[:,2]
vlp_pow5 = vlp_pow[:,4]
vlp_pow8 = vlp_pow[:,7]

with open(f'{state}/cern_psd.pkl', 'rb') as f:
    cern = pickle.load(f)

cern_list = list(cern.items())
cern_pow = np.array(cern_list[0][1])
cern_pow3 = cern_pow[:,2]
cern_pow5 = cern_pow[:,4]
cern_pow8 = cern_pow[:,7]

with open(f'{state}/gpi_psd.pkl', 'rb') as f:
    gpi = pickle.load(f)

gpi_list = list(gpi.items())
gpi_pow = np.array(gpi_list[0][1])
gpi_pow24 = gpi_pow[:,23]

with open(f'{state}/cerc_psd.pkl', 'rb') as f:
    cerc = pickle.load(f)

cerc_list = list(cerc.items())
cerc_pow = np.array(cerc_list[0][1])
cerc_pow3 = cerc_pow[:,2]
cerc_pow5 = cerc_pow[:,4]
cerc_pow8 = cerc_pow[:,7]

#%% PD data

state1="Data\pdpd2"

with open(f'{state1}/trn_psd.pkl', 'rb') as f:
    trn1 = pickle.load(f)

trn_list1 = list(trn1.items())
trn_pow1 = np.array(trn_list1[0][1])
trn_pow3_1 = trn_pow1[:,2]
trn_pow5_1 = trn_pow1[:,4]
trn_pow8_1 = trn_pow1[:,7]

with open(f'{state1}/vla_psd.pkl', 'rb') as f:
    vla1 = pickle.load(f)

vla_list1 = list(vla1.items())
vla_pow1 = np.array(vla_list1[0][1])
vla_pow3_1 = vla_pow1[:,2]
vla_pow5_1 = vla_pow1[:,4]
vla_pow8_1 = vla_pow1[:,7]

with open(f'{state1}/vlp_psd.pkl', 'rb') as f:
    vlp1 = pickle.load(f)

vlp_list1 = list(vlp1.items())
vlp_pow1 = np.array(vlp_list1[0][1])
vlp_pow3_1 = vlp_pow1[:,2]
vlp_pow5_1 = vlp_pow1[:,4]
vlp_pow8_1 = vlp_pow1[:,7]

with open(f'{state1}/cern_psd.pkl', 'rb') as f:
    cern1 = pickle.load(f)

cern_list1 = list(cern1.items())
cern_pow1 = np.array(cern_list1[0][1])
cern_pow3_1 = cern_pow1[:,2]
cern_pow5_1 = cern_pow1[:,4]
cern_pow8_1 = cern_pow1[:,7]

with open(f'{state1}/gpi_psd.pkl', 'rb') as f:
    gpi1 = pickle.load(f)

gpi_list1 = list(gpi1.items())
gpi_pow1 = np.array(gpi_list1[0][1])
gpi_pow24_1 = gpi_pow1[:,23]

with open(f'{state1}/cerc_psd.pkl', 'rb') as f:
    cerc1 = pickle.load(f)

cerc_list1 = list(cerc1.items())
cerc_pow1 = np.array(cerc_list1[0][1])
cerc_pow3_1 = cerc_pow1[:,2]
cerc_pow5_1 = cerc_pow1[:,4]
cerc_pow8_1 = cerc_pow1[:,7]

#%% Healthy data

state2="Data/hh2"

with open(f'{state2}/trn_psd.pkl', 'rb') as f:
    trn2 = pickle.load(f)

trn_list2 = list(trn2.items())
trn_pow2 = np.array(trn_list2[0][1])
trn_pow3_2 = trn_pow2[:,2]
trn_pow5_2 = trn_pow2[:,4]
trn_pow8_2 = trn_pow2[:,7]

with open(f'{state2}/vla_psd.pkl', 'rb') as f:
    vla2 = pickle.load(f)

vla_list2 = list(vla2.items())
vla_pow2 = np.array(vla_list2[0][1])
vla_pow3_2 = vla_pow2[:,2]
vla_pow5_2 = vla_pow2[:,4]
vla_pow8_2 = vla_pow2[:,7]

with open(f'{state2}/vlp_psd.pkl', 'rb') as f:
    vlp2 = pickle.load(f)

vlp_list2 = list(vlp2.items())
vlp_pow2 = np.array(vlp_list2[0][1])
vlp_pow3_2 = vlp_pow2[:,2]
vlp_pow5_2 = vlp_pow2[:,4]
vlp_pow8_2 = vlp_pow2[:,7]

with open(f'{state2}/cern_psd.pkl', 'rb') as f:
    cern2 = pickle.load(f)

cern_list2 = list(cern2.items())
cern_pow2 = np.array(cern_list2[0][1])
cern_pow3_2 = cern_pow2[:,2]
cern_pow5_2 = cern_pow2[:,4]
cern_pow8_2 = cern_pow2[:,7]

with open(f'{state2}/gpi_psd.pkl', 'rb') as f:
    gpi2 = pickle.load(f)

gpi_list2 = list(gpi2.items())
gpi_pow2 = np.array(gpi_list2[0][1])
gpi_pow24_2 = gpi_pow2[:,23]

with open(f'{state2}/cerc_psd.pkl', 'rb') as f:
    cerc2 = pickle.load(f)

cerc_list2 = list(cerc2.items())
cerc_pow2 = np.array(cerc_list2[0][1])
cerc_pow3_2 = cerc_pow2[:,2]
cerc_pow5_2 = cerc_pow2[:,4]
cerc_pow8_2 = cerc_pow2[:,7]

#%% Tremor-off data

state="Data/trofftroff2"

with open(f'{state}/trn_psd.pkl', 'rb') as f:
    trn3 = pickle.load(f)

trn_list3 = list(trn3.items())
trn_pow_3 = np.array(trn_list3[0][1])
trn_pow3_3 = trn_pow_3[:,2]
trn_pow5_3 = trn_pow_3[:,4]
trn_pow8_3 = trn_pow_3[:,7]

with open(f'{state}/vla_psd.pkl', 'rb') as f:
    vla3 = pickle.load(f)

vla_list3 = list(vla3.items())
vla_pow_3 = np.array(vla_list3[0][1])
vla_pow3_3 = vla_pow_3[:,2]
vla_pow5_3 = vla_pow_3[:,4]
vla_pow8_3 = vla_pow_3[:,7]

with open(f'{state}/vlp_psd.pkl', 'rb') as f:
    vlp3 = pickle.load(f)

vlp_list3 = list(vlp3.items())
vlp_pow_3 = np.array(vlp_list3[0][1])
vlp_pow3_3 = vlp_pow_3[:,2]
vlp_pow5_3 = vlp_pow_3[:,4]
vlp_pow8_3 = vlp_pow_3[:,7]

with open(f'{state}/cern_psd.pkl', 'rb') as f:
    cern3 = pickle.load(f)

cern_list3 = list(cern3.items())
cern_pow_3 = np.array(cern_list3[0][1])
cern_pow3_3 = cern_pow_3[:,2]
cern_pow5_3 = cern_pow_3[:,4]
cern_pow8_3 = cern_pow_3[:,7]

with open(f'{state}/gpi_psd.pkl', 'rb') as f:
    gpi3 = pickle.load(f)

gpi_list3 = list(gpi3.items())
gpi_pow_3 = np.array(gpi_list3[0][1])
gpi_pow24_3 = gpi_pow_3[:,23]

with open(f'{state}/cerc_psd.pkl', 'rb') as f:
    cerc3 = pickle.load(f)

cerc_list3 = list(cerc3.items())
cerc_pow_3 = np.array(cerc_list3[0][1])
cerc_pow3_3 = cerc_pow_3[:,2]
cerc_pow5_3 = cerc_pow_3[:,4]
cerc_pow8_3 = cerc_pow_3[:,7]
#%% Statistics

# Healthy and PD
print("Healthy and PD")
t_stat_gpi, p_val_gpi = stats.ttest_ind(gpi_pow24_1, gpi_pow24_2)
print(f'GPi, 24Hz: t-statistic = {t_stat_gpi} pvalue = {p_val_gpi}')

#PD and Tremor
print("PD and tremor")
# #VLA
# t_stat_vla_3, p_val_vla_3 = stats.ttest_ind(vla_pow3, vla_pow3_1)
# print(f'VLA, 3Hz: t-statistic = {t_stat_vla_3} pvalue = {p_val_vla_3}')

# t_stat_vla_5, p_val_vla_5 = stats.ttest_ind(vla_pow5, vla_pow5_1)
# print(f'VLA, 5Hz: t-statistic = {t_stat_vla_5} pvalue = {p_val_vla_5}')

# t_stat_vla_8, p_val_vla_8 = stats.ttest_ind(vla_pow8, vla_pow8_1)
# print(f'VLA, 8Hz: t-statistic = {t_stat_vla_8} pvalue = {p_val_vla_8}')

#VLP
t_stat_vlp_3, p_val_vlp_3 = stats.ttest_ind(vlp_pow3, vlp_pow3_1)
print(f'VLP, 3Hz: t-statistic = {t_stat_vlp_3} pvalue = {p_val_vlp_3}')

t_stat_vlp_5, p_val_vlp_5 = stats.ttest_ind(vlp_pow5, vlp_pow5_1)
print(f'VLP, 5Hz: t-statistic = {t_stat_vlp_5} pvalue = {p_val_vlp_5}')

# t_stat_vlp_8, p_val_vlp_8 = stats.ttest_ind(vlp_pow8, vlp_pow8_1)
# print(f'VLP, 8Hz: t-statistic = {t_stat_vlp_8} pvalue = {p_val_vlp_8}')

#TRN
# t_stat_trn_3, p_val_trn_3 = stats.ttest_ind(trn_pow3, trn_pow3_1)
# print(f'TRN, 3Hz: t-statistic = {t_stat_trn_3} pvalue = {p_val_trn_3}')

# t_stat_trn_5, p_val_trn_5 = stats.ttest_ind(trn_pow5, trn_pow5_1)
# print(f'TRN, 5Hz: t-statistic = {t_stat_trn_5} pvalue = {p_val_trn_5}')

# t_stat_trn_8, p_val_trn_8 = stats.ttest_ind(trn_pow8, trn_pow8_1)
# print(f'TRN, 8Hz: t-statistic = {t_stat_trn_8} pvalue = {p_val_trn_8}')

#Cern
t_stat_cern_3, p_val_cern_3 = stats.ttest_ind(cern_pow3, cern_pow3_1)
print(f'Cern, 3Hz: t-statistic = {t_stat_cern_3} pvalue = {p_val_cern_3}')

# t_stat_cern_5, p_val_cern_5 = stats.ttest_ind(cern_pow5, cern_pow5_1)
# print(f'Cern, 5Hz: t-statistic = {t_stat_cern_5} pvalue = {p_val_cern_5}')

# t_stat_cern_8, p_val_cern_8 = stats.ttest_ind(cern_pow8, cern_pow8_1)
# print(f'Cern, 8Hz: t-statistic = {t_stat_cern_8} pvalue = {p_val_cern_8}')

#Cerc
t_stat_cerc_3, p_val_cerc_3 = stats.ttest_ind(cerc_pow3, cerc_pow3_1)
print(f'Cerc, 3Hz: t-statistic = {t_stat_cerc_3} pvalue = {p_val_cerc_3}')

t_stat_cerc_5, p_val_cerc_5 = stats.ttest_ind(cerc_pow5, cerc_pow5_1)
print(f'Cerc, 5Hz: t-statistic = {t_stat_cerc_5} pvalue = {p_val_cerc_5}')

# t_stat_cerc_8, p_val_cerc_8 = stats.ttest_ind(cerc_pow8, cerc_pow8_1)
# print(f'Cerc, 8Hz: t-statistic = {t_stat_cerc_8} pvalue = {p_val_cerc_8}')

#Tremor and Tremor-off
print("Tremor and tremor-off")
#VLA
# t_stat_vla_31, p_val_vla_31 = stats.ttest_ind(vla_pow3, vla_pow3_3)
# print(f'VLA, 3Hz: t-statistic = {t_stat_vla_31} pvalue = {p_val_vla_31}')

# t_stat_vla_51, p_val_vla_51 = stats.ttest_ind(vla_pow5, vla_pow5_3)
# print(f'VLA, 5Hz: t-statistic = {t_stat_vla_51} pvalue = {p_val_vla_51}')

# t_stat_vla_81, p_val_vla_81 = stats.ttest_ind(vla_pow8, vla_pow8_3)
# print(f'VLA, 8Hz: t-statistic = {t_stat_vla_81} pvalue = {p_val_vla_81}')

#VLP
t_stat_vlp_31, p_val_vlp_31 = stats.ttest_ind(vlp_pow3, vlp_pow3_3)
print(f'VLP, 3Hz: t-statistic = {t_stat_vlp_31} pvalue = {p_val_vlp_31}')

t_stat_vlp_51, p_val_vlp_51 = stats.ttest_ind(vlp_pow5, vlp_pow5_3)
print(f'VLP, 5Hz: t-statistic = {t_stat_vlp_51} pvalue = {p_val_vlp_51}')

# t_stat_vlp_81, p_val_vlp_81 = stats.ttest_ind(vlp_pow8, vlp_pow8_3)
# print(f'VLP, 8Hz: t-statistic = {t_stat_vlp_81} pvalue = {p_val_vlp_81}')

#TRN
# t_stat_trn_31, p_val_trn_31 = stats.ttest_ind(trn_pow3, trn_pow3_3)
# print(f'TRN, 3Hz: t-statistic = {t_stat_trn_31} pvalue = {p_val_trn_31}')

# t_stat_trn_51, p_val_trn_51 = stats.ttest_ind(trn_pow5, trn_pow5_3)
# print(f'TRN, 5Hz: t-statistic = {t_stat_trn_51} pvalue = {p_val_trn_51}')

# t_stat_trn_81, p_val_trn_81 = stats.ttest_ind(trn_pow8, trn_pow8_3)
# print(f'TRN, 8Hz: t-statistic = {t_stat_trn_81} pvalue = {p_val_trn_81}')

#Cern
t_stat_cern_31, p_val_cern_31 = stats.ttest_ind(cern_pow3, cern_pow3_3)
print(f'Cern, 3Hz: t-statistic = {t_stat_cern_31} pvalue = {p_val_cern_31}')

# t_stat_cern_51, p_val_cern_51 = stats.ttest_ind(cern_pow5, cern_pow5_3)
# print(f'Cern, 5Hz: t-statistic = {t_stat_cern_51} pvalue = {p_val_cern_51}')

# t_stat_cern_81, p_val_cern_81 = stats.ttest_ind(cern_pow8, cern_pow8_3)
# print(f'Cern, 8Hz: t-statistic = {t_stat_cern_81} pvalue = {p_val_cern_81}')

#Cerc
t_stat_cerc_31, p_val_cerc_31 = stats.ttest_ind(cerc_pow3, cerc_pow3_3)
print(f'Cerc, 3Hz: t-statistic = {t_stat_cerc_31} pvalue = {p_val_cerc_31}')

t_stat_cerc_51, p_val_cerc_51 = stats.ttest_ind(cerc_pow5, cerc_pow5_3)
print(f'Cerc, 5Hz: t-statistic = {t_stat_cerc_51} pvalue = {p_val_cerc_51}')

# t_stat_cerc_81, p_val_cerc_81 = stats.ttest_ind(cerc_pow8, cerc_pow8_3)
# print(f'Cerc, 8Hz: t-statistic = {t_stat_cerc_81} pvalue = {p_val_cerc_81}')