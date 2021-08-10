#ifndef ASTRO_ACCELERATE_AA_FDAS_DEVICE_HPP
#define ASTRO_ACCELERATE_AA_FDAS_DEVICE_HPP

#include <cufft.h>
#include <stdio.h>
#include <cuda_runtime.h>
#include "aa_fdas_device.hpp"
#include "aa_params.hpp"
#include "cuda_bf16.h"

namespace astroaccelerate {

  /** \brief CUDA kernels. */

  __global__ void cuda_overlap_copy(double2* d_ext_data, double2* d_cpx_signal, int sigblock,  int sig_rfftlen, int sig_tot_convlen, int kern_offset, int total_blocks);

  /** \brief Kernel wrapper function for overlap_copy kernel function. */
  void call_kernel_cuda_overlap_copy(double2 *const d_ext_data, double2 *const d_cpx_signal, const int &sigblock, const int &sig_rfftlen, const int &sig_tot_convlen, const int &kern_offset, const int &total_blocks);
  
  __global__ void cuda_overlap_copy_smallblk(double2* d_ext_data, double2* d_cpx_signal, int sigblock,  int sig_rfftlen, int sig_tot_convlen, int kern_offset, int total_blocks);

  /** \brief Kernel wrapper function for cuda_overlap_copy_smallbl kernel function. */
  void call_kernel_cuda_overlap_copy_smallblk(const int &blocks, double2 *const d_ext_data, double2 *const d_cpx_signal, const int &sigblock, const int &sig_rfftlen, const int &sig_tot_convlen, const int &kern_offset, const int &total_blocks);

  __global__ void cuda_convolve_reg_1d_halftemps(double2* d_kernel, double2* d_signal, double2* d_ffdot_plane, int sig_tot_convlen, float scale);

  /** \brief Kernel wrapper function for cuda_convolve_reg_1d_halftemps kernel function. */
  void call_kernel_cuda_convolve_reg_1d_halftemps(const int &blocks, const int &threads, double2 *const d_kernel, double2 *const d_signal, double2 *const d_ffdot_plane, const int &sig_tot_convlen, const float &scale);

  __global__ void cuda_ffdotpow_concat_2d(double2* d_ffdot_plane_cpx, double* d_ffdot_plane, int sigblock, int kern_offset, int total_blocks,  int sig_tot_convlen, int sig_totlen);

  /** \brief Kernel wrapper function for cuda_ffdotpow_concat_2d kernel function. */
  void call_kernel_cuda_ffdotpow_concat_2d(const dim3 &blocks, const dim3 &threads, double2 *const d_ffdot_plane_cpx, double *const d_ffdot_plane, const int &sigblock, const int &kern_offset, const int &total_blocks, const int &sig_tot_convlen, const int &sig_totlen);

  __global__ void cuda_ffdotpow_concat_2d_inbin(double2* d_ffdot_plane_cpx, double* d_ffdot_plane, int sigblock, int kern_offset, int total_blocks, int  sig_tot_convlen, int sig_totlen);

  /** \brief Kernel wrapper function for cuda_ffdotpow_concat_2d_inbin kernel function. */
  void call_kernel_cuda_ffdotpow_concat_2d_inbin(const dim3 &blocks, const dim3 &threads, double2 *const d_ffdot_plane_cpx, double *const d_ffdot_plane, const int &sigblock, const int &kern_offset, const int &total_blocks, const int &sig_tot_convlen, const int &sig_totlen);

  __global__ void cuda_ffdotpow_concat_2d_ndm_inbin(double2* d_ffdot_plane_cpx, double* d_ffdot_plane, int kernlen, int siglen, int nkern, int kern_offset, int total_blocks, int sig_tot_convlen, int sig_totlen, int ndm);

  __global__ void cuda_convolve_customfft_wes_no_reorder02(double2* d_kernel, double2* d_signal, double *d_ffdot_pw, int sigblock, int sig_tot_convlen, int sig_totlen, int offset, float scale);

  /** \brief Kernel wrapper function for cuda_convolve_customfft_wes_no_reorder02 kernel function. */
  void call_kernel_cuda_convolve_customfft_wes_no_reorder02(const int &blocks, double2 *const d_kernel, double2 *const d_signal, double *const d_ffdot_pw, const int &sigblock, const int &sig_tot_convlen, const int &sig_totlen, const int &offset, const float &scale);

  __global__ void cuda_convolve_customfft_wes_no_reorder02_inbin(double2* d_kernel, double2* d_signal, double *d_ffdot_pw, int sigblock, int sig_tot_convlen, int sig_totlen, int offset, float scale, float2 *ip_edge_points);

  /** \brief Kernel wrapper function for cuda_convolve_customfft_wes_no_reorder02_inbin kernel function. */
  void call_kernel_cuda_convolve_customfft_wes_no_reorder02_inbin(const int &blocks, double2 *const d_kernel, double2 *const d_signal, double *const d_ffdot_pw, const int &sigblock, const int &sig_tot_convlen, const int &sig_totlen, const int &offset, const float &scale, float2 *const ip_edge_points);

  __global__ void GPU_CONV_kFFT_mk11_2elem_2v(double2 const* __restrict__ d_input_signal, double *d_output_plane_reduced, double2 const* __restrict__ d_templates, int useful_part_size, int offset, int nConvolutions, float scale);

  __global__ void GPU_CONV_kFFT_mk11_4elem_2v(double2 const* __restrict__ d_input_signal, double *d_output_plane_reduced, double2 const* __restrict__ d_templates, int useful_part_size, int offset, int nConvolutions, float scale);

  /** \brief Kernel wrapper function for GPU_CONV_kFFT_mk11_4elem_2v kernel function. */
  void call_kernel_GPU_CONV_kFFT_mk11_4elem_2v(const dim3 &grid_size, const dim3 &block_size, double2 const*const d_input_signal, double *const d_output_plane_reduced, double2 const*const d_templates, const int &useful_part_size, const int &offset, const int &nConvolutions, const float &scale);

  __global__ void customfft_fwd_temps_no_reorder(double2* d_signal);

  /** \brief Kernel wrapper function for customfft_fwd_temps_no_reorder kernel function. */
  void call_kernel_customfft_fwd_temps_no_reorder(double2 *const d_signal);

  void call_kernel_cast_double_to_float(float *d_output, double *d_input, size_t data_length_bytes);

  __global__ void cast_double_to_float(float *d_output, double *d_input, unsigned long long N_floats);

  void call_kernel_cast_double2_to_float2(float2 *d_output, double2 *d_input, size_t data_length_bytes);

  __global__ void cast_double2_to_float2(float2 *d_output, double2 *d_input, unsigned long long N_floats);

  void call_kernel_cast_float_to_double(double *d_output, float *d_input, size_t data_length_bytes);

  __global__ void cast_float_to_double(double *d_output, float *d_input, unsigned long long N_floats);

  void call_kernel_cast_float2_to_double2(double2 *d_output, float2 *d_input, size_t data_length_bytes);

  __global__ void cast_float2_to_double2(double2 *d_output, float2 *d_input, unsigned long long N_floats);

} // namespace astroaccelerate

#endif // ASTRO_ACCELERATE_AA_FDAS_DEVICE_HPP
