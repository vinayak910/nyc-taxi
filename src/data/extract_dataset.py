import logging
from zipfile import ZipFile
from pathlib import Path
from src.logger import create_log_path, CustomLogger

# path to save the log files
log_file_path = create_log_path('extract_dataset')

# create the cutom Logger object
extract_logger = CustomLogger('extract_dataset' , log_file_path)

# set the level of logging to INFO
extract_logger.set_log_level(level = logging.INFO)


def extract_zip_file(input_path:Path , output_path : Path):
    with ZipFile(file = input_path) as f:
        f.extractall(path = output_path)
        input_file_name = input_path.stem + input_path.suffix
        extract_logger.save_logs(msg = f'{input_file_name} extracted successfully at the target path',
                                 log_level = 'info')
        
def main():
    # current file path
    current_path = Path(__file__)
    #root directory path
    root_path = current_path.parent.parent.parent
    # raw data directory path
    raw_data_path = root_path/'data'/'raw'
    # zip files path
    input_path = raw_data_path/'zipped'
    # making directory for extracted data
    output_path = raw_data_path/'extracted'
    output_path.mkdir(exist_ok=True , parents=True)


    # extract the train and test files
    # for the train file
    extract_zip_file(input_path= input_path/'train.zip' , output_path= output_path)
    # for the test file
    extract_zip_file(input_path= input_path/'test.zip', output_path= output_path)
    


if __name__ == "__main__":
    # call the main function
    main()
    