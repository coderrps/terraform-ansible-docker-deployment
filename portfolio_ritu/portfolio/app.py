from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Portfolio Data
portfolio_data = {
    "name": "Ritu Priya Singh",
    "title": "Software Engineer",
    "location": "New Delhi, India",
    "email": "ritupriyasingh.work@gmail.com",
    "phone": "+91-9876543210",
    "linkedin": "https://www.linkedin.com/in/ritupriyasingh",
    "github": "https://github.com/coderrps",
    "summary": "Detail-oriented Software Engineer with experience in cloud technologies, DevOps, and system debugging. Passionate about resolving complex issues using data-driven approaches and automation.",
    "skills": {
        "Programming/Scripting": ["Python", "Bash", "Erlang"],
        "Databases": ["MySQL", "PostgreSQL"],
        "Cloud": ["Azure", "AWS"],
        "DevOps": ["Docker", "Kubernetes", "GitHub Actions", "Jenkins", "JIRA"],
        "Monitoring & Logging": ["Grafana", "Elastic Search"],
        "Operating Systems": ["Linux"]
    },
    "experience": [
        {
            "role": "Software Engineer",
            "company": "Grey Orange",
            "period": "September 2025 – Present",
            "points": [
                "Investigated and resolved customer issues by performing RCA, collaborating with cross-functional teams, and ensuring timely resolution.",
                "Debugged core system issues using Erlang, Linux CLI, and real-time log analysis.",
                "Analyzed logs and system performance using Elastic Search and Grafana to identify anomalies and spikes.",
                "Queried and validated data using SQL, supporting issue diagnosis and system analysis.",
                "Automated workflows and data extraction using Erlang and Bash scripting, and managed incidents via JIRA."
            ]
        },
        {
            "role": "Technical Support Engineer",
            "company": "Data Resolve Technologies",
            "period": "December 2024",
            "points": [
                "Performed database cleanup by deleting all data from the PostgreSQL database.",
                "Developed Shell scripts to automate database maintenance tasks and streamline system operations.",
                "Worked on a monitoring tool that enables policy creation, such as blocking social media and file uploads, for clients.",
                "Identified and fixed bugs related to policy enforcement and backend server issues on the dashboard."
            ]
        }
    ],
    "projects": [
        {
            "title": "Azure DevOps CI/CD Pipeline for App Deployment",
            "tech": ["Python", "Azure Services", "Docker", "Git/GitHub"],
            "points": [
                "Built and deployed CI/CD pipelines for Flask app deployment on Azure App Service.",
                "Created and optimized Dockerfiles to containerize Flask applications for consistent and efficient deployment.",
                "Integrated Git/GitHub to enable version control and trigger automated CI/CD workflows.",
                "Implemented automated build validation and deployment checks to ensure reliable releases."
            ],
            "github": "https://github.com"
        },
        {
            "title": "Integration of Power BI & SQL",
            "tech": ["MySQL", "Power BI"],
            "points": [
                "Conducted revenue analysis using SQL and Power BI, revealing trends and patterns such as peak order days and top-selling products.",
                "Utilized DAX and dashboards for data visualization and business insights.",
                "Analyzed product performance to identify top/bottom contributors.",
                "Developed interactive dashboards to track KPIs and support data-driven decision making."
            ],
            "github": "https://github.com"
        }
    ],
    "education": [
        {
            "degree": "B.Tech. (CSE)",
            "score": "7.73 CGPA",
            "institution": "Lovely Professional University",
            "period": "2020 – 2024",
            "location": "Phagwara, Punjab"
        },
        {
            "degree": "Higher Secondary",
            "score": "64%",
            "institution": "Evergreen Public School",
            "period": "2020",
            "location": "Najafgarh, Delhi"
        },
        {
            "degree": "Secondary",
            "score": "74%",
            "institution": "Baldwin Academy",
            "period": "2018",
            "location": "Patna, Bihar"
        }
    ],
    "certifications": [
        {
            "title": "Microsoft Certified: Azure Fundamentals",
            "issuer": "Microsoft",
            "date": "Aug 2024",
            "score": "921/1000"
        },
        {
            "title": "Red Hat Program Learner",
            "issuer": "Red Hat Academy",
            "date": "May 2024"
        },
        {
            "title": "AWS Cloud Foundations with DevOps",
            "issuer": "Lovely Professional University",
            "date": "July 2022"
        }
    ],
    "achievements": [
        "Scored 921/1000 in AZ900 – Microsoft Certified: Azure Fundamentals.",
        "Presented paper on Alzheimer's Disease Detection Model Using CNN and RNN at IEEE IC3SE-2024, Amity University; received Certificate of Presentation.",
        "Linux Red Hat Program Learner in Red Hat Academy.",
        "Hosted Multiple Virtual Events for GeeksForGeeks Student Organization."
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
