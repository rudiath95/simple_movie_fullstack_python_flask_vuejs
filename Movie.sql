CREATE TYPE "level" AS ENUM (
  'admin',
  'user'
);

CREATE TYPE "enum_gender" AS ENUM (
  'male',
  'female',
  'other'
);

CREATE TABLE "users" (
  "id" bigserial PRIMARY KEY,
  "email" varchar NOT NULL,
  "password" varchar NOT NULL,
  "level" level DEFAULT 'user',
  "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "user_detail" (
  "id" bigserial PRIMARY KEY,
  "user_id" bigint,
  "name" varchar NOT NULL,
  "gender" enum_gender NOT NULL,
  "age" int NOT NULL,
  "address" varchar NOT NULL,
  "phone" int NOT NULL
);

CREATE TABLE "genre" (
  "id" bigserial PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "title_type" (
  "id" bigserial PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "movie" (
  "id" bigserial PRIMARY KEY,
  "title_type_id" bigint,
  "title" varchar NOT NULL,
  "genre_id" bigint,
  "release_date" date,
  "finish_date" date,
  "rating" uint,
  "user_id" bigint,
  "status" bool DEFAULT false,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE INDEX ON "users" ("email");

CREATE INDEX ON "user_detail" ("name");

CREATE INDEX ON "user_detail" ("address");

CREATE INDEX ON "user_detail" ("phone");

ALTER TABLE "user_detail" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "movie" ADD FOREIGN KEY ("title_type_id") REFERENCES "title_type" ("id");

ALTER TABLE "movie" ADD FOREIGN KEY ("genre_id") REFERENCES "genre" ("id");

ALTER TABLE "movie" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
