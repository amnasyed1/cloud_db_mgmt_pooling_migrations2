USE amnahw;

INSERT INTO patients (id, first_name, last_name, date_of_birth, gender) VALUES
('131313', 'Jimmy', 'Apple', '1990-10-27', 'Male'),
('878787', 'Isabella', 'Smith', '1977-01-07','Female'),
('101010', 'Tracy', 'Flowerton', '1965-05-13', 'Female'),
('181818', 'Harry', 'Payne', '1994-02-14','Male'),
('636363', 'Lily', 'Gilmore', '2000-09-08', 'Female');

INSERT INTO allergy_tests (id, patient_id, test_name, test_result, test_date) VALUES 
('20424475', '131313', 'environmental skin test', 'Positive', '2023-10-22'),
('58357624', '878787', 'enviornmental skin test', 'Negative', '2023-09-26'),
('23975635', '101010', 'food blood test', 'Negative', '2023-08-12'),
('57264953', '181818', 'environmental blood test', 'Positive', '2023-07-09'),
('83752358', '636363', 'food skin test', 'Positive', '2023-10-01');