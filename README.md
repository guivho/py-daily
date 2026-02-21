# 🐍 py-daily

A collection of small, practical Python scripts for everyday tasks — because the best automation is the kind you actually use.

---

## What's inside

| Module | Description |
|---|---|
| `renamer/` | Data driven file renamer and mover |
| `wiper/` | Data driven temporary file wiper |
| `picknrs/` | Get random nrs for some number games |
| `sendnrs/` | Send picked nrs to my email box at set days |
| `p3/` | Common module |

---

## Getting started

**Requirements:** Python 3.8+

```bash
# Clone the repo
git clone https://github.com/your-username/py-daily.git
cd py-daily

# Install dependencies
pip install -r requirements.txt
```

---

## Authentication

Authentication info is provided via a constants.py file
that - for obvious reasons - is absent from the repo.
It is expected to have following content:

```python
picked_numbers_email = "*** <***@***.***>"
sender_email = "***@***.***"
sender_password = "***"
smtp_port = 587
smtp_server = "***"
```

---

## Usage

Each module is self-contained. Run any script directly:

```bash
python renamer.py
python wiper.py
python picknrs.py
python sendnrs.py
```

The renamer.py is called every 5' from the windows task scheduler.
The sendnrs.py is called once a day from the task scheduler.

---

## Contributing

Got a useful daily script? PRs are welcome. Keep it simple, keep it readable.

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-script`)
3. Commit your changes
4. Open a pull request

---

## License

[MIT](LICENSE)
