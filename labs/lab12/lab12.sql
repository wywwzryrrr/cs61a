CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

CREATE TABLE big AS
  SELECT f.course 
  FROM finals f
  JOIN sizes s ON f.hall = s.room
  GROUP BY f.course
  HAVING SUM(s.seats) >= 1000;

CREATE TABLE remaining AS
  SELECT f.course, SUM(s.seats) - MAX(s.seats)
  FROM finals f
  JOIN sizes s ON f.hall = s.room
  GROUP BY f.course;

CREATE TABLE sharing AS
  SELECT f1.course,
         COUNT(DISTINCT f1.hall) AS shared
  FROM finals f1
  JOIN finals f2 ON f1.hall = f2.hall
  WHERE f1.course != f2.course
  GROUP BY f1.course
  ORDER BY f1.course;

CREATE TABLE pairs AS
    SELECT f1.room || " and " || f2.room
    || " together have " || (f1.seats + f2.seats) 
    || " seats" AS rooms
    FROM sizes f1
    JOIN sizes f2 ON (f1.room < f2.room)
    WHERE (f1.seats + f2.seats) >= 1000
    ORDER BY (f1.seats + f2.seats) DESC;