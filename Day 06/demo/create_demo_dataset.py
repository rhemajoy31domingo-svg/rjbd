"""Day 06 - Generate the DEMO datasets used in the pre-recorded video lesson.

These datasets are DELIBERATELY DIFFERENT from the activity datasets:
  - Activity data is e-commerce (customers in Day06_messy_data.csv, orders in
    Day06_practice.db).
  - Demo data is HR / payroll (staff roster + payroll runs).
That way the recorded demo teaches the CLEANING SKILLS without giving away the
activity answers. The issue TYPES are the same so the skills transfer directly.

Creates:
  1. Day06_demo_staff.csv  -- deliberately dirty CSV for the Power Query demo
  2. Day06_demo.db         -- SQLite database with a dirty 'payroll' table for the SQL demo
"""
import sys, io, os, sqlite3, csv
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# PART 1: Messy STAFF CSV for the Power Query demo
# Issue TYPES mirror the activity CSV (Day06_messy_data.csv):
#   duplicates, blank row, casing, spaces, mixed dates, N/A in a number, blanks
# ============================================================
csv_path = os.path.join(SCRIPT_DIR, "Day06_demo_staff.csv")

staff_rows = [
    ["EmpID", "Full Name", "Email", "Dept", "Branch", "Phone", "Hire Date", "Salary", "Status"],
    ["E001", "Maria Santos", "maria.santos@company.com", "IT", "Manila", "09171234567", "2022-01-15", "45000", "Active"],
    ["E002", "Juan Dela Cruz", "juan.delacruz@company.com", "HR", "cebu city", "09181234567", "2021-03-20", "38000", "Active"],  # branch lowercase
    ["E003", "Ana Reyes", "ana.reyes@company.com", "Finance", "Davao City", "09191234567", "March 10, 2022", "52000", "active"],  # date format, status lowercase
    ["E004", "Carlos Garcia", "carlos.garcia@company.com", "IT", "MAKATI", "09201234567", "2020-11-05", "48000", "Active"],  # branch caps
    ["E005", "Sofia Mendoza", "", "Operations", "Quezon City", "09211234567", "2023-04-18", "35000", "Active"],  # missing email
    ["E006", "Miguel Torres", "miguel.torres@company.com", "Operations", " Cebu City", "09221234567", "2022-08-22", "41000", "Active"],  # branch leading space
    ["E007", "Isabella Cruz", "isabella.cruz@company.com", "Sales", "Manila", "09231234567", "2022-05-01", "33000", "Active"],
    ["E002", "Juan Dela Cruz", "juan.delacruz@company.com", "HR", "cebu city", "09181234567", "2021-03-20", "38000", "Active"],  # DUPLICATE of E002
    ["E008", "Rafael Aquino", "rafael.aquino@company.com", "Finance", "davao city", "09241234567", "2021-01-30", "55000", "Active"],  # branch lowercase
    ["E009", "Patricia  Lim", "patricia.lim@company.com", "IT", "Makati", "09251234567", "2023-06-15", "47000", "Active"],  # double space in name
    ["E010", "Daniel Tan", "daniel.tan@company.com", "Sales", "Iloilo City", "639261234567", "2022-06-10", "36000", "Inactive"],  # different phone format
    ["E011", "Angela Rivera", "angela.rivera@company.com", "HR", "Quezon City", "09271234567", "2021-02-14", "39000", "Active"],
    ["E012", "Roberto Flores", "roberto.flores@company.com", "Finance", "Makati", "09281234567", "Sept 1, 2020", "60000", "ACTIVE"],  # date format, status caps
    ["E013", "Christine Go", "christine.go@company.com", "IT", "Cebu City", "", "2023-07-20", "44000", "Active"],  # missing phone
    ["E014", "Marco Villanueva", "marco.villanueva@company.com", "Sales", "quezon city", "09301234567", "2022-03-25", "34000", "Active"],  # branch lowercase
    ["E015", "Joy Bautista", "joy.bautista@company.com", "Operations", "Manila", "09311234567", "2023-08-01", "N/A", "Active"],  # N/A in numeric field
    ["E016", "Kenneth Sy", "kenneth.sy@company.com", "IT", "Cebu City", "09321234567", "2021-01-10", "49000", "Active"],
    ["E017", " Grace Domingo", "grace.domingo@company.com", "HR", "Davao City", "09331234567", "2022-04-05", "37000", "active"],  # leading space in name, status lowercase
    ["E018", "Leo Pascual", "leo.pascual@company.com", "Finance", "Quezon City", "09341234567", "2020-12-01", "58000", "Active"],
    ["E019", "Nicole Ramos", "nicole.ramos@company.com", "Sales", "Cagayan de Oro", "09351234567", "2023-05-15", "32000", "Inactive"],
    ["E020", "Patrick Ong", "patrick.ong@company.com", "IT", "Makati", "09361234567", "2020-10-20", "51000", "Active"],
    ["E009", "Patricia  Lim", "patricia.lim@company.com", "IT", "Makati", "09251234567", "2023-06-15", "47000", "Active"],  # DUPLICATE of E009
    ["E021", "Lily Chua", "lily.chua@company.com", "HR", "Manila", "09371234567", "2024-01-05", "35000", "On Leave"],
    ["E022", "Mark Reyes", "mark.reyes@company.com", "Operations", "Cebu City", "09381234567", "Jan 12, 2024", "40000", "Active"],  # date format
    ["", "Unknown Employee", "", "", "", "", "", "", ""],  # completely empty / placeholder row
    ["E023", "Sarah David", "sarah.david@company.com", "Finance", "Davao City", "09391234567", "2024-02-01", "53000", "Active"],
    ["E024", "James Lim", "james.lim@company.com", "Sales", "Quezon City", "09401234567", "2024-02-15", "33000", "Active"],
    ["E025", "Anne Tan", "anne.tan@company.com", "IT", "Iloilo City", "09411234567", "2024-03-01", "36000", "active"],  # status lowercase
]

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(staff_rows)

