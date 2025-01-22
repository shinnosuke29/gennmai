import subprocess

def test_sum():
    result = subprocess.run(
        "printf '10\n20\n30\n' | python3 scripts/numstats.py --sum",
        shell=True, capture_output=True, text=True
    )
    assert "Sum: 60.0" in result.stdout

def test_average():
    result = subprocess.run(
        "printf '10\n20\n30\n' | python3 scripts/numstats.py --avg",
        shell=True, capture_output=True, text=True
    )
    assert "Average: 20.00" in result.stdout
