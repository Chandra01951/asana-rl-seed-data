PRAGMA foreign_keys = ON;

-- =========================
-- 1. organizations
-- =========================
CREATE TABLE organizations (
    org_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL
);

-- =========================
-- 2. teams
-- =========================
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    function TEXT CHECK (function IN ('engineering', 'marketing', 'ops')),
    FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

-- =========================
-- 3. users
-- =========================
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT CHECK (role IN ('IC', 'Senior IC', 'Lead', 'Manager', 'Senior Manager', 'Director')),
    joined_at TIMESTAMP NOT NULL,
    FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

-- =========================
-- 4. team_memberships (M:N)
-- =========================
CREATE TABLE team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    joined_at TIMESTAMP NOT NULL,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- =========================
-- 5. projects
-- =========================
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    name TEXT NOT NULL,
    project_type TEXT CHECK (project_type IN ('sprint', 'campaign', 'ops')),
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- =========================
-- 6. sections
-- =========================
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- =========================
-- 7. tasks
-- =========================
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT NOT NULL,
    assignee_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    created_at TIMESTAMP NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id),
    CHECK (
        completed = 0 OR 
        (completed = 1 AND completed_at IS NOT NULL)
    )
);

-- =========================
-- 8. subtasks
-- =========================
CREATE TABLE subtasks (
    subtask_id TEXT PRIMARY KEY,
    parent_task_id TEXT NOT NULL,
    name TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id)
);

-- =========================
-- 9. comments
-- =========================
CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (author_id) REFERENCES users(user_id)
);

-- =========================
-- 10. custom_field_definitions
-- =========================
CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT CHECK (field_type IN ('enum', 'number')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- =========================
-- 11. custom_field_values
-- =========================
CREATE TABLE custom_field_values (
    value_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id)
);

-- =========================
-- 12. tags
-- =========================
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- =========================
-- 13. task_tags (M:N)
-- =========================
CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

-- =========================
-- 14. attachments (optional but realistic)
-- =========================
CREATE TABLE attachments (
    attachment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_type TEXT,
    uploaded_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);