# ---- compute CSV ground-truth ----
header, data = staff_rows[0], staff_rows[1:]
ids = [r[0] for r in data if r[0].strip()]
dup_ids = {k: v for k, v in Counter(ids).items() if v > 1}
dup_extra = sum(v - 1 for v in dup_ids.values())
blank_rows = sum(1 for r in data if not r[0].strip())
rows_after = len(data) - dup_extra - blank_rows

print("=== Day06_demo_staff.csv (Power Query demo) ===")
print(f"Saved: {csv_path}")
print(f"  Total lines incl header : {len(staff_rows)}")
print(f"  Data rows (before clean) : {len(data)}")
print(f"  Duplicate EmpIDs         : {dup_ids}  (extra rows to remove: {dup_extra})")
print(f"  Blank/placeholder rows   : {blank_rows}")
print(f"  Rows AFTER cleaning      : {rows_after}")

# ============================================================
# PART 2: SQLite database with a dirty 'payroll' table for the SQL demo
# Issue TYPES mirror the activity DB (orders): NULLs, casing, spaces, junk row.
# ============================================================
db_path = os.path.join(SCRIPT_DIR, "Day06_demo.db")
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("""
CREATE TABLE payroll (
    record_id     INTEGER PRIMARY KEY,
    employee_name TEXT,
    email         TEXT,
    branch        TEXT,
    position      TEXT,
    department    TEXT,
    hours         INTEGER,
    rate          REAL,
    gross_pay     REAL,
    pay_date      TEXT,
    status        TEXT
)
""")

