import numpy as np
import os
import nibabel as nib

def split_nifti_time(path_to_nii_cine, path_to_nii_split):
    '''
        Splits a nifti file of dimensions (height, width, depth, time) by time, retains the original header information
    '''
    
    os.makedirs(path_to_nii_split, exist_ok=True)
    
    for filename in os.listdir(path_to_nii_cine):
        if '.nii.gz' in filename[-7:] or '.nii' in filename[-4:]:
            nii_data = nib.load(os.path.join(dir_nifti_cine, filename))
            img = nii_data.get_fdata()
            header = nii_data.header
            affine = nii_data.affine
    
            header['dim'][4] = 1
    
            height, width, depth, time = img.shape
    
            for index_time in range(time):
                print(index_time)
                img_current = np.expand_dims(img[:, :, :, index_time], -1)
                nii_data_current = nib.Nifti1Image(img_current, header=header, affine=affine)
                nib.save(nii_data_current, os.path.join(path_to_nii_split, f'{index_time}.nii'))