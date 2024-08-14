-- Show users and update (or not) email
SELECT * FROM users;

-- Update valid_email for bob@dylan.com without changing email
UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";

-- Change email for sylvie@dylan.com, which should reset valid_email
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";

-- Update the name without changing email, valid_email should remain the same
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";

SELECT * FROM users;

-- Attempt to update the email to the same value, valid_email should not change
UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";

SELECT * FROM users;

