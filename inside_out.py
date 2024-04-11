#This script defines two classes: DataSource and SaasProgram. DataSource represents a single data source with attributes like name, type, and description. 
#You can use this script by creating an instance of SaasProgram, adding data sources using the add_data_source method, and then listing the data sources 
#using the list_data_sources method.

import os

class DataSource:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

class SaasCredentials:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    @classmethod
    def from_environment(cls, url_env_var, api_key_env_var):
        url = os.getenv(url_env_var)
        api_key = os.getenv(api_key_env_var)
        return cls(url, api_key)

class SaasProgram:
    def __init__(self, name, credentials):
        self.name = name
        self.credentials = credentials
        self.data_sources = []

    def add_data_source(self, name, type, description):
        data_source = DataSource(name, type, description)
        self.data_sources.append(data_source)

    def list_data_sources(self):
        print(f"Data Sources for {self.name}:")
        for idx, data_source in enumerate(self.data_sources, start=1):
            print(f"{idx}. Name: {data_source.name}")
            print(f"   Type: {data_source.type}")
            print(f"   Description: {data_source.description}\n")

# Example usage
if __name__ == "__main__":
    credentials = SaasCredentials.from_environment("SAAS_URL", "SAAS_API_KEY")
    saas_program = SaasProgram("Example SaaS Program", credentials)
    saas_program.add_data_source("Database", "SQL", "Customer information database")
    saas_program.add_data_source("API", "REST", "Third-party service for analytics")
    saas_program.add_data_source("File Storage", "CSV", "Uploaded files by users")

    saas_program.list_data_sources()
