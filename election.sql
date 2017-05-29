-- Table: public."Handle"

-- DROP TABLE public."Handle";

CREATE TABLE public."Handle"
(
  "HNR" integer NOT NULL,
  "Name" text NOT NULL,
  CONSTRAINT "Handle_pkey" PRIMARY KEY ("HNR")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Handle"
  OWNER TO postgres;

-- Table: public."Hashtag"

-- DROP TABLE public."Hashtag";

CREATE TABLE public."Hashtag"
(
  "HtNR" integer NOT NULL,
  "TNR" integer[] NOT NULL,
  "Text" text NOT NULL,
  CONSTRAINT "Hashtag_pkey" PRIMARY KEY ("HtNR"),
  CONSTRAINT "Hashtag_TNR_fkey" FOREIGN KEY ("TNR")
      REFERENCES public."Tweet" ("TNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Hashtag"
  OWNER TO postgres;


-- Table: public."Reply"

-- DROP TABLE public."Reply";

CREATE TABLE public."Reply"
(
  "HNR" integer NOT NULL,
  "TNR" integer[] NOT NULL,
  reply_to text NOT NULL,
  CONSTRAINT "Reply_HNR_fkey" FOREIGN KEY ("HNR")
      REFERENCES public."Handle" ("HNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT "Reply_TNR_fkey" FOREIGN KEY ("TNR")
      REFERENCES public."Tweet" ("TNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Reply"
  OWNER TO postgres;


-- Table: public."Retweet"

-- DROP TABLE public."Retweet";

CREATE TABLE public."Retweet"
(
  "HNR" integer NOT NULL,
  "TNR" integer[] NOT NULL,
  original_autor text NOT NULL,
  CONSTRAINT "Retweet_HNR_fkey" FOREIGN KEY ("HNR")
      REFERENCES public."Handle" ("HNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT "Retweet_TNR_fkey" FOREIGN KEY ("TNR")
      REFERENCES public."Tweet" ("TNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Retweet"
  OWNER TO postgres;

-- Table: public."Tweet"

-- DROP TABLE public."Tweet";

CREATE TABLE public."Tweet"
(
  "TNR" integer[] NOT NULL,
  favorite_count integer NOT NULL,
  retweet_count integer NOT NULL,
  "HNR" integer NOT NULL,
  "Datum" timestamp without time zone NOT NULL,
  "Text" text NOT NULL,
  "HtNR" integer NOT NULL,
  CONSTRAINT "Tweet_pkey" PRIMARY KEY ("TNR"),
  CONSTRAINT "Tweet_HNR_fkey" FOREIGN KEY ("HNR")
      REFERENCES public."Handle" ("HNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT "Tweet_HtNR_fkey" FOREIGN KEY ("HtNR")
      REFERENCES public."Hashtag" ("HtNR") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Tweet"
  OWNER TO postgres;
