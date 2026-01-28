from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Basic configuration
    app.config["SECRET_KEY"] = "change-this-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        # Import models after db is initialized
        from models import ContactMessage  # noqa: F401

        db.create_all()

    register_routes(app)
    return app


class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)


ADMIN_PASSWORD = "2020/EN/12566"


def is_admin_authenticated():
    return session.get("is_admin") is True


def register_routes(app: Flask):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.post("/contact")
    def contact():
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in your name, email, and message.", "error")
            return redirect(url_for("index") + "#contact")

        contact_message = ContactMessage(
            name=name, email=email, subject=subject, message=message
        )
        db.session.add(contact_message)
        db.session.commit()

        flash("Thank you for reaching out! I will get back to you soon.", "success")
        return redirect(url_for("index") + "#contact")

    @app.route("/admin/login", methods=["GET", "POST"])
    def admin_login():
        if request.method == "POST":
            password = request.form.get("password", "")
            if password == ADMIN_PASSWORD:
                session["is_admin"] = True
                flash("Welcome back, Ebube.", "success")
                return redirect(url_for("admin_dashboard"))
            flash("Invalid password. Please try again.", "error")
        return render_template("admin_login.html")

    @app.route("/admin/logout")
    def admin_logout():
        session.pop("is_admin", None)
        flash("You have been logged out.", "info")
        return redirect(url_for("index"))

    @app.route("/admin")
    def admin_dashboard():
        if not is_admin_authenticated():
            return redirect(url_for("admin_login"))

        messages = ContactMessage.query.order_by(
            ContactMessage.created_at.desc()
        ).all()
        unread_count = ContactMessage.query.filter_by(is_read=False).count()
        return render_template(
            "admin_dashboard.html",
            messages=messages,
            unread_count=unread_count,
        )

    @app.post("/admin/messages/<int:message_id>/toggle-read")
    def toggle_message_read(message_id: int):
        if not is_admin_authenticated():
            return redirect(url_for("admin_login"))

        message = ContactMessage.query.get_or_404(message_id)
        message.is_read = not message.is_read
        db.session.commit()
        return redirect(url_for("admin_dashboard"))


if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)

