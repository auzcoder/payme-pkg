# Generated by Django 5.1.2 on 2024-12-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PaymeTransactions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_id", models.CharField(max_length=50)),
                ("account_id", models.BigIntegerField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "state",
                    models.IntegerField(
                        choices=[
                            (0, "Created"),
                            (1, "Initiating"),
                            (2, "Successfully"),
                            (-2, "Canceled after successful performed"),
                            (-1, "Canceled during initiation"),
                        ],
                        default=0,
                    ),
                ),
                ("cancel_reason", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "performed_at",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "cancelled_at",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
            ],
            options={
                "verbose_name": "Payme Transaction",
                "verbose_name_plural": "Payme Transactions",
                "db_table": "payme_transactions",
                "ordering": ["-created_at"],
            },
        ),
    ]
