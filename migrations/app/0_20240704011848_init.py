from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `user` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `contractor` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `companyName` VARCHAR(255) NOT NULL UNIQUE,
    `email` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `truck` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `displayName` VARCHAR(255) NOT NULL UNIQUE,
    `contractorsId_id` CHAR(36) NOT NULL,
    CONSTRAINT `fk_truck_contract_eed508f7` FOREIGN KEY (`contractorsId_id`) REFERENCES `contractor` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `driver` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_deleted` BOOL NOT NULL  DEFAULT 0,
    `givenName` VARCHAR(255) NOT NULL UNIQUE,
    `gender` BOOL NOT NULL UNIQUE,
    `contractorsId_id` CHAR(36) NOT NULL,
    CONSTRAINT `fk_driver_contract_a5f42020` FOREIGN KEY (`contractorsId_id`) REFERENCES `contractor` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
