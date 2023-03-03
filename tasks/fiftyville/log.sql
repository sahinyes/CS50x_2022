-- Keep a log of any SQL queries you execute as you solve the mystery.

select * from crime_scene_reports where day = 28 and month = 7 and street = "Humphrey Street";
-- at 10.15 am and interview with 3 witnesses


select * from interviews where day = 28 and month = 7 and transcript like "%bakery%";
-- 10 min of the theft - parking
-- Leggett Street - ATM
-- Phone call less than a minute - Earliest flight on tomorrow


-- 10 min of theft - parking;
select * from people join bakery_security_logs on bakery_security_logs.license_plate = people.license_plate where day = 28 and month = 7 and hour = 10 and  minute >= 15 and minute <= 25;

+--------+---------+----------------+-----------------+---------------+-----+------+-------+-----+------+--------+----------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate | id  | year | month | day | hour | minute | activity | license_plate |
+--------+---------+----------------+-----------------+---------------+-----+------+-------+-----+------+--------+----------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       | 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       | 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       | 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       | 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       | 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       | 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       | 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       | 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+--------+---------+----------------+-----------------+---------------+-----+------+-------+-----+------+--------+----------+---------------+




-- Legget Street - ATM
select name,phone_number,license_plate,passport_number from people join bank_accounts on bank_accounts.person_id = people.id join atm_transactions on atm_transactions.account_number = bank_accounts.account_number where atm_location = "Leggett Street" and day = 28 and month = 7;

+---------+----------------+---------------+-----------------+
|  name   |  phone_number  | license_plate | passport_number |
+---------+----------------+---------------+-----------------+
| Bruce   | (367) 555-5533 | 94KL13X       | 5773159633      |
| Kaelyn  | (098) 555-1164 | I449449       | 8304650265      |
| Diana   | (770) 555-1861 | 322W7JE       | 3592750733      |
| Brooke  | (122) 555-4581 | QX4YZN3       | 4408372428      |
| Kenny   | (826) 555-1652 | 30G67EN       | 9878712108      |
| Iman    | (829) 555-5269 | L93JTIZ       | 7049073643      |
| Luca    | (389) 555-5198 | 4328GD8       | 8496433585      |
| Taylor  | (286) 555-6063 | 1106N58       | 1988161715      |
| Benista | (338) 555-6650 | 8X428L0       | 9586786673      |
+---------+----------------+---------------+-----------------+

-- Phone call less than a minute
select caller,receiver,duration from phone_calls where day = 28 and month = 7 and duration <= 60;

+----------------+----------------+----------+
|     caller     |    receiver    | duration |
+----------------+----------------+----------+
| (130) 555-0289 | (996) 555-8899 | 51       |
| (499) 555-9472 | (892) 555-8872 | 36       |
| (367) 555-5533 | (375) 555-8161 | 45       |
| (609) 555-5876 | (389) 555-5198 | 60       |
| (499) 555-9472 | (717) 555-1342 | 50       |
| (286) 555-6063 | (676) 555-6554 | 43       |
| (770) 555-1861 | (725) 555-3243 | 49       |
| (031) 555-6622 | (910) 555-3251 | 38       |
| (826) 555-1652 | (066) 555-9701 | 55       |
| (338) 555-6650 | (704) 555-2131 | 54       |
+----------------+----------------+----------+

-- Earliest flight on tomorrow from "Fiftyville"
select name,phone_number from people join passengers on passengers.passport_number = people.passport_number where passengers.flight_id = (select id from flights where month = 7 and day = 29 and origin_airport_id = (select id from airports where city = "Fiftyville")order by hour limit 1);

+--------+----------------+
|  name  |  phone_number  |
+--------+----------------+
| Doris  | (066) 555-9701 |
| Sofia  | (130) 555-0289 |
| Bruce  | (367) 555-5533 |
| Edward | (328) 555-1152 |
| Kelsey | (499) 555-9472 |
| Taylor | (286) 555-6063 |
| Kenny  | (826) 555-1652 |
| Luca   | (389) 555-5198 |
+--------+----------------+

-- To where?

select * from airports where id = (select destination_airport_id from flights where day = 29 and month = 7 and origin_airport_id = (select id from airports where city = "Fiftyville")order by hour limit 1);
+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City |
+----+--------------+-------------------+---------------+


-- Then i compared which informations i got;
-- 10 min of theft - parking // Legget Street - ATM
select name,phone_number from people join bakery_security_logs on bakery_security_logs.license_plate = people.license_plate where day = 28 and month = 7 and hour = 10 and  minute >= 15 and minute <= 25 intersect select name,phone_number from people join bank_accounts on bank_accounts.person_id = people.id join atm_transactions on atm_transactions.account_number = bank_accounts.account_number where atm_location = "Leggett Street" and day = 28 and month = 7;

+-------+----------------+
| name  |  phone_number  |
+-------+----------------+
| Bruce | (367) 555-5533 |
| Diana | (770) 555-1861 |
| Iman  | (829) 555-5269 |
| Luca  | (389) 555-5198 |
+-------+----------------+

-- Just "Bruce" has phone record as a caller (Phone call less than a minute)

-- Than i see also "Bruce" calling this number (375) 555-8161

select name from people where phone_number = "(375) 555-8161";

+-------+
| name  |
+-------+
| Robin |
+-------+