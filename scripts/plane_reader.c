#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <errno.h>

extern int errno ;

struct experiment {
	char bfloat_noise_plane_path[400];
	char single_noise_plane_path[400];
	float period;
};


int main(){

	FILE *experimentCountFilePointer = fopen("noiseplanes.txt","r");
	int lines = 0;
	int ch = 0;
	while(!feof(experimentCountFilePointer)){
		ch = fgetc(experimentCountFilePointer);
		if(ch == '\n'){
			lines++;
		}
	}

	int NUMEXPERIMENTS = lines/3;
	struct experiment experimentList[NUMEXPERIMENTS];

	FILE *directoryFilePointer = fopen("noiseplanes.txt","r");
	int bufferLength = 1000;
	char buffer[bufferLength];
	int lineCounter = 0;
	int len = 0;
	while(fgets(buffer, bufferLength, directoryFilePointer)) {
		if (lineCounter % 3 == 0) {
			len=strlen(buffer);
			buffer[len-1]='\0';
			strcpy(experimentList[lineCounter/3].bfloat_noise_plane_path, buffer);
		} else if (lineCounter % 3 == 1) {
			len=strlen(buffer);
			buffer[len-1]='\0';
			strcpy(experimentList[lineCounter/3].single_noise_plane_path, buffer);
		} else if (lineCounter % 3 == 2) {
			experimentList[lineCounter/3].period = atof(buffer);
		}
		lineCounter += 1;
	}

	printf("Finished building experiment struct\n");

	double temp_acc, temp_acc1, temp_jfreq;
	long long int temp_j;
	float temp_pow, temp_sigma;
	FILE *bfloatFilePointer, *singleFilePointer;

	for (int experimentCounter = 0; experimentCounter < NUMEXPERIMENTS; experimentCounter++){

		double upper_freq_bound_0 = (1000/experimentList[experimentCounter].period)*1.5;
		double upper_freq_bound_1 = (1000/experimentList[experimentCounter].period)*2.5;
		double upper_freq_bound_2 = (1000/experimentList[experimentCounter].period)*3.5;
		
		int errnum;


		printf("experimentCounter: %d, upper_freq_bound_0: %lf, upper_freq_bound_1: %lf, upper_freq_bound_2: %lf\n", experimentCounter, upper_freq_bound_0, upper_freq_bound_1, upper_freq_bound_2);

		double bfloat_peak_acc_0, bfloat_peak_acc_1, bfloat_peak_acc_2;
		double single_peak_acc_0, single_peak_acc_1, single_peak_acc_2;
		bfloat_peak_acc_0 = bfloat_peak_acc_1 = bfloat_peak_acc_2 = 0;
		single_peak_acc_0 = single_peak_acc_1 = single_peak_acc_2 = 0;

		double bfloat_peak_freq_0, bfloat_peak_freq_1, bfloat_peak_freq_2;
		double single_peak_freq_0, single_peak_freq_1, single_peak_freq_2;
		bfloat_peak_freq_0 = bfloat_peak_freq_1 = bfloat_peak_freq_2 = 0;
		single_peak_freq_0 = single_peak_freq_1 = single_peak_freq_2 = 0;

		float bfloat_peak_pow_0, bfloat_peak_pow_1, bfloat_peak_pow_2;
		float single_peak_pow_0, single_peak_pow_1, single_peak_pow_2;
		bfloat_peak_pow_0 = bfloat_peak_pow_1 = bfloat_peak_pow_2 = 0;
		single_peak_pow_0 = single_peak_pow_1 = single_peak_pow_2 = 0;

		float lowest_peak = 0;




		bfloatFilePointer = fopen(experimentList[experimentCounter].bfloat_noise_plane_path, "r");
		singleFilePointer = fopen(experimentList[experimentCounter].single_noise_plane_path, "r");

		if (bfloatFilePointer == NULL) {
			printf("bfloat fopen failed, errno = %d\n", errno);
		} else {
			;//printf("bfloat fopen succeeded\n");
		}
		if (singleFilePointer == NULL) {
			printf("single fopen failed, errno = %d\n", errno);
		} else {
			;//printf("single fopen succeeded\n");
		}

		fseek(bfloatFilePointer, 0, SEEK_SET);
		fseek(singleFilePointer, 0, SEEK_SET);

		clock_t begin_bfloat = clock();
		while( fscanf(bfloatFilePointer,"%lf %lf %lld %lf %f %f", &temp_acc, &temp_acc1, &temp_j , &temp_jfreq, &temp_pow, &temp_sigma) == 6)
		{
			if (temp_pow > lowest_peak){
				if (temp_jfreq < upper_freq_bound_0){
					if (temp_pow > bfloat_peak_pow_0){
						bfloat_peak_pow_0 = temp_pow;
						bfloat_peak_acc_0 = temp_acc;
						bfloat_peak_freq_0 = temp_jfreq;
					}
				} else if ((temp_jfreq > upper_freq_bound_0) && (temp_jfreq < upper_freq_bound_1)){
					if (temp_pow > bfloat_peak_pow_1){
						bfloat_peak_pow_1 = temp_pow;
						bfloat_peak_acc_1 = temp_acc;
						bfloat_peak_freq_1 = temp_jfreq;
					}
				} else if ((temp_jfreq > upper_freq_bound_1) && (temp_jfreq < upper_freq_bound_2)){
					if (temp_pow > bfloat_peak_pow_2){
						bfloat_peak_pow_2 = temp_pow;
						bfloat_peak_acc_2 = temp_acc;
						bfloat_peak_freq_2 = temp_jfreq;
					}
				}
				lowest_peak = bfloat_peak_pow_0;
				if (bfloat_peak_pow_1 < lowest_peak){
					lowest_peak = bfloat_peak_pow_1;
				}
				if (bfloat_peak_pow_2 < lowest_peak){
					lowest_peak = bfloat_peak_pow_2;
				}
			}
		}
		clock_t end_bfloat = clock();

		double time_spent_bfloat = (double)(end_bfloat - begin_bfloat) / CLOCKS_PER_SEC;
		printf("Time spent reading + processing bfloat plane: %lf\n", time_spent_bfloat);

		clock_t begin_single = clock();
		while( fscanf(singleFilePointer,"%lf %lf %lld %lf %f %f", &temp_acc, &temp_acc1, &temp_j , &temp_jfreq, &temp_pow, &temp_sigma) == 6)
		{
			if (temp_pow > lowest_peak){
				if (temp_jfreq < upper_freq_bound_0){
					if (temp_pow > single_peak_pow_0){
						single_peak_pow_0 = temp_pow;
						single_peak_acc_0 = temp_acc;
						single_peak_freq_0 = temp_jfreq;
					}
				} else if ((temp_jfreq > upper_freq_bound_0) && (temp_jfreq < upper_freq_bound_1)){
					if (temp_pow > single_peak_pow_1){
						single_peak_pow_1 = temp_pow;
						single_peak_acc_1 = temp_acc;
						single_peak_freq_1 = temp_jfreq;
					}
				} else if ((temp_jfreq > upper_freq_bound_1) && (temp_jfreq < upper_freq_bound_2)){
					if (temp_pow > single_peak_pow_2){
						single_peak_pow_2 = temp_pow;
						single_peak_acc_2 = temp_acc;
						single_peak_freq_2 = temp_jfreq;
					}
				}
				lowest_peak = single_peak_pow_0;
				if (single_peak_pow_1 < lowest_peak){
					lowest_peak = single_peak_pow_1;
				}
				if (single_peak_pow_2 < lowest_peak){
					lowest_peak = single_peak_pow_2;
				}
			}
		}
		clock_t end_single = clock();

		double time_spent_single = (double)(end_single - begin_single) / CLOCKS_PER_SEC;
		printf("Time spent reading + processing single plane: %lf\n", time_spent_single);



		printf("bfloat_peak_pow_0: %f, bfloat_peak_acc_0: %lf, bfloat_peak_freq_0: %lf\n", bfloat_peak_pow_0, bfloat_peak_acc_0, bfloat_peak_freq_0);

		//printf("single_pow: %f, single_acc: %lf, single_freq: %lf\n\n", single_peak_pow, single_peak_acc, single_peak_freq);

		fclose(bfloatFilePointer);
		fclose(singleFilePointer);

		FILE *fptr;
		fptr = fopen("results.dat", "a");

		fprintf(fptr, "%f, %lf, %lf, %f, %lf, %lf, %f, %lf, %lf, %s, %f, %lf, %lf, %f, %lf, %lf, %f, %lf, %lf, %s\n", bfloat_peak_pow_0, bfloat_peak_acc_0, bfloat_peak_freq_0,bfloat_peak_pow_1, bfloat_peak_acc_1, bfloat_peak_freq_1,bfloat_peak_pow_2, bfloat_peak_acc_2, bfloat_peak_freq_2, experimentList[experimentCounter].bfloat_noise_plane_path, single_peak_pow_0, single_peak_acc_0, single_peak_freq_0,single_peak_pow_1, single_peak_acc_1, single_peak_freq_1,single_peak_pow_2, single_peak_acc_2, single_peak_freq_2,experimentList[experimentCounter].single_noise_plane_path);

		fclose(fptr);
	}
}