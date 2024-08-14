-- Create the missing tables
CREATE TABLE IF NOT EXISTS projects (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int NOT NULL,
    project_id int NOT NULL,
    score int DEFAULT 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

-- Populate the tables with sample data
INSERT INTO projects (name) VALUES ("C is fun");
INSERT INTO projects (name) VALUES ("Python is cool");

INSERT INTO corrections (user_id, project_id, score) VALUES (1, 1, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 2, 96);
INSERT INTO corrections (user_id, project_id, score) VALUES (2, 1, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (2, 2, 73);

