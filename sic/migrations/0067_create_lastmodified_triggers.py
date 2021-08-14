# Generated by Django 3.1.3 on 2021-08-14 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sic", "0066_create_tag_views"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_aggregation AFTER UPDATE OF name, description, 'default', discoverable, private ON sic_taggregation FOR EACH ROW
BEGIN
    UPDATE sic_taggregation
    SET last_modified = strftime('%Y-%m-%d %H:%M:%f000', 'now')
WHERE
    id = NEW.id;
END;""",
                    [],
                )
            ],
            reverse_sql=[("DROP TRIGGER update_last_modified_aggregation;", [])],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_story_on_insert_comment AFTER INSERT ON sic_comment FOR EACH ROW
BEGIN
    UPDATE sic_story
    SET last_active = NEW.last_modified
WHERE
    id = NEW.story_id;
END;""",
                    [],
                )
            ],
            reverse_sql=[
                ("DROP TRIGGER update_last_modified_story_on_insert_comment;", [])
            ],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_story_on_update_comment AFTER UPDATE OF last_modified ON sic_comment FOR EACH ROW
BEGIN
    UPDATE sic_story
    SET last_active = NEW.last_modified
WHERE
    id = NEW.story_id;
END;""",
                    [],
                )
            ],
            reverse_sql=[
                ("DROP TRIGGER update_last_modified_story_on_update_comment;", [])
            ],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_story_on_delete_comment AFTER DELETE ON sic_comment FOR EACH ROW
BEGIN
    UPDATE sic_story
    SET last_active = strftime('%Y-%m-%d %H:%M:%f000', 'now')
WHERE
    id = OLD.story_id;
END;""",
                    [],
                )
            ],
            reverse_sql=[
                ("DROP TRIGGER update_last_modified_story_on_delete_comment;", [])
            ],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_story_on_insert_vote AFTER INSERT ON sic_vote FOR EACH ROW
BEGIN
    UPDATE sic_story
    SET last_active = NEW.created
WHERE
    id = NEW.story_id;
END;""",
                    [],
                )
            ],
            reverse_sql=[
                ("DROP TRIGGER update_last_modified_story_on_insert_vote;", [])
            ],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_story_on_update_vote AFTER UPDATE ON sic_vote FOR EACH ROW
BEGIN
    UPDATE sic_story
    SET last_active = strftime('%Y-%m-%d %H:%M:%f000', 'now')
WHERE
    id = NEW.story_id;
END;""",
                    [],
                )
            ],
            reverse_sql=[
                ("DROP TRIGGER update_last_modified_story_on_update_vote;", [])
            ],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER update_last_modified_story_on_delete_vote AFTER DELETE ON sic_vote FOR EACH ROW
BEGIN
    UPDATE sic_story
    SET last_active = strftime ('%Y-%m-%d %H:%M:%f000', 'now')
WHERE
    id = OLD.story_id;
END;""",
                    [],
                )
            ],
            reverse_sql=[
                ("DROP TRIGGER update_last_modified_story_on_delete_vote;", [])
            ],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE VIEW taggregation_last_active AS
SELECT
    MAX(s.last_active) AS last_active,
    t.taggregation_id AS taggregation_id
FROM
    sic_story AS s
    JOIN taggregation_stories AS t ON t.id = s.id
GROUP BY
    t.taggregation_id;""",
                    [],
                )
            ],
            reverse_sql=[("DROP VIEW taggregation_last_active;", [])],
        ),
    ]
