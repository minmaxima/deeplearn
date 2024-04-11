#This script defines two classes: DataSource and SaasProgram. 
# DataSource represents a single data source with attributes like name, type, and description. 
# SaasProgram represents the SaaS program itself, with a name and a list of data sources. 
# It has methods to add data sources and list all the data sources.
#You can use this script by creating an instance of SaasProgram, adding data sources
# using the add_data_source method, and then listing the data sources using the list_data_sources method.

import datetime
import os

class DataSource:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description
        self.users = []
        self.data = []
        
    def add_user(self, user):
        self.users.append(user)
        
    def add_data(self, data):
        self.data.append(data)
        
    def list_users(self):
        print(f"Users for {self.name}:")
        for idx, user in enumerate(self.users, start=1):
            print(f"{idx}. Name: {user.name}")
            print(f"   Email: {user.email}\n")      

    def list_data(self):
        print(f"Data for {self.name}:")
        for idx, data in enumerate(self.data, start=1):
            print(f"{idx}. {data}\n")   
            
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

class UserLister:
    @staticmethod
    def list_users(data_source):
        data_source.list_users()       
         
class DateRangeFilter:
    @staticmethod
    def filter_data_by_date(data_source, start_date, end_date):
        print(f"Data within the data range {start_date} to {end_date}:")
        filtered_data = [data for data in data_source.data if start_date <= data["date"] <= end_date]
        return filtered_data    
  
# Example usage
if __name__ == "__main__":
    credentials = SaasCredentials.from_environment("SAAS_URL", "SAAS_API_KEY")
    saas_program = SaasProgram("Example SaaS Program", credentials)
    saas_program.add_data_source("Database", "SQL", "Customer information database")
    saas_program.add_data_source("API", "REST", "Third-party service for analytics")
    saas_program.add_data_source("File Storage", "CSV", "Uploaded files by users")

# Add some sample data with dates
    data_source = saas_program.data_sources[0]
    data_source.add_data({"date": datetime(2024, 4, 1), "value": "Data 1"})
    data_source.add_data({"date": datetime(2024, 4, 5), "value": "Data 2"})
    data_source.add_data({"date": datetime(2024, 4, 10), "value": "Data 3"})

# Filter data by date range
    start_date = datetime(2024, 4, 1)
    end_date = datetime(2024, 4, 5)
    DateRangeFilter.filter_data_by_date(data_source, start_date, end_date)

 # List all data sources
    saas_program.list_data_sources()
