from django.db import migrations

initial_sql = """
-- Core schema: create tables and seed initial data
CREATE TABLE IF NOT EXISTS "Department" (
  "department_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "department_name" TEXT NOT NULL UNIQUE,
  "department_leader_id" INTEGER,
  "department_leader" TEXT,
  "department_location" TEXT
);

CREATE TABLE IF NOT EXISTS "Team" (
  "team_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "team_name" TEXT NOT NULL UNIQUE,
  "team_leader" TEXT,
  "department_id" INTEGER NOT NULL,
  FOREIGN KEY("department_id") REFERENCES "Department"("department_id")
);

CREATE TABLE IF NOT EXISTS "HealthCheckCard" (
  "card_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "title" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "Session" (
  "session_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "date" TEXT NOT NULL,
  "team_id" INTEGER NOT NULL,
  "session" TEXT CHECK("session" IN ('Active','Completed','Cancelled')),
  FOREIGN KEY("team_id") REFERENCES "Team"("team_id")
);

CREATE TABLE IF NOT EXISTS "User" (
  "user_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "username" TEXT NOT NULL UNIQUE,
  "email" TEXT NOT NULL UNIQUE,
  "password" TEXT NOT NULL,
  "role" TEXT NOT NULL CHECK("role" IN ('Engineer','Team Leader')),
  "team_id" INTEGER,
  "is_team_leader" TEXT NOT NULL,
  FOREIGN KEY("team_id") REFERENCES "Team"("team_id")
);

CREATE TABLE IF NOT EXISTS "Vote" (
  "vote_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER NOT NULL,
  "session_id" INTEGER NOT NULL,
  "card_id" INTEGER NOT NULL,
  "vote_value" TEXT NOT NULL CHECK("vote_value" IN ('Green','Amber','Red')),
  "progress_status" TEXT,
  FOREIGN KEY("card_id") REFERENCES "HealthCheckCard"("card_id"),
  FOREIGN KEY("session_id") REFERENCES "Session"("session_id"),
  FOREIGN KEY("user_id") REFERENCES "User"("user_id")
);

-- Seed data
INSERT OR IGNORE INTO "Department" ("department_id","department_name","department_leader_id","department_leader","department_location") VALUES
 (1,'Software Engineering',101,'Alice Johnson','Building A'),
 (2,'Quality Assurance',102,'Bob Smith','Building B'),
 (3,'IT Support',103,'Charlie Brown','Building C');

INSERT OR IGNORE INTO "Team" ("team_id","team_name","team_leader","department_id") VALUES
 (1,'Frontend Team','David Lee',1),
 (2,'Backend Team','Emma Wilson',1),
 (3,'QA Automation','Frank Harris',2),
 (4,'Support Engineers','Grace White',3);

INSERT OR IGNORE INTO "User" ("user_id","name","username","email","password","role","team_id","is_team_leader") VALUES
 (1,'John Doe','johndoe','johndoe@example.com','hashedpassword1','Engineer',1,'No'),
 (2,'Jane Smith','janesmith','janesmith@example.com','hashedpassword2','Team Leader',1,'Yes'),
 (3,'Michael Brown','michaelb','michaelb@example.com','hashedpassword3','Engineer',2,'No'),
 (4,'Sara Davis','sarad','sarad@example.com','hashedpassword4','Team Leader',2,'Yes'),
 (5,'Tom Clark','tomc','tomc@example.com','hashedpassword5','Engineer',3,'No'),
 (6,'Laura Wilson','lauraw','lauraw@example.com','hashedpassword6','Engineer',4,'No');

"""

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.RunSQL(initial_sql),
    ]
