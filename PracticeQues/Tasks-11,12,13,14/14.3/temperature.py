def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    assert c_to_f(0) == 32.0
    assert c_to_f(100) == 212.0
    assert f_to_c(32) == 0.0

    print("All self-tests passed")
    print(f"0°C  = {c_to_f(0)} °F")
    print(f"37°C = {c_to_f(37)} °F")