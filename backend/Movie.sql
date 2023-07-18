DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'level') THEN
        CREATE TYPE "level" AS ENUM (
            'admin',
            'user'
        );
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_gender') THEN
        CREATE TYPE "enum_gender" AS ENUM (
            'male',
            'female',
            'other'
        );
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS "users" (
    "id" bigserial PRIMARY KEY,
    "email" varchar NOT NULL,
    "password" varchar NOT NULL,
    "level" level DEFAULT 'user',
    "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE IF NOT EXISTS "user_detail" (
    "id" bigserial PRIMARY KEY,
    "user_id" bigint,
    "name" varchar NOT NULL,
    "gender" enum_gender NOT NULL,
    "age" int NOT NULL,
    "address" varchar NOT NULL,
    "phone" int NOT NULL
);

CREATE TABLE IF NOT EXISTS "genre" (
    "id" bigserial PRIMARY KEY,
    "name" varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS "title_type" (
    "id" bigserial PRIMARY KEY,
    "name" varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS "movie" (
    "id" bigserial PRIMARY KEY,
    "title_type_id" bigint,
    "title" varchar NOT NULL,
    "genre_id" bigint,
    "release_date" date,
    "finish_date" date,
    "rating" int,
    "user_id" bigint,
    "status" bool DEFAULT false,
    "created_at" timestamp NOT NULL DEFAULT (now()),
    "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE INDEX IF NOT EXISTS "index_users_email" ON "users" ("email");

CREATE INDEX IF NOT EXISTS "index_user_detail_name" ON "user_detail" ("name");

CREATE INDEX IF NOT EXISTS "index_user_detail_address" ON "user_detail" ("address");

CREATE INDEX IF NOT EXISTS "index_user_detail_phone" ON "user_detail" ("phone");

DO $$ BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM   pg_constraint
        WHERE  conname = 'fk_user_detail_user_id'
          AND  conrelid = 'user_detail'::regclass
    ) THEN
        ALTER TABLE "user_detail"
        ADD CONSTRAINT "fk_user_detail_user_id"
        FOREIGN KEY ("user_id")
        REFERENCES "users" ("id");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM   pg_constraint
        WHERE  conname = 'fk_movie_title_type_id'
          AND  conrelid = 'movie'::regclass
    ) THEN
        ALTER TABLE "movie"
        ADD CONSTRAINT "fk_movie_title_type_id"
        FOREIGN KEY ("title_type_id")
        REFERENCES "title_type" ("id");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM   pg_constraint
        WHERE  conname = 'fk_movie_genre_id'
          AND  conrelid = 'movie'::regclass
    ) THEN
        ALTER TABLE "movie"
        ADD CONSTRAINT "fk_movie_genre_id"
        FOREIGN KEY ("genre_id")
        REFERENCES "genre" ("id");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM   pg_constraint
        WHERE  conname = 'fk_movie_user_id'
          AND  conrelid = 'movie'::regclass
    ) THEN
        ALTER TABLE "movie"
        ADD CONSTRAINT "fk_movie_user_id"
        FOREIGN KEY ("user_id")
        REFERENCES "users" ("id");
    END IF;
END $$;

