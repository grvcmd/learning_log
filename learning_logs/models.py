from django.db import models


# Create your models here.
# Code wise, a model is just a class
# A model tells Django how to work with the data that will be stored in the app.


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    # Foreign Key isa DB term; it's a reference to another record in the db.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # the delete arg deletes all associated entries of a deleted Topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Meta class holds extra information for managing a model
    class Meta:
        # Uses 'entries' when Django needs to refer to more than one entry.
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text




