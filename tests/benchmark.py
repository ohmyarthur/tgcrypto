#!/usr/bin/env python3
import os
import time
import tgcrypto

def human_speed(data_size_mb, elapsed):
    return data_size_mb / elapsed if elapsed > 0 else 0.0

def benchmark_ige256(size_mb=10):
    data = os.urandom(size_mb * 1024 * 1024)
    data += bytes(-len(data) % 16)
    key, iv = os.urandom(32), os.urandom(32)

    t0 = time.perf_counter()
    enc = tgcrypto.ige256_encrypt(data, key, iv)
    t1 = time.perf_counter()
    dec = tgcrypto.ige256_decrypt(enc, key, iv)
    t2 = time.perf_counter()

    assert data == dec
    return human_speed(size_mb, t1 - t0), human_speed(size_mb, t2 - t1)

def benchmark_ctr256(size_mb=10):
    data = os.urandom(size_mb * 1024 * 1024)
    key, iv = os.urandom(32), bytearray(os.urandom(16))
    iv2 = iv.copy()

    t0 = time.perf_counter()
    enc = tgcrypto.ctr256_encrypt(data, key, iv, bytes(1))
    t1 = time.perf_counter()
    dec = tgcrypto.ctr256_decrypt(enc, key, iv2, bytes(1))
    t2 = time.perf_counter()

    assert data == dec
    return human_speed(size_mb, t1 - t0), human_speed(size_mb, t2 - t1)

def benchmark_cbc256(size_mb=10):
    data = os.urandom(size_mb * 1024 * 1024)
    data += bytes(-len(data) % 16)
    key, iv = os.urandom(32), bytearray(os.urandom(16))
    iv2 = iv.copy()

    t0 = time.perf_counter()
    enc = tgcrypto.cbc256_encrypt(data, key, iv)
    t1 = time.perf_counter()
    dec = tgcrypto.cbc256_decrypt(enc, key, iv2)
    t2 = time.perf_counter()

    assert data == dec
    return human_speed(size_mb, t1 - t0), human_speed(size_mb, t2 - t1)

def main():
    size_mb = 10
    print(f"TgCrypto Benchmark ({size_mb}MB)")
    print("-" * 40)
    for name, func in [
        ("IGE256", benchmark_ige256),
        ("CTR256", benchmark_ctr256),
        ("CBC256", benchmark_cbc256)
    ]:
        enc, dec = func(size_mb)
        print(f"{name}: {enc:.1f} MB/s enc, {dec:.1f} MB/s dec")

if __name__ == "__main__":
    main()
