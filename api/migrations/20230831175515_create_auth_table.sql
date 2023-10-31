-- migrate:up
CREATE TABLE `auth` (
    `id` int AUTO_INCREMENT,
    `username` varchar(60) NOT NULL UNIQUE,
    `password` varchar(130) NOT NULL,`created_at` datetime NOT NULL DEFAULT NOW(), /* SHA512 */
    `role` ENUM('admin', 'user', 'mod') NOT NULL DEFAULT 'user',
    `active` tinyint(1) NOT NULL DEFAULT 1,
    `updated_at` datetime NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);

INSERT INTO `auth` (`username`, `password`, `role`) VALUES
('admin','c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', 'admin');
INSERT INTO `auth` (`username`, `password`) VALUES
('user','b14361404c078ffd549c03db443c3fede2f3e534d73f78f77301ed97d4a436a9fd9db05ee8b325c0ad36438b43fec8510c204fc1c1edb21d0941c00e9e2c1ce2');

-- migrate:down
SET FOREIGN_KEY_CHECKS=0; -- to disable them
DROP TABLE IF EXISTS `auth`;
SET FOREIGN_KEY_CHECKS=1; -- to re-enable them

