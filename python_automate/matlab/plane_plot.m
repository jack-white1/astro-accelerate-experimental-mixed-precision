data_table = readtable('/home/jack/hdd/dat/period_22.9_width_50.0_snrpeak_5_dm_50_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_09-08-2021-23-34-29.998354_double_plane.dat');
data_xyz = table2array(data_table);
data_table = [];
data_xyz = [data_xyz(:,1) data_xyz(:,4) data_xyz(:,5)];
data_xyz = single(data_xyz);
cropped_data_xyz = [];
for i = 0:1:192
    cropped_data_xyz = [cropped_data_xyz; data_xyz(1+i*2097151:1+i*2097151 + 200000,:)];
    disp(i);
end
data_xyz = [];
cropped_data_xyz = single(cropped_data_xyz);

dotsize = 50;  %adjust as needed
scatter3(cropped_data_xyz(:,1), cropped_data_xyz(:,2), cropped_data_xyz(:,3), dotsize, cropped_data_xyz(:,3), 'filled');
colormap turbo