import json 
from file_manager import FileManager 

def test_save_then_load_preserves_item_data(tmp_path):
    """Saving and loading item data store list contents."""
    filename = tmp_path / "items.json"  #  create temporary file path
    manager = FileManager(filename)  # manager for the file
    expected = [{"name": "Milk", "purchased": False}]  # data to save
    assert manager.save_items(expected) is True  # save should succeed
    assert manager.load_items() == expected  # load should restore the same list


def test_missing_file_loads_empty_list(tmp_path):
    """Loading from a missing file should return an empty list."""
    filename = tmp_path / "items.json"  # file does not exist yet
    manager = FileManager(filename)  # manager uses the missing file path
    assert manager.load_items() == []  # should safely return an empty list


def test_invalid_json_loads_empty_list(tmp_path):
    """Invalid JSON content should be handled."""
    filename = tmp_path / "items.json" 
    filename.write_text("not json")  # write invalid JSON content
    manager = FileManager(filename) 
    assert manager.load_items() == []  # should return empty list instead of crashing


def test_json_object_instead_of_list_loads_empty_list(tmp_path):
    """Non list JSON should be rejected and return an empty list."""
    filename = tmp_path / "items.json"  # create a temp file path
    filename.write_text(json.dumps({"name": "Milk"}))  # write a JSON object
    manager = FileManager(filename)  # manager loads the bad structure
    assert manager.load_items() == []  # only JSON lists should be accepted
