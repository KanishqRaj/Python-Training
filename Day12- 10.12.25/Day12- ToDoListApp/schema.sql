
CREATE TABLE IF NOT EXISTS tasks (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  title       TEXT    NOT NULL,
  description TEXT,
  status      TEXT    NOT NULL DEFAULT 'Pending',  -- 'Pending' or 'Completed'
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
