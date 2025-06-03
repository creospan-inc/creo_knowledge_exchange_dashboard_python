import sqlite3
import pandas as pd
import random

# === Create Teams ===
teams = pd.DataFrame({
    "team_id": [f"team_{i:02d}" for i in range(1, 6)],
    "team_name": [f"Team {chr(64+i)}" for i in range(1, 6)],
    "team_lead": [f"Lead {chr(64+i)}" for i in range(1, 6)],
    "department": random.choices(["Engineering", "Product", "Design"], k=5)
})

# === Function to attach team_id to any DataFrame ===
def add_team_id(df, n=None):
    team_ids = teams["team_id"].tolist()
    n = n or len(df)
    return df.assign(team_id=[random.choice(team_ids) for _ in range(n)])

# === Overview Metrics ===
metrics_data = add_team_id(pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar'],
    'Deployment Frequency': [2.4, 2.8, 3.1],
    'Lead Time': [4.8, 4.5, 4.2],
    'Team Satisfaction': [65, 68, 72],
    'AI Adoption': [42, 48, 53]
}))

# === DORA Metrics ===
deployment_frequency_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Frequency': [2.4, 2.8, 3.1]
}))

lead_time_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Lead Time': [4.8, 4.5, 4.2]
}))

failure_rate_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Failure Rate': [20, 18, 15]
}))

restore_time_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Restore Time': [6.5, 5.0, 4.2]
}))

cycle_time_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Cycle Time': [8.0, 6.5, 5.2]
}))

# === SPACE Metrics ===
satisfaction_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Score': [65, 68, 72]
}))

performance_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Quality': [70, 75, 80],
    'Impact': [60, 65, 70]
}))

communication_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Collaboration': [70, 75, 80]
}))

efficiency_data = add_team_id(pd.DataFrame({
    'Task': ['Code Review', 'Testing', 'Documentation', 'Bug Fixing', 'Feature Dev'],
    'Traditional': [120, 180, 150, 200, 300],
    'AI-Assisted': [45, 90, 60, 100, 180]
}))

efficiency_trend_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Time Saved': [12, 18, 24, 30, 36, 42, 48],
    'Productive Hours': [22, 24, 26, 28, 30, 32, 34],
    'Overhead': [18, 16, 14, 12, 10, 8, 6]
}))

activity_data = add_team_id(pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'user': ['Alex Johnson', 'Sarah Miller', 'David Chen', 'Emily Wilson', 'Michael Brown'],
    'type': ['ai-prompt', 'commit', 'pull-request', 'comment', 'ai-prompt'],
    'description': [
        'Generated test cases using AI assistant',
        'Committed AI-generated code refactoring',
        'Opened PR for AI-assisted feature implementation',
        'Discussed AI adoption strategy in team meeting',
        'Used AI to optimize database queries'
    ],
    'time': ['2 hours ago', '3 hours ago', '5 hours ago', '1 day ago', '1 day ago']
}))

activity_trend_data = add_team_id(pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Prompts': [120, 150, 180, 210, 240, 270, 300],
    'Commits': [180, 195, 210, 225, 240, 255, 270]
}))

# === Agile Metrics ===
velocity_data = add_team_id(pd.DataFrame({
    'Sprint': ['S1', 'S2', 'S3'],
    'Velocity': [28, 32, 36]
}))

sprint_burndown_data = add_team_id(pd.DataFrame({
    'Day': [f"Day {i}" for i in range(1, 6)],
    'Remaining': [40, 32, 24, 16, 8],
    'Ideal': [40, 30, 20, 10, 0]
}))

ai_adoption_by_team = add_team_id(pd.DataFrame({
    'Team': ['Frontend', 'Backend', 'DevOps', 'QA', 'Mobile'],
    'Adoption': [75, 82, 68, 85, 72],
    'Impact': [70, 78, 65, 82, 68],
    'Satisfaction': [85, 88, 80, 90, 82]
}))

ai_adoption_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Adoption Rate': [40, 55, 68]
})

# === AI Time Saving by Role Metrics ===
time_saving_by_role = pd.DataFrame({
    'Role': ['Product Manager', 'Designer', 'Engineer', 'QA'],
    'Hours Saved': [15.3, 12.8, 20.5, 18.2],
    'Percent Time Saved': [22, 18, 28, 25],
    'Traditional Hours': [68, 72, 75, 70],
    'AI-Assisted Hours': [53, 59, 54, 52]
})

time_saving_by_role_trend = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Product Manager': [8.2, 10.5, 12.8, 14.1, 15.3, 16.7],
    'Designer': [6.5, 8.2, 9.4, 10.6, 12.8, 14.0],
    'Engineer': [12.4, 14.8, 16.5, 18.2, 20.5, 22.3],
    'QA': [10.2, 12.5, 14.7, 16.4, 18.2, 19.8]
})

# === Write to SQLite ===
if __name__ == "__main__":
    conn = sqlite3.connect("dashboard_metrics_original.db")

    tables = {
        "teams": teams,
        "metrics_data": metrics_data,
        "deployment_frequency_data": deployment_frequency_data,
        "lead_time_data": lead_time_data,
        "failure_rate_data": failure_rate_data,
        "restore_time_data": restore_time_data,
        "cycle_time_data": cycle_time_data,
        "satisfaction_data": satisfaction_data,
        "performance_data": performance_data,
        "communication_data": communication_data,
        "efficiency_data": efficiency_data,
        "efficiency_trend_data": efficiency_trend_data,
        "activity_data": activity_data,
        "activity_trend_data": activity_trend_data,
        "velocity_data": velocity_data,
        "sprint_burndown_data": sprint_burndown_data,
        "ai_adoption_by_team": ai_adoption_by_team,
        "ai_adoption_data": ai_adoption_data,
        "time_saving_by_role": time_saving_by_role,
        "time_saving_by_role_trend": time_saving_by_role_trend,
    }

    for name, df in tables.items():
        df.to_sql(name, conn, if_exists="replace", index=False)
        print(f"✅ Saved to DB: {name}")

    conn.close()
    print("🎉 All data written to dashboard_metrics.db")