# AgriSathi — Setup (get this running in ~5 min)

## 1. Install dependencies
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Database
This app now points at your existing `agridb` database (crops, schemes, users tables).
Run this one-time fix so password hashes fit (they're longer than 50 chars):
```sql
ALTER TABLE users MODIFY password VARCHAR(255);
```
`schema.sql` in this folder is the original demo schema — not used anymore, kept for reference only.

## 3. Configure DB password
Open `config.py` and set your MySQL password, OR set an env var:
```bash
export MYSQL_PASSWORD=yourpassword
export MYSQL_DB=agridb
```

## 4. Run
```bash
python app.py
```
Visit **http://localhost:5000** — it'll redirect to login. Click "Register" to create a farmer account, then log in.

---

## What's already working
- ✅ **Auth**: Register / Login / Logout (session-based, password hashing)
- ✅ **Schemes Explorer**: search by name/description, filter by category, detail view
- ✅ **Dashboard**: shows latest schemes + latest prices
- ✅ **Crop Prices**: list grouped by crop, market comparison table, price trend graph (Chart.js)

## Who should work on what (2-3 people, ~2-3 hrs left)
- **Person A**: `schemes.py` + `templates/schemes/` — already functional, polish UI / add more filters if time allows
- **Person B**: `prices.py` + `templates/prices/` — core queries work, look for `# TODO (teammate)` comments to extend (date filters, better graph styling)
- **Person C**: Multi-language support + notifications (see "Next steps" below), or start the PPT/demo script

## Next steps if time allows
- **Multi-language**: `users.language_pref` is already stored at registration. Simplest path in the time you have: keep an English-only UI for demo, mention multi-language as "designed for, partially implemented" — full i18n (Flask-Babel) is a bigger lift than 2-3 hrs allows.
- **Notifications**: `notifications` table already exists. Quickest win: on dashboard load, show a static banner like "3 new schemes added this week" pulled from a `COUNT(*)` query — looks real in a demo without needing a background job.
- **Live APIs**: currently uses demo seed data in MySQL, which is safer for a live demo than depending on external API uptime. Only swap to a real API if you have time to spare and test it.

## File structure
```
agrisathi/
├── app.py              # Flask app factory + routes registration
├── config.py            # MySQL config
├── db.py                # DB connection helpers (query_db, execute_db)
├── auth.py               # Register/Login/Logout + @login_required decorator
├── dashboard.py
├── schemes.py
├── prices.py
├── schema.sql           # Run this first — creates DB + demo data
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── auth/{login,register}.html
│   ├── schemes/{index,detail}.html
│   └── prices/{index,trend}.html
└── static/css/style.css
```
