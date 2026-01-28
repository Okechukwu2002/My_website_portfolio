"""
Keep-Alive Script for Render Free Tier
Pings the site every 10 minutes to prevent spin-down
Run this script locally or on another free service to keep your Render app alive
"""
import time
import requests
import sys
from datetime import datetime

# Your Render app URL - UPDATE THIS with your actual Render URL
RENDER_URL = "https://your-app-name.onrender.com"  # Change this!

# Health check endpoint
HEALTH_ENDPOINT = f"{RENDER_URL}/health"

# Ping interval in seconds (10 minutes = 600 seconds)
# Render free tier spins down after 15 minutes of inactivity
PING_INTERVAL = 600  # 10 minutes


def ping_site():
    """Ping the health check endpoint."""
    try:
        response = requests.get(HEALTH_ENDPOINT, timeout=10)
        if response.status_code == 200:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✓ Site is alive - Status: {response.status_code}")
            return True
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ⚠ Site responded with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✗ Failed to ping site: {e}")
        return False


def main():
    """Main loop to keep pinging the site."""
    print(f"Starting keep-alive bot for {RENDER_URL}")
    print(f"Pinging every {PING_INTERVAL // 60} minutes...")
    print("Press Ctrl+C to stop\n")

    ping_count = 0
    
    try:
        while True:
            ping_count += 1
            print(f"Ping #{ping_count}: ", end="")
            ping_site()
            
            # Wait before next ping
            time.sleep(PING_INTERVAL)
            
    except KeyboardInterrupt:
        print(f"\n\nStopped after {ping_count} pings.")
        sys.exit(0)


if __name__ == "__main__":
    if RENDER_URL == "https://your-app-name.onrender.com":
        print("⚠ ERROR: Please update RENDER_URL in keep_alive.py with your actual Render URL!")
        sys.exit(1)
    
    main()
