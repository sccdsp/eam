from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                "CREATE TABLE IF NOT EXISTS `cmdb_agent` ("
                "`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,"
                "`name` varchar(255) NOT NULL UNIQUE,"
                "`version` varchar(64) NOT NULL,"
                "`status` varchar(32) NOT NULL,"
                "`last_heartbeat` datetime(6) NULL,"
                "`host_id` bigint NOT NULL,"
                "CONSTRAINT `cmdb_agent_host_id_96eeee74_fk_cmdb_host_id` FOREIGN KEY (`host_id`) REFERENCES `cmdb_host` (`id`)"
                ")"
            ),
            reverse_sql="DROP TABLE IF EXISTS `cmdb_agent`",
        ),
    ]

