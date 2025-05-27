from django.db import models
import datetime

# Ticket model
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING, default="Nowy")

    def __str__(self):
        return self.title

# Correct word ending
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

# Ticket status model
class Status(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# Correct word ending
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

