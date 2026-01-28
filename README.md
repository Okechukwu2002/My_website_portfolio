## Ebube Okechukwu – Portfolio

Ultra‑modern personal portfolio for **Mechatronics Engineering, Cybersecurity, Software Development, CAD, and Quality Management**, built with **Flask**, **Jinja**, **Tailwind CSS**, and **Flask‑SQLAlchemy**.

### Features

- **Fully responsive single‑page portfolio** (hero, about, skills, experience, projects, contact).
- **Dark / light mode toggle** with preference saved in `localStorage`.
- **Contact form** that stores messages in a SQLite database and shows toast‑style flash messages.
- **Admin dashboard** (password‑protected) to review and mark contact messages as read/unread.
- **Modern UI** using Tailwind via CDN, gradients, glassmorphism effects, and cards.
- **Health check endpoint** (`/health`) for monitoring and keep-alive.

### Tech Stack

- Backend: `Flask`, `Flask‑SQLAlchemy`, SQLite, Gunicorn
- Frontend: Jinja templates, Tailwind CSS (CDN), vanilla JavaScript

### Local Setup

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

---

## 🚀 Deployment on Render (Free Tier)

### Step 1: Deploy to Render

1. **Push your code to GitHub** (create a repository and push this project)

2. **Go to [Render.com](https://render.com)** and sign up/login

3. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Name**: `portfolio-website` (or your choice)
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:application`
     - **Plan**: Free

4. **Environment Variables** (optional but recommended):
   - `SECRET_KEY`: Generate a strong random secret key
   - `FLASK_ENV`: `production`

5. **Click "Create Web Service"** and wait for deployment

### Step 2: Set Up Keep-Alive Bot

Render's free tier spins down after 15 minutes of inactivity. To keep your site alive:

#### Option A: Run Keep-Alive Script Locally (Recommended)

1. **Update the URL** in `keep_alive.py`:
   ```python
   RENDER_URL = "https://your-app-name.onrender.com"  # Your actual Render URL
   ```

2. **Run the script**:
   ```bash
   python keep_alive.py
   ```

3. **Keep it running** on your computer (or a VPS/always-on device)

#### Option B: Use Free Uptime Monitoring Service

Use a free service like **UptimeRobot** (https://uptimerobot.com):

1. Sign up for free account
2. Add a new monitor:
   - **Monitor Type**: HTTP(s)
   - **URL**: `https://your-app-name.onrender.com/health`
   - **Monitoring Interval**: 5 minutes
3. This will ping your site every 5 minutes automatically

#### Option C: Use Another Free Service

You can also use:
- **Cron-job.org** (free cron jobs)
- **EasyCron** (free tier)
- **GitHub Actions** (free, runs on schedule)

### Step 3: Verify Deployment

- Visit your Render URL: `https://your-app-name.onrender.com`
- Check health endpoint: `https://your-app-name.onrender.com/health`
- Test the contact form
- Access admin dashboard: `https://your-app-name.onrender.com/admin/login`

### Important Notes

- **First request** after spin-down may take 30-60 seconds (cold start)
- **Database**: SQLite works on Render free tier, but data persists only on the filesystem
- **For production**, consider upgrading to paid tier or using Render PostgreSQL (free tier available)
- **Keep-alive** is essential for free tier to prevent spin-downs

### Troubleshooting

- **App won't start**: Check Render logs for errors
- **Database errors**: Ensure migrations run correctly (they run automatically on startup)
- **Site spins down**: Make sure keep-alive is running and pinging `/health` endpoint
- **Static files not loading**: Check that image paths are correct in templates

