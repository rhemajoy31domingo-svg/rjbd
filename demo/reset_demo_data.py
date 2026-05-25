"""Day 06 - Reset the DEMO data to its dirty starting state.

Run this BEFORE every rehearsal take and BEFORE the real recording.

What it does:
  - Rebuilds Day06_demo.db (the SQL demo database) from scratch, so all the
    UPDATE / DELETE queries you ran during rehearsal are undone.
  - Re-writes Day06_demo_staff.csv (the Power Query demo CSV) back to its
    original messy version, in case you re-saved or edited it.

It is safe to run this any number of times. It only touches the two demo
files in this folder. It does NOT touch:
  - Day06_messy_data.csv     (activity data — students')
  - Day06_practice.db        (activity data — students')
  - any other file in the repo

Usage from PowerShell, inside this folder:
    python reset_demo_data.py

Under the hood: this re-runs create_demo_dataset.py, which is the single
source of truth for the demo data. If you ever change the demo data,
edit create_demo_dataset.py — never this file.
"""
import os
import runpy
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATOR  = os.path.join(SCRIPT_DIR, "create_demo_dataset.py")
DB_FILE    = os.path.join(SCRIPT_DIR, "Day06_demo.db")
CSV_FILE   = os.path.join(SCRIPT_DIR, "Day06_demo_staff.csv")

print("=" * 60)
print(" Day 06 - RESETTING demo data to dirty starting state")
print("=" * 60)

if not os.path.exists(GENERATOR):
    print(f"\nERROR: cannot find {GENERATOR}")
    print("Make sure you are running this from the Day 06 folder.")
    sys.exit(1)

# Show what we're about to overwrite (just for transparency)
for label, path in [("SQL demo DB ", DB_FILE), ("PQ  demo CSV", CSV_FILE)]:
    state = "exists - will be replaced" if os.path.exists(path) else "missing - will be created"
    print(f"  {label}: {state}")

print("\nRunning create_demo_dataset.py ...\n")
print("-" * 60)

# Re-run the canonical generator with __name__ == '__main__' semantics.
# This is the single source of truth — never duplicate the data here.
runpy.run_path(GENERATOR, run_name="__main__")

print("-" * 60)
print("\n[OK] Demo data is back to its dirty starting state.")
print("     You can rehearse the recording again.\n")
print("Files reset in this folder:")
print(f"  - Day06_demo.db        (SQL demo: payroll table, 30 dirty rows)")
print(f"  - Day06_demo_staff.csv (PQ  demo: 28 dirty staff rows)")
print("\nReminder: this does NOT touch the activity files")
print("  (Day06_practice.db, Day06_messy_data.csv) — those stay as-is.")
