from src.main import up_first

def test_up_first():
    assert up_first('skypro') == 'Skypro'
    assert up_first('111') == '111'

def test_up_first_for_empty():
    assert up_first('') == ''
