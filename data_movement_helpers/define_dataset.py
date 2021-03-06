# Defines a tabular dataset on top of an Azure ML datastore
from azureml.core import Workspace, Datastore, Dataset
from azureml.data import DataType
from azureml.core.authentication import AzureCliAuthentication

# Retrieve a datastore from a ML workspace
ws = Workspace.from_config(auth=AzureCliAuthentication())
datastore_name = 'workspaceblobstore'
datastore = Datastore.get(ws, datastore_name)

# Register dataset and sebset version for each data split
for data_split in ['train', 'test']:
    for set in ['', 'subset_']:
        # Create a TabularDataset from paths in datastore in split folder
        # Note that wildcards can be used
        datastore_paths = [
            (datastore, '{}.csv'.format(set + data_split))
        ]

        print(datastore_paths)

        # Create a TabularDataset from paths in datastore
        dataset = Dataset.File.from_files(
            path=datastore_paths
        )

        # Register the defined dataset for later use
        dataset.register(
            workspace=ws,
            name=('newsgroups_' + set + data_split),
            description='newsgroups data',
            create_new_version=True
        )

        dataset.download(target_path='C:/Users/mideboer.EUROPE/Documents/GitHub/aml-mlops-workshop/data_movement_helpers', overwrite=False)
