import pandas as pd

# Overview sample data
# Sample metrics data
metrics_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar'],
    'Deployment Frequency': [2.4, 2.8, 3.1],
    'Lead Time': [4.8, 4.5, 4.2],
    'Team Satisfaction': [65, 68, 72],
    'AI Adoption': [42, 48, 53]
})


# Sample dora metrics data
deployment_frequency_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Frequency': [2.4, 2.8, 3.1]
})

cycle_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Cycle Time': [8.0, 6.5, 5.2]
})

failure_rate_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Failure Rate': [20, 18, 15]
})

lead_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Lead Time': [4.8, 4.5, 4.2]
})

restore_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Restore Time': [6.5, 5.0, 4.2]
})

# Sample space metrics data

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

performance_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Quality': [70, 75, 80],
    'Impact': [60, 65, 70]
})

satisfaction_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Score': [65, 68, 72]
})


sprint_burndown_data = pd.DataFrame({
    'Day': [f"Day {i}" for i in range(1, 6)],
    'Remaining': [40, 32, 24, 16, 8],
    'Ideal': [40, 30, 20, 10, 0]
})

velocity_data = pd.DataFrame({
    'Sprint': ['S1', 'S2', 'S3'],
    'Velocity': [28, 32, 36]
})

ai_adoption_by_team = pd.DataFrame({
    'Team': ['Frontend', 'Backend', 'DevOps', 'QA', 'Mobile'],
    'Adoption': [75, 82, 68, 85, 72],
    'Impact': [70, 78, 65, 82, 68],
    'Satisfaction': [85, 88, 80, 90, 82]
})

# Sample agile metrics data
ai_adoption_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Adoption Rate': [40, 55, 68]
})
