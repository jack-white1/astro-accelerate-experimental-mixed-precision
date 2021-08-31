data_table = readtable('/home/jack/hdd/dat/period_1.25_width_50_snrpeak_4_dm_500_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_binary_nan_bper_336_bphase_0.2_bpmass_1.5_bcmass_5.0_12-08-2021-23-53-54.248506_bfloat_peaks.dat');
data_xyz = table2array(data_table);
data_table = [];
data_xyz = [data_xyz(:,1) data_xyz(:,4) data_xyz(:,5)];
dotsize = 50;  %adjust as needed
scatter3(data_xyz(:,1), data_xyz(:,2), data_xyz(:,3), dotsize, data_xyz(:,3), 'filled');
colormap turbo