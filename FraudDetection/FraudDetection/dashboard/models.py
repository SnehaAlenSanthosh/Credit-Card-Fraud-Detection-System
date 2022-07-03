from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
# Create your models here.



class Data(models.Model):
    time = models.PositiveIntegerField(blank=True, null=True)
    v1 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v2 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v3 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v4 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v5 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v6 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v7 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v8 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v9 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v10 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v11 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v12= models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v13 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v14 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v15 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v16 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v17 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v18 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v19 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v20 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v21 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v22 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v23 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v24 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v25 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v26 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v27 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    v28 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    amount = models.PositiveIntegerField(blank=True, null=True)
    predictions = models.PositiveIntegerField(null = True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/lore.joblib')
        self.predictions = ml_model.predict([[self.time, self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.v8, self.v9, self.v10, self.v11, self.v12, self.v13, self.v14, self.v15, self.v16, self.v17, self.v18, self.v19, self.v20, self.v21, self.v22, self.v23, self.v24, self.v25, self.v26, self.v27, self.v28, self.amount]])
        return super().save(*args, *kwargs)
      

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.amount)



























   