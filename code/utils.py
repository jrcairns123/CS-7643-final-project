import tarfile


def extract_tar(tar_path, output_path):
    '''
    simple function to extract all files from a .tar file at tar_path 
    to the folder output_path

    Parameters
    ----------
    tar_path : str
        path to tar file which files will be extracted from.
    output_path : str
        output path (folder) where extracted files will be saved.

    Returns
    -------
    None.

    '''
    # open the tar file using the 'tarfile' module
    tar = tarfile.open(tar_path)
    
    # extract all the contents of the tar file to the specified directory
    tar.extractall(path=output_path)
    
    # close the tar file
    tar.close()



if __name__ == '__main__':

    output_path = r"E:\GaTech OMS Analytics\Degree Courses\2023 Spring\CS 7643 - Deep Learning\Project\peoples_speech\test_data"
    tar_path = r"C:\Users\jrcai\Downloads\clean_000000.tar"
    
    extract_tar(tar_path, output_path)