# Changelog

## v2.0.0 (2025-10-30)

### Breaking Changes
- Dropped Python 3.7, 3.8, 3.9 support
- Minimum Python version is now 3.10+

### Features
- Python 3.10, 3.11, 3.12, 3.13 support
- MTProto 2.0 compliant implementation
- Enhanced compiler optimizations (LTO, -O3, native arch)
- Zero external dependencies
- Direct pip install from git supported
- GitHub Actions CI/CD pipeline
- Automated releases to GitHub

### C Code Modernization (2025)
- C11/C17 standard compliance
- `restrict` keyword for pointer optimization
- `inline` function hints for better performance
- Modern compiler directives

### Optimizations
- Link-Time Optimization (LTO) enabled
- Native architecture optimization (-march=native)
- Aggressive function inlining
- Loop unrolling optimizations
- Fast math optimizations
- Multi-architecture wheel builds (x86_64, ARM64)

### Changes
- Updated build system to latest setuptools (>=75.0.0)
- Simplified codebase and documentation
- Cleaner API documentation
- Modern Python packaging standards

### Infrastructure
- GitHub Actions workflows for CI/CD
- Automated wheel building with cibuildwheel v3.2.1
- Dependabot for dependency updates
- Automated GitHub releases
- Dynamic versioning from source

### Installation
```bash
# Direct from GitHub
pip install git+https://github.com/ohmyarthur/tgcrypto.git

# Or specific version
pip install git+https://github.com/ohmyarthur/tgcrypto.git@v2.0.0
``

---

Original project: [pyrogram/tgcrypto](https://github.com/pyrogram/tgcrypto)  
Fork maintained by: [ohmyarthur](https://github.com/ohmyarthur)
