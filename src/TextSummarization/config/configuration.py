from TextSummarization.constants import *
from TextSummarization.utils.common import read_yaml,create_directories
from TextSummarization.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):

        # Load YAML files into dictionaries
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure the root directory for artifacts exists
        create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Correctly access the 'data_ingestion' section of the config
        config = self.config['data_ingestion']

        # Ensure the root directory for data ingestion exists
        create_directories([config['root_dir']])

        # Initialize and return the DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_URL=config['source_URL'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )

        return data_ingestion_config