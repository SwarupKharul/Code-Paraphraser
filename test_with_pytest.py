import subprocess

def test_always_passes():
    check = subprocess.run(["python", "tokenize.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(check.stderr)
    if check.stderr:
        assert False
    assert True

test_always_passes()
