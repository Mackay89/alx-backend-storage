ALTER TABLE names ADD COLUMN score INT;
CREATE INDEX idx_name_first_score ON names (name(1), score);
