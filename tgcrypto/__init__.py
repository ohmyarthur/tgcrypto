from tgcrypto._version import __version__

try:
    from tgcrypto.tgcrypto import (
        ige256_encrypt,
        ige256_decrypt,
        ctr256_encrypt,
        ctr256_decrypt,
        cbc256_encrypt,
        cbc256_decrypt,
    )
except ImportError:
    pass

__all__ = [
    "__version__",
    "ige256_encrypt",
    "ige256_decrypt",
    "ctr256_encrypt",
    "ctr256_decrypt",
    "cbc256_encrypt",
    "cbc256_decrypt",
]
