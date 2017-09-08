SELECT * FROM friendships.users;

INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`) VALUES ('Robert', 'Amato', now());

INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`) VALUES ('Maggie', 'Amato', now());

INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`) VALUES ('Honri', 'Levon', now());

INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`) VALUES ('Jullian', 'Timmons', now());

INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`) VALUES ('Tony', 'Williams', now());

SELECT CONCAT(users.first_name, ' ', users.last_name) AS user_names, friendships.users_id,
GROUP_CONCAT(friendships.friend_id) AS friends_id,
GROUP_CONCAT(users1.first_name, ' ', users1.last_name) AS friends
FROM users
LEFT JOIN friendships ON users.id = friendships.users_id
LEFT JOIN users AS users1 ON users1.id = friendships.friend_id
GROUP BY users.id
ORDER BY users.id;
