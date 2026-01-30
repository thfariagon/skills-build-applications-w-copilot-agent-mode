#!/bin/bash

# Setup and populate OctoFit Database
cd /workspaces/skills-build-applications-w-copilot-agent-mode

echo "=========================================="
echo "Activating Python virtual environment..."
echo "=========================================="
source octofit-tracker/backend/venv/bin/activate

echo ""
echo "=========================================="
echo "Running makemigrations..."
echo "=========================================="
python octofit-tracker/backend/manage.py makemigrations

echo ""
echo "=========================================="
echo "Running migrate..."
echo "=========================================="
python octofit-tracker/backend/manage.py migrate

echo ""
echo "=========================================="
echo "Populating database with test data..."
echo "=========================================="
python octofit-tracker/backend/manage.py populate_db

echo ""
echo "=========================================="
echo "Verifying database with mongosh..."
echo "=========================================="
echo "Listing collections in octofit_db:"
mongosh --eval "db.getMongo().getDB('octofit_db').getCollectionNames()" 2>/dev/null || echo "MongoDB connection details will be shown after mongosh starts"

echo ""
echo "=========================================="
echo "Database setup completed!"
echo "=========================================="
echo ""
echo "To verify the data, you can use mongosh:"
echo "  mongosh"
echo "  use octofit_db"
echo "  db.users.find().pretty()"
echo "  db.teams.find().pretty()"
echo "  db.activities.find().limit(1).pretty()"
echo "  db.leaderboard.find().pretty()"
echo "  db.workouts.find().pretty()"
