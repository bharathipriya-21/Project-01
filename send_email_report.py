import smtplib
from email.mime.text import MIMEText
from datetime import date

report_data = {
    "stale_branches": [
        {
            "branch": "main",
            "committer": "Your Name",  
            "date": "2025-05-09",
            "message": "Initialized readme file",
            "days_inactive": "2 days",
            "commits": "8 commits"
        }
    ],
    "open_prs": [
        {
            "title": "Initialized readme file",
            "created_at": "2025-05-09",
            "days_active": "2 days",
            "creator": "YourGitHubUsername", 
            "url": "https://github.com/yourusername/repo-health-automation/pull/1",
            "reviewers": []
        }
    ],
    "repo_info": {
        "name": "repo-health-automation",
        "owner": "yourusername",  
        "description": "A tool to monitor GitHub repo health.",
        "default_branch": "main",
        "visibility": "private",
        "open_issues_count": 2
    }
}

def format_report(data):
    repo = data["repo_info"]
    lines = [
        f" Repository: {repo['name']} ({repo['visibility']})",
        f" Owner: {repo['owner']}",
        f" Description: {repo['description']}",
        f" Default Branch: {repo['default_branch']}",
        f" Open Issues: {repo['open_issues_count']}\n",
        " Stale Branches (> 30 days inactive):"
    ]

    for branch in data["stale_branches"]:
        lines.append(f" - {branch['branch']} (by {branch['committer']} on {branch['date']}, "
                     f"{branch['days_inactive']}, {branch['commits']})")

    lines.append("\n Open PRs (> 7 days):")
    for pr in data["open_prs"]:
        reviewers = ", ".join(pr["reviewers"]) if pr["reviewers"] else "No reviewers"
        lines.append(f" - \"{pr['title']}\" by {pr['creator']} on {pr['created_at']} ({pr['days_active']})")
        lines.append(f"   {pr['url']} [Reviewers: {reviewers}]")

    return "\n".join(lines)

def send_email(body):
    sender = "your.email@gmail.com"      
    password = "your_app_password"         
    recipient = "recipient@example.com"    

    msg = MIMEText(body)
    msg["Subject"] = f" Repo Health Report - {date.today()}"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

    print(" Email sent!")

if __name__ == "__main__":
    report = format_report(report_data)
    send_email(report)
