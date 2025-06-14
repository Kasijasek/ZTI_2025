import requests

def notify_user_by_email(to, subject, body):
    try:
        requests.post("http://email-service:8001/send-email", json={
            "to": to,
            "subject": subject,
            "body": body
        })
    except Exception as e:
        print("❌ Błąd wysyłki e-maila:", e)
