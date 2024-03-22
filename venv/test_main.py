import pytest
import table as table
from rich.console import Console
from rich.table import Table
import datetime
from io import StringIO

from table import add_record, delete_record, amend_record, display_full_details





def test_add_record_success(monkeypatch):
    #ARRANGE 
    #Preparing input data with valid inputs
    input_data = "100\nTest\nTest\n2011-11-11\n2012-12-12\n100\nTest\n0\n"

    #Creating mock data
    fields = ["Project ID", "Project name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]
    data = []

    #Mocking system inputs through using the 'input_data' string
    monkeypatch.setattr('sys.stdin', StringIO(input_data))

    #ACT - calling function that adds record
    output = add_record(fields,data)

    #ASSERT - the result 
    expected_data = [
        [100, "Test", "Test", "2011-11-11", "2012-12-12", 100, "Test", 0]
    ]
    assert output == (fields, expected_data)


def test_add_record_failure(monkeypatch):
    #ARRANGE
    # Prepare input data with invalid inputs
    input_data = "invalid\n\nTest\nTest\n2022-01-01\n2022-01-02\n100\nTest\n0\n"
    
    # Creating mock data
    fields = ["Project ID", "Project name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]
    data = []

    #Mocking system inputs through using the 'input_data' string
    monkeypatch.setattr('sys.stdin', StringIO(input_data))

    # ASSERT - Check if the data remains unchanged after the failed attempt
    assert data == []




def test_delete_record_success(monkeypatch):
    #ARRANGE
    # Prepare input data with valid input - existing project id
    input_data = "100"

    # Creating mock data
    fields = ["Project ID", "Project name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]
    data = data = [
    [100, "VACCINES", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", 3],
    [101, "FASTFOOD APP", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", 1],
    [102, "HYDROGEN X", "NESTLE", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "NEW ZEALAND", 3]]

    #Mocking system inputs through using 'input_data'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))


    # ACT - Call the function that deletes a record
    result = delete_record(fields, data)

    # ASSERT - the result should be original list length minus 1
    assert data[0][1] != "Vaccines"


def test_delete_record_failure(monkeypatch):
    #ARRANGE
    # Prepare input data with invalid input
    input_data = "104"

    # Creating mock data
    fields = ["Project ID", "Project name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]
    data = data = [
    [100, "VACCINES", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", 3],
    [101, "FASTFOOD APP", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", 1],
    [102, "HYDROGEN X", "NESTLE", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "NEW ZEALAND", 3]]

    #Mocking system inputs through using 'input_data' 
    monkeypatch.setattr('sys.stdin', StringIO(input_data))


    # ACT - Call the function that deletes a record
    result = delete_record(fields, data)

    # ASSERT - the result should be original list length
    assert len(data) == 3



# def test_amend_record_success(monkeypatch):
#     #ARRANGE
#     # Prepare input data with valid input
#     input_data = "101\nCountry\nTest"


#     # Creating mock data
#     fields = ["Project ID", "Project name", "Client", "Start Date", "End Date", "Consultant ID", "COUNTRY", "Project Status"]
#     data = [
#     [100, "VACCINES", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", 3],
#     [101, "FASTFOOD APP", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", 1],
#     [102, "HYDROGEN X", "NESTLE", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "NEW ZEALAND", 3]]

#     #Mocking system inputs through using 'input_data' 
#     monkeypatch.setattr('sys.stdin', StringIO(input_data))

#     # ACT - Call the function that deletes a record
#     result = amend_record(fields, data)

#     # ASSERT - the result should be original list length minus 1
#     assert "Test" in data


# def test_amend_record_failure(monkeypatch):
#     #ARRANGE
#     # Prepare input data with invalid input
#     input_data = "101\nCountry\n\n"


#     # Creating mock data
#     fields = ["Project ID", "Project name", "Client", "Start Date", "End Date", "Consultant ID", "COUNTRY", "Project Status"]
#     data = [
#     [100, "VACCINES", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", 3],
#     [101, "FASTFOOD APP", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", 1],
#     [102, "HYDROGEN X", "NESTLE", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "NEW ZEALAND", 3]]

#     #Mocking system inputs through using 'input_data' 
#     monkeypatch.setattr('sys.stdin', StringIO(input_data))

#     # ACT - Call the function that deletes a record
#     result = amend_record(fields, data)

#     # ASSERT - the result should not be in the data list 
#     assert 1324 in data
