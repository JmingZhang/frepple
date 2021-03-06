#
# Copyright (C) 2020 by frePPLe bv
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ArchiveManager",
            fields=[
                (
                    "snapshot_date",
                    models.DateTimeField(
                        db_index=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="snapshot date",
                    ),
                ),
                ("total_records", models.IntegerField(verbose_name="total_records")),
                ("buffer_records", models.IntegerField(verbose_name="buffer_records")),
                ("demand_records", models.IntegerField(verbose_name="demand_records")),
                (
                    "operationplan_records",
                    models.IntegerField(verbose_name="operationplan_records"),
                ),
            ],
            options={
                "verbose_name": "archive manager",
                "verbose_name_plural": "archive managers",
                "db_table": "ax_manager",
                "ordering": ["snapshot_date"],
            },
        ),
        migrations.CreateModel(
            name="ArchivedBuffer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="identifier"
                    ),
                ),
                (
                    "snapshot_date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="archive.ArchiveManager",
                        verbose_name="snapshot date",
                    ),
                ),
                (
                    "item",
                    models.CharField(
                        db_index=True, max_length=300, verbose_name="item"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        db_index=True, max_length=300, verbose_name="location"
                    ),
                ),
                (
                    "batch",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="batch"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=20,
                        null=True,
                        verbose_name="cost",
                    ),
                ),
                (
                    "onhand",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=20,
                        null=True,
                        verbose_name="onhand",
                    ),
                ),
                (
                    "safetystock",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=20,
                        null=True,
                        verbose_name="safety stock",
                    ),
                ),
            ],
            options={
                "verbose_name": "archived buffer",
                "verbose_name_plural": "archived buffers",
                "db_table": "ax_buffer",
                "ordering": ["item", "location", "batch"],
            },
        ),
        migrations.CreateModel(
            name="ArchivedDemand",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="identifier"
                    ),
                ),
                (
                    "snapshot_date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="archive.ArchiveManager",
                        verbose_name="snapshot date",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="name")),
                (
                    "item",
                    models.CharField(
                        db_index=True, max_length=300, verbose_name="item"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=20,
                        null=True,
                        verbose_name="cost",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        db_index=True, max_length=300, verbose_name="location"
                    ),
                ),
                (
                    "customer",
                    models.CharField(
                        db_index=True, max_length=300, verbose_name="customer"
                    ),
                ),
                ("due", models.DateTimeField(verbose_name="due")),
                (
                    "status",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="status"
                    ),
                ),
                ("priority", models.IntegerField(verbose_name="priority")),
                (
                    "quantity",
                    models.DecimalField(
                        decimal_places=8, max_digits=20, verbose_name="quantity"
                    ),
                ),
                (
                    "deliverydate",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="delivery date"
                    ),
                ),
                (
                    "quantityplanned",
                    models.DecimalField(
                        decimal_places=8,
                        max_digits=20,
                        blank=True,
                        null=True,
                        verbose_name="quantity planned",
                    ),
                ),
            ],
            options={
                "verbose_name": "archived sales order",
                "verbose_name_plural": "archived sales orders",
                "db_table": "ax_demand",
                "ordering": ["priority", "due"],
            },
        ),
        migrations.CreateModel(
            name="ArchivedOperationPlan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="identifier"
                    ),
                ),
                (
                    "snapshot_date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="archive.ArchiveManager",
                        verbose_name="snapshot date",
                    ),
                ),
                (
                    "reference",
                    models.CharField(max_length=300, verbose_name="reference"),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="status"
                    ),
                ),
                (
                    "type",
                    models.CharField(db_index=True, max_length=5, verbose_name="type"),
                ),
                (
                    "quantity",
                    models.DecimalField(
                        decimal_places=8, max_digits=20, verbose_name="quantity"
                    ),
                ),
                (
                    "startdate",
                    models.DateTimeField(
                        blank=True,
                        help_text="start date",
                        null=True,
                        verbose_name="start date",
                    ),
                ),
                (
                    "enddate",
                    models.DateTimeField(
                        blank=True,
                        help_text="end date",
                        null=True,
                        verbose_name="end date",
                    ),
                ),
                (
                    "operation",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="operation"
                    ),
                ),
                (
                    "owner",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="owner"
                    ),
                ),
                (
                    "batch",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="batch"
                    ),
                ),
                (
                    "item",
                    models.CharField(
                        db_index=True, max_length=300, verbose_name="item"
                    ),
                ),
                (
                    "item_cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=20,
                        null=True,
                        verbose_name="item cost",
                    ),
                ),
                (
                    "itemsupplier_cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=20,
                        null=True,
                        verbose_name="itemsupplier cost",
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="origin"
                    ),
                ),
                (
                    "destination",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=300,
                        null=True,
                        verbose_name="destination",
                    ),
                ),
                (
                    "supplier",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="supplier"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="location"
                    ),
                ),
                (
                    "demand",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="demand"
                    ),
                ),
                (
                    "due",
                    models.DateTimeField(blank=True, null=True, verbose_name="due"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=1000,
                        null=True,
                        verbose_name="name",
                    ),
                ),
            ],
            options={
                "verbose_name": "operationplan",
                "verbose_name_plural": "operationplans",
                "db_table": "ax_operationplan",
                "ordering": ["reference"],
            },
        ),
        migrations.RunSQL(
            """
            insert into common_parameter
            (name, value, description, lastmodified)
            values
            ('archive.frequency','week','Frequency of history snapshot. Values: week, month, none',now())
            on conflict (name) do nothing
            """
        ),
    ]
