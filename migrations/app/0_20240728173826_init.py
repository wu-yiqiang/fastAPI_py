from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `picture` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `contractor` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `companyName` VARCHAR(255) NOT NULL UNIQUE,
    `email` VARCHAR(255) NOT NULL,
    `type` INT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `truck` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `displayName` VARCHAR(255) NOT NULL UNIQUE,
    `contractors_id` INT NOT NULL,
    CONSTRAINT `fk_truck_contract_83b728e5` FOREIGN KEY (`contractors_id`) REFERENCES `contractor` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `driver` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `givenName` VARCHAR(255) NOT NULL UNIQUE,
    `gender` BOOL NOT NULL UNIQUE,
    `contractorsId_id` INT NOT NULL,
    CONSTRAINT `fk_driver_contract_a5f42020` FOREIGN KEY (`contractorsId_id`) REFERENCES `contractor` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `roles` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `role_name` VARCHAR(255) NOT NULL UNIQUE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `routers` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `router_name` VARCHAR(255) NOT NULL UNIQUE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `menus` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `menu_name` VARCHAR(255) NOT NULL UNIQUE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `buttons` (
    `uuid` CHAR(36) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `button_name` VARCHAR(255) NOT NULL UNIQUE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users_buttons` (
    `users_id` INT NOT NULL,
    `buttons_id` INT NOT NULL,
    FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`buttons_id`) REFERENCES `buttons` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_users_butto_users_i_ad7546` (`users_id`, `buttons_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users_roles` (
    `users_id` INT NOT NULL,
    `roles_id` INT NOT NULL,
    FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`roles_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_users_roles_users_i_7be870` (`users_id`, `roles_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users_menus` (
    `users_id` INT NOT NULL,
    `menus_id` INT NOT NULL,
    FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`menus_id`) REFERENCES `menus` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_users_menus_users_i_075d5e` (`users_id`, `menus_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users_routers` (
    `users_id` INT NOT NULL,
    `routers_id` INT NOT NULL,
    FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`routers_id`) REFERENCES `routers` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_users_route_users_i_2f03ae` (`users_id`, `routers_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
