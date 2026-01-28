## Ebube Okechukwu – Portfolio

Ultra‑modern personal portfolio for **Mechatronics Engineering, Cybersecurity, Software Development, CAD, and Quality Management**, built with **Flask**, **Jinja**, **Tailwind CSS**, and **Flask‑SQLAlchemy**.

### Features

- **Fully responsive single‑page portfolio** (hero, about, skills, experience, projects, contact).
- **Dark / light mode toggle** with preference saved in `localStorage`.
- **Contact form** that stores messages in a SQLite database and shows toast‑style flash messages.
- **Admin dashboard** (password‑protected) to review and mark contact messages as read/unread.
- **Modern UI** using Tailwind via CDN, gradients, glassmorphism effects, and cards.

### Tech Stack

- Backend: `Flask`, `Flask‑SQLAlchemy`, SQLite
- Frontend: Jinja templates, Tailwind CSS (CDN), vanilla JavaScript

### Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows PowerShell

pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

### Admin Dashboard

- **Login URL**: `/admin/login`
- **Password**: `2020/EN/12566`

Once logged in, you can see messages submitted from the contact form and toggle their read status.

