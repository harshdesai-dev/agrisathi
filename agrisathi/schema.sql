-- AgriSathi Database Schema
-- Run: mysql -u root -p < schema.sql

CREATE DATABASE IF NOT EXISTS agrisathi;
USE agrisathi;

-- ============================
-- USERS (Farmer accounts)
-- ============================
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    location VARCHAR(100),
    language_pref VARCHAR(10) DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================
-- SCHEMES (Government Schemes)
-- ============================
CREATE TABLE IF NOT EXISTS schemes (
    scheme_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,          -- e.g. Financial Support, Insurance, Subsidy
    description TEXT,
    eligibility TEXT,
    benefits TEXT,
    required_documents TEXT,
    application_process TEXT,
    official_link VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================
-- CROPS
-- ============================
CREATE TABLE IF NOT EXISTS crops (
    crop_id INT AUTO_INCREMENT PRIMARY KEY,
    crop_name VARCHAR(100) NOT NULL,
    category VARCHAR(50)                    -- e.g. Grain, Vegetable, Fruit
);

-- ============================
-- MARKET PRICES
-- ============================
CREATE TABLE IF NOT EXISTS market_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    crop_id INT NOT NULL,
    market_name VARCHAR(100) NOT NULL,
    price_per_quintal DECIMAL(10,2) NOT NULL,
    price_date DATE NOT NULL,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id) ON DELETE CASCADE
);

-- ============================
-- NOTIFICATIONS (future use)
-- ============================
CREATE TABLE IF NOT EXISTS notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message VARCHAR(255) NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ============================
-- SEED DATA: Schemes (demo)
-- ============================
INSERT INTO schemes (name, category, description, eligibility, benefits, required_documents, application_process, official_link) VALUES
('PM-KISAN', 'Financial Support', 'Income support scheme providing direct cash transfer to farmer families.', 'All landholding farmer families with cultivable land.', 'Rs. 6000 per year in 3 equal installments.', 'Aadhaar Card, Land Records, Bank Account Details', 'Apply online via PM-KISAN portal or through local CSC center.', 'https://pmkisan.gov.in'),
('Pradhan Mantri Fasal Bima Yojana', 'Insurance', 'Crop insurance scheme protecting farmers against crop loss due to natural calamities.', 'Farmers growing notified crops in notified areas.', 'Insurance cover for crop loss, low premium rates.', 'Aadhaar Card, Land Records, Bank Passbook, Sowing Certificate', 'Apply through banks, insurance companies, or CSC centers before cutoff dates.', 'https://pmfby.gov.in'),
('Kisan Credit Card (KCC)', 'Financial Support', 'Provides farmers with affordable credit for agricultural needs.', 'Farmers, tenant farmers, sharecroppers, and self-help groups.', 'Low interest short-term credit for cultivation and other needs.', 'Aadhaar Card, Land Documents, Passport size photo', 'Apply at any nationalized bank or via KCC portal.', 'https://www.myscheme.gov.in'),
('Soil Health Card Scheme', 'Subsidy', 'Provides farmers with soil health cards to improve productivity through judicious use of inputs.', 'All farmers with agricultural land.', 'Free soil testing and nutrient recommendation every 2 years.', 'Land Records, Aadhaar Card', 'Apply through local agriculture department office.', 'https://soilhealth.dac.gov.in'),
('National Agriculture Market (e-NAM)', 'Market Access', 'Online trading platform for agricultural commodities to ensure better price discovery.', 'All farmers and traders registered with local mandis.', 'Access to nationwide market, transparent price discovery.', 'Aadhaar Card, Bank Account, Mandi Registration', 'Register on e-NAM portal through local mandi.', 'https://enam.gov.in'),
('Paramparagat Krishi Vikas Yojana', 'Subsidy', 'Promotes organic farming through cluster approach.', 'Farmer groups willing to adopt organic farming practices.', 'Rs. 50,000 per hectare over 3 years for organic inputs and certification.', 'Aadhaar Card, Land Records, Group Formation Certificate', 'Apply through State Agriculture Department.', 'https://pgsindia-ncof.gov.in');

-- ============================
-- SEED DATA: Crops
-- ============================
INSERT INTO crops (crop_name, category) VALUES
('Wheat', 'Grain'),
('Rice', 'Grain'),
('Maize', 'Grain'),
('Cotton', 'Cash Crop'),
('Sugarcane', 'Cash Crop'),
('Onion', 'Vegetable'),
('Tomato', 'Vegetable'),
('Potato', 'Vegetable');

-- ============================
-- SEED DATA: Market Prices (demo)
-- ============================
INSERT INTO market_prices (crop_id, market_name, price_per_quintal, price_date) VALUES
(1, 'Azadpur Mandi, Delhi', 2250.00, CURDATE()),
(1, 'Indore Mandi, MP', 2180.00, CURDATE()),
(1, 'Ludhiana Mandi, Punjab', 2300.00, CURDATE()),
(2, 'Azadpur Mandi, Delhi', 3100.00, CURDATE()),
(2, 'Raipur Mandi, Chhattisgarh', 2950.00, CURDATE()),
(2, 'Kolkata Mandi, WB', 3050.00, CURDATE()),
(3, 'Nizamabad Mandi, Telangana', 1980.00, CURDATE()),
(3, 'Davangere Mandi, Karnataka', 1920.00, CURDATE()),
(4, 'Guntur Mandi, AP', 6200.00, CURDATE()),
(4, 'Rajkot Mandi, Gujarat', 6450.00, CURDATE()),
(5, 'Muzaffarnagar Mandi, UP', 350.00, CURDATE()),
(5, 'Kolhapur Mandi, MH', 340.00, CURDATE()),
(6, 'Lasalgaon Mandi, MH', 1800.00, CURDATE()),
(6, 'Bengaluru Mandi, KA', 1650.00, CURDATE()),
(7, 'Kolar Mandi, KA', 1200.00, CURDATE()),
(7, 'Nashik Mandi, MH', 1350.00, CURDATE()),
(8, 'Agra Mandi, UP', 950.00, CURDATE()),
(8, 'Hooghly Mandi, WB', 1020.00, CURDATE());