payroll = [
    (1,  "Maria Santos",      "maria.santos@company.com",   "Manila",          "Developer",  "it",         160, 280, 44800, "2025-01-31", "Processed"),  # dept lowercase
    (2,  "Juan Dela Cruz",    "juan.delacruz@company.com",  "cebu city",       "Analyst",    "Finance",    160, 240, 38400, "2025-01-31", "Processed"),  # branch lowercase
    (3,  " Ana Reyes",        "ana.reyes@company.com",      "Davao City",      "Specialist", "HR",         160, 230, 36800, "2025-01-31", "processed"),  # leading space, status lowercase
    (4,  "Carlos Garcia",     "carlos.garcia@company.com",  "MAKATI",          "Developer",  "IT",         160, 300, 48000, "2025-01-31", "Processed"),  # branch caps
    (5,  "Sofia Mendoza",     None,                          "Quezon City",     "Officer",    "operations", 160, 220, 35200, "2025-01-31", "Processed"),  # NULL email, dept lowercase
    (6,  "Miguel Torres",     "miguel.torres@company.com",  "Cebu City",       "Officer",    "Operations", 160, 256, 40960, "2025-02-28", "Processed"),
    (7,  "Isabella Cruz ",    "isabella.cruz@company.com",  "Manila",          "Associate",  "sales",      160, 206, 32960, "2025-02-28", "Processed"),  # trailing space, dept lowercase
    (8,  "Rafael Aquino",     "rafael.aquino@company.com",  "davao city",      "Analyst",    "Finance",    160, 344, 55040, "2025-02-28", "Pending"),    # branch lowercase
    (9,  "Patricia Lim",      "patricia.lim@company.com",   "Makati",          "Developer",  "IT",         160, 294, 47040, "2025-02-28", "Processed"),
    (10, "Daniel Tan",        "daniel.tan@company.com",     "Iloilo City",     "Associate",  "Sales",      160, 225, 36000, "2025-02-28", "Processed"),
    (11, "Angela Rivera",     "angela.rivera@company.com",  "Pasig",           "Specialist", "hr",         160, 244, 39040, "2025-02-28", "Hold"),       # dept lowercase
    (12, "Roberto Flores",    "roberto.flores@company.com", "Makati",          "Manager",    "Finance",    160, 375, 60000, "2025-03-31", "Processed"),
    (13, "Christine Go",      "christine.go@company.com",   "Cebu City",       "Specialist", "IT",         160, 275, 44000, "2025-03-31", "Processed"),
    (14, "Marco Villanueva",  "marco.villanueva@company.com","quezon city",    "Associate",  "SALES",      160, 213, 34080, "2025-03-31", "Processed"),  # branch lowercase, dept caps
    (15, "Joy Bautista",      "joy.bautista@company.com",   "Manila",          "Officer",    "Operations", 160, 219, 35040, "2025-03-31", "Pending"),
    (16, "Kenneth Sy",        "kenneth.sy@company.com",     "Cebu City",       "Developer",  "IT",         160, 306, 48960, "2025-03-31", "Processed"),
    (17, " Grace Domingo",    "grace.domingo@company.com",  "Davao City",      "Specialist", "HR",         160, 231, 36960, "2025-03-31", "Processed"),  # leading space
    (18, "Leo Pascual",       "leo.pascual@company.com",    "Quezon City",     "Manager",    "Finance",    160, 363, 58080, "2025-04-30", "Processed"),
    (19, "Nicole Ramos",      None,                          "Cagayan de Oro",  "Associate",  "Sales",      160, 200, 32000, "2025-04-30", "Processed"),  # NULL email
    (20, "Patrick Ong",       "patrick.ong@company.com",    "MAKATI",          "Developer",  "it",         160, 319, 51040, "2025-04-30", "Processed"),  # branch caps, dept lowercase
    (21, "Maria Santos",      "maria.santos@company.com",   "Manila",          "Developer",  "IT",         160, 280, 44800, "2025-04-30", "Processed"),
    (22, "Juan Dela Cruz",    "juan.delacruz@company.com",  "cebu city",       "Analyst",    "Finance",    160, 240, 38400, "2025-04-30", "Processed"),  # branch lowercase
    (23, " Ana Reyes",        "ana.reyes@company.com",      "Davao City",      "Specialist", "HR",         160, 230, 36800, "2025-05-31", "PROCESSED"),  # leading space, status caps
    (24, "Carlos Garcia",     "carlos.garcia@company.com",  "MAKATI",          "Developer",  "IT",         160, 300, 48000, "2025-05-31", "Processed"),  # branch caps
    (25, "Sofia Mendoza",     None,                          "Quezon City",     "Officer",    "Operations", 160, 220, 35200, "2025-05-31", "Processed"),  # NULL email
    (26, "test entry",        "test@test.com",              "test",            "test",       "test",         0,   0,     0, "2025-01-01", "test"),       # junk row
    (27, "Miguel Torres",     "miguel.torres@company.com",  "Cebu City",       "Officer",    "operations", 160, 256, 40960, "2025-05-31", "Processed"),  # dept lowercase
    (28, "Isabella Cruz ",    "isabella.cruz@company.com",  "Manila",          "Associate",  "Sales",      160, 206, 32960, "2025-05-31", "Pending"),    # trailing space
    (29, "Rafael Aquino",     "rafael.aquino@company.com",  "davao city",      "Analyst",    "Finance",    160, 344, 55040, "2025-06-30", "Processed"),  # branch lowercase
    (30, "Patricia Lim",      "patricia.lim@company.com",   "Makati",          "Developer",  "IT",         160, 294, 47040, "2025-06-30", "Processed"),
]

cur.executemany("INSERT INTO payroll VALUES (?,?,?,?,?,?,?,?,?,?,?)", payroll)
conn.commit()

# ---- compute DB ground-truth ----
def col(q):
    return [r[0] for r in cur.execute(q)]

row_count       = cur.execute("SELECT COUNT(*) FROM payroll").fetchone()[0]
branches        = sorted(col("SELECT DISTINCT branch FROM payroll"))
departments     = sorted(col("SELECT DISTINCT department FROM payroll"))
statuses        = sorted(col("SELECT DISTINCT status FROM payroll"))
null_email_ids  = col("SELECT record_id FROM payroll WHERE email IS NULL")
spaced_name_ids = col("SELECT record_id FROM payroll WHERE employee_name != TRIM(employee_name)")
junk_ids        = col("SELECT record_id FROM payroll WHERE employee_name = 'test entry'")

print("\n=== Day06_demo.db -> payroll table (SQL demo) ===")
print(f"Saved: {db_path}")
print(f"  Row count                : {row_count}")
print(f"  Distinct branch (before) : {branches}")
print(f"  Distinct department      : {departments}")
print(f"  Distinct status          : {statuses}")
print(f"  NULL emails              : {len(null_email_ids)} -> record_ids {null_email_ids}")
print(f"  Names with extra spaces  : {spaced_name_ids}")
print(f"  Junk row record_id       : {junk_ids}")
print(f"  Row count AFTER delete   : {row_count - 1}")

conn.close()
