# import sqlite3
import pandas as pd
from .db import get_db_engine

# === Overview Metrics ===
metrics_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar'],
    'Deployment Frequency': [2.4, 2.8, 3.1],
    'Lead Time': [4.8, 4.5, 4.2],
    'Team Satisfaction': [65, 68, 72],
    'AI Adoption': [42, 48, 53]
})

# === DORA Metrics ===
deployment_frequency_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Frequency': [2.4, 2.8, 3.1]
})

lead_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Lead Time': [4.8, 4.5, 4.2]
})

failure_rate_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Failure Rate': [20, 18, 15]
})

restore_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Restore Time': [6.5, 5.0, 4.2]
})

cycle_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Cycle Time': [8.0, 6.5, 5.2]
})

# === SPACE Metrics ===
satisfaction_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Score': [65, 68, 72]
})

performance_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Quality': [70, 75, 80],
    'Impact': [60, 65, 70]
})

communication_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Collaboration': [70, 75, 80]
})

efficiency_data = pd.DataFrame({
    'Task': ['Code Review', 'Testing', 'Documentation', 'Bug Fixing', 'Feature Dev'],
    'Traditional': [120, 180, 150, 200, 300],
    'AI-Assisted': [45, 90, 60, 100, 180]
})

efficiency_trend_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Time Saved': [12, 18, 24, 30, 36, 42, 48],
    'Productive Hours': [22, 24, 26, 28, 30, 32, 34],
    'Overhead': [18, 16, 14, 12, 10, 8, 6]
})

activity_data = pd.DataFrame({
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
})

activity_trend_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Prompts': [120, 150, 180, 210, 240, 270, 300],
    'Commits': [180, 195, 210, 225, 240, 255, 270]
})

# === Agile Metrics ===
velocity_data = pd.DataFrame({
    'Sprint': ['S1', 'S2', 'S3'],
    'Velocity': [28, 32, 36]
})

sprint_burndown_data = pd.DataFrame({
    'Day': [f"Day {i}" for i in range(1, 6)],
    'Remaining': [40, 32, 24, 16, 8],
    'Ideal': [40, 30, 20, 10, 0]
})

ai_adoption_by_team = pd.DataFrame({
    'Team': ['Frontend', 'Backend', 'DevOps', 'QA', 'Mobile'],
    'Adoption': [75, 82, 68, 85, 72],
    'Impact': [70, 78, 65, 82, 68],
    'Satisfaction': [85, 88, 80, 90, 82]
})

ai_adoption_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Adoption Rate': [40, 55, 68]
})

# Optional: Save all tables as CSVs for inspection
if __name__ == "__main__":
    try:
        engine = get_db_engine()
        print("Attempting to connect to PostgreSQL...")
        with engine.connect() as connection_test:
             print("✔ Successfully connected to PostgreSQL.")

        tables = {
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
        }

        with engine.connect() as connection:
            print("Writing tables to PostgreSQL...")
            for name, df in tables.items():
                try:
                    df.to_sql(name, connection, if_exists="replace", index=False, method='multi')
                    print(f"  ✔ Wrote table: {name}")
                except Exception as e:
                    print(f"  ❌ Failed to write table {name}: {e}")

        print("🎉 Finished writing data to PostgreSQL.")

    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
    except Exception as e:
        print(f"❌ An error occurred during database setup: {e}")

