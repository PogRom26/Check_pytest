from src.reverse import reverse_string

def test_up_reverse():
    assert reverse_string('skypro') == 'orpyks'
    assert reverse_string('111') == '111'
    assert reverse_string('') == ''