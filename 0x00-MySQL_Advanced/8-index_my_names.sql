-- Creates an index idx_name_first on table names and first letter of name 
-- only first letter of name must be indexed


CREATE INDEX idx_name_first ON names (name(1));
