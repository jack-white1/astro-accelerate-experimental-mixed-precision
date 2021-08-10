data_table = readtable('/home/jack/hdd/dat/period_22.9_width_50.0_snrpeak_1_dm_50_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_binary_nan_bper_2.45_bphase_0.1_bpmass_1.338_bcmass_1.249_02-08-2021-01-17-10.436579_bfloat_peaks.dat');
data_xyz = table2array(data_table);
data_table = [];
data_xyz = [data_xyz(:,1) data_xyz(:,4) data_xyz(:,5)];
dotsize = 50;  %adjust as needed
scatter3(data_xyz(:,1), data_xyz(:,2), data_xyz(:,3), dotsize, data_xyz(:,3), 'filled');
colormap turbo