# Issues found in parcel_tracker.py

Before: Pylint 4.91/10, Bandit 1 High + 1 Medium + 2 Low, Flake8 11 issues.
After: Pylint 10.00/10, Bandit 0 issues, Flake8 0 issues.
(Line numbers are from the original file / the "before" reports.)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell injection (B602, High) | Security | 49 | `subprocess.check_output("ping -c 1 " + hubAddress, shell=True)` runs user text through a shell, so `8.8.8.8; rm -rf /` would execute | Validate with `ipaddress.ip_address()`, pass a list `["ping","-c","1",addr]`, drop `shell=True` |
| Insecure temp file (B306, Medium) | Security | 45 | `tempfile.mktemp()` only returns a name; another process can create that file first (race condition) | Use `tempfile.mkstemp()` (creates the file atomically), close the fd, return the path |
| Weak random for OTP (B311, Low) | Security | 68 | `random.randint` is predictable, not safe for an OTP | `1000 + secrets.randbelow(9000)` |
| subprocess import (B404, Low) | Security | 2 | Informational flag for importing subprocess | Usage is now safe (validated, no shell); documented with `# nosec B404` + reason |
| Mutable default arg (W0102) | Bug | 11 | `history=[]` is created once and shared by every call | Default to `None`, create a new list inside the function |
| Broad exception (W0718) | Bug / Design | 34 | `except Exception` hides unrelated bugs | `except KeyError` |
| Merge comparisons (R1714) | Refactor | 41 | `status == "Picked Up" or status == "In Transit"` | `status in ("Picked Up", "In Transit")` |
| Naming (C0103) x14 | Style | many | camelCase names (`bookParcel`, `trackingId`, `weightKg`...) | Renamed to snake_case |
| Missing docstrings (C0114, C0116) x10 | Style | 1, 11, 19... | No module/function docstrings | Added short docstrings |
| E302 / E305 | Formatting | 11, 19, 25, 31, 39, 43, 47, 51, 72 | Need 2 blank lines around top-level defs | Added blank lines |
| E225 | Formatting | 26 | `cost=50` | `cost = 50` |
| E231 | Formatting | 70 | `"...today:",len(...)` | Space after comma |
