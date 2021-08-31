data_table = readtable('/home/jack/hdd/dat/period_6834.71204_width_12.91678_snrpeak_0.09032_dm_251_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_binary_nan_bper_187.46437_bphase_0.2_bpmass_1.15891_bcmass_0.81846_25-08-2021-19-01-09.743319_double_plane.dat');
data_xyz = table2array(data_table);
data_table = [];
data_xyz = [data_xyz(:,1) data_xyz(:,4) data_xyz(:,5)];
data_xyz = single(data_xyz);
cropped_data_xyz = [];
for i = 0:1:192
    cropped_data_xyz = [cropped_data_xyz; data_xyz(1+i*2097151:1+i*2097151 + 20000,:)];
    disp(i);
end
data_xyz = [];
cropped_data_xyz = single(cropped_data_xyz);

dotsize = 50;  %adjust as needed
scatter3(cropped_data_xyz(:,1), cropped_data_xyz(:,2), cropped_data_xyz(:,3), dotsize, cropped_data_xyz(:,3), 'filled');
colormap turbo